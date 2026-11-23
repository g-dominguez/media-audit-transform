## Start generating

### POST /v1/text_to_video

Text to video

This endpoint will start a new task to generate a video from a text prompt.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 29 shapes, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/text_to_video - model `gen4.5`

- `promptText` (string, required) - max length 1000. A non-empty string up to 1000 characters (measured in UTF-16 code units). This should describe in detail what should appear in the output.
- `ratio` (string, required) - one of `1280:720`, `720:1280`. The resolution of the output video.
- `duration` (integer, required) - 2-10. The number of seconds of duration for the output video. Must be an integer from 2 to 10.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `contentModeration` (object) - Settings that affect the behavior of the content moderation system.
  - `publicFigureThreshold` (string) - one of `auto`, `low`. When set to `low`, the content moderation system will be less strict about preventing generations that include recognizable public figures.
- `outputFormat` (string) - one of `mp4`, `prores`, `png_sequence`, `hdr10`, `hlg`, `sdr_rec709_10bit`, `hdr_pq_12bit_master`, `hdr_prores`, `hdr_png_sequence`, `hdr_exr_sequence`, `hdr_exr_acescg_sequence_1_3`, `hdr_exr_acescg_sequence_2_0`. The container/encoding of the output. `mp4` (default) returns an H.264 .mp4. `prores` returns a ProRes .mov. `png_sequence` returns a .zip of PNG frames (plus a separate .wav artifact when the output has audio). `hdr1...
- `proresProfile` (string) - one of `422`, `4444`, `422 Proxy`, `422 LT`, `422 HQ`, `4444 XQ`. The ProRes profile to use. Only valid when `outputFormat` is `prores` or `hdr_prores`. For `prores`, any profile is accepted and the default is `4444`. For `hdr_prores`, only `422`, `422 HQ` and `4444` are available a...
- `model` (string, required) - one of `gen4.5`

#### POST /v1/text_to_video - model `veo3.1`

- `promptText` (string, required) - max length 1000. A non-empty string up to 1000 characters (measured in UTF-16 code units). This should describe in detail what should appear in the output.
- `ratio` (string, required) - one of `1280:720`, `720:1280`, `1080:1920`, `1920:1080`. The resolution of the output video.
- `audio` (boolean) - default `true`. Whether to generate audio for the video. Audio inclusion affects pricing.
- `negativePrompt` (string) - max length 1000. Text describing what should not appear in the output video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `duration` (number) - one of `4`, `6`, `8`. The number of seconds of duration for the output video.
- `model` (string, required) - one of `veo3.1`

#### POST /v1/text_to_video - model `veo3.1_fast`

- `promptText` (string, required) - max length 1000. A non-empty string up to 1000 characters (measured in UTF-16 code units). This should describe in detail what should appear in the output.
- `ratio` (string, required) - one of `1280:720`, `720:1280`, `1080:1920`, `1920:1080`. The resolution of the output video.
- `audio` (boolean) - default `true`. Whether to generate audio for the video. Audio inclusion affects pricing.
- `negativePrompt` (string) - max length 1000. Text describing what should not appear in the output video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `duration` (number) - one of `4`, `6`, `8`. The number of seconds of duration for the output video.
- `model` (string, required) - one of `veo3.1_fast`

#### POST /v1/text_to_video - model `klingO3_4k`

- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `providerSettings` (object) - Provider-specific settings for multishot video generation.
  - `multiPrompt` (array of object) - min 1 items; max 6 items. An array of prompt segments for multishot video generation. Each segment has its own prompt and duration. Total duration across all segments must be between 3 and 15 seconds. `promptText` is still required when `shotT...
    - `prompt` (string, required) - max length 512. The text prompt for this segment.
    - `duration` (integer, required) - 1-15. Duration in seconds for this segment.
  - `shotType` (string) - one of `intelligence`, `customize`. Shot transition type for multishot videos. Defaults to "customize" when multiPrompt is provided.
- `promptText` (string) - max length 2500. A text prompt describing what should appear in the output video.
- `ratio` (string, required) - one of `3840:2160`, `2160:3840`, `2880:2880`. The resolution of the output video.
- `duration` (integer) - 3-15. The number of seconds of duration for the output video.
- `model` (string, required) - one of `klingO3_4k`

#### POST /v1/text_to_video - model `hailuo3`

