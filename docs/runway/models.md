---
title: Available AI Models
description: Explore available AI models in Runway Dev. Learn about Gen-4.5 and models from other leading labs for video and image creation in your applications.
---

The API supports the models below. See [pricing](/guides/pricing) for per-model costs. [Create an account](https://dev.runway.com/) to start building on Runway Dev.

HDR, pipeline formats, and upscaling an existing video are covered in [Professional outputs](/guides/professional-outputs).

<Aside type="note" title="Prefer not to decide the right model yourself?">
  Use a [Model Router](/model-routers) to automatically route each request to the best available model based on your cost, latency, or quality preferences. No additional cost.
</Aside>

<ModelCatalog />

For audio-only speech with Eleven v4, Eleven v3, or Multilingual v2, you can use a voice designed or cloned through the Voices API. See [generating speech with a custom voice](/characters/custom-voice#generating-speech-with-a-custom-voice).

## Kling 4.0 multi-shot prompts

To generate several shots in one Kling 4.0 video, describe the shot order, time ranges, and transitions in `promptText`. Set `duration` to the total clip length, with the shot ranges covering that duration.

For example, this [text-to-video](/api#tag/Start-generating/paths/~1v1~1text_to_video/post) request asks for an 8-second video with cuts at 2 and 6 seconds:

\<Code code={codeSample\`
import RunwayML from '@runwayml/sdk';

```
const client = new RunwayML();
const task = await client.textToVideo
  .create({
    model: 'kling_4',
    promptText: [
      "An 8-second film with exactly three distinct camera shots and hard cuts at 2 " +
      "seconds and 6 seconds. Keep the same objects and kitchen throughout. No dissolves, " +
      "no text, no extra shots.",
      "SHOT 1 — 0–2 seconds: SHOT 1. Wide frontal view of a glossy red ceramic teapot and " +
      "a white cup on a pale wooden table in a sunlit kitchen. A hand reaches for the " +
      "teapot. Locked camera. Photorealistic.",
      "SHOT 2 — 2–6 seconds: SHOT 2. Hard cut to a tight side close-up of the same glossy " +
      "red ceramic teapot pouring amber tea into the same white cup on the pale wooden " +
      "table. Only the spout, tea stream and cup are visible. Photorealistic.",
      "SHOT 3 — 6–8 seconds: SHOT 3. Hard cut to a directly overhead view of the same " +
      "white cup full of amber tea beside the same red ceramic teapot on the pale wooden " +
      "table. The hand exits. Locked camera. Photorealistic.",
    ].join('\\n'),
    ratio: '1280:720',
    duration: 8,
  })
  .waitForTaskOutput();

console.log(task.output);
`.trim()} lang="ts" />
```

Shot timings are instructions to the model, not frame-exact edit points. Review the generated clip when precise pacing matters. See [Kling's prompting guide](https://kling.ai/quickstart/kling-4-model-user-guide) for more examples.

To try this in the [Playground](https://dev.runway.com/playground), choose Kling 4.0 text-to-video, paste the shot list into the prompt field, and set the duration to 8 seconds.

## Seedream 5 Pro Layers

Seedream 5 Pro Layers (`seedream5_pro_layers`) separates one source image into a base image and editable transparent layers. Send one image to `POST /v1/text_to_image`; `promptText` is optional and can describe how to split the image. The default prompt asks the model to split the image automatically.

`resolution` accepts `auto` (the default), `1k`, `1.5k`, or `2k`. `optimizePromptMode` accepts `standard` (the default) or `fast`. `outputFormat` sets the base image format to `png` (the default) or `jpeg`; separated layers are always PNG with transparency. The request returns one decomposition, regardless of resolution.

```json
{
  "model": "seedream5_pro_layers",
  "referenceImages": [
    { "uri": "https://example.com/source.png" }
  ],
  "promptText": "Separate the title, plant, cup, and sun into layers",
  "resolution": "2k",
  "optimizePromptMode": "standard",
  "outputFormat": "png"
}
```

When the task succeeds, `output` contains the image URLs and `layers` describes the separated layers. Each layer's `uri` matches the output URL at the same index. Layer details may include a `name`, `zIndex` (stacking order), and `boundingBox` in absolute and normalized coordinates. See [image input requirements](/assets/inputs#seedream-layers-inputs) and [pricing](/guides/pricing#seedream-5-pro-layers).

## Seedream 5.5 Layers

Seedream 5.5 Layers (`seedream5.5_layers`) separates one source image into a base image and editable transparent layers, in the same way as [Seedream 5 Pro Layers](#seedream-5-pro-layers). Send one image to `POST /v1/text_to_image`; `promptText` is optional and can describe which elements to separate.

`resolution` accepts `auto` (the default), `1k`, `1.5k`, or `2k`. `outputFormat` sets the base image format to `png` (the default) or `jpeg`; separated layers are always PNG with transparency. `maxImages` sets the most images the task may return, counting the base image, from 2–100 (default 30). `optimizePromptMode` is not supported.

```json
{
  "model": "seedream5.5_layers",
  "referenceImages": [
    { "uri": "https://example.com/source.png" }
  ],
  "promptText": "Separate the title, plant, cup, and sun into layers",
  "resolution": "2k",
  "outputFormat": "png",
  "maxImages": 12
}
```

The completed task has the same `output` and `layers` fields as Seedream 5 Pro Layers. Each returned image is billed, so a lower `maxImages` lowers the credits a task needs to start. See [image input requirements](/assets/inputs#seedream-layers-inputs) and [pricing](/guides/pricing#seedream-55-layers).

## Seedance 2.5 4K output

Choose 4K output with a pixel `ratio` on [text to video](/api#tag/Start-generating/paths/~1v1~1text_to_video/post), [image to video](/api#tag/Start-generating/paths/~1v1~1image_to_video/post), or [video to video](/api#tag/Start-generating/paths/~1v1~1video_to_video/post) in `reference` mode. Use `ratio`, not a separate `resolution` parameter. Omitting it still defaults to 720p (`1280:720`).

| Aspect ratio | 4K `ratio` |
| --- | --- |
| 21:9 | `3840:1646` |
| 16:9 | `3840:2160` |
| 4:3 | `3840:2880` |
| 1:1 | `3840:3840` |
| 3:4 | `2880:3840` |
| 9:16 | `2160:3840` |

For example, send this body to `POST /v1/text_to_video`:

```json
{
  "model": "seedance2_5",
  "promptText": "A red panda walks through a lantern-lit alley",
  "ratio": "3840:2160",
  "duration": 5
}
```

Durations remain 4–30 seconds, or `auto`. Video-to-video `extend` and `edit` modes do not accept a ratio and do not render at 4K. Draft previews remain 480p, and enhancing a draft produces 1080p, not 4K. See [pricing](/guides/pricing#video-generation-pricing), [input requirements](/assets/inputs), and [usage limits](/usage/tiers).

## Seedance 2.5 draft mode

Seedance 2.5 (`seedance2_5`) can render a faster 480p preview, then enhance that preview to 1080p. Use a preview to check a prompt, then pay the 1080p rate for the take you keep. See [pricing](/guides/pricing) for both rates.

### Render a preview

Set `draft` to `true` on a normal [text to video](/api#tag/Start-generating/paths/~1v1~1text_to_video/post), [image to video](/api#tag/Start-generating/paths/~1v1~1image_to_video/post), or [video to video](/api#tag/Start-generating/paths/~1v1~1video_to_video/post) request. Prompt, `ratio`, `duration` (including `auto`), references, `audio`, and `seed` work the same way as a full generation.

The preview is always 480p `.mp4`, and it is billed at the 480p rate. `outputFormat: "mov"` is rejected with `draft: true`, and the enhanced 1080p take is `.mp4` too. `ratio` still chooses the aspect ratio: a 720p, 1080p, or 4K ratio is accepted, and the preview uses the 480p frame for that aspect (16:9 / 9:16 land on `854:480` / `480:854`).

```json
{
  "model": "seedance2_5",
  "promptText": "A red panda walks through a lantern-lit alley",
  "ratio": "1280:720",
  "duration": 5,
  "draft": true
}
```

Poll the returned task until `status` is `SUCCEEDED`. The task id is what you pass to enhance it.

### Enhance a preview to 1080p

Enhancement is always a [text to video](/api#tag/Start-generating/paths/~1v1~1text_to_video/post) request, including when the preview came from image to video or video to video. Send `model` and `draftTaskId` only. The 1080p video reuses the preview's prompt, references, duration, seed, and audio setting — when the preview used `duration: "auto"`, the enhancement uses the measured length. An enhance request that also includes `promptText`, `ratio`, `duration`, `seed`, `audio`, references, or `draft` is rejected.

```json
{
  "model": "seedance2_5",
  "draftTaskId": "11111111-1111-4111-8111-111111111111"
}
```

The preview task has to belong to the same account, have succeeded, and have been created with `draft: true`. Previews can be enhanced within 7 days of creation. The result is 1080p at the preview's aspect ratio, billed at the 1080p rate for that output duration and any input video. The preview's charge is unchanged.

## Seedance 2.5 video to video modes

On [video to video](/api#tag/Start-generating/paths/~1v1~1video_to_video/post), `mode` sets how Seedance 2.5 uses `promptVideo`:

| `mode` | What it does | Requirements |
| --- | --- | --- |
| `reference` (default) | Generates a new video conditioned on the input video | Accepts `duration` and `ratio` |
| `extend` | Continues the input video | Requires `promptText`; does not accept `ratio` |
| `edit` | Changes the input video in place | Requires `promptText` and `duration: "auto"`; does not accept `ratio` |

`extend` and `edit` keep the input video's aspect ratio. They render at 1080p when the input video is larger than 720p, and at 720p otherwise.

```json
{
  "model": "seedance2_5",
  "promptVideo": "https://example.com/input.mp4",
  "promptText": "Change the jacket to red leather",
  "mode": "edit",
  "duration": "auto"
}
```

<table hidden>
  <caption>Model index</caption>
  <thead>
    <tr><th>Model</th><th>Model ID</th><th>Category</th></tr>
  </thead>
  <tbody>
    <tr><td>Kling 4.0</td><td><code>kling_4</code></td><td>Video</td></tr>
    <tr><td>Seedance 2.5</td><td><code>seedance2_5</code></td><td>Video</td></tr>
    <tr><td>Seedance 2.5 Flash</td><td><code>seedance2_5_flash</code></td><td>Video</td></tr>
    <tr><td>Seedance 2.0</td><td><code>seedance2</code></td><td>Video</td></tr>
    <tr><td>Seedance 2.0 Fast</td><td><code>seedance2_fast</code></td><td>Video</td></tr>
    <tr><td>Seedance 2.0 Mini</td><td><code>seedance2_mini</code></td><td>Video</td></tr>
    <tr><td>Aleph 2.0</td><td><code>aleph2</code></td><td>Video</td></tr>
    <tr><td>Gen-4.5</td><td><code>gen4.5</code></td><td>Video</td></tr>
    <tr><td>Gen-4 Turbo</td><td><code>gen4_turbo</code></td><td>Video</td></tr>
    <tr><td>Kling 3.0 Pro</td><td><code>kling3.0_pro</code></td><td>Video</td></tr>
    <tr><td>Kling O3 Pro</td><td><code>klingO3_pro</code></td><td>Video</td></tr>
    <tr><td>MiniMax H3</td><td><code>hailuo3</code></td><td>Video</td></tr>
    <tr><td>MiniMax H3 Max</td><td><code>h3_max</code></td><td>Video</td></tr>
    <tr><td>WAN 3.0</td><td><code>wan3</code></td><td>Video</td></tr>
    <tr><td>WAN 3.0 Prime</td><td><code>wan3_prime</code></td><td>Video</td></tr>
    <tr><td>Grok Imagine Video 1.5</td><td><code>grok_imagine_1_5</code></td><td>Video</td></tr>
    <tr><td>Grok Imagine Video 1.5 Lite</td><td><code>grok_imagine_1_5_lite</code></td><td>Video</td></tr>
    <tr><td>HappyHorse 1.0</td><td><code>happyhorse_1_0</code></td><td>Video</td></tr>
    <tr><td>Veo 3.1</td><td><code>veo3.1</code></td><td>Video</td></tr>
    <tr><td>Veo 3.1 Fast</td><td><code>veo3.1_fast</code></td><td>Video</td></tr>
    <tr><td>Gemini Omni Flash 1.1</td><td><code>gemini_omni_flash_1.1</code></td><td>Video</td></tr>
    <tr><td>Gemini Omni Flash</td><td><code>gemini_omni_flash</code></td><td>Video</td></tr>
    <tr><td>Act-Two</td><td><code>act_two</code></td><td>Video</td></tr>
    <tr><td>Kling 3.0 Standard</td><td><code>kling3.0_standard</code></td><td>Video</td></tr>
    <tr><td>Kling 3.0 4K</td><td><code>kling3.0_4k</code></td><td>Video</td></tr>
    <tr><td>Kling O3 Standard</td><td><code>klingO3_standard</code></td><td>Video</td></tr>
    <tr><td>Kling O3 4K</td><td><code>klingO3_4k</code></td><td>Video</td></tr>
    <tr><td>Kling 2.5 Turbo Pro</td><td><code>kling2.5_turbo_pro</code></td><td>Video</td></tr>
    <tr><td>Kling 4.0 Flash</td><td><code>kling_4_flash</code></td><td>Video</td></tr>
    <tr><td>MiniMax H3 Image</td><td><code>minimax_h3_image</code></td><td>Image</td></tr>
    <tr><td>GPT Image 2.6 Flare</td><td><code>gpt_image_2_6_flare</code></td><td>Image</td></tr>
    <tr><td>GPT Image 2.6 Sunburst</td><td><code>gpt_image_2_6_sunburst</code></td><td>Image</td></tr>
    <tr><td>Gemini Omni 1.2 Flash</td><td><code>gemini_omni_flash_1.2</code></td><td>Video</td></tr>
    <tr><td>GPT Image 2.5 Sunburst</td><td><code>gpt_image_2_5_sunburst</code></td><td>Image</td></tr>
    <tr><td>GPT Image 2.5 Flare</td><td><code>gpt_image_2_5_flare</code></td><td>Image</td></tr>
    <tr><td>GPT Image 2</td><td><code>gpt_image_2</code></td><td>Image</td></tr>
    <tr><td>Nano Banana 2.1</td><td><code>nano_banana_2.1</code></td><td>Image</td></tr>
    <tr><td>Ideogram 4.5</td><td><code>ideogram_4_5</code></td><td>Image</td></tr>
    <tr><td>Ideogram 4.0</td><td><code>ideogram_4_0</code></td><td>Image</td></tr>
    <tr><td>Ideogram Vector</td><td><code>ideogram_vector</code></td><td>Image</td></tr>
    <tr><td>Nano Banana 2</td><td><code>gemini_image3.1_flash</code></td><td>Image</td></tr>
    <tr><td>Nano Banana 2 Lite</td><td><code>gemini_image3.1_flash_lite</code></td><td>Image</td></tr>
    <tr><td>Nano Banana Pro</td><td><code>gemini_image3_pro</code></td><td>Image</td></tr>
    <tr><td>Nano Banana</td><td><code>gemini_2.5_flash</code></td><td>Image</td></tr>
    <tr><td>Seedream 5.5</td><td><code>seedream5.5</code></td><td>Image</td></tr>
    <tr><td>Seedream 5.5 Layers</td><td><code>seedream5.5_layers</code></td><td>Image</td></tr>
    <tr><td>Seedream 5.0 Pro</td><td><code>seedream5_pro</code></td><td>Image</td></tr>
    <tr><td>Seedream 5 Pro Layers</td><td><code>seedream5_pro_layers</code></td><td>Image</td></tr>
    <tr><td>Seedream 5.0 Lite</td><td><code>seedream5_lite</code></td><td>Image</td></tr>
    <tr><td>Seedream 5.0 Flash</td><td><code>seedream5_flash</code></td><td>Image</td></tr>
    <tr><td>Grok Imagine Image 2</td><td><code>grok_imagine_image_2</code></td><td>Image</td></tr>
    <tr><td>Muse Image</td><td><code>muse_image</code></td><td>Image</td></tr>
    <tr><td>FIBO 1.5</td><td><code>bria_fibo_1_5</code></td><td>Image</td></tr>
    <tr><td>FIBO Edit 1.5</td><td><code>bria_fibo_edit_1_5</code></td><td>Image</td></tr>
    <tr><td>Gen-4 Image Turbo</td><td><code>gen4_image_turbo</code></td><td>Image</td></tr>
    <tr><td>Gen-4 Image</td><td><code>gen4_image</code></td><td>Image</td></tr>
    <tr><td>Characters</td><td><code>gwm1_avatars</code></td><td>Real-time</td></tr>
    <tr><td>Magnific Precision Upscaler</td><td><code>magnific_precision_upscaler_v2</code></td><td>Upscale &amp; HDR</td></tr>
    <tr><td>Magnific Video Upscaler</td><td><code>magnific_video_upscaler_creative</code></td><td>Upscale &amp; HDR</td></tr>
    <tr><td>Enhance Frame Rate</td><td><code>enhance_frame_rate</code></td><td>Upscale &amp; HDR</td></tr>
    <tr><td>Ruby</td><td><code>ruby</code></td><td>Upscale &amp; HDR</td></tr>
    <tr><td>Eleven v4</td><td><code>eleven_v4</code></td><td>Audio</td></tr>
    <tr><td>Eleven v3</td><td><code>eleven_v3</code></td><td>Audio</td></tr>
    <tr><td>Multilingual v2</td><td><code>eleven_multilingual_v2</code></td><td>Audio</td></tr>
    <tr><td>ElevenLabs Sound Effects</td><td><code>eleven_text_to_sound_v2</code></td><td>Audio</td></tr>
    <tr><td>ElevenLabs Voice Isolation</td><td><code>eleven_voice_isolation</code></td><td>Audio</td></tr>
    <tr><td>ElevenLabs Voice Dubbing</td><td><code>eleven_voice_dubbing</code></td><td>Audio</td></tr>
    <tr><td>Multilingual Speech to Speech</td><td><code>eleven_multilingual_sts_v2</code></td><td>Audio</td></tr>
    <tr><td>Seed Audio 1.0</td><td><code>seed_audio</code></td><td>Audio</td></tr>
  </tbody>
</table>
