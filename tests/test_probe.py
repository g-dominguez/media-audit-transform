from media_audit.probe import probe


def test_plain_landscape(tmp_path, make):
    m = probe(make(tmp_path / "a.mp4"))
    assert (m["width"], m["height"]) == (320, 180)
    assert m["orientation"] == "landscape"
    assert m["rotation"] == 0
    assert m["fps"] == 30.0
    assert m["codec"] == "h264"
    assert m["has_audio"] is True
    assert abs(m["duration"] - 3) < 0.2


def test_rotation_flag_makes_it_portrait(tmp_path, make):
    m = probe(make(tmp_path / "r.mp4", rotation=90))
    assert abs(m["rotation"]) == 90
    assert m["stored_width"] == 320 and m["stored_height"] == 180
    assert (m["width"], m["height"]) == (180, 320)
    assert m["orientation"] == "portrait"


def test_stored_portrait_without_flag(tmp_path, make):
    m = probe(make(tmp_path / "p.mp4", size="180x320"))
    assert m["rotation"] == 0 and m["orientation"] == "portrait"


def test_no_audio(tmp_path, make):
    assert probe(make(tmp_path / "n.mp4", audio=False))["has_audio"] is False


def test_av1(tmp_path, make):
    assert probe(make(tmp_path / "x.mp4", codec="libsvtav1"))["codec"] == "av1"


def test_not_a_video(tmp_path):
    f = tmp_path / "pic.jpg"
    f.write_bytes(b"not really a jpeg")
    assert probe(f)["is_video"] is False
