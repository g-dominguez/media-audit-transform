# Media Audit → Runway Cartoon Clip: Scoping Brief

Written 2026-11-22 (updated the same day), to start a grilling/scoping session. Rough idea, not a spec.

## The idea

Two parts:

1. **Audit:** a script scans a folder of video and reports what's there and what shape it's in, so a person can review the files one by one.
2. **Transform:** take one reviewed clip, prepare it locally, and use Runway to turn it into a cartoon version with sound.

**Flow:** scan (ffprobe) → audit report → you review and pick a clip → prepare locally (trim, rotate, frame rate) → Runway Aleph 2.0 cartoon restyle → add audio → download and log.

**Who it's for:** anyone with a folder or archive of video they don't know much about, from a personal phone library to a studio or agency archive. Before footage goes into an AI pipeline, you need to know what you have: which files are ready, which need fixing first, which are probably junk, and what an action would cost before spending anything.

**Working pattern:** test first, a person reviews, then it runs for real. Nothing is spent or changed without approval.

**Out of scope:** choosing highlights and editing clips together. Runway is built to generate and transform video. Shot selection and assembly are expected to happen before or after it, in other tools.

## What Runway does (and doesn't)

From the API docs saved in [docs/runway/](docs/runway/README.md), downloaded 2026-11-22:

- **Generate:** video, images, music and sound effects from prompts or images.
- **Transform existing footage:** restyle or edit it with a text prompt (mainly Aleph 2.0).
- **Finish:** upscale, SDR→HDR (Ruby), frame rate, ProRes and other professional formats.
- **Characters:** real-time conversational avatars (not relevant here).
- **Doesn't:** analyze or describe video content. No model or endpoint does this.
- **Doesn't:** edit clips into a sequence from a prompt. Workflows (pipelines built in the Runway app) have utility steps for stitching clips and adding audio, but that's glue between AI steps, not an editor.
- **Reference-video models** (Seedance 2.5, Kling, WAN) generate *new* AI footage that imitates your clips. They don't edit the real footage.

## The Runway part, in detail

### Cartoon restyle: Aleph 2.0
- **Endpoint:** `POST /v1/video_to_video`, model `aleph2` ([api/generate/video_to_video.md](docs/runway/api/generate/video_to_video.md)).
- **Inputs:**
  - **Prompt:** e.g. "transform into a hand-drawn 2D cartoon style, bold outlines, bright flat colors."
  - **Keyframes (optional):** up to 5 style reference images placed at timestamps.
  - **`seed` (optional):** for repeatable results.
- **Input rules:**
  - 2–30 seconds long
  - 30 fps or lower
  - 200 MB max as an upload
- **Output:**
  - Keeps the input's resolution, up to 1080p
  - Default format is H.264 MP4; ProRes and PNG sequence cost extra
- **Cost:** 28 credits per second, 56-credit minimum. 5 seconds ≈ 140 credits, 10 seconds ≈ 280.
- **Unknown:** whether the output keeps the input's audio. The docs don't say. Test it in the Playground.

### Audio (pick one or combine)
| Option | How | Cost |
|---|---|---|
| Original game audio | Extract from the source clip and add it back to the cartoon with ffmpeg | Free |
| Synced sound effects | `POST /v1/video_to_audio`, model `mirelo_sfx_2_0`. Returns audio only (mp3/wav/flac), optional prompt, up to 4 variants | Not in pricing doc; check `estimatedCost` |
| Music | `POST /v1/text_to_music`, model `eleven_music_v2_5`. 3–600 seconds, can be instrumental; prompts naming artists or songs are rejected | Not in pricing doc; check `estimatedCost` |

Combining audio with the video happens locally with ffmpeg in every case.

### Other facts that apply
- **Rotation:** the docs don't say whether Runway honors a video's rotation flag. Rotate locally first.
- **Cost before spending:** `estimatedCost` comes back only after a job is created, so a preview has to be calculated locally from [pricing.md](docs/runway/pricing.md).
- **Moderation:** a moderated job comes back as `FAILED` and still costs credits ([ai-context.md](docs/runway/ai-context.md)).
- **Output links expire:** download results right away.
- **Cost tracking:** `X-Runway-Tags` labels each job (e.g. `project:softball`).
- **Runway Dev MCP:** connected, but its tools cover account state only (models, projects, credit balance, checking jobs). The script should use the Python SDK (`runwayml`).
- **Credits available:** about 1,000.
- **Try first:** the Developer Portal Playground has Aleph 2.0 (dev.runway.com → video_to_video). One manual test there answers the audio question and shows real quality and cost before any code.

## The audit part

### Checks from metadata (free)
- Real orientation, using the rotation flag
- Length: too short (possible junk); too long for Aleph (over 30s, cut first)
- File size against the 200 MB upload limit
- **Frame rate:** over 30 fps needs converting for Aleph
- Resolution (4K will come back at 1080p)
- Codec and container against Runway's supported list
- Has audio or not; creation date present
- Possible duplicates (same length and size)
- Non-video files in the folder
- **Ready for Aleph:** yes/no, with the reason

### Test set: the Softball folder (29 clips)
- All recorded on a Pixel phone, 4K HEVC MP4, about 10.5 minutes total.
- **Orientation catch:** 28 of 29 files are stored as landscape 3840×2160. The portrait ones only have a 90° rotation flag, so reading pixel size alone calls everything landscape. Real count: **18 landscape, 11 portrait.**
- **Over 30 seconds:** 9 clips.
- **Over 200 MB:** 6 clips, plus 1 borderline (200.3 MB).
- **5 seconds or shorter:** 3 clips (possible junk).
- **Frame rate:** not checked yet.
- **Odd file:** `…NS-02.MAIN.mp4` is the only one stored as true portrait with no rotation flag. Reason unknown.
- Two `.jpg` stills are also in the folder; the scan should skip or report them.
- **ffmpeg/ffprobe aren't installed yet** (`brew install ffmpeg`). The scan so far used macOS metadata plus a small MP4 header reader.

