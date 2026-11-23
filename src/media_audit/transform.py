import csv
import hashlib
import json
import math
import os
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from media_audit.audit import RESULT_COLUMNS, snap_fps
from media_audit.probe import probe

MODEL = "aleph2"
CREDITS_PER_SECOND = 28
MIN_CREDITS = 56
MIN_SECONDS = 2
DEFAULT_MAX_SECONDS = 10
API_MAX_SECONDS = 30
MAX_UPLOAD_BYTES = 200_000_000
MAX_SEED = 4_294_967_295
MAX_PROMPT = 1000
DEFAULT_PROMPT = "transform into a hand-drawn 2D cartoon style, bold outlines, bright flat colors"
# Bump when Prep's ffmpeg settings change, so cached files are rebuilt.
PREP_VERSION = "1"
TASK_TIMEOUT = 15 * 60


class SelectionError(Exception):
    """A selected row can't be sent, or the run would break a guardrail. Nothing has been spent."""


@dataclass
class Job:
    filename: str
    source: Path
    start: float
    end: float
    prompt: str
    seed: int | None
    fps: float | None

    @property
    def length(self) -> float:
        return round(self.end - self.start, 3)

    @property
    def credits(self) -> int:
        return estimate_credits(self.length)

    @property
    def key(self) -> str:
        stat = self.source.stat()
        raw = f"{self.filename}|{stat.st_size}|{self.start}|{self.end}|{PREP_VERSION}"
        return hashlib.sha256(raw.encode()).hexdigest()[:10]


def parse_time(text: str) -> float:
    """Seconds from '12.5', 'm:ss(.f)' or 'h:mm:ss(.f)'."""
    parts = text.strip().split(":")
    if not 1 <= len(parts) <= 3:
        raise ValueError(f"not a time: {text!r}")
    try:
        values = [float(p) for p in parts]
    except ValueError:
        raise ValueError(f"not a time: {text!r}") from None
    seconds = 0.0
    for v in values:
        seconds = seconds * 60 + v
    if seconds < 0 or any(v < 0 for v in values):
        raise ValueError(f"negative time: {text!r}")
    return round(seconds, 3)


def estimate_credits(seconds: float) -> int:
    """Aleph 2.0 list price: 28 credits per second, rounded up, 56 minimum."""
    return max(MIN_CREDITS, math.ceil(CREDITS_PER_SECOND * seconds - 1e-9))


def _read_report(report: Path) -> tuple[list[str], list[dict]]:
    with open(report, newline="") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    for col in RESULT_COLUMNS:
        if col not in fields:
            fields.append(col)
    return fields, rows


def _write_report(report: Path, fields: list[str], rows: list[dict]) -> None:
    tmp = report.with_name(report.name + ".tmp")
    with open(tmp, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, report)


def _job_from_row(row: dict, folder: Path, allow_long: bool) -> Job:
    name = row["filename"]

    def fail(msg):
        raise SelectionError(f"{name}: {msg}")

    if not (row.get("in") or "").strip() or not (row.get("out") or "").strip():
        fail("send is set but in and out points are not both filled in")
    try:
        start, end = parse_time(row["in"]), parse_time(row["out"])
    except ValueError as e:
        fail(str(e))
    source = folder / name
    if not source.is_file():
        fail(f"source file not found in {folder}")
    meta = probe(source)
    if not meta["is_video"]:
        fail("not a video")
    if end <= start:
        fail("out point must be after in point")
    if end > meta["duration"] + 0.05:
        fail(f"out point {end}s is past the end of the file ({meta['duration']:.2f}s)")
    length = end - start
    if length < MIN_SECONDS:
        fail(f"clip is {length:.2f}s; Aleph needs at least 2s")
    if length > API_MAX_SECONDS:
        fail(f"clip is {length:.2f}s; Aleph accepts at most 30s")
    if length > DEFAULT_MAX_SECONDS and not allow_long:
        fail(f"clip is {length:.2f}s, over 10s; pass --allow-long to send it")
    seed = None
    if (row.get("seed") or "").strip():
        try:
            seed = int(row["seed"].strip())
        except ValueError:
            fail(f"seed must be a whole number, got {row['seed']!r}")
        if not 0 <= seed <= MAX_SEED:
            fail(f"seed must be between 0 and {MAX_SEED}")
    prompt = (row.get("prompt") or "").strip() or DEFAULT_PROMPT
    if len(prompt) > MAX_PROMPT:
        fail(f"prompt is {len(prompt)} characters; the limit is {MAX_PROMPT}")
    return Job(name, source, start, end, prompt, seed, meta["fps"])


def select_jobs(report: Path, folder: Path, force: bool = False, allow_long: bool = False) -> tuple[list[Job], list[str]]:
    """Validated Jobs for every row marked send, plus notes on rows skipped. Raises on the first invalid row."""
    _, rows = _read_report(Path(report))
    jobs, skipped = [], []
    for row in rows:
        marked = (row.get("send") or "").strip().lower() in ("y", "yes")
        if not marked:
            if (row.get("in") or row.get("out") or "").strip():
                skipped.append(f"{row['filename']}: has in/out points but send is not 'y'")
            continue
        if (row.get("task_id") or "").strip() and not force:
            skipped.append(f"{row['filename']}: already sent (task {row['task_id']}); use --force to resend")
            continue
        jobs.append(_job_from_row(row, Path(folder), allow_long))
    return jobs, skipped


