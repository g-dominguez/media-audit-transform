import csv
import json
from types import SimpleNamespace

import pytest

from media_audit.audit import COLUMNS, run_audit
from media_audit.probe import probe
from media_audit.transform import (
    SelectionError,
    estimate_credits,
    parse_time,
    prep,
    run_jobs,
    select_jobs,
)


def test_parse_time():
    assert parse_time("12.5") == 12.5
    assert parse_time("0:12.5") == 12.5
    assert parse_time("1:02") == 62
    assert parse_time("0:00:12") == 12  # Google Sheets turns 0:12 into h:mm:ss
    with pytest.raises(ValueError):
        parse_time("abc")
    with pytest.raises(ValueError):
        parse_time("-1")


def test_estimate_credits():
    assert estimate_credits(5) == 140
    assert estimate_credits(10) == 280
    assert estimate_credits(2) == 56
    assert estimate_credits(1.5) == 56
    assert estimate_credits(2.7) == 76


def _report(tmp_path, make, files=("a.mp4",), seconds=12, **probe_kw):
    src = tmp_path / "src"
    src.mkdir()
    for name in files:
        make(src / name, seconds=seconds, **probe_kw)
    out = tmp_path / "report.csv"
    run_audit(src, out)
    return src, out


def _select(csv_path, **by_name):
    with open(csv_path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r.update(by_name.get(r["filename"], {}))
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)


def test_only_send_rows_are_selected(tmp_path, make):
    src, report = _report(tmp_path, make, files=("a.mp4", "b.mp4"))
    _select(report, **{"a.mp4": {"send": "y", "in": "1", "out": "6"}, "b.mp4": {"in": "1", "out": "6"}})
    jobs, skipped = select_jobs(report, src)
    assert [j.filename for j in jobs] == ["a.mp4"]
    assert jobs[0].length == 5
    assert jobs[0].credits == 140
    assert any("b.mp4" in s for s in skipped)


def test_blank_prompt_uses_default_and_seed_parses(tmp_path, make):
    src, report = _report(tmp_path, make)
    _select(report, **{"a.mp4": {"send": "Y", "in": "0", "out": "3", "seed": "42"}})
    job = select_jobs(report, src)[0][0]
    assert "cartoon" in job.prompt
    assert job.seed == 42


@pytest.mark.parametrize("sel, message", [
    ({"in": "5", "out": "3"}, "out point must be after"),
    ({"in": "0", "out": "1.5"}, "at least 2s"),
    ({"in": "0", "out": "11"}, "over 10s"),
    ({"in": "0", "out": "99"}, "past the end"),
    ({"in": "", "out": "3"}, "in and out"),
    ({"in": "0", "out": "3", "seed": "x"}, "seed"),
])
def test_invalid_row_aborts(tmp_path, make, sel, message):
    src, report = _report(tmp_path, make)
    _select(report, **{"a.mp4": {"send": "y", **sel}})
    with pytest.raises(SelectionError, match=message):
        select_jobs(report, src)


def test_allow_long_lifts_10s_but_not_30s(tmp_path, make):
    src, report = _report(tmp_path, make, seconds=35)
    _select(report, **{"a.mp4": {"send": "y", "in": "0", "out": "12"}})
    assert select_jobs(report, src, allow_long=True)[0][0].length == 12
    _select(report, **{"a.mp4": {"send": "y", "in": "0", "out": "31"}})
    with pytest.raises(SelectionError, match="30s"):
        select_jobs(report, src, allow_long=True)


def test_row_with_task_id_is_skipped_unless_forced(tmp_path, make):
    src, report = _report(tmp_path, make)
    _select(report, **{"a.mp4": {"send": "y", "in": "0", "out": "3", "task_id": "t-1"}})
    jobs, skipped = select_jobs(report, src)
    assert jobs == [] and any("already sent" in s for s in skipped)
    assert len(select_jobs(report, src, force=True)[0]) == 1


def test_prep_trims_rotates_downscales_and_caches(tmp_path, make):
    src, report = _report(tmp_path, make, seconds=6, size="1920x1080", rotation=90)
    # source is stored landscape with a rotation flag; downscale needs something over 1080
    _select(report, **{"a.mp4": {"send": "y", "in": "1", "out": "4"}})
    job = select_jobs(report, src)[0][0]
    out = prep(job, tmp_path / "prep")
    m = probe(out)
    assert m["rotation"] == 0
    assert (m["width"], m["height"]) == (1080, 1920)
    assert abs(m["duration"] - 3) < 0.1
    assert m["codec"] == "h264" and m["has_audio"]
    mtime = out.stat().st_mtime
    assert prep(job, tmp_path / "prep") == out and out.stat().st_mtime == mtime


