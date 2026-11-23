## Start generating

### POST /v1/video_to_video

Video to video

This endpoint will start a new task to generate a video from a video.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 17 shapes, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/video_to_video - model `aleph2`

- `promptText` (string) - max length 1000. A non-empty and optional string describing what should appear in the output.
- `keyframes` (array of object) - min 1 items; max 5 items. Timed guidance images placed at specific points in the input video. Up to 5 keyframes.
  - `uri` (string, required)
  - `seconds` (number) - 0-30. Absolute timestamp in seconds from the start of the input video when this guidance image should apply.
  - `range` (object)
    - `start_seconds` (integer, required)
    - `end_seconds` (integer, required)
  - `at` (number) - 0-1. Position as a fraction [0.0, 1.0] of the input video duration when this guidance image should apply.
- `videoUri` (string, required) - The input video to edit. Must be 30 seconds or shorter.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `ratio` (string)
- `targetAspectRatio` (string) - one of `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `21:9`. Target aspect ratio for expand/outpaint. Letterboxes the input video and keyframes before generation.
- `contentModeration` (object) - Settings that affect the behavior of the content moderation system.
  - `publicFigureThreshold` (string) - one of `auto`, `low`. When set to `low`, the content moderation system will be less strict about preventing generations that include recognizable public figures.
- `outputFormat` (string) - one of `mp4`, `prores`, `png_sequence`, `sdr_rec709_10bit`. The container/encoding of the output. `mp4` (default) returns an H.264 .mp4. `prores` returns a ProRes .mov. `png_sequence` returns a .zip of PNG frames. `sdr_rec709_10bit` returns a 10-bit Rec.709 HEVC .mp4 for SDR g...
- `proresProfile` (string) - one of `422`, `4444`, `422 Proxy`, `422 LT`, `422 HQ`, `4444 XQ`. The ProRes profile to use. Only valid when `outputFormat` is `prores`. Defaults to `4444`. Note: generated content contains no transparency - the alpha channel in `4444` / `4444 XQ` outputs is present but fully opaque...
- `model` (string, required) - one of `aleph2`

#### POST /v1/video_to_video - model `klingO3_4k`

- `providerSettings` (object) - default `{"keepOriginalSound":true}`. Provider-specific settings for multishot video generation and video editing.
  - `multiPrompt` (array of object) - min 1 items; max 6 items. An array of prompt segments for multishot video generation. Each segment has its own prompt and duration. Total duration across all segments must be between 3 and 15 seconds. `promptText` is still required when `shotT...
    - `prompt` (string, required) - max length 512. The text prompt for this segment.
    - `duration` (integer, required) - 1-15. Duration in seconds for this segment.
  - `shotType` (string) - one of `intelligence`, `customize`. Shot transition type for multishot videos. Defaults to "customize" when multiPrompt is provided.
  - `keepOriginalSound` (boolean) - default `true`. Whether to preserve the original audio when editing a video. Only applicable for video-to-video. Defaults to true.
- `promptText` (string, required) - max length 2500. A text prompt describing what should appear in the output video.
- `promptVideo` (string, required) - The input video to edit. Must be at most 10 seconds long, with width and height each between 720px and 3840px.
- `references` (string or array of object) - An optional array of reference images (up to 4). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `position` (string) - one of `first`, `last`. The position of the image in the output video. "first" will use the image as the first frame, "last" as the last frame. Omit for a reference image.
- `model` (string, required) - one of `klingO3_4k`

#### POST /v1/video_to_video - model `hailuo3`

- `promptVideo` (string, required) - The input video to use as a reference for the output video. If additional video references are provided, the combined duration across all video references must not exceed 15 seconds.
- `promptText` (string, required) - max length 6000. A non-empty text prompt describing what should appear in the output.
- `resolution` (string) - one of `768p`, `2k`, `768P`, `2K`. The output resolution. Hailuo 3.0 supports 768p and 2k.
- `duration` (integer) - 5-15. The number of seconds of duration for the output video.
- `ratio` (string) - one of `adaptive`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`. The aspect ratio of the output video. Use adaptive only when image or video references are provided; text-only requests require a concrete ratio.
- `references` (array of object) - max 9 items. An optional array of image references (up to 9). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 2 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 3 items. An optional array of audio references. Audio references require a text prompt, and the total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `hailuo3`

#### POST /v1/video_to_video - model `klingO3_pro`

- `providerSettings` (object) - default `{"keepOriginalSound":true}`. Provider-specific settings for multishot video generation and video editing.
  - `multiPrompt` (array of object) - min 1 items; max 6 items. An array of prompt segments for multishot video generation. Each segment has its own prompt and duration. Total duration across all segments must be between 3 and 15 seconds. `promptText` is still required when `shotT...
    - `prompt` (string, required) - max length 512. The text prompt for this segment.
    - `duration` (integer, required) - 1-15. Duration in seconds for this segment.
  - `shotType` (string) - one of `intelligence`, `customize`. Shot transition type for multishot videos. Defaults to "customize" when multiPrompt is provided.
  - `keepOriginalSound` (boolean) - default `true`. Whether to preserve the original audio when editing a video. Only applicable for video-to-video. Defaults to true.