def prep_steps(job: Job) -> list[str]:
    steps = [f"trim {job.start:g}s-{job.end:g}s", "bake in rotation", "downscale to 1080p if larger"]
    if (snap_fps(job.fps) or 0) > 30:
        steps.append("convert to 30 fps")
    return steps


def prep(job: Job, prep_dir: Path) -> Path:
    """Trim (frame-accurate), bake in rotation, cap at 1080p and 30 fps. Cached by Selection."""
    prep_dir = Path(prep_dir)
    prep_dir.mkdir(parents=True, exist_ok=True)
    out = prep_dir / f"{job.source.stem}_{job.key}.mp4"
    if out.exists():
        return out
    filters = ["scale='if(gte(iw,ih),-2,min(iw,1080))':'if(gte(iw,ih),min(ih,1080),-2)'"]
    if (snap_fps(job.fps) or 0) > 30:
        filters.append("fps=30")
    tmp = out.with_name(out.stem + ".tmp.mp4")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-ss", str(job.start), "-i", str(job.source), "-t", str(job.length),
         "-vf", ",".join(filters), "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(tmp)],
        check=True,
    )
    if tmp.stat().st_size > MAX_UPLOAD_BYTES:
        tmp.unlink()
        raise SelectionError(f"{job.filename}: prepared clip is over 200 MB")
    tmp.replace(out)
    return out


def plan(jobs: list[Job], max_credits: int) -> str:
    lines = []
    for j in jobs:
        prompt = j.prompt if len(j.prompt) <= 50 else j.prompt[:47] + "..."
        lines.append(f"{j.filename}  {j.start:g}s-{j.end:g}s ({j.length:g}s)  ~{j.credits} credits  "
                     f"prep: {', '.join(prep_steps(j))}  prompt: {prompt}")
    total = sum(j.credits for j in jobs)
    lines.append(f"{len(jobs)} clip(s), estimated {total} credits at list price (cap {max_credits}).")
    return "\n".join(lines)


def _download(url: str, dest: Path) -> None:
    import httpx

    tmp = dest.with_name(dest.name + ".part")
    with httpx.stream("GET", url, follow_redirects=True, timeout=300) as r:
        r.raise_for_status()
        with open(tmp, "wb") as f:
            for chunk in r.iter_bytes():
                f.write(chunk)
    tmp.replace(dest)


def _cost(details) -> int | str:
    cost = getattr(details, "cost", None)
    return cost.credits if cost is not None else ""


def run_jobs(jobs: list[Job], report: Path, client, output_dir: Path, tag: str, max_credits: int,
             download=_download, log=print) -> None:
    """Send Jobs to Aleph after checking the cap and balance. Writes results back into the report as it goes."""
    from runwayml import TaskFailedError, TaskTimeoutError

    report, output_dir = Path(report), Path(output_dir)
    total = sum(j.credits for j in jobs)
    if total > max_credits:
        raise SelectionError(f"estimated {total} credits is over --max-credits {max_credits}")
    balance = client.organization.retrieve().credit_balance
    if total > balance:
        raise SelectionError(f"estimated {total} credits is over the account balance of {balance}")

    output_dir.mkdir(parents=True, exist_ok=True)
    fields, rows = _read_report(report)
    by_name = {r["filename"]: r for r in rows}

    for job in jobs:
        row = by_name[job.filename]
        entry = {
            "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "filename": job.filename, "in": job.start, "out": job.end, "length": job.length,
            "prep": prep_steps(job), "model": MODEL, "prompt": job.prompt, "seed": job.seed,
            "tag": tag, "estimated_credits": job.credits,
        }
        prepared = prep(job, output_dir / "prep")
        with open(prepared, "rb") as f:
            uri = client.uploads.create_ephemeral(file=f).uri
        params = {"model": MODEL, "video_uri": uri, "prompt_text": job.prompt,
                  "extra_headers": {"X-Runway-Tags": tag}}
        if job.seed is not None:
            params["seed"] = job.seed
        task = client.video_to_video.create(**params)
        # Record the task straight away so a crash can't lead to sending it twice.
        row.update(status="SUBMITTED", task_id=task.id, output_path="", credits="")
        _write_report(report, fields, rows)
        entry["task_id"] = task.id
        log(f"{job.filename}: submitted task {task.id}, waiting...")

        try:
            details = task.wait_for_task_output(timeout=TASK_TIMEOUT)
            dest = output_dir / f"{job.source.stem}_{job.key}_{MODEL}.mp4"
            download(details.output[0], dest)
            entry.update(status="SUCCEEDED", credits=_cost(details), output_path=str(dest))
        except TaskFailedError as e:
            d = e.task_details
            entry.update(status="FAILED", credits=_cost(d), failure=getattr(d, "failure", ""),
                         failure_code=getattr(d, "failure_code", ""))
        except TaskTimeoutError:
            entry.update(status="TIMEOUT", credits="")

        row.update(status=entry["status"], credits=entry["credits"], output_path=entry.get("output_path", ""))
        _write_report(report, fields, rows)
        with open(output_dir / "runs.jsonl", "a") as f:
            f.write(json.dumps(entry) + "\n")
        detail = entry.get("output_path") or entry.get("failure") or "check the task in the Runway dashboard"
        log(f"{job.filename}: {entry['status']} ({entry['credits'] or '?'} credits) {detail}")
