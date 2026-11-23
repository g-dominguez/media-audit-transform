## Recipes

### POST /v1/recipes/ad_localization

Localize an ad image

Localize an existing ad image for a target language, preserving visual creative while adapting on-screen messaging.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `version` (string, required) - one of `2026-06`, `unsafe-latest`. Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to track the newest stable version (may break without notice).
- `referenceImage` (object, required) - Reference ad image to localize. See [our docs](/assets/inputs#images) on image inputs.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `targetLanguage` (string, required) - one of `ar`, `zh`, `zh-Hant`, `nl`, `en`, `fr`, `de`, `hi`, `id`, `it`, `ja`, `ko`, `pl`, `pt`, `ru`, `es`, `sv`, `th`, `tr`, `uk`, `vi`, `el`. Target language for the localized ad. Use ISO-style codes (e.g. "ja" for Japanese, "es" for Spanish).

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

### POST /v1/recipes/marketing_stock_image

Create a marketing stock image

Generate a polished marketing stock image from a text brief and optional brand logo image.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `version` (string, required) - one of `2026-06`, `unsafe-latest`. Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to track the newest stable version (may break without notice).
- `prompt` (string, required) - max length 3500. Marketing image brief. Describe the subject, audience, channel, desired mood, setting, and any constraints.
- `referenceImage` (object) - Optional brand logo image to guide the generated marketing stock image. See [our docs](/assets/inputs#images) on image inputs.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `outputCount` (integer) - 1-4; default `4`. The number of images to generate (1-4). Defaults to 4. Increasing this number affects credits consumed.
- `quality` (string) - one of `low`, `medium`, `high`; default `high`. GPT Image 2 rendering quality (`low`, `medium`, or `high`). Lower settings are faster and use fewer credits; `high` (default) is slowest and highest fidelity.

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

### POST /v1/recipes/product_ad

Create a product ad video

Generate a cinematic product ad from product images, optional style references, product info, and creative direction.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `version` (string, required) - one of `2026-06`, `2026-07`, `unsafe-latest`. Workflow version. Use a dated version (e.g. "2026-07") to pin behavior, or "unsafe-latest" to track the newest stable version (may break without notice).
- `productImages` (array of object, required) - min 1 items; max 10 items. Product images (1-10). Multiple angles of the same product. All images inform product analysis and reference generation; only the first image is used as the primary product reference in the storyboard grid. See [our d...
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `styleImages` (array of object) - max 4 items. Optional style reference images (0-4). Defines the visual treatment (lighting, palette, mood). Treated as a moodboard when multiple are provided.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `productInfo` (string) - max length 2500; default ``. Optional product description and specifications to inform creative direction and which product elements to highlight.
- `userConcept` (string) - max length 3500; default ``. Optional creative direction describing brand voice, product framing, scene specifics, lighting, camera motion, and narrative.
- `ratio` (string) - one of `1280:720`, `720:1280`, `960:960`, `834:1112`, `1920:1080`, `1080:1920`, `1440:1440`, `1248:1664`. The resolution of the output video.
- `duration` (integer) - 4-15. Duration of the output video in seconds (4-15). Defaults to 10 seconds.
- `audio` (boolean) - default `false`. Whether to generate audio for the video.

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

### POST /v1/recipes/product_campaign_image

Create product campaign images

Generate four fashion campaign images from a product image and style brief.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `version` (string, required) - one of `2026-06`, `unsafe-latest`. Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to track the newest stable version (may break without notice).
- `image` (object, required) - Product image to preserve across the generated campaign. See [our docs](/assets/inputs#images) on image inputs.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `prompt` (string, required) - max length 3500. Style / creative brief for the fashion campaign, e.g. "High-key fashion editorial, gorpcore-meets-blokecore-meets-Y2K".

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

### POST /v1/recipes/product_swap

Swap a product in a reference video

Replace the product in a reference video with a new product, preserving camera motion, lighting, and scene composition.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `version` (string, required) - one of `2026-06`, `unsafe-latest`. Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to track the newest stable version (may break without notice).
- `referenceVideo` (object, required) - Reference video containing the product to swap. Duration must be between 1.8 and 15 seconds. See [our docs](/assets/inputs#videos) on video inputs.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
- `originalProductImage` (object, required) - Image of the original product being swapped out. See [our docs](/assets/inputs#images) on image inputs.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `newProductImages` (array of object, required) - min 1 items; max 10 items. Reference images of the new product (1-10). Supply multiple angles when the reference video shows the product from different views - optionally label each with `view` ("front", "side", or "back"). A single pre-compose...
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `view` (string) - one of `front`, `side`, `back`. Optional view label for this reference (front, side, or back). Omit when supplying a single reference sheet or when view labels are unknown.
- `duration` (integer) - 4-15. Duration of the output video in seconds (4-15). Defaults to 10 seconds.
- `resolution` (string) - one of `720p`, `1080p`. Output video resolution. Defaults to 720p.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

### POST /v1/recipes/multi_shot_video

Create a multi-shot video

Generate a multi-cut video from a story prompt (auto mode) or a custom shot list (custom mode).

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 2 shapes, selected by `mode`. Only the fields listed under a given `mode` are valid.

#### POST /v1/recipes/multi_shot_video - mode `auto`

- `mode` (string, required) - one of `auto`. Workflow mode. `auto` decomposes a story prompt into exactly 5 shots.
- `prompt` (string, required) - max length 2500. Story prompt for auto mode.
- `version` (string, required) - one of `2026-06`, `unsafe-latest`. Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to track the newest stable version (may break without notice).
- `firstFrame` (object) - Optional image used as the first frame of the output video. See [our docs](/assets/inputs#images) on image inputs.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `ratio` (string) - one of `1280:720`, `720:1280`, `960:960`, `1920:1080`, `1080:1920`, `1440:1440`. Output dimensions as width:height. 720p ratios (`1280:720`, `720:1280`, `960:960`) use the standard tier; 1080p ratios (`1920:1080`, `1080:1920`, `1440:1440`) use the pro tier. Defaults to `1280:720`.
- `duration` (number) - one of `5`, `10`, `15`. Total duration of the output video in seconds. Defaults to 10 seconds.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.

#### POST /v1/recipes/multi_shot_video - mode `custom`

- `mode` (string, required) - one of `custom`. Workflow mode. `custom` polishes a user-provided shot list of 3-5 shots.
- `shots` (array of object, required) - min 3 items; max 5 items. Shot list for custom mode (3-5 shots). Per-shot durations must sum to `duration`.
  - `prompt` (string, required) - max length 512. Shot description prompt.
  - `duration` (integer, required) - 1-15. Duration of this shot in seconds.
- `version` (string, required) - one of `2026-06`, `unsafe-latest`. Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to track the newest stable version (may break without notice).
- `firstFrame` (object) - Optional image used as the first frame of the output video. See [our docs](/assets/inputs#images) on image inputs.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `ratio` (string) - one of `1280:720`, `720:1280`, `960:960`, `1920:1080`, `1080:1920`, `1440:1440`. Output dimensions as width:height. 720p ratios (`1280:720`, `720:1280`, `960:960`) use the standard tier; 1080p ratios (`1920:1080`, `1080:1920`, `1440:1440`) use the pro tier. Defaults to `1280:720`.
- `duration` (number) - one of `5`, `10`, `15`. Total duration of the output video in seconds. Defaults to 10 seconds.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

### POST /v1/recipes/product_ugc

Create a product UGC video

Generate a vertical user-generated content ad from a character image, product image, product details, and optional creative direction.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `version` (string, required) - one of `2026-06`, `unsafe-latest`. Workflow version. Use a dated version (e.g. "2026-06") to pin behavior, or "unsafe-latest" to track the newest stable version (may break without notice).
- `characterImage` (object, required) - Image of the character who will appear on camera in the UGC video. Aspect ratio (width / height) must be between 0.4 and 4. See [our docs](/assets/inputs#images) for image input requirements.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `productImage` (object, required) - Image of the product being promoted. Aspect ratio (width / height) must be between 0.4 and 4. See [our docs](/assets/inputs#images) for image input requirements.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `productInfo` (string) - max length 2500; default ``. Product details and creative brief - what the product is, key benefits, and any specifics the script should reference.
- `userConcept` (string) - max length 3500; default ``. Optional creative direction for the UGC video - tone, voice register, specific message, or an entire dialog script.
- `duration` (integer) - 4-15. Duration of the output video in seconds (4-15). Defaults to 15 seconds.
- `ratio` (string) - one of `720:1280`, `1080:1920`. The resolution of the output video.
- `audio` (boolean) - default `true`. Whether to generate audio for the video.

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