- `promptText` (string, required) - max length 2500. A text prompt describing what should appear in the output video.
- `promptVideo` (string, required) - The input video to edit. Must be at most 10 seconds long, with width and height each between 720px and 3840px.
- `references` (string or array of object) - An optional array of reference images (up to 4). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `position` (string) - one of `first`, `last`. The position of the image in the output video. "first" will use the image as the first frame, "last" as the last frame. Omit for a reference image.
- `model` (string, required) - one of `klingO3_pro`

#### POST /v1/video_to_video - model `klingO3_standard`

- `providerSettings` (object) - default `{"keepOriginalSound":true}`. Provider-specific settings for multishot video generation and video editing.
  - `multiPrompt` (array of object) - min 1 items; max 6 items. An array of prompt segments for multishot video generation. Each segment has its own prompt and duration. Total duration across all segments must be between 3 and 15 seconds. `promptText` is still required when `shotT...
    - `prompt` (string, required) - max length 512. The text prompt for this segment.
    - `duration` (integer, required) - 1-15. Duration in seconds for this segment.
  - `shotType` (string) - one of `intelligence`, `customize`. Shot transition type for multishot videos. Defaults to "customize" when multiPrompt is provided.
  - `keepOriginalSound` (boolean) - default `true`. Whether to preserve the original audio when editing a video. Only applicable for video-to-video. Defaults to true.
- `promptText` (string, required) - max length 2500. A text prompt describing what should appear in the output video.
- `promptVideo` (string, required) - The input video to edit. Must be at most 10 seconds long, with width and height each between 720px and 3840px.
- `references` (string or array of object) - An optional array of reference images (up to 4). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `position` (string) - one of `first`, `last`. The position of the image in the output video. "first" will use the image as the first frame, "last" as the last frame. Omit for a reference image.
- `model` (string, required) - one of `klingO3_standard`

#### POST /v1/video_to_video - model `seedance2`

- `promptVideo` (string, required) - The input video to use as a reference for the output video. If additional video references are provided, the combined duration across all video references must not exceed 15 seconds.
- `promptText` (string) - max length 10000. An optional text prompt up to 10000 characters describing what should appear in the output.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `bitrate` (string) - one of `standard`, `high`; default `standard`. Bitrate of the output video. `high` keeps more detail with fewer compression artifacts, at a larger file size. Defaults to `standard`.
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes.
- `ratio` (string) - one of `992:432`, `864:496`, `752:560`, `640:640`, `560:752`, `496:864`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`, `2206:946`, `1920:1080`, `1664:1248`, `1440:1440`, `1248:1664`, `1080:1920`, `3840:1646`, `3840:2160`, `3840:2880`, `3840:3840`, `2880:3840`, `2160:3840`. The resolution of the output video.
- `references` (array of object) - max 9 items. An optional array of image references (up to 9). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 2 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 3 items. An optional array of audio references. The total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `seedance2`

#### POST /v1/video_to_video - model `seedance2_fast`

- `promptVideo` (string, required) - The input video to use as a reference for the output video. If additional video references are provided, the combined duration across all video references must not exceed 15 seconds.
- `promptText` (string) - max length 10000. An optional text prompt up to 10000 characters describing what should appear in the output.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `bitrate` (string) - one of `standard`, `high`; default `standard`. Bitrate of the output video. `high` keeps more detail with fewer compression artifacts, at a larger file size. Defaults to `standard`.
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes.
- `ratio` (string) - one of `992:432`, `864:496`, `752:560`, `640:640`, `560:752`, `496:864`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`. The resolution of the output video. Seedance 2.0 Fast supports 480p and 720p only.
- `references` (array of object) - max 9 items. An optional array of image references (up to 9). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 2 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 3 items. An optional array of audio references. The total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `seedance2_fast`

#### POST /v1/video_to_video - model `seedance2_mini`

- `promptVideo` (string, required) - The input video to use as a reference for the output video. If additional video references are provided, the combined duration across all video references must not exceed 15 seconds.
- `promptText` (string) - max length 10000. An optional text prompt up to 10000 characters describing what should appear in the output.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `bitrate` (string) - one of `standard`, `high`; default `standard`. Bitrate of the output video. `high` keeps more detail with fewer compression artifacts, at a larger file size. Defaults to `standard`.
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes.
- `ratio` (string) - one of `992:432`, `864:496`, `752:560`, `640:640`, `560:752`, `496:864`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`. The resolution of the output video. Seedance 2.0 Mini supports 480p and 720p only.
- `references` (array of object) - max 9 items. An optional array of image references (up to 9). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 2 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 3 items. An optional array of audio references. The total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `seedance2_mini`

