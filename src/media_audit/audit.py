import csv
import math
import os
from datetime import datetime
from pathlib import Path

from media_audit.probe import probe

MAX_SECONDS = 30
MIN_SECONDS = 2
MAX_BYTES = 200_000_000
MAX_FPS = 30
DEFAULT_VERY_SHORT = 5.0

SUPPORTED_CODECS = {
    ".mp4": {"h264", "hevc", "av1"},
    ".mov": {"h264", "hevc", "prores"},
    ".mkv": {"h264", "hevc", "vp8", "vp9", "av1"},
}

FACT_COLUMNS = [
    "filename", "orientation", "resolution", "fps", "duration",
    "size", "codec", "has_audio", "creation_date",
    "flags", "readiness", "reason",
]
SELECTION_COLUMNS = ["send", "in", "out", "prompt", "seed"]
RESULT_COLUMNS = ["status", "task_id", "output_path", "credits"]
COLUMNS = FACT_COLUMNS + SELECTION_COLUMNS + RESULT_COLUMNS + ["merge_note"]
PRESERVED = SELECTION_COLUMNS + RESULT_COLUMNS


COMMON_FPS = (24, 25, 30, 48, 50, 60)


def snap_fps(fps: float | None) -> float | None:
    """Snap to a common frame rate when within 5% (29.97 -> 30); otherwise keep one decimal."""
    if not fps:
        return None
    nearest = min(COMMON_FPS, key=lambda c: abs(c - fps))
    return float(nearest) if abs(nearest - fps) / nearest <= 0.05 else round(fps, 1)


def format_fps(fps: float | None) -> str:
    snapped = snap_fps(fps)
    if snapped is None:
        return ""
    return str(int(snapped)) if snapped == int(snapped) else str(snapped)


def format_duration(seconds: float) -> str:
    """Whole seconds, rounded up."""
    return str(math.ceil(seconds - 1e-6))


def format_size(size: int) -> str:
    mb = size / 1_000_000
    if mb >= 1000:
        return f"{mb / 1000:.1f} GB"
    return f"{mb:.1f} MB" if mb < 10 else f"{mb:.0f} MB"


def format_date(iso: str) -> str:
    """MM/DD/YYYY in local time, or blank if missing or unreadable."""
    try:
        return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone().strftime("%m/%d/%Y")
    except ValueError:
        return ""


def assess(meta: dict) -> tuple[str, str]:
    """Readiness of a Source file for Aleph, with the reasons it is not ready."""
    if not meta.get("is_video"):
        return "unsupported", "not a video"
    if meta["duration"] < MIN_SECONDS:
        return "unsupported", "under 2s Aleph minimum"
    steps = []
    if meta["duration"] > MAX_SECONDS:
        steps.append("trim: over 30s")
    if meta["size"] > MAX_BYTES:
        steps.append("trim: over 200 MB")
    if meta["rotation"] % 360:
        steps.append("rotate: bake in rotation flag")
    if snap_fps(meta["fps"]) and snap_fps(meta["fps"]) > MAX_FPS:
        steps.append("convert fps: over 30")
    if meta["codec"] not in SUPPORTED_CODECS.get(meta["ext"], set()):
        steps.append(f"transcode: {meta['codec']} in {meta['ext'] or 'no extension'} not accepted")
    return ("needs_prep", "; ".join(steps)) if steps else ("ready", "")


def _row(path: Path, very_short: float) -> tuple[dict, tuple | None]:
    """Report row, plus the exact (duration, size) used for duplicate detection."""
    meta = probe(path)
    readiness, reason = assess(meta)
    row = dict.fromkeys(COLUMNS, "")
    row.update(filename=path.name, readiness=readiness, reason=reason)
    if meta["is_video"]:
        row.update(
            orientation=meta["orientation"],
            resolution=f"{meta['width']}x{meta['height']}", fps=format_fps(meta["fps"]),
            duration=format_duration(meta["duration"]), size=format_size(meta["size"]),
            codec=meta["codec"], has_audio="yes" if meta["has_audio"] else "no",
            creation_date=format_date(meta["creation_date"]),
        )
        if meta["duration"] <= very_short:
            row["flags"] = "very_short"
        return row, (round(meta["duration"], 3), meta["size"])
    return row, None


def _flag_duplicates(rows: list[dict], keys: list[tuple | None]) -> None:
    groups: dict[tuple, list[dict]] = {}
    for r, key in zip(rows, keys):
        if key is not None:
            groups.setdefault(key, []).append(r)
    for group in groups.values():
        for r in group:
            flags = [r["flags"]] if r["flags"] else []
            flags += [f"possible_duplicate:{o['filename']}" for o in group if o is not r]
            r["flags"] = ";".join(flags)


def _read_previous(path: Path) -> dict[str, dict] | None:
    """Existing report keyed by filename, or None if it can't be merged cleanly."""
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames or "filename" not in reader.fieldnames:
                return None
            return {r["filename"]: r for r in reader}
    except (OSError, UnicodeDecodeError, csv.Error):
        return None


def _merge(rows: list[dict], previous: dict[str, dict]) -> list[dict]:
    seen = set()
    for r in rows:
        seen.add(r["filename"])
        old = previous.get(r["filename"])
        if not old:
            continue
        for col in PRESERVED:
            r[col] = old.get(col) or ""
        changed = (old.get("size") or "") != r["size"] or (old.get("duration") or "") != r["duration"]
        if changed and any(r[c] for c in PRESERVED):
            r["merge_note"] = "file changed since selection was made; check in/out points"
    for name, old in previous.items():
        if name in seen or not any(old.get(c) for c in PRESERVED):
            continue
        kept = {c: old.get(c) or "" for c in COLUMNS}
        kept["merge_note"] = "file missing from folder"
        rows.append(kept)
    return sorted(rows, key=lambda r: r["filename"])


def run_audit(folder: Path, out: Path, very_short: float = DEFAULT_VERY_SHORT) -> Path:
    """Audit a folder into a CSV, merging into an existing report. Returns the path written."""
    folder, out = Path(folder), Path(out)
    files = sorted(p for p in folder.iterdir() if p.is_file() and not p.name.startswith("."))
    rows, keys = zip(*[_row(p, very_short) for p in files]) if files else ((), ())
    rows = list(rows)
    _flag_duplicates(rows, list(keys))
    if out.exists():
        previous = _read_previous(out)
        if previous is None:
            out = out.with_name(f"{out.stem}.{datetime.now():%Y%m%d-%H%M%S}{out.suffix}")
        else:
            rows = _merge(rows, previous)
    tmp = out.with_name(out.name + ".tmp")
    with open(tmp, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, out)
    return out


def summarize(csv_path: Path) -> str:
    with open(csv_path, newline="") as f:
        rows = list(csv.DictReader(f))
    counts = {k: sum(r["readiness"] == k for r in rows) for k in ("ready", "needs_prep", "unsupported")}
    portrait = sum(r["orientation"] == "portrait" for r in rows)
    landscape = sum(r["orientation"] == "landscape" for r in rows)
    short = sum("very_short" in r["flags"] for r in rows)
    dup = sum("possible_duplicate" in r["flags"] for r in rows)
    return (
        f"{len(rows)} files: {counts['ready']} ready, {counts['needs_prep']} needs_prep, "
        f"{counts['unsupported']} unsupported | {landscape} landscape, {portrait} portrait | "
        f"{short} very_short, {dup} possible duplicates"
    )