- `promptText` (string, required) - max length 6000. A non-empty text prompt describing what should appear in the output.
- `resolution` (string) - one of `768p`, `2k`, `768P`, `2K`. The output resolution. Hailuo 3.0 supports 768p and 2k.
- `duration` (integer) - 5-15. The number of seconds of duration for the output video.
- `ratio` (string) - one of `adaptive`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`. The aspect ratio of the output video. Use adaptive only when image or video references are provided; text-only requests require a concrete ratio.
- `references` (array of object) - max 9 items. An optional array of image references (up to 9). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 3 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 3 items. An optional array of audio references. Audio references require a text prompt, and the total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `hailuo3`

#### POST /v1/text_to_video - model `kling3.0_4k`

- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `providerSettings` (object) - Provider-specific settings for multishot video generation.
  - `multiPrompt` (array of object) - min 1 items; max 6 items. An array of prompt segments for multishot video generation. Each segment has its own prompt and duration. Total duration across all segments must be between 3 and 15 seconds. `promptText` is still required when `shotT...
    - `prompt` (string, required) - max length 512. The text prompt for this segment.
    - `duration` (integer, required) - 1-15. Duration in seconds for this segment.
  - `shotType` (string) - one of `intelligence`, `customize`. Shot transition type for multishot videos. Defaults to "customize" when multiPrompt is provided.
- `cfgScale` (number) - 0-1; default `0.5`. Creativity/freedom scale for generation. 0 gives the model maximum creative freedom, 1 makes it follow the prompt most strictly. Defaults to 0.5.
- `promptText` (string) - max length 2500. A text prompt describing what should appear in the output video.
- `ratio` (string, required) - one of `3840:2160`, `2160:3840`, `2880:2880`. The resolution of the output video.
- `duration` (integer) - 3-15. The number of seconds of duration for the output video.
- `model` (string, required) - one of `kling3.0_4k`

#### POST /v1/text_to_video - model `happyhorse_1_0`

- `promptText` (string, required) - max length 2500. A non-empty string up to 2500 characters (measured in UTF-16 code units). This should describe in detail what should appear in the output.
- `duration` (integer) - 3-15. The number of seconds of duration for the output video.
- `ratio` (string) - one of `1280:720`, `720:1280`, `960:960`, `1108:832`, `832:1108`, `1920:1080`, `1080:1920`, `1440:1440`, `1662:1248`, `1248:1662`. The resolution of the output video.
- `model` (string, required) - one of `happyhorse_1_0`

#### POST /v1/text_to_video - model `kling2.5_turbo_pro`

- `promptText` (string, required) - max length 2500. A text prompt describing what should appear in the output video.
- `ratio` (string) - one of `1920:1080`, `1440:1440`, `1080:1920`, `1280:720`, `720:720`, `720:1280`; default `1920:1080`
- `cfgScale` (number) - 0-1; default `0.5`. Creativity/freedom scale for generation. 0 gives the model maximum creative freedom, 1 makes it follow the prompt most strictly. Defaults to 0.5.
- `duration` (number) - one of `5`, `10`. The duration of the output video in seconds. Defaults to 5.
- `model` (string, required) - one of `kling2.5_turbo_pro`

#### POST /v1/text_to_video - model `kling3.0_pro`

- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `providerSettings` (object) - Provider-specific settings for multishot video generation.
  - `multiPrompt` (array of object) - min 1 items; max 6 items. An array of prompt segments for multishot video generation. Each segment has its own prompt and duration. Total duration across all segments must be between 3 and 15 seconds. `promptText` is still required when `shotT...
    - `prompt` (string, required) - max length 512. The text prompt for this segment.
    - `duration` (integer, required) - 1-15. Duration in seconds for this segment.
  - `shotType` (string) - one of `intelligence`, `customize`. Shot transition type for multishot videos. Defaults to "customize" when multiPrompt is provided.
- `cfgScale` (number) - 0-1; default `0.5`. Creativity/freedom scale for generation. 0 gives the model maximum creative freedom, 1 makes it follow the prompt most strictly. Defaults to 0.5.
- `promptText` (string) - max length 2500. A text prompt describing what should appear in the output video.
- `ratio` (string, required) - one of `1920:1080`, `1080:1920`, `1440:1440`. The resolution of the output video.
- `duration` (integer) - 3-15. The number of seconds of duration for the output video.
- `model` (string, required) - one of `kling3.0_pro`

#### POST /v1/text_to_video - model `kling3.0_standard`

- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `providerSettings` (object) - Provider-specific settings for multishot video generation.
  - `multiPrompt` (array of object) - min 1 items; max 6 items. An array of prompt segments for multishot video generation. Each segment has its own prompt and duration. Total duration across all segments must be between 3 and 15 seconds. `promptText` is still required when `shotT...
    - `prompt` (string, required) - max length 512. The text prompt for this segment.
    - `duration` (integer, required) - 1-15. Duration in seconds for this segment.
  - `shotType` (string) - one of `intelligence`, `customize`. Shot transition type for multishot videos. Defaults to "customize" when multiPrompt is provided.
