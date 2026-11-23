---
title: Professional outputs
description: Generate HDR and pipeline formats with Gen-4.5 and Aleph 2.0, or upscale, change frame rate, and convert SDR to HDR on a video you already have.
---

Professional film and video work typically specifies a resolution, frame rate, and/or color grade beyond what a generated clip already has. The pipeline often also needs a container it can open directly, such as ProRes or a PNG sequence.

Runway Dev covers both: [Gen-4.5](/guides/models?modality=video\&q=gen4.5) and [Aleph 2.0](/guides/models?modality=video\&q=aleph2) generate these formats natively. Additionally, we have post-production models that can upscale, change the frame rate, or convert SDR to HDR on a video you already have.

# Editorial containers

[Gen-4.5](/guides/models?modality=video\&q=gen4.5) and [Aleph 2.0](/guides/models?modality=video\&q=aleph2) can deliver ProRes, a PNG sequence, or the default H.264 `.mp4` on the generation request. These files stay in standard dynamic range. [HDR](#generate-hdr-video) is a separate delivery.

To generate outputs in these formats, simply specify an `outputFormat` in your request:

| `outputFormat` | Delivery |
| -------------- | -------- |
| `mp4` (default) | H.264 `.mp4` |
| `prores` | ProRes `.mov` |
| `png_sequence` | `.zip` of PNG frames (plus a separate `.wav` when the output has audio) |

For `prores`, optionally set `proresProfile` (`422 Proxy`, `422 LT`, `422`,
`422 HQ`, `4444`, or `4444 XQ`; default `4444`).

The same two models can also deliver 10-bit Rec.709 SDR when a grade needs more precision than 8-bit H.264. That file is still SDR.

| `outputFormat` | Delivery | Models |
| -------------- | -------- | ------ |
| `sdr_rec709_10bit` | HEVC Main 10, Rec.709 `.mp4` | Gen-4.5, Aleph 2.0 |

`prores` and `png_sequence` add 5 credits per second. 10-bit SDR uses the higher per-second surcharge. See [pricing](/guides/pricing#professional-and-hdr-output-formats).

[Seedance 2.5](/guides/models?modality=video\&q=seedance2_5) can deliver a `.mov` instead of the default `.mp4`: set `outputFormat: "mov"` on text to video, image to video, or video to video. It keeps higher color precision for grading and compositing, and costs the same as `mp4`. [Draft previews](/guides/models#seedance-25-draft-mode) are `.mp4` only.

[Seedance 2.0](/guides/models?modality=video\&q=seedance2), Seedance 2.0 Fast, and Seedance 2.0 Mini render at standard bitrate by default. Set `bitrate: "high"` to keep more detail with fewer compression artifacts, at a larger file size. Both settings cost the same.

# Generate HDR video

HDR (high dynamic range) stores a wider span of brightness than standard dynamic range (SDR). Highlights keep detail that an SDR file would clip, which is what HDR playback, broadcast, and theatrical specs ask for. A default H.264 `.mp4` is SDR and cannot carry that range.

[Gen-4.5](/guides/models?modality=video\&q=gen4.5) can generate HDR natively. Set `outputFormat` to one of the HDR values below.

[Ruby](/guides/models?modality=upscale\&q=ruby) converts any SDR video, including an Aleph edit, to HDR on [`POST /v1/video_to_hdr`](/api#tag/Start-generating/paths/~1v1~1video_to_hdr/post). Inputs must be SDR, at most 30 seconds, and up to 4K.

## HDR and high bit-depth (Gen-4.5 only)

Gen-4.5 HDR outputs are true HDR renders, graded into BT.2020 with measured HDR10 metadata.

| `outputFormat` | Delivery |
| -------------- | -------- |
| `hdr10` | HEVC Main 10, BT.2020 + PQ `.mp4` |
| `hlg` | HEVC Main 10, BT.2020 + HLG `.mp4` |
| `hdr_pq_12bit_master` | 12-bit 4:4:4 BT.2020 + PQ `.mov` (lossless) |
| `hdr_prores` | BT.2020 + PQ ProRes `.mov` |
| `hdr_png_sequence` | `.zip` of 16-bit PNG frames + colorimetry sidecar (plus a separate `.wav` when the output has audio) |
| `hdr_exr_sequence` | `.zip` of half-float OpenEXR frames as linear BT.2020 light (1.0 = 100 nits) + colorimetry sidecar (plus a separate `.wav` when the output has audio) |
| `hdr_exr_acescg_sequence_1_3` | The EXR delivery as scene-referred ACEScg for ACES 1.3 pipelines — reads with the stock `ACES - ACEScg` input transform |
| `hdr_exr_acescg_sequence_2_0` | The same scene-referred ACEScg delivery for ACES 2.0 pipelines (inverted through the ACES 2.0 Output Transform) |

For `hdr_prores`, `proresProfile` accepts `422`, `422 HQ`, or `4444`
(default `422 HQ`). On `/v1/video_to_hdr`, sources with an alpha channel are
delivered as `4444` regardless of `proresProfile`.

The ACEScg EXRs are scene-referred: the delivered picture is inverted
through the ACES 1.3 Output Transform (Rec.2100 PQ, 1000-nit), so reading
the frames with the stock `ACES - ACEScg` input transform and viewing
through your ACES pipeline reproduces the delivered picture — no Read-node
changes needed. The `colorimetry.json` sidecar names the ACES version and
the inverted transform.

These formats use the higher per-second surcharge — see [pricing](/guides/pricing#professional-and-hdr-output-formats).

# Upscale resolution and frame rate

A clip you already have can still fall short of the resolution or frame rate a timeline, broadcast spec, or playback target asks for.

* **Higher resolution.** [Magnific Video Upscaler](/guides/models?modality=upscale\&q=magnific_video_upscaler_creative) raises the video to 4K. Inputs can be at most 30 seconds. Complete spec is in the [video upscale reference](/api#tag/Start-generating/paths/~1v1~1video_upscale/post).
* **A set frame rate.** [Enhance Frame Rate](/guides/models?modality=upscale\&q=enhance_frame_rate) retimes the clip, including the drop-frame rates. Inputs can be at most 300 seconds. Complete spec is in the [video upscale reference](/api#tag/Start-generating/paths/~1v1~1video_upscale/post).