def test_prep_downscales_4k(tmp_path, make):
    src, report = _report(tmp_path, make, seconds=3, size="3840x2160", audio=False)
    _select(report, **{"a.mp4": {"send": "y", "in": "0", "out": "2"}})
    m = probe(prep(select_jobs(report, src)[0][0], tmp_path / "prep"))
    assert (m["width"], m["height"]) == (1920, 1080)


class FakeClient:
    def __init__(self, balance=1000, fail=False):
        self.balance = balance
        self.fail = fail
        self.created = []
        self.organization = SimpleNamespace(retrieve=lambda: SimpleNamespace(credit_balance=self.balance))
        self.uploads = SimpleNamespace(create_ephemeral=lambda file: SimpleNamespace(uri="runway://upload/1"))
        self.video_to_video = SimpleNamespace(create=self._create)

    def _create(self, **kw):
        self.created.append(kw)
        client = self

        class Task:
            id = f"task-{len(client.created)}"

            def wait_for_task_output(self, timeout=None):
                if client.fail:
                    from runwayml import TaskFailedError
                    raise TaskFailedError(SimpleNamespace(
                        id=self.id, status="FAILED", failure="moderated", failure_code="SAFETY.INPUT",
                        cost=SimpleNamespace(credits=140)))
                return SimpleNamespace(id=self.id, status="SUCCEEDED", output=["https://x/out.mp4"],
                                       cost=SimpleNamespace(credits=140))
        return Task()


def _fake_download(url, dest):
    dest.write_bytes(b"video")


def test_run_writes_results_back_and_logs(tmp_path, make):
    src, report = _report(tmp_path, make)
    _select(report, **{"a.mp4": {"send": "y", "in": "0", "out": "5", "prompt": "8-bit", "seed": "7"}})
    jobs, _ = select_jobs(report, src)
    client = FakeClient()
    run_jobs(jobs, report, client, tmp_path / "output", tag="project:test", max_credits=300, download=_fake_download)
    sent = client.created[0]
    assert sent["model"] == "aleph2" and sent["prompt_text"] == "8-bit" and sent["seed"] == 7
    assert sent["video_uri"] == "runway://upload/1"
    assert sent["extra_headers"] == {"X-Runway-Tags": "project:test"}
    row = next(csv.DictReader(open(report)))
    assert row["status"] == "SUCCEEDED" and row["task_id"] == "task-1" and row["credits"] == "140"
    assert (tmp_path / "output" / row["output_path"].split("/")[-1]).exists()
    log = [json.loads(l) for l in open(tmp_path / "output" / "runs.jsonl")]
    assert log[0]["seed"] == 7 and log[0]["estimated_credits"] == 140 and log[0]["credits"] == 140
    # a second run skips the row
    assert select_jobs(report, src)[0] == []


def test_failed_task_is_recorded_with_cost(tmp_path, make):
    src, report = _report(tmp_path, make)
    _select(report, **{"a.mp4": {"send": "y", "in": "0", "out": "5"}})
    jobs, _ = select_jobs(report, src)
    run_jobs(jobs, report, FakeClient(fail=True), tmp_path / "output", tag="t", max_credits=300,
             download=_fake_download)
    row = next(csv.DictReader(open(report)))
    assert row["status"] == "FAILED" and row["credits"] == "140" and row["task_id"] == "task-1"
    log = json.loads(open(tmp_path / "output" / "runs.jsonl").readline())
    assert log["failure_code"] == "SAFETY.INPUT"


def test_run_refuses_over_cap_or_balance(tmp_path, make):
    src, report = _report(tmp_path, make)
    _select(report, **{"a.mp4": {"send": "y", "in": "0", "out": "10"}})
    jobs, _ = select_jobs(report, src)
    with pytest.raises(SelectionError, match="max-credits"):
        run_jobs(jobs, report, FakeClient(), tmp_path / "o", tag="t", max_credits=200, download=_fake_download)
    with pytest.raises(SelectionError, match="balance"):
        run_jobs(jobs, report, FakeClient(balance=100), tmp_path / "o", tag="t", max_credits=300,
                 download=_fake_download)