- `cfgScale` (number) - 0-1; default `0.5`. Creativity/freedom scale for generation. 0 gives the model maximum creative freedom, 1 makes it follow the prompt most strictly. Defaults to 0.5.
- `promptText` (string) - max length 2500. A text prompt describing what should appear in the output video.
- `ratio` (string, required) - one of `1280:720`, `720:1280`, `960:960`. The resolution of the output video.
- `duration` (integer) - 3-15. The number of seconds of duration for the output video.
- `model` (string, required) - one of `kling3.0_standard`

#### POST /v1/text_to_video - model `klingO3_pro`

- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `providerSettings` (object) - Provider-specific settings for multishot video generation.
  - `multiPrompt` (array of object) - min 1 items; max 6 items. An array of prompt segments for multishot video generation. Each segment has its own prompt and duration. Total duration across all segments must be between 3 and 15 seconds. `promptText` is still required when `shotT...
    - `prompt` (string, required) - max length 512. The text prompt for this segment.
    - `duration` (integer, required) - 1-15. Duration in seconds for this segment.
  - `shotType` (string) - one of `intelligence`, `customize`. Shot transition type for multishot videos. Defaults to "customize" when multiPrompt is provided.
- `promptText` (string) - max length 2500. A text prompt describing what should appear in the output video.
- `ratio` (string, required) - one of `1920:1080`, `1080:1920`, `1440:1440`. The resolution of the output video.
- `duration` (integer) - 3-15. The number of seconds of duration for the output video.
- `model` (string, required) - one of `klingO3_pro`

#### POST /v1/text_to_video - model `klingO3_standard`

- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `providerSettings` (object) - Provider-specific settings for multishot video generation.
  - `multiPrompt` (array of object) - min 1 items; max 6 items. An array of prompt segments for multishot video generation. Each segment has its own prompt and duration. Total duration across all segments must be between 3 and 15 seconds. `promptText` is still required when `shotT...
    - `prompt` (string, required) - max length 512. The text prompt for this segment.
    - `duration` (integer, required) - 1-15. Duration in seconds for this segment.
  - `shotType` (string) - one of `intelligence`, `customize`. Shot transition type for multishot videos. Defaults to "customize" when multiPrompt is provided.
- `promptText` (string) - max length 2500. A text prompt describing what should appear in the output video.
- `ratio` (string, required) - one of `1280:720`, `720:1280`, `960:960`. The resolution of the output video.
- `duration` (integer) - 3-15. The number of seconds of duration for the output video.
- `model` (string, required) - one of `klingO3_standard`

#### POST /v1/text_to_video - model `seedance2`

- `promptText` (string, required) - max length 10000. A non-empty text prompt up to 10000 characters describing what should appear in the output.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `bitrate` (string) - one of `standard`, `high`; default `standard`. Bitrate of the output video. `high` keeps more detail with fewer compression artifacts, at a larger file size. Defaults to `standard`.
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes.
- `ratio` (string) - one of `992:432`, `864:496`, `752:560`, `640:640`, `560:752`, `496:864`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`, `2206:946`, `1920:1080`, `1664:1248`, `1440:1440`, `1248:1664`, `1080:1920`, `3840:1646`, `3840:2160`, `3840:2880`, `3840:3840`, `2880:3840`, `2160:3840`. The resolution of the output video.
- `references` (array of object) - max 9 items. An optional array of image references (up to 9). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 3 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 3 items. An optional array of audio references. The total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `seedance2`

#### POST /v1/text_to_video - model `seedance2_fast`

- `promptText` (string, required) - max length 10000. A non-empty text prompt up to 10000 characters describing what should appear in the output.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `bitrate` (string) - one of `standard`, `high`; default `standard`. Bitrate of the output video. `high` keeps more detail with fewer compression artifacts, at a larger file size. Defaults to `standard`.
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes.
- `ratio` (string) - one of `992:432`, `864:496`, `752:560`, `640:640`, `560:752`, `496:864`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`. The resolution of the output video. Seedance 2.0 Fast supports 480p and 720p only.
- `references` (array of object) - max 9 items. An optional array of image references (up to 9). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 3 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 3 items. An optional array of audio references. The total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `seedance2_fast`