#### POST /v1/video_to_video - model `gemini_omni_flash`

- `videoUri` (string, required) - The input video to edit. The output is 720p, with the orientation (landscape or portrait) matched to the input. The output duration matches the input, up to 10 seconds. The input must be at most 10 seconds.
- `promptText` (string, required) - max length 4000. A non-empty instruction describing the edit to apply.
- `references` (array of object) - max 5 items. An optional array of image references to guide the edit.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `model` (string, required) - one of `gemini_omni_flash`

#### POST /v1/video_to_video - model `gemini_omni_flash_1.1`

- `videoUri` (string, required) - The input video to use as a reference, extend, or edit. Reference and edited videos may be up to 10 seconds and extended videos up to 30 seconds.
- `promptText` (string, required) - max length 4000. A non-empty prompt describing the output or extension.
- `mode` (string) - one of `reference`, `extend`, `edit`; default `reference`. How the input video is used. `reference` generates a new video guided by the input, `extend` continues it, and `edit` transforms it according to the prompt.
- `ratio` (string) - one of `640:360`, `360:640`, `1280:720`, `720:1280`, `1920:1080`, `1080:1920`, `3840:2160`, `2160:3840`. The resolution and aspect ratio of the output video.
- `duration` (string or integer) - The duration in seconds. In reference mode, this is the output video length. In extend mode, this is the amount of footage added to the input video. Use "auto" to let the model choose a duration.
- `references` (array of object) - max 5 items. An optional array of image references to guide the output.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `model` (string, required) - one of `gemini_omni_flash_1.1`

#### POST /v1/video_to_video - model `seedance2_5`

- `promptVideo` (string, required) - The input video to use as a reference for the output video. If additional video references are provided, the combined duration across all video references must not exceed 30 seconds.
- `promptText` (string) - max length 15000. An optional text prompt up to 15000 characters describing what should appear in the output.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `outputFormat` (string) - one of `mp4`, `mov`. Container for the output video. `mov` keeps high colour precision for grading and compositing. Defaults to `mp4`. Draft mode only supports `mp4`.
- `mode` (string) - one of `reference`, `extend`, `edit`; default `reference`. How the input video is used. `reference` (the default) generates a new video conditioned on the input video and accepts `duration` and `ratio`. `extend` continues the input video, requires `promptText`, and matches th...
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes. Defaults to 5.
- `ratio` (string) - one of `992:432`, `854:480`, `752:560`, `640:640`, `560:752`, `480:854`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`, `2206:946`, `1920:1080`, `1664:1248`, `1440:1440`, `1248:1664`, `1080:1920`, `3840:1646`, `3840:2160`, `3840:2880`, `3840:3840`, `2880:3840`, `2160:3840`. The resolution of the output video. Seedance 2.5 supports 480p, 720p, 1080p, and 4K.
- `references` (array of object) - max 30 items. An optional array of image references (up to 30). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 9 items. An optional array of video references. The combined duration across all video references must not exceed 30 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 10 items. An optional array of audio references. The total combined duration must be less than 30 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `draft` (boolean) - Generate a cheap 480p preview instead of a full-quality video. The returned task ID can later be enhanced to a 1080p video with the same content by passing it as `draftTaskId` to `text_to_video`. Drafts can be enhance...
- `model` (string, required) - one of `seedance2_5`

#### POST /v1/video_to_video - model `kling_4`

- `videoUri` (string, required) - The video to edit.
- `promptText` (string, required) - max length 26000. A text prompt describing how to edit the video.
- `ratio` (string) - one of `1280:720`, `720:1280`, `940:940`, `1460:624`, `1920:1080`, `1080:1920`, `1440:1440`, `2200:940`, `auto_720p`, `auto_1080p`. The target output size. Use a pixel ratio such as `1280:720` or `auto_720p` / `auto_1080p` for adaptive framing.
- `duration` (integer) - 3-30. The duration of the edited video in seconds.
- `promptImage` (string or array of unknown) - Optional first, middle, and last frames guiding the edit. Middle or last frames can be provided without a first frame.
- `references` (array of object) - min 0 items; max 10 items. Images of characters, objects or styles to use in the video. Up to 10 images in total, frames included.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of unknown) - min 0 items; max 4 items. Up to 4 videos whose style, motion or camera work should guide the output, together at most 30 seconds long.
- `model` (string, required) - one of `kling_4`

#### POST /v1/video_to_video - model `gemini_omni_flash_1.2`

- `videoUri` (string, required) - The input video to use as a reference, extend, or edit.
- `promptText` (string, required) - max length 4000. A non-empty prompt describing the output or extension.
- `mode` (string) - one of `reference`, `extend`, `edit`; default `reference`. How the input video is used. `reference` generates a new video guided by the input, `extend` continues it, and `edit` transforms it according to the prompt.
- `resolution` (string) - one of `360p`, `720p`, `1080p`, `4k`. The output resolution when editing or extending a video. In reference mode, use ratio instead.
- `ratio` (string) - one of `640:360`, `360:640`, `1280:720`, `720:1280`, `1920:1080`, `1080:1920`, `3840:2160`, `2160:3840`. The resolution and aspect ratio of the output video.
- `duration` (string or integer) - The duration in seconds. In reference mode, this is the output video length. In extend mode, this is the amount of footage added to the input video. Use "auto" to let the model choose a duration.
- `references` (array of object) - min 0 items; max 5 items. An optional array of image references to guide the output.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `model` (string, required) - one of `gemini_omni_flash_1.2`

#### POST /v1/video_to_video - model `kling_4_flash`

- `promptText` (string, required) - max length 26000. A text prompt describing what should happen in the video.
- `videoUri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `duration` (integer) - 3-20. The duration of the output video in seconds.
- `references` (array of object) - min 0 items; max 10 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - min 0 items; max 5 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `ratio` (string) - one of `1280:720`, `720:1280`, `960:960`, `1464:628`, `auto_720p`, `940:940`, `1460:624`. The output size, or auto_720p for adaptive framing. Legacy values 940:940 and 1460:624 are accepted as aliases for 960:960 and 1464:628, respectively.
- `model` (string, required) - one of `kling_4_flash`