| File | Orientation | Rotation flag | Length | Size | Flags |
|---|---|---|---|---|---|
| PXL_20250301_170416910.mp4 | 9:16 | 90° | 38s | 229 MB | over 30s; over 200 MB |
| PXL_20250301_170532838.mp4 | 9:16 | 90° | 7s | 41 MB | — |
| PXL_20250419_172242025.mp4 | 9:16 | 90° | 17s | 103 MB | — |
| PXL_20250419_180011142.mp4 | 9:16 | 90° | 10s | 58 MB | — |
| PXL_20250906_154006792.mp4 | 16:9 | 0° | 8s | 50 MB | — |
| PXL_20250906_160552296.mp4 | 16:9 | 0° | 9s | 52 MB | — |
| PXL_20250920_160929328.mp4 | 16:9 | 0° | 37s | 222 MB | over 30s; over 200 MB |
| PXL_20250920_161112694.mp4 | 16:9 | 0° | 20s | 118 MB | — |
| PXL_20250920_163327035.mp4 | 16:9 | 0° | 41s | 245 MB | over 30s; over 200 MB |
| PXL_20250920_165217169.mp4 | 16:9 | 0° | 24s | 143 MB | — |
| PXL_20250920_173953317.mp4 | 16:9 | 0° | 39s | 236 MB | over 30s; over 200 MB |
| PXL_20250920_180125099.mp4 | 16:9 | 0° | 33s | 200 MB | over 30s; size borderline |
| PXL_20251011_171334305.mp4 | 9:16 | 90° | 9s | 56 MB | — |
| PXL_20251011_173503701.mp4 | 9:16 | 90° | 49s | 298 MB | over 30s; over 200 MB |
| PXL_20260314_184929293.mp4 | 16:9 | 0° | 21s | 124 MB | — |
| PXL_20260321_183801850.mp4 | 16:9 | 0° | 23s | 137 MB | — |
| PXL_20260321_185513572.mp4 | 16:9 | 0° | 32s | 193 MB | over 30s |
| PXL_20260321_215534333.mp4 | 16:9 | 0° | 33s | 196 MB | over 30s |
| PXL_20260502_014035260.mp4 | 16:9 | 0° | 8s | 45 MB | — |
| PXL_20260502_021737268.mp4 | 16:9 | 0° | 68s | 407 MB | over 30s; over 200 MB |
| PXL_20260502_022037345.mp4 | 16:9 | 0° | 28s | 167 MB | — |
| PXL_20260502_022448679.mp4 | 9:16 | 90° | 8s | 50 MB | — |
| PXL_20260912_185230551.mp4 | 16:9 | 0° | 19s | 116 MB | — |
| PXL_20260912_185400029.mp4 | 16:9 | 0° | 4s | 25 MB | possible junk |
| PXL_20260912_191053657.mp4 | 16:9 | 0° | 8s | 49 MB | — |
| PXL_20260926_214901318.mp4 | 9:16 | 90° | 12s | 75 MB | — |
| PXL_20260926_220827835.mp4 | 9:16 | 90° | 15s | 88 MB | — |
| PXL_20261119_021615558.mp4 | 9:16 | 90° | 3s | 16 MB | possible junk |
| PXL_20261119_024256881.NS-02.MAIN.mp4 | 9:16 | 0° (stored portrait) | 5s | 32 MB | possible junk |

Lengths are rounded to the nearest second; sizes are in decimal MB.

## Decisions to make

1. **Audit output:** terminal table, CSV, or JSON? Which columns?
2. **Cutoffs:** "junk" length (≤3s? ≤5s?). Hard-coded or configurable?
3. **Junk handling:** flag only (recommended), or move files to a review folder? Never delete.
4. **Picking the clip:** how you choose which clip (and which seconds of it) goes to Runway: a CSV column, command-line flags, or a prompt.
5. **Preparation:** trim to what length (5s? 10s?), downscale 4K to 1080p before upload, and convert frame rate if over 30 fps.
6. **Cartoon style:** prompt only, or prompt plus a style reference image? Fixed prompt or passed in?
7. **Audio:** original game audio, generated sound effects, generated music, or a mix?
8. **Cost guardrail:** a per-run credit cap and a dry-run default that spends nothing.
9. **Outputs:** where results are saved, and what's logged (task ID, prompt, seed, estimated and actual credits, tags).
10. **Version 1 vs later:** the smallest version that's useful on its own.
11. **Privacy:** footage of minors goes to Runway's servers. Runway's data retention policy hasn't been checked.

## Suggested smallest version (to challenge in the session)

- **Step 0 (manual, no code):** one trimmed clip through the Aleph 2.0 Playground with two or three cartoon prompts. Answers the audio question and shows quality.
- **Version 1:** scan + audit report on the Softball folder. Zero credits; works without Runway.
- **Version 1.5:** prepare one chosen clip (≤10 seconds, rotated, ≤30 fps), run Aleph 2.0, add the original audio back with ffmpeg, save and log. About 140–280 credits.
- **Later:** generated sound effects or music, more clips, style reference images.

## References

- Runway docs (local): [docs/runway/README.md](docs/runway/README.md). Start with `ai-context.md`, then `api/generate/video_to_video.md`.
- Live Runway docs index: https://docs.dev.runwayml.com/llms.txt