#### POST /v1/text_to_video - model `seedance2_mini`

- `promptText` (string, required) - max length 10000. A non-empty text prompt up to 10000 characters describing what should appear in the output.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `bitrate` (string) - one of `standard`, `high`; default `standard`. Bitrate of the output video. `high` keeps more detail with fewer compression artifacts, at a larger file size. Defaults to `standard`.
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes.
- `ratio` (string) - one of `992:432`, `864:496`, `752:560`, `640:640`, `560:752`, `496:864`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`. The resolution of the output video. Seedance 2.0 Mini supports 480p and 720p only.
- `references` (array of object) - max 9 items. An optional array of image references (up to 9). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 3 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 3 items. An optional array of audio references. The total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `seedance2_mini`

#### POST /v1/text_to_video - model `gemini_omni_flash`

- `promptText` (string, required) - max length 4000. A non-empty text prompt describing the video to generate.
- `ratio` (string) - one of `1280:720`, `720:1280`. The aspect ratio of the output video: `1280:720` (landscape) or `720:1280` (portrait).
- `duration` (integer) - 3-10. The duration of the output video in seconds, as a whole number from 3 to 10.
- `model` (string, required) - one of `gemini_omni_flash`

#### POST /v1/text_to_video - model `grok_imagine_1_5`

- `promptText` (string, required) - max length 2500. A non-empty text prompt describing what should appear in the output.
- `resolution` (string) - one of `480p`, `720p`, `1080p`. The output resolution. Requests with image references are capped at 720p.
- `duration` (integer) - 1-15. The number of seconds of duration for the output video.
- `ratio` (string) - one of `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`. The aspect ratio of the output video.
- `references` (array of object) - max 7 items. An optional array of image references. Referenced images can be addressed in the prompt as [Image 1], [Image 2], and so on. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceAudio` (array of object) - max 3 items. An optional array of audio references. Audio references require at least one image reference, and each clip must be between 3 and 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `grok_imagine_1_5`

#### POST /v1/text_to_video - model `wan3`

- `promptText` (string, required) - max length 20000. A non-empty text prompt describing what should appear in the output.
- `audio` (boolean) - Whether to generate audio with the video.
- `duration` (integer) - 2-30. The number of seconds of duration for the output video.
- `ratio` (string) - one of `832:480`, `720:544`, `624:624`, `544:720`, `480:832`, `1280:720`, `1104:832`, `960:960`, `832:1104`, `720:1280`, `1920:1080`, `1648:1248`, `1440:1440`, `1248:1648`, `1080:1920`, `auto_480p`, `auto_720p`, `auto_1080p`. The resolution of the output video, as `<width>:<height>`. Keyframe image-to-video requests must use `auto_480p`, `auto_720p`, or `auto_1080p` because their aspect ratio follows the first frame.
- `references` (array of object) - max 10 items. An optional array of image references (up to 10). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 5 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 5 items. An optional array of audio references. The total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `wan3`

#### POST /v1/text_to_video - model `gemini_omni_flash_1.1`

- `promptText` (string, required) - max length 4000. A non-empty text prompt describing the video to generate.
- `ratio` (string) - one of `640:360`, `360:640`, `1280:720`, `720:1280`, `1920:1080`, `1080:1920`, `3840:2160`, `2160:3840`. The resolution and aspect ratio of the output video.
- `duration` (string or integer) - The duration of the output video in seconds. Use "auto" to let the model choose a duration. Numeric durations must be between 3 and 10 seconds.
- `references` (array of object) - max 5 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 3 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `model` (string, required) - one of `gemini_omni_flash_1.1`

#### POST /v1/text_to_video - model `wan3_prime`

