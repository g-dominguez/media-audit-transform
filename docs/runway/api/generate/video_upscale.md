## Start generating

### POST /v1/video_upscale

Video upscale

This endpoint starts a task to upscale a video. Set `model` to choose the upscaler.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 2 shapes, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/video_upscale - model `magnific_video_upscaler_creative`

- `videoUri` (string, required) - Video to upscale. See [video inputs](/assets/inputs#videos) for URL, upload, and file size limits. Maximum duration is 30 seconds.
- `resolution` (string) - one of `720p`, `1k`, `2k`, `4k`. Target output resolution from 720p to 4k. Defaults to `2k`.
- `creativity` (integer) - 0-100. How much AI-generated detail to add during upscaling, from 0 (faithful) to 100.
- `sharpen` (integer) - 0-100. Sharpness intensity from 0 (none) to 100.
- `smartGrain` (integer) - 0-100. Grain and texture enhancement from 0 to 100.
- `flavor` (string) - one of `vivid`, `natural`. Processing style: `vivid` for enhanced color and detail, `natural` for faithful reproduction.
- `fpsBoost` (boolean) - Whether to increase the output frame rate.
- `model` (string, required) - one of `magnific_video_upscaler_creative`

#### POST /v1/video_upscale - model `enhance_frame_rate`

- `videoUri` (string, required) - The video to convert. See [video inputs](/assets/inputs#videos) for URL, upload, and file size limits. Maximum duration is 300 seconds.
- `targetFramerate` (string, required) - one of `24`, `25`, `30`, `48`, `50`, `60`, `120`, `23_98`, `29_97`, `59_94`. The output frame rate.
- `model` (string, required) - one of `enhance_frame_rate`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

