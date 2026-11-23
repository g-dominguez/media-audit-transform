import json
import subprocess
from pathlib import Path


def _fps(stream):
    for key in ("avg_frame_rate", "r_frame_rate"):
        num, _, den = stream.get(key, "0/0").partition("/")
        if float(den or 0):
            return round(float(num) / float(den), 3)
    return None


def _rotation(stream):
    for side in stream.get("side_data_list", []):
        if "rotation" in side:
            return int(round(float(side["rotation"])))
    return int(stream.get("tags", {}).get("rotate", 0))


def probe(path: Path) -> dict:
    """Return file facts from ffprobe, or {"is_video": False} if there is no readable video."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", str(path)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return {"is_video": False}
    info = json.loads(result.stdout)
    streams = info.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video" and not s.get("disposition", {}).get("attached_pic")), None)
    if video is None:
        return {"is_video": False}
    fmt = info.get("format", {})
    format_name = fmt.get("format_name", "")
    if format_name.startswith("image2") or format_name.endswith("_pipe"):
        return {"is_video": False}
    rotation = _rotation(video)
    w, h = video["width"], video["height"]
    sideways = abs(rotation) % 180 == 90
    width, height = (h, w) if sideways else (w, h)
    return {
        "is_video": True,
        "ext": path.suffix.lower(),
        "codec": video.get("codec_name"),
        "container": fmt.get("format_name"),
        "stored_width": w,
        "stored_height": h,
        "width": width,
        "height": height,
        "rotation": rotation,
        "orientation": "portrait" if height > width else "landscape" if width > height else "square",
        "fps": _fps(video),
        "duration": float(fmt.get("duration") or video.get("duration") or 0),
        "size": int(fmt.get("size") or path.stat().st_size),
        "has_audio": any(s.get("codec_type") == "audio" for s in streams),
        "creation_date": fmt.get("tags", {}).get("creation_time", ""),
    }