- `promptText` (string, required) - max length 20000. A non-empty text prompt describing what should appear in the output.
- `audio` (boolean) - Whether to generate audio with the video.
- `duration` (integer) - 2-30. The number of seconds of duration for the output video.
- `ratio` (string) - one of `832:480`, `720:544`, `624:624`, `544:720`, `480:832`, `1280:720`, `1104:832`, `960:960`, `832:1104`, `720:1280`, `1920:1080`, `1648:1248`, `1440:1440`, `1248:1648`, `1080:1920`, `auto_480p`, `auto_720p`, `auto_1080p`. The resolution of the output video, as `<width>:<height>`. Keyframe image-to-video requests must use `auto_480p`, `auto_720p`, or `auto_1080p` because their aspect ratio follows the first frame.
- `references` (array of object) - max 10 items. An optional array of image references (up to 10). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 5 items. An optional array of video references. The combined duration across all video references must not exceed 15 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 5 items. An optional array of audio references. The total combined duration must not exceed 15 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `wan3_prime`

#### POST /v1/text_to_video - model `h3_max`

- `promptText` (string, required) - max length 6000. A non-empty text prompt describing what should appear in the output.
- `resolution` (string) - one of `480p`, `768p`. The output resolution. MiniMax H3 Max supports 480p and 768p.
- `promptExpansionMode` (string) - one of `disabled`, `balanced`, `quality`. How the model rewrites the prompt before generating. disabled keeps the prompt as written. balanced (the default) does a short rewrite. quality spends extra time rewriting for a stronger result.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Identical results also need promptExpansionMode set to disabled; balanced and quality rewrite the prompt and will not repeat.
- `duration` (integer) - 5-15. The number of seconds of duration for the output video.
- `model` (string, required) - one of `h3_max`

#### POST /v1/text_to_video - model `seedance2_5`

