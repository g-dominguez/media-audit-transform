import shutil
import subprocess

import pytest


def _ffmpeg(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def make_video(path, seconds=3, size="320x180", rate=30, codec="libx264", audio=True, rotation=None):
    inputs = ["-f", "lavfi", "-i", f"testsrc=duration={seconds}:size={size}:rate={rate}"]
    if audio:
        inputs += ["-f", "lavfi", "-i", f"sine=duration={seconds}"]
    out = ["-c:v", codec, "-pix_fmt", "yuv420p"]
    if audio:
        out += ["-c:a", "aac", "-shortest"]
    _ffmpeg(*inputs, *out, str(path))
    if rotation is not None:
        # Set the display-matrix rotation flag by remuxing, as a phone does.
        flagged = path.with_name("flagged_" + path.name)
        _ffmpeg("-display_rotation", str(rotation), "-i", str(path), "-c", "copy", str(flagged))
        flagged.replace(path)
    return path


@pytest.fixture
def make():
    return make_video


@pytest.fixture(scope="session", autouse=True)
def _require_ffmpeg():
    if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
        pytest.skip("ffmpeg/ffprobe not installed")
