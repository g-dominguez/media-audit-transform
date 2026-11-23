---
title: API Input Parameters
description: Learn about input parameters for Runway Dev. Understand how to format images, videos, text prompts and other inputs for AI generation requests.
---

When starting tasks on Runway Dev, you'll often need to provide assets like images.
Some restrictions exist for what you can provide.

Assets can be provided via URLs or Data URIs.

# Size limits

The size limits of inputs differ based on whether they are provided as a URL or as a data URI in the JSON request body.

| Input type | URL size limit | Data URI size limit | Ephemeral uploads |
| ---------- | -------------- | ------------------- | ----------------- |
| Image      | 16MB           | 5MB                 | 200MB             |
| Video      | 32MB           | 5MB                 | 200MB             |
| Audio      | 32MB           | 5MB                 | 200MB             |

# Inputs using URLs

In all cases, URLs must meet some basic minimum requirements:

1. All URLs must be HTTPS.
2. URLs must reference a domain name in the hostname position, not an IP address.
3. The server should respond with valid `Content-Type` and `Content-Length` headers.
4. Redirects are not followed. If the URL returns a 3XX response code, the request is considered failed.
5. The length of any single URL should not exceed `2048` characters.

Additionally, the server responding to the request must support HTTP `HEAD` requests.

## `Content-Type` values

