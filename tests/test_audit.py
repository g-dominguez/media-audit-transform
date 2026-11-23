import csv
import shutil

from media_audit.audit import COLUMNS, run_audit


def read(path):
    with open(path, newline="") as f:
        return {r["filename"]: r for r in csv.DictReader(f)}


def test_one_row_per_visible_file(tmp_path, make):
    src = tmp_path / "src"
    src.mkdir()
    make(src / "a.mp4")
    make(src / "b.mp4", seconds=1)
    (src / "pic.jpg").write_bytes(b"x")
    (src / ".DS_Store").write_bytes(b"x")
    out = tmp_path / "audit.csv"
    run_audit(src, out)
    rows = read(out)
    assert set(rows) == {"a.mp4", "b.mp4", "pic.jpg"}
    assert rows["pic.jpg"]["readiness"] == "unsupported"
    assert rows["pic.jpg"]["reason"] == "not a video"
    assert rows["a.mp4"]["readiness"] == "ready"
    assert rows["b.mp4"]["readiness"] == "unsupported"


def test_columns_include_selection_and_result(tmp_path, make):
    src = tmp_path / "src"
    src.mkdir()
    make(src / "a.mp4")
    out = tmp_path / "audit.csv"
    run_audit(src, out)
    header = next(csv.reader(open(out)))
    assert header == COLUMNS
    for col in ("send", "in", "out", "prompt", "seed", "status", "task_id", "output_path", "credits"):
        assert col in header


def test_very_short_flag_is_configurable(tmp_path, make):
    src = tmp_path / "src"
    src.mkdir()
    make(src / "a.mp4", seconds=4)
    out = tmp_path / "audit.csv"
    run_audit(src, out)
    assert "very_short" in read(out)["a.mp4"]["flags"]
    run_audit(src, out, very_short=3)
    assert "very_short" not in read(out)["a.mp4"]["flags"]


def test_possible_duplicate(tmp_path, make):
    src = tmp_path / "src"
    src.mkdir()
    make(src / "a.mp4")
    shutil.copy(src / "a.mp4", src / "copy.mp4")
    out = tmp_path / "audit.csv"
    run_audit(src, out)
    rows = read(out)
    assert "possible_duplicate:copy.mp4" in rows["a.mp4"]["flags"]
    assert "possible_duplicate:a.mp4" in rows["copy.mp4"]["flags"]


def test_rerun_keeps_selections(tmp_path, make):
    src = tmp_path / "src"
    src.mkdir()
    make(src / "a.mp4")
    out = tmp_path / "audit.csv"
    run_audit(src, out)
    rows = list(csv.DictReader(open(out)))
    rows[0].update(send="y", **{"in": "0:01", "out": "0:03"}, prompt="8-bit")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    make(src / "b.mp4")
    written = run_audit(src, out)
    assert written == out
    r = read(out)
    assert r["a.mp4"]["send"] == "y" and r["a.mp4"]["in"] == "0:01"
    assert r["a.mp4"]["prompt"] == "8-bit"
    assert "b.mp4" in r


def test_rerun_notes_changed_file(tmp_path, make):
    src = tmp_path / "src"
    src.mkdir()
    make(src / "a.mp4", seconds=3)
    out = tmp_path / "audit.csv"
    run_audit(src, out)
    rows = list(csv.DictReader(open(out)))
    rows[0]["send"] = "y"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    make(src / "a.mp4", seconds=5)
    run_audit(src, out)
    r = read(out)["a.mp4"]
    assert r["send"] == "y"
    assert "changed" in r["merge_note"]


def test_missing_file_with_selection_is_kept(tmp_path, make):
    src = tmp_path / "src"
    src.mkdir()
    make(src / "a.mp4")
    make(src / "b.mp4")
    out = tmp_path / "audit.csv"
    run_audit(src, out)
    rows = list(csv.DictReader(open(out)))
    for r in rows:
        if r["filename"] == "a.mp4":
            r["send"] = "y"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    (src / "a.mp4").unlink()
    (src / "b.mp4").unlink()
    run_audit(src, out)
    r = read(out)
    assert "missing" in r["a.mp4"]["merge_note"]
    assert "b.mp4" not in r


def test_unreadable_existing_csv_writes_new_file(tmp_path, make):
    src = tmp_path / "src"
    src.mkdir()
    make(src / "a.mp4")
    out = tmp_path / "audit.csv"
    out.write_text("this,is,not\nan,audit,report\n")
    written = run_audit(src, out)
    assert written != out
    assert out.read_text().startswith("this,is,not")
    assert "a.mp4" in read(written)
