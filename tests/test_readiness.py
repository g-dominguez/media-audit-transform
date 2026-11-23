from media_audit.audit import assess

BASE = dict(
    is_video=True, ext=".mp4", codec="hevc", duration=10.0, size=50_000_000,
    fps=30.0, rotation=0,
)


def meta(**kw):
    return {**BASE, **kw}


def test_ready():
    assert assess(meta()) == ("ready", "")


def test_over_30s_needs_trim():
    assert assess(meta(duration=38)) == ("needs_prep", "trim: over 30s")


def test_over_200mb_needs_trim():
    verdict, reason = assess(meta(size=229_000_000))
    assert verdict == "needs_prep" and "trim: over 200 MB" in reason


def test_4k_alone_is_not_a_blocker():
    assert assess(meta(width=3840, height=2160))[0] == "ready"


def test_fps_over_30():
    assert assess(meta(fps=60.0)) == ("needs_prep", "convert fps: over 30")


def test_rotation_flag_needs_rotate():
    assert assess(meta(rotation=-90)) == ("needs_prep", "rotate: bake in rotation flag")


def test_unsupported_codec_for_container():
    verdict, reason = assess(meta(codec="vp9"))
    assert verdict == "needs_prep" and "transcode" in reason


def test_mov_accepts_prores_mp4_does_not():
    assert assess(meta(ext=".mov", codec="prores"))[0] == "ready"
    assert assess(meta(codec="prores"))[0] == "needs_prep"


def test_multiple_reasons_are_joined():
    verdict, reason = assess(meta(duration=40, fps=60.0))
    assert verdict == "needs_prep"
    assert reason == "trim: over 30s; convert fps: over 30"


def test_not_a_video_is_unsupported():
    assert assess(dict(is_video=False)) == ("unsupported", "not a video")


def test_under_2s_is_unsupported():
    assert assess(meta(duration=1.5)) == ("unsupported", "under 2s Aleph minimum")