#### POST /v1/video_to_video - model `hailuo3_highspeed`

- `promptText` (string, required) - max length 7000. The text prompt describing the output video.
- `resolution` (string) - one of `480p`, `768p`; default `768p`. The output video resolution.
- `promptVideo` (string, required) - An MP4 or MOV reference video, 2-15 seconds long at 22-62 fps. Frame rates near the limits are normalized to 24-60 fps.
- `duration` (integer) - 4-15; default `5`
- `ratio` (string) - one of `adaptive`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
- `references` (array of object) - min 0 items; max 9 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - min 0 items; max 2 items
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - An MP4 or MOV reference video, 2-15 seconds long at 22-62 fps. Frame rates near the limits are normalized to 24-60 fps.
- `referenceAudio` (array of object) - min 0 items; max 3 items
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `hailuo3_highspeed`

#### POST /v1/video_to_video - model `hailuo3_lite`

- `promptText` (string, required) - max length 7000. The text prompt describing the output video.
- `resolution` (string) - one of `480p`, `768p`; default `768p`. The output video resolution.
- `promptVideo` (string, required) - An MP4 or MOV reference video, 2-15 seconds long at 22-62 fps. Frame rates near the limits are normalized to 24-60 fps.
- `duration` (integer) - 4-15; default `5`
- `ratio` (string) - one of `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
- `references` (array of object) - min 0 items; max 9 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - min 0 items; max 2 items
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - An MP4 or MOV reference video, 2-15 seconds long at 22-62 fps. Frame rates near the limits are normalized to 24-60 fps.
- `referenceAudio` (array of object) - min 0 items; max 3 items
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `hailuo3_lite`

#### POST /v1/video_to_video - model `seedance2_5_flash`

- `promptVideo` (string, required) - The input video to use as a reference for the output video. If additional video references are provided, the combined duration across all video references must not exceed 30 seconds.
- `promptText` (string) - max length 15000. An optional text prompt up to 15000 characters describing what should appear in the output.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `outputFormat` (string) - one of `mp4`, `mov`. Container for the output video. `mov` keeps high colour precision for grading and compositing. Defaults to `mp4`.
- `mode` (string) - one of `reference`, `extend`, `edit`; default `reference`. How the input video is used. `reference` (the default) generates a new video conditioned on the input video and accepts `duration` and `ratio`. `extend` continues the input video, requires `promptText`, and matches th...
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes. Defaults to 5.
- `ratio` (string) - one of `992:432`, `854:480`, `752:560`, `640:640`, `560:752`, `480:854`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`. The resolution of the output video. Seedance 2.5 Flash supports 480p and 720p.
- `references` (array of object) - max 10 items. An optional array of image references (up to 10). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 4 items. An optional array of video references. The combined duration across all video references must not exceed 30 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 5 items. An optional array of audio references. The total combined duration must be less than 30 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `seedance2_5_flash`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