- `promptText` (string) - max length 15000. An optional text prompt up to 15000 characters describing what should appear in the output.
- `audio` (boolean) - Whether to generate audio for the video. Defaults to `true`.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `outputFormat` (string) - one of `mp4`, `mov`. Container for the output video. `mov` keeps high colour precision for grading and compositing. Defaults to `mp4`. Draft mode only supports `mp4`.
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes. Defaults to 5.
- `ratio` (string) - one of `992:432`, `854:480`, `752:560`, `640:640`, `560:752`, `480:854`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`, `2206:946`, `1920:1080`, `1664:1248`, `1440:1440`, `1248:1664`, `1080:1920`, `3840:1646`, `3840:2160`, `3840:2880`, `3840:3840`, `2880:3840`, `2160:3840`. The resolution of the output video. Seedance 2.5 supports 480p, 720p, 1080p, and 4K. Defaults to `1280:720`.
- `references` (array of object) - max 30 items. An optional array of image references (up to 30). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 10 items. An optional array of video references. The combined duration across all video references must not exceed 30 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `referenceAudio` (array of object) - max 10 items. An optional array of audio references. The total combined duration must be less than 30 seconds.
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `draft` (boolean) - Generate a cheap 480p preview instead of a full-quality video. The returned task ID can later be enhanced to a 1080p video with the same content by passing it as `draftTaskId` to `text_to_video`. Drafts can be enhance...
- `draftTaskId` (string) - format uuid. The ID of a succeeded draft task to enhance to 1080p. The draft is regenerated with its original prompt, references, and settings, so no other generation fields may be provided.
- `model` (string, required) - one of `seedance2_5`

#### POST /v1/text_to_video - model `grok_imagine_1_5_lite`

- `promptText` (string, required) - max length 2500. A non-empty text prompt describing what should appear in the output.
- `duration` (integer) - 1-15. The number of seconds of duration for the output video.
- `ratio` (string) - one of `848:480`, `480:848`, `480:480`, `640:480`, `480:640`, `720:480`, `480:720`, `1280:720`, `720:1280`, `720:720`, `960:720`, `720:960`, `1088:720`, `720:1088`, `1904:1072`, `1072:1904`, `1424:1424`, `1648:1232`, `1232:1648`, `1744:1152`, `1152:1744`. The resolution of the output video. The 1080p sizes are rendered at 720p and upscaled.
- `model` (string, required) - one of `grok_imagine_1_5_lite`

#### POST /v1/text_to_video - model `kling_4`

- `promptText` (string, required) - max length 26000. A text prompt describing what should happen in the video.
- `ratio` (string) - one of `1280:720`, `720:1280`, `940:940`, `1460:624`, `1920:1080`, `1080:1920`, `1440:1440`, `2200:940`, `auto_720p`, `auto_1080p`. The target output size. Use a pixel ratio such as `1280:720` or `auto_720p` / `auto_1080p` for adaptive framing.
- `duration` (integer) - 3-30. The duration of the output video in seconds.
- `references` (array of object) - min 0 items; max 10 items. Images of characters, objects or styles to use in the video. Up to 10 images in total, frames included.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of unknown) - min 0 items; max 5 items. Up to 5 videos whose style, motion or camera work should guide the output, together at most 30 seconds long.
- `model` (string, required) - one of `kling_4`

#### POST /v1/text_to_video - model `gemini_omni_flash_1.2`

- `promptText` (string, required) - max length 4000. A non-empty text prompt describing the video to generate.
- `ratio` (string) - one of `640:360`, `360:640`, `1280:720`, `720:1280`, `1920:1080`, `1080:1920`, `3840:2160`, `2160:3840`. The resolution and aspect ratio of the output video.
- `duration` (string or integer) - The duration of the output video in seconds. Use "auto" to let the model choose a duration. Numeric durations must be between 3 and 15 seconds.
- `references` (array of object) - min 0 items; max 5 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - min 0 items; max 3 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `model` (string, required) - one of `gemini_omni_flash_1.2`

#### POST /v1/text_to_video - model `kling_4_flash`

- `promptText` (string, required) - max length 26000. A text prompt describing what should happen in the video.
- `duration` (integer) - 3-20. The duration of the output video in seconds.
- `references` (array of object) - min 0 items; max 10 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - min 0 items; max 5 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `ratio` (string) - one of `1280:720`, `720:1280`, `960:960`, `1464:628`, `auto_720p`, `940:940`, `1460:624`. The output size, or auto_720p for adaptive framing. Legacy values 940:940 and 1460:624 are accepted as aliases for 960:960 and 1464:628, respectively.
- `model` (string, required) - one of `kling_4_flash`

#### POST /v1/text_to_video - model `hailuo3_highspeed`

- `promptText` (string, required) - max length 7000. The text prompt describing the output video.
- `resolution` (string) - one of `480p`, `768p`; default `768p`. The output video resolution.
- `duration` (integer) - 4-15; default `5`
- `ratio` (string) - one of `adaptive`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
- `references` (array of object) - min 0 items; max 9 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - min 0 items; max 3 items
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - An MP4 or MOV reference video, 2-15 seconds long at 22-62 fps. Frame rates near the limits are normalized to 24-60 fps.
- `referenceAudio` (array of object) - min 0 items; max 3 items
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `hailuo3_highspeed`

#### POST /v1/text_to_video - model `hailuo3_lite`

- `promptText` (string, required) - max length 7000. The text prompt describing the output video.
- `resolution` (string) - one of `480p`, `768p`; default `768p`. The output video resolution.
- `duration` (integer) - 4-15; default `5`
- `ratio` (string) - one of `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
- `references` (array of object) - min 0 items; max 9 items
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - min 0 items; max 3 items
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - An MP4 or MOV reference video, 2-15 seconds long at 22-62 fps. Frame rates near the limits are normalized to 24-60 fps.
- `referenceAudio` (array of object) - min 0 items; max 3 items
  - `type` (string, required) - one of `audio`
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `model` (string, required) - one of `hailuo3_lite`

#### POST /v1/text_to_video - model `seedance2_5_flash`

- `promptText` (string) - max length 15000. An optional text prompt up to 15000 characters describing what should appear in the output.
- `audio` (boolean) - Whether to generate audio for the video. Defaults to `true`.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `outputFormat` (string) - one of `mp4`, `mov`. Container for the output video. `mov` keeps high colour precision for grading and compositing. Defaults to `mp4`.
- `duration` (integer or string) - Seconds of video to generate, or `auto` to let the model choose. `auto` is billed at the variant maximum up front; unused credits are refunded after the generation finishes. Defaults to 5.
- `ratio` (string) - one of `992:432`, `854:480`, `752:560`, `640:640`, `560:752`, `480:854`, `1470:630`, `1280:720`, `1112:834`, `960:960`, `834:1112`, `720:1280`. The resolution of the output video. Seedance 2.5 Flash supports 480p and 720p. Defaults to `1280:720`.
- `references` (array of object) - max 10 items. An optional array of image references (up to 10). See [our docs](/assets/inputs#images) on image inputs for more information.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `referenceVideos` (array of object) - max 5 items. An optional array of video references. The combined duration across all video references must not exceed 30 seconds. See [our docs](/assets/inputs#videos) on video inputs for more information.
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

