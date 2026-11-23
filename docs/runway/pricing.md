---
title: API Pricing & Costs
description: Understand Runway Dev pricing and costs. View rates for Gen-4.5, Seedance, Kling, GPT Image and other models to budget for your AI video integration project.
---

Each generation you run on Runway Dev costs credits. Credits can be purchased
for $0.01 per credit in the developer portal for a project. Sales tax may
apply depending on your location. [Create an account](https://dev.runway.com/) to start building on Runway Dev.

Generations routed through a [Model Router](/model-routers) are billed at the standard rate of whichever model the router selects. The response metadata reports the model used and the realized cost in credits.

# Video Generation Pricing

| Model                     | Pricing                                                |
| ------------------        | ------------------------------------------------------ |
| `kling2.5_turbo_pro`      | 12 credits per second                                  |
| `kling3.0_standard` (no audio) | 9 credits per second                              |
| `kling3.0_standard` (audio) | 13 credits per second                                |
| `kling3.0_pro` (no audio) | 12 credits per second                                  |
| `kling3.0_pro` (audio)    | 17 credits per second                                  |
| `kling3.0_4k`             | 43 credits per second                                  |
| `klingO3_standard`        | 13 credits per second                                  |
| `klingO3_pro`             | 17 credits per second                                  |
| `klingO3_4k`              | 43 credits per second                                  |
| `kling_4_flash` (720p) | 9.4 credits per second without input video; with input video, 6.3 credits per second of output plus 6.3 credits per second of the greater of total input-video duration and output duration. Rounded up to the next credit; 29-credit minimum |
| `kling_4` (720p)          | 20% off through November 30, 2026 UTC: 12.56 credits per second without an input video; with an input video, 7.52 credits per second of output plus 7.52 credits per second of the greater of total input-video duration and output duration. List price: 15.7 and 9.4 credits per second |
| `kling_4` (1080p)         | 20% off through November 30, 2026 UTC: 18.8 credits per second without an input video; with an input video, 11.28 credits per second of output plus 11.28 credits per second of the greater of total input-video duration and output duration. List price: 23.5 and 14.1 credits per second |
| `wan3` (480p)             | 5 credits per second                                   |
| `wan3` (720p)             | 10 credits per second                                  |
| `wan3` (1080p)            | 20 credits per second                                  |
| `wan3_prime` (480p)       | 6.8 credits per second                                 |
| `wan3_prime` (720p)       | 14 credits per second                                  |
| `wan3_prime` (1080p)      | 28 credits per second                                  |
| `seedance2_5` (480p)      | 20 credits per second of output, plus 10 credits per second of input and reference video (combined video capped at 30 seconds); reference images and audio are free (80 credit minimum per generation) |
| `seedance2_5` (720p)      | 30 credits per second of output, plus 15 credits per second of input and reference video (combined video capped at 30 seconds); reference images and audio are free (80 credit minimum per generation) |
| `seedance2_5` (1080p)     | 68 credits per second of output, plus 34 credits per second of input and reference video (combined video capped at 30 seconds); reference images and audio are free (80 credit minimum per generation) |
| `seedance2_5` (4K)        | 110 credits per second of output, plus 57 credits per second of input and reference video (combined video capped at 30 seconds); reference images and audio are free (80 credit minimum per generation) |
| `seedance2_5_flash` (480p) | 13 credits per second of output, plus 7 credits per second of input and reference video (combined video capped at 30 seconds); reference images and audio are free (52 credit minimum per generation) |
| `seedance2_5_flash` (720p) | 20 credits per second of output, plus 10 credits per second of input and reference video (combined video capped at 30 seconds); reference images and audio are free (52 credit minimum per generation) |
| `grok_imagine_1_5` (480p) | 10 credits per second, plus 1 credit per image or audio reference (including an image-to-video start frame) |
| `grok_imagine_1_5` (720p) | 16 credits per second, plus 1 credit per image or audio reference (including an image-to-video start frame) |
| `grok_imagine_1_5` (1080p)| 29 credits per second, plus 1 credit per image or audio reference (including an image-to-video start frame) |
| `grok_imagine_1_5_lite` (480p) | 2 credits per second, plus 1 credit for an image-to-video start frame |
| `grok_imagine_1_5_lite` (720p) | 3 credits per second, plus 1 credit for an image-to-video start frame |
| `grok_imagine_1_5_lite` (1080p) | 14 credits per second, plus 1 credit for an image-to-video start frame |
| `seedance2` (480p)        | 14 credits per second (56 credit minimum per generation) |
| `seedance2` (720p)        | 30 credits per second (56 credit minimum per generation) |
| `seedance2` (1080p)       | 40 credits per second (56 credit minimum per generation) |
| `seedance2` (4K)          | 150 credits per second (56 credit minimum per generation) |
| `seedance2_fast` (480p)   | 11 credits per second (44 credit minimum per generation) |
| `seedance2_fast` (720p)   | 24 credits per second (44 credit minimum per generation) |
| `seedance2_mini` (480p)   | 7 credits per second (28 credit minimum per generation) |
| `seedance2_mini` (720p)   | 15 credits per second (28 credit minimum per generation) |
| `h3_max` (480p)           | 5 credits per second                                   |
| `h3_max` (768p)           | 8 credits per second                                   |
| `hailuo3` (768P)          | 10 credits per second, plus 2 credits per reference image or keyframe (including an image-to-video start frame); reference video billed at the same per-second rate as output (capped at 15 seconds) |
| `hailuo3` (2K)            | 15 credits per second, plus 2 credits per reference image or keyframe (including an image-to-video start frame); reference video billed at the same per-second rate as output (capped at 15 seconds) |
| `aleph2`                  | 28 credits per second (56 credit minimum per generation) |
| `gen4.5`                  | 12 credits per second                                  |
| `gen4_turbo`              | 5 credits per second                                   |
| `act_two`                 | 5 credits per second                                   |
| `veo3.1 (audio)`          | 40 credits per second                                  |
| `veo3.1 (no audio)`       | 20 credits per second                                  |
| `veo3.1_fast (audio)`     | 15 credits per second                                  |
| `veo3.1_fast (no audio)`  | 10 credits per second                                  |
| `happyhorse_1_0` (720p)   | 15 credits per second                                  |
| `happyhorse_1_0` (1080p)  | 30 credits per second                                  |
| `gemini_omni_flash` (text to video)  | 10 credits per second                       |
| `gemini_omni_flash` (image to video) | 10 credits per second, plus 1 credit for the first-frame image |
| `gemini_omni_flash` (video to video) | 11 credits per second of input video (capped at 10 seconds), plus 1 credit per reference image |
| `gemini_omni_flash_1.2` (360p) | 2 credits per second, plus 1 credit per reference image or keyframe and 1 credit per second of input video |
| `gemini_omni_flash_1.2` (720p) | 7 credits per second, plus 1 credit per reference image or keyframe and 1 credit per second of input video |
| `gemini_omni_flash_1.2` (1080p) | 10 credits per second, plus 1 credit per reference image or keyframe and 1 credit per second of input video |
| `gemini_omni_flash_1.2` (4K) | 21 credits per second, plus 1 credit per reference image or keyframe and 1 credit per second of input video |
| `gemini_omni_flash_1.1` (360p) | 3.4 credits per second, plus 1 credit per reference image (including an image-to-video start frame) and 1 credit per second of input video |
| `gemini_omni_flash_1.1` (720p) | 10 credits per second, plus 1 credit per reference image (including an image-to-video start frame) and 1 credit per second of input video |
| `gemini_omni_flash_1.1` (1080p) | 15 credits per second, plus 1 credit per reference image (including an image-to-video start frame) and 1 credit per second of input video |
| `gemini_omni_flash_1.1` (4K) | 30 credits per second, plus 1 credit per reference image (including an image-to-video start frame) and 1 credit per second of input video |

At 4K, a 5-second Seedance 2.5 generation without video references costs 550 credits ($5.50). Adding 5 seconds of input or reference video makes it 835 credits ($8.35): `5 × 110 + 5 × 57`. Image and audio references add no charge. The calculator below estimates output-only costs; add any input and reference video charges separately.

Seedance 2.5 draft mode uses these same rates. A preview (`draft: true` on text to video, image to video, or video to video) bills at the 480p rate. Enhancing that preview to 1080p (`draftTaskId` on text to video) bills at the 1080p rate for the same output duration and input video. The two calls are charged separately. See [draft mode](/guides/models#seedance-25-draft-mode). Seedance 2.5 and Seedance 2.5 Flash `outputFormat: "mov"` is billed at the same rates as the default `mp4`. Seedance 2.5 Flash has no draft mode. Seedance 2.0, 2.0 Fast, and 2.0 Mini bill `bitrate: "standard"` (the default) and `bitrate: "high"` at the same rates.

`audio` defaults to `true`. Kling 3.0 Standard and Pro use the no-audio rate when `audio` is `false`. Kling 3.0 4K uses the same rate either way. Kling O3 is billed at the rates above whether or not `audio` is `false`. Kling O3 video-to-video is billed per second of the input video.

Kling 4.0 includes audio and has no audio toggle. Charges are rounded up to the next credit. Through November 30, 2026 UTC, the list-price charge is rounded up, then discounted 20% and rounded up again — a 5 second 720p video without an input video is 64 credits. List prices apply from December 1, 2026 UTC. Input video is a video-to-video source or any reference video. Each input clip counts at most 30 seconds, and the combined input is capped at 30 seconds. A video edit uses the source video's length as the output duration.

## Professional and HDR output formats

These formats add a per-second surcharge on top of the model's rate. Available
on Gen-4.5 and Aleph 2.0 — see
[Professional outputs](/guides/professional-outputs#editorial-containers) for which
`outputFormat` values each model supports.

| Formats | Surcharge |
| ------- | --------- |
| `prores`, `png_sequence` | 5 credits per second |
| 10-bit and HDR profiles (`hdr10`, `hlg`, `sdr_rec709_10bit`, `hdr_pq_12bit_master`, `hdr_prores`, `hdr_png_sequence`, `hdr_exr_sequence`, `hdr_exr_acescg_sequence_1_3`, `hdr_exr_acescg_sequence_2_0`) | 20 credits per second; 40 credits per second when the output is larger than 4 megapixels (roughly 4K) |

`kling_4_flash` includes audio at the same price on every endpoint. Input-video duration is the sum of the source and reference clips, with each capped at 20 seconds and a combined 20-second budget. Image references have no separate charge. The total is rounded up once per generation. For example, a 5-second output without input video costs 47 credits; with 3 seconds of input video it costs 63 credits; with 10 seconds of input video it costs 95 credits. The calculator covers only requests without input video. The Kling 4.0 promotion does not apply to Flash.

`gemini_omni_flash_1.2` defaults to 720p. The total output, image, and input-video charges are rounded up to the next credit, with a 6-credit minimum per request. With `duration: "auto"`, generation and extension reserve 15 seconds of output, then settle to the generated duration rounded up to a whole second (3–15 seconds). Extension bills only the newly added output footage, plus the input video. Editing bills the input video's duration at the output rate, plus the input-video and reference-image charges. The calculator below does not include this model's reference charges or mode-specific billing; use these rates instead.

# Image Generation Pricing

| Model                     | Pricing                                                |
| ------------------        | ------------------------------------------------------ |
| `gen4_image`              | 5 credits per 720p image, or 8 credits per 1080p image |
| `gen4_image_turbo`        | 2 credits per image, any resolution                    |
| `muse_image`              | 1 credit per image, any resolution                     |
| `grok_imagine_image_2`    | 4–8 credits per image, by quality and resolution, plus 1 credit per reference image ([details](#grok-imagine-image-2)) |
| `minimax_h3_image`        | 3–18 credits per image, or 4–27 with `highspeed: true`, by resolution and reference count ([details](#minimax-h3-image)) |
| `seedream5.5`             | 2 credits per 1K or 1.5K image, 4 credits per 2K image, plus 0.8 credits per reference image ([details](#seedream-55)) |
| `seedream5.5_layers`      | 2 credits per 1K or 1.5K image, 4 credits per 2K or auto image, for the base image and each layer ([details](#seedream-55-layers)) |
| `seedream5_pro`           | 5 credits per 1K image, 9 credits per 2K image |
| `seedream5_pro_layers`    | 3 credits per 1K or 1.5K image, 5 credits per 2K or auto image, for the base image and each layer ([details](#seedream-5-pro-layers)) |
| `seedream5_lite`          | 4 credits per image, any resolution            |
| `seedream5_flash`         | 2 credits per image, any resolution            |
| `gemini_image3_pro`       | 20 credits per 1K or 2K image, 40 credits per 4K image |
| `gemini_image3.1_flash`   | 5 credits per 512px image, 7 credits per 1K image, 11 credits per 2K image, 16 credits per 4K image |
| `gemini_image3.1_flash_lite` | 4 credits per 1K image |
| `nano_banana_2.1`         | 4 credits per 1K image, 6 credits per 2K image, 12 credits per 4K image |
| `ideogram_4_5`            | 1–25 credits per image, by quality ([details](#ideogram-45-and-40)) |
| `ideogram_4_0`            | 4–11 credits per image, by quality ([details](#ideogram-45-and-40)) |
| `ideogram_vector`         | 11–35 credits per SVG, by endpoint, quality and references ([details](#ideogram-vector)) |
| `gpt_image_2`             | 1–41 credits per image, by quality and resolution ([details](#gpt-image-2)) |
| `gpt_image_2_6_flare`     | 2–19 credits per PNG, JPEG, or WebP image, plus 1 credit per reference image; GIF and SVG priced separately ([details](#gpt-image-26-flare-and-sunburst)) |
| `gpt_image_2_6_sunburst`  | 2–19 credits per PNG, JPEG, or WebP image, plus 1 credit per reference image; GIF and SVG priced separately ([details](#gpt-image-26-flare-and-sunburst)) |
| `gpt_image_2_5_flare`     | 1–75 credits per image, by quality, resolution and aspect ratio, plus 1 credit per reference image ([details](#gpt-image-25-flare-and-sunburst)) |
| `gpt_image_2_5_sunburst`  | 1–75 credits per image, by quality, resolution and aspect ratio, plus 1 credit per reference image ([details](#gpt-image-25-flare-and-sunburst)) |
| `bria_fibo_1_5`           | 5 credits per 1MP image, 10 credits per 4MP image      |
| `bria_fibo_edit_1_5`      | 5 credits per image                                    |
| `gemini_2.5_flash`        | 5 credits per image, any resolution                    |

## Grok Imagine Image 2

`grok_imagine_image_2` is billed as `outputCount × perImage + referenceCount × 1`. Reference images cost 1 credit each and are charged once per request, not per output image — for example, four 1K `medium` images with two references is `4 × 6 + 2` = 26 credits. Default quality is `medium`; anything other than `low` (including an omitted `quality`) bills as `medium`. `auto_1k` and `auto_2k` bill at the 1K and 2K tiers. A plain 1K generation is 6 credits (the minimum charge). With `outputCount` capped at 4 and references at 3, the maximum for a single request is 35 credits.

| Quality  | 1K (incl. `auto_1k`) | 2K (incl. `auto_2k`) |
| -------- | -------------------- | -------------------- |
| `low`    | 4                    | 6                    |
| `medium` | 6                    | 8                    |

## MiniMax H3 Image

`minimax_h3_image` is billed as `outputCount` times the credits per image below. `auto_1k`, `auto_2k`, and `auto_4k` use the 1K, 2K, and 4K columns. `highspeed` defaults to false. The rate of every generated image depends on how many reference images the request has, and adding one reference doesn't always change it. For example, one 2K Highspeed image with 4 reference images is 7 credits, and four text-only 4K images are 28 credits. The [cost calculator](#cost-calculator) works this out for any request.

| References | 1K | 2K | 4K | 1K Highspeed | 2K Highspeed | 4K Highspeed |
| ---------- | -- | -- | -- | ------------ | ------------ | ------------ |
| 0  | 3  | 3  | 7  | 4  | 4  | 14 |
| 1  | 3  | 3  | 8  | 5  | 5  | 14 |
| 2  | 4  | 4  | 8  | 6  | 6  | 15 |
| 3  | 4  | 5  | 8  | 7  | 7  | 16 |
| 4  | 5  | 5  | 9  | 7  | 7  | 17 |
| 5  | 6  | 6  | 10 | 8  | 8  | 18 |
| 6  | 6  | 7  | 11 | 9  | 9  | 19 |
| 7  | 7  | 8  | 11 | 10 | 10 | 19 |
| 8  | 8  | 8  | 12 | 11 | 11 | 20 |
| 9  | 9  | 9  | 13 | 12 | 12 | 21 |
| 10 | 9  | 10 | 14 | 13 | 13 | 22 |
| 11 | 10 | 11 | 14 | 13 | 14 | 23 |
| 12 | 11 | 12 | 15 | 14 | 14 | 24 |
| 13 | 12 | 12 | 16 | 15 | 15 | 25 |
| 14 | 12 | 13 | 17 | 16 | 16 | 25 |
| 15 | 13 | 14 | 18 | 17 | 17 | 26 |
| 16 | 14 | 15 | 18 | 18 | 18 | 27 |

## Seedream 5.5

`seedream5.5` is billed as `outputCount × (perImage + referenceCount × 0.8)`, rounded up to a whole credit per request. `auto_1k`, `auto_1.5k` and `auto_2k` bill at the 1K, 1.5K and 2K rates. For example, four 2K images with two reference images is `4 × (4 + 1.6)` = 22.4, charged as 23 credits.

## Seedream 5.5 Layers

`seedream5.5_layers` is billed per returned image, counting the base image and each layer, plus 0.8 credits for the source image, rounded up to a whole credit. A decomposition reserves credits for `maxImages` (default 30), then settles to the images returned. With the default, it reserves 61 credits at 1K or 1.5K and 121 credits at 2K or auto. For example, a 2K decomposition that returns a base image and 8 layers costs 37 credits. A task needs enough credits for the full reservation to start, so set a lower `maxImages` to reserve less.

## Seedream 5 Pro Layers

`seedream5_pro_layers` is billed per returned image, counting the base image and each layer. A decomposition returns at most 17 images (a base image plus 16 layers), so it reserves 51 credits at 1K or 1.5K and 85 credits at 2K or auto, then settles to the images returned. For example, a 2K decomposition that returns a base image and 8 layers costs 45 credits. A task needs enough credits for the full reservation to start.

## Ideogram 4.5 and 4.0

`ideogram_4_5` and `ideogram_4_0` are billed as credits per image × `outputCount`, at any resolution. `ideogram_4_5` defaults to `medium` when generating from reference images and `high` otherwise, including `preciseEdit`; `very_low` requires reference images and is not available with `preciseEdit`. `ideogram_4_0` defaults to `medium`. For example, four `medium` images on `ideogram_4_5` cost 32 credits.

| Quality    | `ideogram_4_5` | `ideogram_4_0` |
| ---------- | -------------- | -------------- |
| `very_low` | 1              | —              |
| `low`      | 4              | 4              |
| `medium`   | 8              | 7              |
| `high`     | 25             | 11             |

## Ideogram Vector

`ideogram_vector` returns one SVG per request. On text to image, it is billed by `quality`, which defaults to `medium`. `high` costs more when the request includes reference images. Converting an image on `POST /v1/image_to_vector` costs 11 credits, for either `vectorizationMode`.

| Request                                    | `ideogram_vector` |
| ------------------------------------------ | ----------------- |
| Text to image, `low`                       | 14                |
| Text to image, `medium`                    | 17                |
| Text to image, `high`                      | 22                |
| Text to image, `high` with reference images | 35               |
| Image to vector                            | 11                |

## GPT Image 2

`gpt_image_2` is billed as credits per image × `outputCount`. The `auto` resolution is billed at the 4K tier. Default quality is `high`. For example, four 1K `medium` images cost 20 credits.

| Quality  | 1K / 2K   | 4K (incl. `auto`) |
| -------- | --------- | ----------------- |
| `low`    | 1         | 2                 |
| `medium` | 5         | 11                |
| `high`   | 20        | 41                |
| `auto`   | 20        | 41                |

## GPT Image 2.6 Flare and Sunburst

For PNG, JPEG and WebP, `gpt_image_2_6_flare` and `gpt_image_2_6_sunburst` are billed on the tables below, at the same resolutions as [GPT Image 2.5](#gpt-image-25-flare-and-sunburst). `high` costs the same as on GPT Image 2.5, and `low` and `medium` cost more. `xhigh` and `max` are not supported. Both models default to `quality: "high"` and `reasoningEffort: "high"`. Reasoning effort does not change the price. `png`, `jpeg` and `webp` output cost the same. GPT Image 2.5's reference charges and `auto` settlement apply, with `outputCount` from 1–10 (default 1) and a minimum of 2 credits per image. With `ratio: "auto"`, the request is charged 9 credits at `low`, 16 at `medium` and 19 at `high` up front. For example, one 1K `high` square PNG with one reference image costs 12 credits.

**1K**

| Quality  | 1:1 | 4:5, 5:4 | 3:4, 4:3 | 2:3, 3:2 | 9:16, 16:9 | 21:9 |
| -------- | ---- | -------- | -------- | -------- | ---------- | ---- |
| `low`    | 5 | 4 | 4 | 3 | 2 | 2 |
| `medium` | 9 | 6 | 6 | 5 | 4 | 3 |
| `high`   | 11 | 8 | 7 | 6 | 5 | 4 |

**2K**

| Quality  | 1:1 | 4:5, 5:4 | 3:4, 4:3 | 2:3, 3:2 | 9:16, 16:9 | 21:9 |
| -------- | ---- | -------- | -------- | -------- | ---------- | ---- |
| `low`    | 8 | 5 | 5 | 4 | 3 | 3 |
| `medium` | 13 | 9 | 8 | 7 | 5 | 4 |
| `high`   | 16 | 11 | 10 | 8 | 6 | 5 |

**4K**

| Quality  | 1:1 | 4:5, 5:4 | 3:4, 4:3 | 2:3, 3:2 | 9:16, 16:9 | 21:9 |
| -------- | ---- | -------- | -------- | -------- | ---------- | ---- |
| `low`    | 9 | 8 | 7 | 6 | 5 | 4 |
| `medium` | 16 | 13 | 12 | 11 | 9 | 6 |
| `high`   | 19 | 15 | 14 | 13 | 11 | 7 |

**GIF output** is priced per animation by `quality` and `frameCount` (default 9). `frameDurationMs` does not change the price. Multiply the table value by `outputCount`.

| Frames | `low` | `medium` | `high` |
| ------ | ----- | -------- | ------ |
| 2–8    | 2     | 4        | 4      |
| 9–12   | 4     | 7        | 8      |
| 13–16  | 6     | 10       | 12     |

**SVG output** uses the PNG prices above plus a 50-credit authoring charge per output. With `ratio: "auto"`, the image portion follows the same deposit and settlement rules; the 50-credit charge remains. GIF and SVG do not accept reference images.

## GPT Image 2.5 Flare and Sunburst

`gpt_image_2_5_flare` and `gpt_image_2_5_sunburst` are billed on the tables below, as (credits per image + 1 credit per reference image) × `outputCount` — reference images are charged once per generated image, not once per request. The price per image depends on the quality, the resolution tier and the aspect ratio of `ratio`: square images cost the most, and wider or taller ones cost less. With `ratio: "auto"`, the request is charged the 4K square price up front, then settled at the square price of the tier the image was rendered at. Default quality is `high`. For example, one 2K `high` 16:9 image with two reference images costs 8 credits.

**1K** (1:1: `1920:1920`; 4:5, 5:4: `1536:1920`, `1920:1536`; 3:4, 4:3: `1440:1920`, `1920:1440`; 2:3, 3:2: `1280:1920`, `1920:1280`; 9:16, 16:9: `1088:1920`, `1920:1088`; 21:9: `2048:880`)

| Quality  | 1:1 | 4:5, 5:4 | 3:4, 4:3 | 2:3, 3:2 | 9:16, 16:9 | 21:9 |
| -------- | ---- | -------- | -------- | -------- | ---------- | ---- |
| `low`    | 2 | 1 | 1 | 1 | 1 | 1 |
| `medium` | 3 | 2 | 2 | 2 | 2 | 1 |
| `high`   | 11 | 8 | 7 | 6 | 5 | 4 |
| `xhigh`  | 19 | 13 | 12 | 10 | 8 | 6 |
| `max`    | 42 | 29 | 26 | 22 | 17 | 12 |

**2K** (1:1: `2560:2560`; 4:5, 5:4: `2048:2560`, `2560:2048`; 3:4, 4:3: `1920:2560`, `2560:1920`; 2:3, 3:2: `1712:2560`, `2560:1712`; 9:16, 16:9: `1440:2560`, `2560:1440`; 21:9: `2912:1248`)

| Quality  | 1:1 | 4:5, 5:4 | 3:4, 4:3 | 2:3, 3:2 | 9:16, 16:9 | 21:9 |
| -------- | ---- | -------- | -------- | -------- | ---------- | ---- |
| `low`    | 2 | 2 | 2 | 1 | 1 | 1 |
| `medium` | 4 | 3 | 3 | 2 | 2 | 2 |
| `high`   | 16 | 11 | 10 | 8 | 6 | 5 |
| `xhigh`  | 28 | 19 | 17 | 14 | 11 | 8 |
| `max`    | 63 | 43 | 38 | 31 | 24 | 18 |

**4K** (1:1: `2880:2880`; 4:5, 5:4: `2560:3200`, `3200:2560`; 3:4, 4:3: `2448:3264`, `3264:2448`; 2:3, 3:2: `2336:3504`, `3504:2336`; 9:16, 16:9: `2160:3840`, `3840:2160`; 21:9: `3840:1648`)

| Quality  | 1:1 | 4:5, 5:4 | 3:4, 4:3 | 2:3, 3:2 | 9:16, 16:9 | 21:9 |
| -------- | ---- | -------- | -------- | -------- | ---------- | ---- |
| `low`    | 3 | 2 | 2 | 2 | 2 | 1 |
| `medium` | 5 | 4 | 4 | 4 | 3 | 2 |
| `high`   | 19 | 15 | 14 | 13 | 11 | 7 |
| `xhigh`  | 34 | 27 | 25 | 23 | 19 | 12 |
| `max`    | 75 | 60 | 55 | 50 | 43 | 26 |

# Image Upscale Pricing

| Model                                | Pricing                                                           |
| ------------------------------------ | ----------------------------------------------------------------- |
| `magnific_precision_upscaler_v2`     | 25 credits per image, or 150 credits when output exceeds 4096px   |

# Video Upscale Pricing

`magnific_video_upscaler_creative` is billed per output frame, not per second of video. Credits = `ceil(USD / 0.01)`, where `USD = rate × fps × duration_seconds`. Minimum 1 credit per generation. When `fpsBoost` is enabled, output frame count may differ from input and affect cost. Frame-rate conversion on the same endpoint is billed separately — see [Enhance Frame Rate pricing](#enhance-frame-rate-pricing).

| Resolution | USD per frame | Example (10s @ 30fps) |
| ---------- | ------------- | --------------------- |
| `720p`, `1k` | $0.007      | 210 credits           |
| `2k`       | $0.009        | 270 credits           |
| `4k`       | $0.012        | 360 credits           |

# Enhance Frame Rate Pricing

Enhance Frame Rate (`enhance_frame_rate`) converts a video to a target frame rate on `POST /v1/video_upscale`. Billed per second of input.

| Model | Pricing |
| ----- | ------- |
| `enhance_frame_rate` | 1 credit per 2 seconds |

# SDR to HDR Pricing

Ruby (`ruby`) converts SDR video to true HDR on `POST /v1/video_to_hdr`. Billed
per second of output at the source's own resolution.

| Model | Pricing |
| ----- | ------- |
| `ruby` | 20 credits per second; 40 credits per second when the source is larger than 4 megapixels (roughly 4K) |

# Audio Generation Pricing

| Model                        | Pricing                                                |
| ------------------           | ------------------------------------------------------ |
| `seed_audio`                 | 0.25 credits per second (5 credit minimum per generation) |
| `eleven_v4`                  | 2.2 credits per 1,000 characters until October 12, 2026 PT, then 5 credits per 1,000 characters (minimum 1 credit) |
| `eleven_v3`                  | 1 credit per 50 characters (minimum 1 credit)          |
| `eleven_multilingual_v2`     | 1 credit per 50 characters                             |
| `eleven_text_to_sound_v2 (provided duration)`    | 1 credit per second of audio       |
| `eleven_text_to_sound_v2 (no duration)`    | 2 credits                              |
| `eleven_voice_isolation`     | 1 credit per 6s of audio                               |
| `eleven_voice_dubbing`       | 1 credit per 2s of audio                               |
| `eleven_multilingual_sts_v2` | 1 credit per 3s of audio                               |

# Real-time Pricing

| Model          | Pricing                                               |
| -------------- | ----------------------------------------------------- |
| `gwm1_avatars` (real-time sessions) | 2 credits upfront, then 2 credits per 6 seconds |
| `gwm1_avatars` (avatar videos, `POST /v1/avatar_videos`) | 1 credit per 3 seconds of video. Text scripts add 1 credit per 50 characters, rounded up, for speech generation (2 credit minimum per video) |

# Recipe Pricing

| Recipe                     | Pricing                                                |
| -------------------------- | ------------------------------------------------------ |
| `product_ad`               | 720p: 200 credits for a 4 second video, plus 36 credits per additional second.<br>1080p: 216 credits for a 4 second video, plus 40 credits per additional second.<br>(4 second minimum, 15 second maximum per generation) |
| `product_swap`             | 720p: 212 credits for a 4 second video, plus 36 credits per additional second.<br>1080p: 228 credits for a 4 second video, plus 40 credits per additional second.<br>(4 second minimum, 15 second maximum per generation) |
| `product_ugc`              | 720p: 192 credits for a 4 second video, plus 36 credits per additional second.<br>1080p: 208 credits for a 4 second video, plus 40 credits per additional second.<br>(4 second minimum, 15 second maximum per generation) |
| `multi_shot_video`         | 720p: 13 credits per second of video.<br>1080p: 17 credits per second of video.<br>(5 second minimum, 15 second maximum per generation) |
| `ad_localization`          | 21 credits per localized image |
| `marketing_stock_image`    | 8 credits per call for prompt processing, plus 1–20 credits per generated image by `quality` (same 1K/2K tiers as [Image Generation Pricing](#image-generation-pricing)) × `outputCount`. Default (`outputCount: 4`, `quality: high`): **88 credits** total. |
| `product_campaign_image`   | 36 credits per 1080p image (4 images generated per call) |

# Cost calculator

You can calculate the cost of your intended usage:

<div id="billing-calculator" class="mb-4">
  <div class="flex items-center space-x-4">
    <label for="num-images" class="whitespace-nowrap">Images:</label>
    <input type="number" id="num-images-1" min="1" value="1" class="w-20 px-2 bg-gray-700 border border-gray-600 rounded h-8 text-sm">
    <span class="whitespace-nowrap">x 720p <i>(5 credits)</i> + </span>
    <input type="number" id="num-images-2" min="1" value="1" class="w-20 px-2 bg-gray-700 border border-gray-600 rounded h-8 text-sm">
    <span class="whitespace-nowrap">x 1080p <i>(8 credits)</i></span>
      <span id="total-image-cost" class="mt-2"> = $0.13</span>
  </div>
  <div class="flex items-center space-x-4">
    <label for="h3img-count" class="whitespace-nowrap">MiniMax H3 Image:</label>
    <input type="number" id="h3img-count" min="1" max="10" value="1" class="w-20 px-2 bg-gray-700 border border-gray-600 rounded h-8 text-sm">
    <span class="whitespace-nowrap">x</span>
    <select id="h3img-resolution" aria-label="Resolution" class="px-2 bg-gray-700 border border-gray-600 rounded h-8 text-sm appearance-none">
      <option value="0">1K</option>
      <option value="1" selected>2K</option>
      <option value="2">4K</option>
    </select>
    <span class="whitespace-nowrap">with</span>
    <input type="number" id="h3img-references" aria-label="Reference images" min="0" max="16" value="0" class="w-20 px-2 bg-gray-700 border border-gray-600 rounded h-8 text-sm">
    <span class="whitespace-nowrap">references</span>
    <label for="h3img-highspeed" class="whitespace-nowrap"><input type="checkbox" id="h3img-highspeed"> Highspeed</label>
      <span id="h3img-cost" class="mt-2" aria-live="polite">= $0.03</span>
  </div>
  <div class="flex items-center space-x-4">
    <label for="num-videos" class="whitespace-nowrap">Videos:</label>
    <select id="vid-model" class="px-2 bg-gray-700 border border-gray-600 rounded h-8 text-sm appearance-none">
      <option value="kling2.5_turbo_pro">Kling 2.5 Turbo Pro</option>
      <option value="kling3.0_standard">Kling 3.0 Standard (no audio)</option>
      <option value="kling3.0_standard_audio">Kling 3.0 Standard (audio)</option>
      <option value="kling3.0_pro">Kling 3.0 Pro (no audio)</option>
      <option value="kling3.0_pro_audio">Kling 3.0 Pro (audio)</option>
      <option value="kling3.0_4k">Kling 3.0 4K</option>
      <option value="klingO3_standard">Kling O3 Standard</option>
      <option value="klingO3_pro">Kling O3 Pro</option>
      <option value="klingO3_4k">Kling O3 4K</option>
      <option value="kling_4_flash">Kling 4.0 Flash (720p, no input video)</option>
      <option value="kling_4">Kling 4.0 (720p, no input video)</option>
      <option value="kling_4_1080p">Kling 4.0 (1080p, no input video)</option>
      <option value="wan3_480p">WAN 3.0 (480p)</option>
      <option value="wan3_720p">WAN 3.0 (720p)</option>
      <option value="wan3">WAN 3.0 (1080p)</option>
      <option value="seedance2_5_480p">Seedance 2.5 (480p)</option>
      <option value="seedance2_5">Seedance 2.5 (720p)</option>
      <option value="seedance2_5_1080p">Seedance 2.5 (1080p)</option>
      <option value="seedance2_5_4k">Seedance 2.5 (4K)</option>
      <option value="seedance2_5_flash_480p">Seedance 2.5 Flash (480p)</option>
      <option value="seedance2_5_flash">Seedance 2.5 Flash (720p)</option>
      <option value="grok_imagine_1_5">Grok Imagine Video 1.5 (480p)</option>
      <option value="grok_imagine_1_5_lite_480p">Grok Imagine Video 1.5 Lite (480p)</option>
      <option value="grok_imagine_1_5_lite_720p">Grok Imagine Video 1.5 Lite (720p)</option>
      <option value="grok_imagine_1_5_lite_1080p">Grok Imagine Video 1.5 Lite (1080p)</option>
      <option value="seedance2_480p">Seedance 2.0 (480p)</option>
      <option value="seedance2">Seedance 2.0 (720p)</option>
      <option value="seedance2_fast_480p">Seedance 2.0 Fast (480p)</option>
      <option value="seedance2_fast">Seedance 2.0 Fast (720p)</option>
      <option value="seedance2_mini_480p">Seedance 2.0 Mini (480p)</option>
      <option value="seedance2_mini">Seedance 2.0 Mini (720p)</option>
      <option value="h3_max_480p">MiniMax H3 Max (480p)</option>
      <option value="h3_max">MiniMax H3 Max (768p)</option>
      <option value="hailuo3">MiniMax H3 (768P)</option>
      <option value="aleph2">Aleph 2.0</option>
      <option value="gemini_omni_flash">Gemini Omni Flash</option>
      <option value="gen4.5">Gen-4.5</option>
      <option value="ruby">Ruby</option>
      <option value="ruby_4k">Ruby (4K / &gt;4MP)</option>
      <option value="enhance_frame_rate">Enhance Frame Rate</option>
      <option value="g4t">Gen-4 Turbo</option>
      <option value="act-two">Act-Two</option>
    </select>
    <input type="number" id="num-videos" min="1" value="1" class="w-20 px-2 bg-gray-700 border border-gray-600 rounded h-8 text-sm">
    <label id="vid-label" class="whitespace-nowrap">video</label>
    <label for="vid-duration" class="whitespace-nowrap">x Duration:</label>
    <input type="number" id="vid-duration" min="1" value="1" class="w-20 px-2 bg-gray-700 border border-gray-600 rounded h-8 text-sm">
      <span id="total-cost" class="mt-2" aria-live="polite">=$0.25</span>
  </div>
</div>

<script>
  function calculateImageCost() {
    const numImages1 = Math.max(0, parseInt(document.getElementById('num-images-1').value) || 0);
    const numImages2 = Math.max(0, parseInt(document.getElementById('num-images-2').value) || 0);
    const totalCredits = numImages1 * 5 + numImages2 * 8;
    const costInDollars = (totalCredits * 0.01).toFixed(2);
    document.getElementById('total-image-cost').textContent = `=  $${costInDollars}`;
  }

  // Credits per image by reference count (0–16), as [1K, 2K, 4K]. Must match the MiniMax H3 Image table above.
  const minimaxH3ImageCredits = {
    standard: [
      [3, 3, 7], [3, 3, 8], [4, 4, 8], [4, 5, 8], [5, 5, 9], [6, 6, 10], [6, 7, 11], [7, 8, 11], [8, 8, 12],
      [9, 9, 13], [9, 10, 14], [10, 11, 14], [11, 12, 15], [12, 12, 16], [12, 13, 17], [13, 14, 18], [14, 15, 18],
    ],
    highspeed: [
      [4, 4, 14], [5, 5, 14], [6, 6, 15], [7, 7, 16], [7, 7, 17], [8, 8, 18], [9, 9, 19], [10, 10, 19], [11, 11, 20],
      [12, 12, 21], [13, 13, 22], [13, 14, 23], [14, 14, 24], [15, 15, 25], [16, 16, 25], [17, 17, 26], [18, 18, 27],
    ],
  };

  function calculateMinimaxH3ImageCost() {
    const output = document.getElementById('h3img-cost');
    const count = Number(document.getElementById('h3img-count').value);
    const references = Number(document.getElementById('h3img-references').value);
    if (!(Number.isInteger(count) && count >= 1 && count <= 10)) {
      output.textContent = 'Enter 1 to 10 images.';
      return;
    }
    if (!(Number.isInteger(references) && references >= 0 && references <= 16)) {
      output.textContent = 'Enter 0 to 16 references.';
      return;
    }
    const mode = document.getElementById('h3img-highspeed').checked ? 'highspeed' : 'standard';
    const resolution = Number(document.getElementById('h3img-resolution').value);
    const credits = count * minimaxH3ImageCredits[mode][references][resolution];
    output.textContent = `=  $${(credits * 0.01).toFixed(2)} (${credits} credits)`;
  }

  function calculateVideoCost() {
    const kling4Promo = Date.now() < Date.UTC(2026, 11, 1);
    const costPerSecond = {
      'kling2.5_turbo_pro': 12,
      'kling3.0_standard': 9,
      'kling3.0_standard_audio': 13,
      'kling3.0_pro': 12,
      'kling3.0_pro_audio': 17,
      'kling3.0_4k': 43,
      'klingO3_standard': 13,
      'klingO3_pro': 17,
      'klingO3_4k': 43,
      'kling_4_flash': 9.4,
      'kling_4': 15.7,
      'kling_4_1080p': 23.5,
      'h3_max': 8,
      'h3_max_480p': 5,
      'wan3': 20,
      'wan3_720p': 10,
      'wan3_480p': 5,
      'gen4.5': 12,
      'aleph2': 28,
      'g4t': 5,
      'act-two': 5,
      'seedance2_5': 30,
      'seedance2_5_1080p': 68,
      'seedance2_5_4k': 110,
      'seedance2_5_480p': 20,
      'seedance2_5_flash': 20,
      'seedance2_5_flash_480p': 13,
      'grok_imagine_1_5': 10,
      'grok_imagine_1_5_lite_480p': 2,
      'grok_imagine_1_5_lite_720p': 3,
      'grok_imagine_1_5_lite_1080p': 14,
      'ruby': 20,
      'ruby_4k': 40,
      'enhance_frame_rate': 0.5,
      'seedance2': 30,
      'seedance2_480p': 14,
      'seedance2_fast': 24,
      'seedance2_fast_480p': 11,
      'seedance2_mini': 15,
      'seedance2_mini_480p': 7,
      'hailuo3': 10,
      'gemini_omni_flash': 10,
    };
    const minimumCredits = {
      'kling_4_flash': 29,
      'aleph2': 56,
      'seedance2_5': 80,
      'seedance2_5_1080p': 80,
      'seedance2_5_4k': 80,
      'seedance2_5_480p': 80,
      'seedance2_5_flash': 52,
      'seedance2_5_flash_480p': 52,
      'seedance2': 56,
      'seedance2_480p': 56,
      'seedance2_fast': 44,
      'seedance2_fast_480p': 44,
      'seedance2_mini': 28,
      'seedance2_mini_480p': 28,
    };
    // Accepted duration range in seconds, for models whose limits are documented.
    const durationLimits = {
      'seedance2_5': [4, 30],
      'seedance2_5_1080p': [4, 30],
      'seedance2_5_4k': [4, 30],
      'seedance2_5_480p': [4, 30],
      'seedance2_5_flash': [4, 30],
      'seedance2_5_flash_480p': [4, 30],
    };
    const roundedUpModels = new Set(['kling_4_flash', 'kling_4', 'kling_4_1080p']);
    const promoDiscount = {
      'kling_4': kling4Promo ? 0.8 : 1,
      'kling_4_1080p': kling4Promo ? 0.8 : 1,
    };
    const ceilCredits = (credits) => Math.ceil(Number(credits.toFixed(6)));
    const model = document.getElementById('vid-model').value;
    const videoCostPerSecond = costPerSecond[model] || 0;
    
    const numVideos = Math.max(0, parseInt(document.getElementById('num-videos').value) || 0);
    const durationInput = document.getElementById('vid-duration');
    const limits = durationLimits[model];
    durationInput.min = limits ? String(limits[0]) : '1';
    durationInput.max = limits ? String(limits[1]) : '';
    const rawDuration = Number(durationInput.value);
    const duration = Math.max(0, Math.floor(rawDuration) || 0);

    // Update label to be singular or plural
    document.getElementById('vid-label').textContent = numVideos === 1 ? 'video' : 'videos';

    if (limits && !(Number.isInteger(rawDuration) && rawDuration >= limits[0] && rawDuration <= limits[1])) {
      document.getElementById('total-cost').textContent = `Enter a whole-number duration from ${limits[0]} to ${limits[1]} seconds.`;
      return;
    }

    let perVideoCredits = Math.max(
      duration * videoCostPerSecond,
      minimumCredits[model] ?? 0
    );
    if (roundedUpModels.has(model)) {
      perVideoCredits = ceilCredits(perVideoCredits);
    }
    if (model in promoDiscount) {
      perVideoCredits = ceilCredits(perVideoCredits * promoDiscount[model]);
    }
    const totalCredits = numVideos * perVideoCredits;
    const costInDollars = (totalCredits * 0.01).toFixed(2);
    document.getElementById('total-cost').textContent = `=  $${costInDollars}`;
  }

  document.getElementById('num-images-1').addEventListener('input', calculateImageCost);
  document.getElementById('num-images-2').addEventListener('input', calculateImageCost);
  document.getElementById('num-videos').addEventListener('input', calculateVideoCost);
  document.getElementById('vid-duration').addEventListener('input', calculateVideoCost);
  document.getElementById('vid-model').addEventListener('change', calculateVideoCost);
  for (const id of ['h3img-count', 'h3img-references']) {
    document.getElementById(id).addEventListener('input', calculateMinimaxH3ImageCost);
  }
  for (const id of ['h3img-resolution', 'h3img-highspeed']) {
    document.getElementById(id).addEventListener('change', calculateMinimaxH3ImageCost);
  }

  calculateVideoCost();
  calculateMinimaxH3ImageCost();
</script>

<style>
  #billing-calculator input[type="number"]::-webkit-inner-spin-button,
  #billing-calculator input[type="number"]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
  #billing-calculator input[type="number"] {
    -moz-appearance: textfield;
    max-width: 80px;
    background-color: var(--sl-color-black);
    border: 1px var(--sl-color-gray-5) solid;
    border-radius: 5px;
    padding: 0 0.5em;
  }
  #billing-calculator select {
    padding: 0.25em;
    border: 1px var(--sl-color-gray-5) solid;
    border-radius: 5px;
  }

  #total-cost {
    padding: 5px;
  }

  label {
    padding: 5px;
  }
</style>
