## Start generating

### POST /v1/image_to_vector

Image to vector

Convert a source image into a scalable SVG.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 1 shape, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/image_to_vector - model `ideogram_vector`

- `imageUri` (string, required) - The source image to convert to SVG.
- `vectorizationMode` (string) - one of `simple`, `default`. Use simple for fewer shapes, or default to retain more detail.
- `model` (string, required) - one of `ideogram_vector`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

