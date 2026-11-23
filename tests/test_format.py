from media_audit.audit import format_date, format_duration, format_fps, format_size


def test_duration_rounds_up():
    assert format_duration(5.47) == "6"
    assert format_duration(5.0) == "5"
    assert format_duration(38.01) == "39"


def test_fps_snaps_to_common_rates():
    assert format_fps(29.97) == "30"
    assert format_fps(30.0) == "30"
    assert format_fps(28.6) == "30"
    assert format_fps(23.976) == "24"


def test_fps_far_off_is_kept():
    assert format_fps(12.0) == "12"
    assert format_fps(41.3) == "41.3"


def test_size_is_human_readable():
    assert format_size(16_300_000) == "16 MB"
    assert format_size(4_500_000) == "4.5 MB"
    assert format_size(229_000_000) == "229 MB"
    assert format_size(1_250_000_000) == "1.2 GB"


def test_date_is_mm_dd_yyyy():
    out = format_date("2026-03-21T18:38:01.000000Z")
    assert len(out) == 10 and out[2] == "/" and out[5] == "/"
    assert out.endswith("/2026")


def test_bad_date_is_blank():
    assert format_date("") == ""
    assert format_date("garbage") == ""
