## Start generating

### POST /v1/image_upscale

Image upscale

Upscale an image with Magnific precision upscaling. Each input dimension must be between 300px and 8000px. Output width and height are the input dimensions multiplied by `scaleFactor` (default 2). Output width times h...

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 1 shape, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/image_upscale - model `magnific_precision_upscaler_v2`

- `imageUri` (string, required) - Image to upscale. See [image inputs](/assets/inputs#images) for URL, upload, and file size limits.
- `scaleFactor` (number) - one of `2`, `4`, `8`, `16`. Multiplies each input dimension to produce output width and height. Defaults to 2.
- `sharpen` (integer) - 0-100. Sharpness intensity from 0 (none) to 100.
- `smartGrain` (integer) - 0-100. Grain and texture enhancement from 0 to 100.
- `ultraDetail` (integer) - 0-100. Fine detail enhancement from 0 to 100.
- `flavor` (string) - one of `sublime`, `photo`, `photo_denoiser`. Optimization preset: `sublime` (illustration), `photo` (photographic), or `photo_denoiser` (noisy photos).
- `model` (string, required) - one of `magnific_precision_upscaler_v2`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