When specifying a URL, the `Content-Type` response header must be returned, and it
must match the media type of your asset. File extensions in URLs are not considered.
The `Content-Type`s that are supported are [listed below](#type-specific-requirements)
for the supported asset types.

Be aware that `application/octet-stream` and other generic values are explicitly not
supported.

## User agent

Runway will use a `User-Agent` header that starts with `RunwayML API/` when making requests
to your server. If you use a scraping-prevention tool or WAF, be sure to allowlist our
user agent string prefix.

# Inputs using Data URIs (base64 encoded)

A [data URI](https://en.wikipedia.org/wiki/Data_URI_scheme) allows you to pass the base64
encoded assets as part of a request to our API, rather than passing a URL to the asset
hosted on another server. This can reduce the complexity of your integration by eliminating
an upload step, but it also has a lower limit on the size of the assets that can be
provided.

Data URIs are accepted in any field where a URL is accepted unless otherwise specified.

* An appropriate [content type](https://en.wikipedia.org/wiki/Media_type) must be
  specified in the data URI. For instance, your data URI for a JPEG should start with
  something like `data:image/jpg;base64,`.
* Data URIs must use the base64 extension. The expected format is
  `data:content/type;base64,`.
* The size limit for your data URI (specified above) is the limit for the
  **encoded data URI**. Keep in mind that base64-encoding your asset increases its size
  by about 33%: to fit an image within the **5MB limit**, the binary file must be **3.3MB**
  or less.

Data URIs that do not follow these rules may be rejected with a 400 Bad Request error.

# Inputs using ephemeral uploads

See [our documentation on ephemeral uploads](/assets/uploads) for more.

# Considerations of URLs, data URIs, and ephemeral uploads

If you do not already have your asset stored in object storage, submitting your asset with
a data URI can save you a step. However, the data URI size limit may be too small for some
assets. If you cannot be sure that all assets are safely within the un-encoded size limit,
you should upload assets to object storage instead.

Submitting a request with data URIs instead of URLs will change the performance
characteristics of your integration. Data URIs are part of the request payload, and thus
cause your HTTP requests to take longer to submit: all data must be sent serially to our
servers. Because the request body JSON must be processed before the assets can be extracted
from their data URIs, this may increase the latency of our server responses.

URLs, on the other hand, can be immediately processed in parallel. This means the time
between submitting your HTTP request and the start of processing is likely much lower.
However, latency between our servers and the server hosting your assets may increase the
total request time. Using a CDN or object storage service will help to minimize this cost.

Runway [ephemeral uploads](/assets/uploads) offer the benefits of object storage (like URLs)
without needing to set up your own infrastructure. Assets are uploaded from your server to
Runway's object storage, returning a `runway://` URI that can be used anywhere a HTTPS URL
could be used. Importantly, these URIs can only be used for 24 hours after being created.
It's also important to note that ephemeral uploads are rate limited, and have a minimum
file size of 512 bytes (0.5KB).

# Type-specific requirements

## Images

For fields that accept images, the asset must use one of the following
encodings, along with the corresponding `Content-Type` header:

| Codec | `Content-Type` header       |
| ----- | --------------------------- |
| JPEG  | `image/jpg` or `image/jpeg` |
| PNG   | `image/png`                 |
| WebP  | `image/webp`                |

GIF images are not supported.

## Videos

For fields that accept videos, the asset must use one of the following
codecs, along with the corresponding `Content-Type` header:

| Container format | Usual file extension | Expected content type | Supported codecs                                                                |
| ---------------- | -------------------- | --------------------- | ------------------------------------------------------------------------------- |
| MP4              | `.mp4`               | `video/mp4`           | H.264, H.265/HEVC, AV1                                                          |
| QuickTime        | `.mov`               | `video/quicktime`     | H.264, H.265/HEVC, Apple ProRes (422 Proxy, 422 LT, 422, 422 HQ, 4444, 4444 XQ) |
| Matroska         | `.mkv`               | `video/x-matroska`    | H.264, H.265/HEVC, VP8, VP9, AV1                                                |
| WebM             | `.webm`              | `video/webm`          | VP8, VP9, AV1                                                                   |
| 3GPP             | `.3gp`               | `video/3gpp`          | H.264                                                                           |
| Ogg              | `.ogv`               | `video/ogg`           | Theora                                                                          |

The following formats are supported but discouraged due to quality, performance, industry support, and file size:

| Container format | Usual file extension | Expected content type | Supported codecs        |
| ---------------- | -------------------- | --------------------- | ----------------------- |
| QuickTime        | `.mov`               | `video/quicktime`     | MJPEG                   |
| Matroska         | `.mkv`               | `video/x-matroska`    | MPEG2 (H.262)           |
| AVI              | `.avi`               | `video/x-msvideo`     | H.264, MJPEG, MSMPEG4v3 |
| Flash Video      | `.flv`               | `video/x-flv`         | FLV1, H.264             |
| MPEG             | `.mpg`, `.mpeg`      | `video/mpeg`          | MPEG2 (H.262)           |

Note that file extension is not considered by the API. Use this value for reference only.

* **H.264 / AVC** - Most widely supported modern codec
* **H.265 / HEVC** - High efficiency successor to H.264
* **AV1** - Royalty-free, modern codec
* **VP8 / VP9** - Google's codecs, primarily for WebM
* **Apple ProRes** - Professional editing codec (422 Proxy, 422 LT, 422, 422 HQ, 4444, 4444 XQ)
* **MPEG2 (H.262)** - Legacy codec for DVDs and broadcasts (discouraged)
* **MJPEG** - Motion JPEG, frame-by-frame compression (discouraged)
* **Theora** - Open codec for Ogg containers
* **FLV1** - Legacy Flash Video codec (discouraged)
* **MSMPEG4v3** - Legacy Microsoft codec (discouraged)

:::caution\[Ruby]
Ruby (`ruby`) on `POST /v1/video_to_hdr` accepts SDR sources only. Videos whose streams are tagged as HDR (a PQ or HLG transfer function, or BT.2020 primaries) are rejected. Sources with an alpha channel (ProRes 4444, WebM with alpha) keep it in the `hdr_prores` and EXR deliveries; `hdr10` and `hlg` cannot carry alpha. :::

## Audio

For fields that accept audio, the asset must use one of the following
codecs, along with the corresponding `Content-Type` header:

| Container format | Usual file extension | Content type                             | Supported codecs       |
| ---------------- | -------------------- | ---------------------------------------- | ---------------------- |
| MP3              | `.mp3`               | `audio/mpeg`, `audio/mp3`                | MP3 (MPEG-1/2 Layer 3) |
| WAV              | `.wav`               | `audio/wav`, `audio/wave`, `audio/x-wav` | PCM (uncompressed)     |
| FLAC             | `.flac`              | `audio/flac`, `audio/x-flac`             | FLAC (lossless)        |
| M4A              | `.m4a`               | `audio/mp4`, `audio/x-m4a`               | AAC, ALAC              |
| AAC              | `.aac`               | `audio/aac`, `audio/x-aac`               | AAC (raw)              |

* **MP3 (MPEG-1/2 Layer 3)** - Universal compatibility, lossy compression
* **AAC (Advanced Audio Coding)** - Modern lossy codec, better quality than MP3 at same bitrate
* **FLAC (Free Lossless Audio Codec)** - Lossless compression, popular for archival
* **PCM (Pulse Code Modulation)** - Uncompressed audio, typically in WAV containers
* **ALAC (Apple Lossless Audio Codec)** - Apple's lossless codec, typically in M4A containers

# Aspect ratios and auto-cropping of inputs

## Video inputs

When using video models, be aware of the supported `ratio` parameters, which configures the dimensions of the output files.

Examples:

* **Gen-4.5 Text-to-Video** supports Landscape `1280:720` and Portrait `720:1280` outputs only.
* **Gen-4.5 Image-to-Video** supports Landscape `1280:720` `1584:672` `1104:832`, Portrait `720:1280` `832:1104` `672:1584` and Square `960:960` outputs.
* **Gen-4 Turbo** and **Act-Two** support Landscape `1280:720` `1584:672` `1104:832`, Portrait `720:1280` `832:1104` and Square `960:960` outputs.
* **Aleph 2.0** preserves the input video's resolution (up to 1080p). Input videos must be 2–30 seconds and 30 FPS or lower.
* **MiniMax H3 Max** supports `resolution` of `480p` or `768p`. Durations are 5–15 seconds. There is no `ratio` parameter. Image-to-video accepts a first frame or first and last keyframes (each at least 256 pixels on both sides); output aspect ratio follows the input image. Optional `promptExpansionMode` is `disabled`, `balanced` (the default), or `quality`.
* **WAN 3.0** supports 480p, 720p, and 1080p (default `auto_1080p`). Durations are 2–30 seconds. Up to 10 image references, 5 video references, and 5 audio references (combined video and audio duration each under 15 seconds). Image-to-video accepts a start frame or first/last keyframes; keyframes cannot be mixed with references.
* **Seedance 2.5** supports 24 `width:height` ratios across 480p, 720p, 1080p, and 4K (default `1280:720`). The 4K ratios are `3840:1646`, `3840:2160`, `3840:2880`, `3840:3840`, `2880:3840`, and `2160:3840`. Durations are 4–30 seconds. 480p 16:9 / 9:16 use `854:480` / `480:854`. Input and reference videos must be at least 480p. Video-to-video supports `mode: "reference"` (default), `mode: "extend"`, or `mode: "edit"`. `extend` and `edit` require `promptText`, do not accept `ratio`, and keep the input video's aspect ratio; `edit` also requires `duration: "auto"`. Both render at 1080p when the input video is larger than 720p, and at 720p otherwise. `draft: true` renders a 480p preview at the requested aspect ratio. Enhance a succeeded preview to 1080p within 7 days by sending `draftTaskId` on text-to-video. See [draft mode](/guides/models#seedance-25-draft-mode). `outputFormat` is `mp4` (default) or `mov` on all three endpoints; `mov` keeps higher color precision for grading and compositing. Drafts and enhanced drafts are always `mp4`: `outputFormat: "mov"` is rejected with `draft: true`, and `outputFormat` can't be combined with `draftTaskId`.
* **Seedance 2.5 Flash** (`seedance2_5_flash`) supports 12 `width:height` ratios across 480p and 720p only (default `1280:720`): `992:432`, `854:480`, `752:560`, `640:640`, `560:752`, `480:854`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, and `720:1280`. Durations are 4–30 seconds, and prompts can be up to 15,000 characters. Up to 10 reference images, 5 reference videos, and 5 reference audio clips; video-to-video reserves one video slot for `promptVideo`. Input and reference videos must be at least 480p. Video-to-video supports the same `reference`, `extend`, and `edit` modes as Seedance 2.5, rendering at 720p. `outputFormat` is `mp4` (default) or `mov`. Draft mode, 1080p, and 4K are not supported — use `seedance2_5` for those.
* **Seedance 2.0** supports 24 `width:height` ratios across 480p, 720p, 1080p, and 4K. `bitrate` is `standard` (default) or `high` on all three endpoints; set `bitrate` to `high` to keep more detail at a larger file size.
* **Seedance 2.0 Fast** supports 12 `width:height` ratios across 480p and 720p only. `bitrate` is `standard` (default) or `high` on all three endpoints; set `bitrate` to `high` to keep more detail at a larger file size.
* **Seedance 2.0 Mini** supports 12 `width:height` ratios across 480p and 720p only. `bitrate` is `standard` (default) or `high` on all three endpoints; set `bitrate` to `high` to keep more detail at a larger file size.
* **MiniMax H3** supports `ratio` values `adaptive`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, and `9:16`, with `resolution` of `768P` or `2K` (default `2K`). Durations are 5–15 seconds. `adaptive` requires at least one reference image or video. Keyframe (`position: first`/`last`) and unpositioned reference-image modes cannot be mixed; reference audio is only valid with unpositioned reference images (not keyframes).
* **Grok Imagine Video 1.5 Text-to-Video** supports `ratio` values `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, and `2:3`, with `resolution` of `480p`, `720p`, or `1080p` (default `480p`). Durations are 1–15 seconds. Up to 7 image references (addressable in the prompt as `[Image 1]`, `[Image 2]`, …) and 3 audio references (each 3–15 seconds). Audio references require at least one image reference, and requests with image references are capped at 720p.
* **Grok Imagine Video 1.5 Image-to-Video** uses `resolution` (`480p` / `720p` / `1080p`, default `480p`) to set output quality. Output aspect ratio follows the input image. Only a single `first` frame is supported via `promptImage`.
* **Grok Imagine Video 1.5 Lite Text-to-Video** supports 21 `width:height` ratios across 480p, 720p, and 1080p (default `848:480`), covering 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, and 2:3 — for example `848:480`, `1280:720`, `720:1280`, `720:720`, and `1904:1072`. The 1080p sizes are rendered at 720p and upscaled. Durations are 1–15 seconds (default 8). Image and audio references are not supported.
* **Grok Imagine Video 1.5 Lite Image-to-Video** uses `ratio` values `auto_480p`, `auto_720p`, or `auto_1080p` (default `auto_480p`) to set output quality; output aspect ratio follows the input image, and `auto_1080p` is rendered at 720p and upscaled. Only a single `first` frame is supported via `promptImage`, and `promptText` is optional.
* **Kling 4.0 Flash** (`kling_4_flash`) generates 3–20 seconds (default 5) at 720p, including audio. Text-to-video `ratio` is `1280:720` (default), `720:1280`, `960:960`, `1464:628`, or `auto_720p`. Legacy values `940:940` and `1460:624` remain accepted as aliases. Image-to-video takes one first frame, not middle or last frames; omit `ratio` or use `auto_720p` to follow its framing. Video-to-video also accepts `duration` and the text-to-video ratios, defaulting to `auto_720p`. All three endpoints accept image `references` and `referenceVideos`: at most 10 images including the first frame, and 5 videos totaling at most 20 seconds including the source video. Input videos must be 3–21 seconds, with clips over 20 seconds trimmed before generation; billing caps each clip at 20 seconds. First-frame images and videos must have aspect ratios from 0.4 to 2.5. Images must be at least 300px on each side; videos must be at least 700px on each side and 24–60 fps. `promptText` supports up to 26,000 English characters or 11,000 non-English characters, sharing that budget for mixed prompts; it may be omitted only for image-to-video without references.
* **Kling 4.0** supports 3–30 second durations (default 5) at `720p` (default) or `1080p`. Text-to-video `ratio` selects the output size: `1280:720`, `720:1280`, `940:940`, or `1460:624` at 720p; `1920:1080`, `1080:1920`, `1440:1440`, or `2200:940` at 1080p. Use `auto_720p` or `auto_1080p` for model-chosen framing. The default output is landscape 720p. Image-to-video and video-to-video accept the auto tokens to select quality while keeping input framing. Image-to-video follows the first frame: `promptImage` is one image, or an array with exactly one `first` frame, up to 8 `middle` frames in array order, and an optional `last` frame. `references` are images of characters, objects, or styles; frames and references together are at most 10. `referenceVideos` takes up to 5 videos (style, motion, or camera), each 3–31 seconds and 24–60 fps, at least 700px on each side, within aspect ratio 0.4–2.5, together at most 30 seconds; clips longer than 30 seconds are trimmed to 30. Video-to-video edits a source clip and does not take `duration`; length and framing follow the source, with up to 10 reference images. Prompt and reference images must be at least 300px on each side. `promptText` allows up to 26,000 English characters or 11,000 non-English characters, and mixed prompts share that budget. `promptText` is required except when image-to-video uses only frames.
* **Kling 2.5 Turbo Pro** text-to-video supports `1920:1080` (default), `1440:1440`, and `1080:1920`. `1280:720`, `720:720`, and `720:1280` are still accepted. Durations are 5 or 10 seconds (default 5). Image-to-video follows the input image and accepts a first frame or first and last frames. `cfgScale` is 0–1 (default 0.5). Prompt images must be at least 300px on each side.
* **Kling 3.0 Standard, Pro, and 4K** support 3–15 second durations (default 5). Text-to-video `ratio` is `1280:720`, `720:1280`, or `960:960` (Standard), `1920:1080`, `1080:1920`, or `1440:1440` (Pro), and `3840:2160`, `2160:3840`, or `2880:2880` (4K). Image-to-video accepts a first frame or first and last frames; `ratio` is optional, and when both keyframes are provided the output aspect ratio follows the first frame. `audio` defaults to `true`. `cfgScale` is 0–1 (default 0.5). `providerSettings.multiPrompt` takes up to 6 segments (each prompt 3–512 characters); total duration across segments is 3–15 seconds. `promptText` is required when `shotType` is `intelligence`. Prompt images must be at least 300px on each side.
* **Kling O3 Standard, Pro, and 4K** use the same durations, ratios, and `audio` default as Kling 3.0. Image-to-video also accepts up to 7 reference images, including keyframes. A last keyframe and `multiPrompt` cannot be combined. Video-to-video edits a clip of at most 10 seconds whose width and height are each between 720px and 3840px, with up to 4 reference images. `providerSettings.keepOriginalSound` defaults to `true`. `multiPrompt` applies to text-to-video and image-to-video.
* **HappyHorse 1.0 Text-to-Video** supports 10 `width:height` ratios across 720p and 1080p (`1280:720`, `1920:1080`, `720:1280`, `1080:1920`, `960:960`, `1440:1440`, `1108:832`, `1662:1248`, `832:1108`, `1248:1662`).
* **HappyHorse 1.0 Image-to-Video** uses `resolution` (`720P` / `1080P`, default `720P`) to set output quality. Output aspect ratio follows the input image. Prompt images must be at least 300px on each side.
* **Gemini Omni 1.2 Flash** (`gemini_omni_flash_1.2`) accepts prompts up to 4,000 characters and generates 3–15 seconds, or a model-chosen duration with `duration: "auto"` (the default). Text-to-video and image-to-video use pixel `ratio` values `640:360`, `360:640`, `1280:720` (default), `720:1280`, `1920:1080`, `1080:1920`, `3840:2160`, or `2160:3840`. Text-to-video accepts up to 5 image `references` and 3 `referenceVideos`, each at most 10 seconds. Image-to-video requires a first frame and optionally accepts a last frame, not additional references. Video-to-video takes one `videoUri`: `mode: "reference"` (default) accepts up to 10 seconds of input and 5 image references; `mode: "extend"` accepts up to 30 seconds of input and no image references; `mode: "edit"` requires input shorter than 10 seconds, accepts up to 5 image references, and requires `duration: "auto"`. In reference mode use `ratio`; in edit or extend mode use `resolution` (`360p`, `720p`, `1080p`, or `4k`, default `720p`) and omit `ratio` because orientation follows the input. All input images and videos together must fit within 64 MiB.
* **Gemini Omni Flash Text-to-Video** and **Image-to-Video** support Landscape `1280:720` and Portrait `720:1280` outputs only (always 720p, default `1280:720`).
* **Gemini Omni Flash Video-to-Video** has no `ratio` parameter; output is 720p with orientation (landscape 16:9 or portrait 9:16) matched to the input video. Input videos can be at most 10 seconds.
* **Magnific Video Upscaler** (`magnific_video_upscaler_creative`) accepts input videos up to 30 seconds. Set `resolution` to `720p`, `1k`, `2k` (default), or `4k` for target output quality. Include `model: magnific_video_upscaler_creative` on `POST /v1/video_upscale`.
* **Enhance Frame Rate** (`enhance_frame_rate`) accepts input videos up to 300 seconds. Required `targetFramerate` is `24`, `25`, `30`, `48`, `50`, `60`, `120`, `23_98`, `29_97`, or `59_94`. Include `model: enhance_frame_rate` on `POST /v1/video_upscale`.

If your input asset is not exactly of the `ratio` you specify, the model will auto-crop your asset from the center to the aspect ratio parameter provided.

Third party models (e.g., `veo3.1`, `veo3.1_fast`, `wan3`, `h3_max`, `minimax_h3_image`, `grok_imagine_1_5`, `grok_imagine_1_5_lite`, `grok_imagine_image_2`, `muse_image`, `seedream5_flash`, `bria_fibo_1_5`, `bria_fibo_edit_1_5`, `gpt_image_2_5_flare`, `gpt_image_2_5_sunburst`, `gpt_image_2_6_flare`, `gpt_image_2_6_sunburst`, `nano_banana_2.1`, `gemini_image3.1_flash_lite`, `ideogram_4_5`, `ideogram_4_0`, `happyhorse_1_0`, `gemini_omni_flash`, `gemini_omni_flash_1.2`, `kling_4_flash`, `kling_4`, `kling2.5_turbo_pro`, `kling3.0_standard`, `kling3.0_pro`, `kling3.0_4k`, `klingO3_standard`, `klingO3_pro`, `klingO3_4k`, etc.) may crop or resize inputs in other ways.

## Image references

Image references may be resized if they are too large or small to be provided to the model you choose. It is not recommended to provide reference images smaller than 640×640px or larger than 4K.

### Seedream 5.5 inputs

Seedream 5.5 (`seedream5.5`) accepts prompts up to 4,000 characters and up to 10 `referenceImages`. Refer to images in the prompt by their order in the array (Figure 1, Figure 2, and so on). The required `ratio` is one of 24 pixel `width:height` sizes across 1K, 1.5K, and 2K, or `auto_1k`, `auto_1.5k`, or `auto_2k` to let the model choose the aspect ratio. `outputFormat` is `png` (the default) or `jpeg`. `background` is `transparent` or `opaque`; omit it to let the model decide from the prompt. A transparent background requires PNG output. `outputCount` accepts 1–4 (default 1).

| Aspect ratio | 1K          | 1.5K        | 2K          |
| ------------ | ----------- | ----------- | ----------- |
| 1:1          | `1024:1024` | `1536:1536` | `2048:2048` |
| 4:3          | `1152:864`  | `1792:1344` | `2368:1776` |
| 3:4          | `864:1152`  | `1344:1792` | `1776:2368` |
| 16:9         | `1424:800`  | `2048:1152` | `2816:1584` |
| 9:16         | `800:1424`  | `1152:2048` | `1584:2816` |
| 3:2          | `1248:832`  | `1872:1248` | `2496:1664` |
| 2:3          | `832:1248`  | `1248:1872` | `1664:2496` |
| 21:9         | `1568:672`  | `2352:1008` | `3136:1344` |

### MiniMax H3 Image inputs

MiniMax H3 Image (`minimax_h3_image`) accepts prompts up to 32,000 characters and up to 16 `referenceImages`. Refer to images in the prompt by their order in the array (image 1, image 2, and so on). Each reference image must be at least 128 pixels on both sides, with an aspect ratio from 1:4 to 4:1. The required `ratio` is one of 45 pixel `width:height` sizes across 1K, 2K, and 4K, or `auto_1k`, `auto_2k`, or `auto_4k` to let the model choose the framing at that tier. `highspeed` defaults to false and selects the faster Highspeed model. `outputCount` accepts 1–10 (default 1). See the [pricing tables](/guides/pricing#minimax-h3-image).

| Aspect ratio | 1K          | 2K          | 4K          |
| ------------ | ----------- | ----------- | ----------- |
| 1:1          | `1024:1024` | `2048:2048` | `4096:4096` |
| 5:4          | `1152:928`  | `2304:1824` | `4576:3648` |
| 4:5          | `928:1152`  | `1824:2304` | `3648:4576` |
| 4:3          | `1184:896`  | `2368:1760` | `4736:3552` |
| 3:4          | `896:1184`  | `1760:2368` | `3552:4736` |
| 3:2          | `1248:832`  | `2496:1664` | `5024:3360` |
| 2:3          | `832:1248`  | `1664:2496` | `3360:5024` |
| 16:9         | `1376:768`  | `2720:1536` | `5472:3072` |
| 9:16         | `768:1376`  | `1536:2720` | `3072:5472` |
| 2:1          | `1440:736`  | `2912:1440` | `5792:2912` |
| 1:2          | `736:1440`  | `1440:2912` | `2912:5792` |
| 21:9         | `1568:672`  | `3136:1344` | `6272:2688` |
| 9:21         | `672:1568`  | `1344:3136` | `2688:6272` |
| 3:1          | `1760:576`  | `3552:1184` | `7104:2368` |
| 1:3          | `576:1760`  | `1184:3552` | `2368:7104` |

### Seedream Layers inputs

Seedream 5 Pro Layers (`seedream5_pro_layers`) and Seedream 5.5 Layers (`seedream5.5_layers`) each accept exactly one source image. Use PNG or JPEG; WebP and other formats are not supported. The source must be between 262,144 pixels total and 36 megapixels total, with an aspect ratio from 1:16 to 16:1. Keep the source at 30 MB or smaller, subject to the lower limits for [URL and data URI inputs](#size-limits). Neither side may exceed 8,000 pixels. The minimum is based on total pixel count, so each side does not need to be at least 512 pixels.

### GPT Image 2.6 inputs

GPT Image 2.6 Flare (`gpt_image_2_6_flare`) and Sunburst (`gpt_image_2_6_sunburst`) accept prompts up to 32,000 characters and up to 16 `referenceImages`. Refer to images by their order in the array, not by `tag`; tags are labels and are not sent to the model. The required `ratio` is one of 30 pixel `width:height` sizes across 1K, 2K, and 4K, or `auto`. See the [size and pricing tables](/guides/pricing#gpt-image-26-flare-and-sunburst). Both support `quality` and `reasoningEffort` of `low`, `medium`, or `high` (both default to `high`), `background` of `auto` (default), `opaque`, or `transparent`, and `outputCount` from 1–10 (default 1). `outputFormat` defaults to `png` and also supports `jpeg`, `webp`, `gif`, and `svg`. JPEG cannot use a transparent background. GIF and SVG cannot use reference images, and GIF requires `ratio: "auto"`. For GIF output only, `frameCount` accepts 2–16 frames and `frameDurationMs` accepts 20–2,000 milliseconds per frame.

### Ideogram Vector inputs

Ideogram Vector (`ideogram_vector`) accepts up to 5 `referenceImages` on [text to image](/api#tag/Start-generating/paths/~1v1~1text_to_image/post) to guide the illustration, with a prompt of up to 9,500 characters. `ratio` accepts only `auto`, which lets the model choose the framing of the SVG. To trace a source image instead, send one `imageUri` to `POST /v1/image_to_vector`. That endpoint takes no prompt, and `vectorizationMode` is `default` (the default, retains more detail) or `simple` (fewer shapes).

## Input asset aspect ratio requirements

For models that accept image or video references, the asset's aspect ratio (width ÷ height) must fall within the supported ranges below:

| Model                             | Input type                          | Min aspect ratio | Max aspect ratio |
| --------------------------------- | ----------------------------------- | ---------------- | ---------------- |
| Gen-4 Turbo Image-to-Video        | Prompt image                        | 0.5              | 2.358            |
| Gen-4 Image-to-Video              | Prompt image                        | 0.5              | 2.358            |
| Gen-4.5 Image-to-Video            | Prompt image                        | 0.5              | 2                |
| Act-Two                           | Character image                     | 0.5              | 2.358            |
| Act-Two                           | Character video                     | 0.5              | 2.358            |
| Act-Two                           | Reference video                     | 0.5              | 2.358            |
| Seedance 2.5 Image-to-Video       | Prompt image (first/last/reference) | 0.4              | 2.5              |
| Seedance 2.5 Text-to-Video        | Reference image                     | 0.4              | 2.5              |
| Seedance 2.5 Video-to-Video       | Reference image                     | 0.4              | 2.5              |
| Seedance 2 Image-to-Video         | Prompt image (first/last/reference) | 0.4              | 2.5              |
| Seedance 2 Text-to-Video          | Reference image                     | 0.4              | 2.5              |
| Seedance 2 Video-to-Video         | Reference image                     | 0.4              | 2.5              |
| Seedance 2.0 Fast Image-to-Video  | Prompt image (first/last/reference) | 0.4              | 2.5              |
| Seedance 2.0 Fast Text-to-Video   | Reference image                     | 0.4              | 2.5              |
| Seedance 2.0 Fast Video-to-Video  | Reference image                     | 0.4              | 2.5              |
| Seedance 2.0 Mini Image-to-Video  | Prompt image (first/last/reference) | 0.4              | 2.5              |
| Seedance 2.0 Mini Text-to-Video   | Reference image                     | 0.4              | 2.5              |
| Seedance 2.0 Mini Video-to-Video  | Reference image                     | 0.4              | 2.5              |
| MiniMax H3 Max Image-to-Video     | Prompt image (first/last)           | 0.2              | 4                |
| MiniMax H3 Image-to-Video         | Prompt image (first/last/reference) | 0.2              | 4                |
| MiniMax H3 Text-to-Video          | Reference image                     | 0.2              | 4                |
| MiniMax H3 Video-to-Video         | Reference image                     | 0.2              | 4                |
| MiniMax H3 Image Text-to-Image    | Reference image                     | 0.25             | 4                |
| Veo 3.1 / 3.1 Fast Image-to-Video | First/last keyframes                | 0.5              | 2                |
| HappyHorse 1.0 Image-to-Video     | Prompt image                        | 0.55             | 1.8              |
| Kling 4.0 Image-to-Video          | Prompt image (first/middle/last), reference image | 0.4 | 2.5              |
| Kling 4.0 Text-to-Video           | Reference image                     | 0.4              | 2.5              |
| Kling 4.0 Video-to-Video          | Reference image                     | 0.4              | 2.5              |
| Kling 2.5 Turbo Pro Image-to-Video | Prompt image (first/last)         | 0.4              | 2.5              |
| Kling 3.0 Image-to-Video          | Prompt image (first/last)           | 0.4              | 2.5              |
| Kling O3 Image-to-Video           | Prompt image (first/last), reference image | 0.4       | 2.5              |
| Kling O3 Video-to-Video           | Reference image                     | 0.4              | 2.5              |
| Kling 4.0 Flash                  | First frame, input/reference video | 0.4              | 2.5              |
| Gemini Omni 1.2 Flash Image-to-Video | First and last frames            | 0.5              | 2                |
| Gemini Omni Flash Image-to-Video  | Prompt image                        | 0.5              | 2                |
| Gemini 2.5 Flash Text-to-Image    | Reference image                     | 0.25             | 4                |
| Nano Banana 2.1 Text-to-Image     | Reference image                     | 0.25             | 4                |
| Nano Banana 2 Lite Text-to-Image  | Reference image                     | 0.25             | 4                |
| Ideogram 4.5 Text-to-Image        | Reference image, mask               | 0.167            | 6                |

Seedance models do not reject images outside their range. Before generation, the image is padded with black bars to the nearest supported aspect ratio: top and bottom for images wider than 2.5, left and right for images narrower than 0.4.
