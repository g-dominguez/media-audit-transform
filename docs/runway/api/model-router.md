## Model Router

### POST /v1/generate/video

Routed video generation

Start a video generation task using a saved Model Router config instead of naming a model.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `configId` (string, required) - The slug of a saved Model Router config to route this request with.
- `dryRun` (boolean) - When true, run the full routing pipeline and return the decision and estimated cost without generating. No task is created, nothing is billed, and no asset is produced.
- `input` (object, required) - Model-agnostic video generation input. Fields are optional; the router selects a model and maps these options to it.
  - `promptText` (string) - max length 26000. A text prompt describing the desired video.
  - `negativePrompt` (string) - max length 1000. A text description of what to avoid in the output.
  - `referenceImages` (array of object) - max 4 items. Optional image inputs. Each entry requires a `role`. At most one `first` and one `last` are allowed; multiple `reference` images are allowed.
    - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
    - `role` (string, required) - one of `first`, `last`, `reference`. How the image is used. `first` is the starting frame; `last` is an end frame; `reference` is additional image context.
  - `referenceVideos` (array of object) - max 2 items. Optional video inputs. Each entry requires a `role`. Use `source` for video-to-video; use `reference` for additional context videos (only models that support them remain eligible). At most one `source` is allowed.
    - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded video. See [our docs](/assets/inputs#videos) on video inputs for more information.
    - `role` (string, required) - one of `source`, `reference`. How the video is used. `source` is the primary video-to-video input; `reference` is additional video context.
  - `referenceAudio` (array of object) - max 1 items. Optional audio inputs for the generation.
    - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
  - `keyframes` (array of object) - max 5 items. Timed guidance images for video restyle. Requires a source video; unsupported models are excluded.
    - `uri` (string, required)
    - `seconds` (number) - 0-30
    - `range` (object)
      - `start_seconds` (integer, required)
      - `end_seconds` (integer, required)
    - `at` (number) - 0-1
  - `duration` (integer) - 2-30. Desired duration of the output video, in seconds. Unsupported values exclude models; with a source video, V2V duration support applies.
  - `aspectRatio` (string) - one of `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`. Desired aspect ratio. Models that do not support the requested aspect are excluded.
  - `resolution` (string) - one of `480p`, `720p`, `1080p`, `4k`. Desired output resolution tier. Models that do not support the requested tier are excluded.
  - `audio` (boolean) - Whether to generate native audio with the video. When true, only models that output audio remain eligible; when false, silent models and models with an audio toggle remain eligible (always-on native-audio models are e...
  - `seed` (integer) - 0-4294967295. A seed for reproducible generation. Random if omitted.
  - `contentModeration` (object) - Settings that affect the behavior of the content moderation system.
    - `publicFigureThreshold` (string) - one of `auto`, `low`. When set to `low`, the content moderation system will be less strict about preventing generations that include recognizable public figures.

Response 200:

- `dryRun` (boolean, required) - one of `false`, `true`
- `id` (string) - format uuid. The ID of the created task. Poll GET /v1/tasks/:id for the result.
- `routing` (object, required)
  - `model` (string, required)
  - `provider` (string, required)
  - `configId` (string, required)
  - `resolvedSettings` (object, required)
    - `optimizeFor` (string, required) - one of `cost`, `latency`, `quality`
    - `priceCeiling` (number or null, required)
  - `resolvedInput` (object, required)
    - `duration` (number, required)
    - `ratio` (string, required)
    - `resolution` (string, required)
  - `estimatedCost` (object, required)
    - `credits` (number, required)
  - `capacityFallback` (object)
    - `skipped` (array of string, required)
    - `allExhausted` (boolean, required)

Other responses: `400`, `404`, `429`

### POST /v1/generate/image

Routed image generation

Start an image generation task using a saved Model Router config instead of naming a model.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `configId` (string, required) - The slug of a saved Model Router config to route this request with.
- `dryRun` (boolean) - When true, run the full routing pipeline and return the decision and estimated cost without generating. No task is created, nothing is billed, and no asset is produced.
- `input` (object, required) - Model-agnostic image generation input. The router selects a model and maps these options to it.
  - `promptText` (string, required) - max length 45000. A text prompt describing the desired image.
  - `referenceImages` (array of object) - max 16 items. Optional reference images for models that support them. Tags are assigned per model when omitted.
    - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `aspectRatio` (string) - one of `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`, `2:3`, `3:2`, `4:5`, `5:4`. Desired aspect ratio. Models that do not support the requested aspect are excluded.
  - `resolution` (string) - one of `1k`, `2k`, `4k`. Desired megapixel tier. Models that do not support the requested tier are excluded.
  - `outputCount` (integer) - 1-10. Number of images to generate (1-10). Models that cannot produce the exact count are excluded and cost scales with this value.
  - `seed` (integer) - 0-4294967295. A seed for reproducible generation. Only gen4_image and gen4_image_turbo accept this field.
  - `contentModeration` (object) - Settings that affect the behavior of the content moderation system.
    - `publicFigureThreshold` (string) - one of `auto`, `low`. When set to `low`, the content moderation system will be less strict about preventing generations that include recognizable public figures.

Response 200:

- `dryRun` (boolean, required) - one of `false`, `true`
- `id` (string) - format uuid. The ID of the created task. Poll GET /v1/tasks/:id for the result.
- `routing` (object, required)
  - `model` (string, required)
  - `provider` (string, required)
  - `configId` (string, required)
  - `resolvedSettings` (object, required)
    - `optimizeFor` (string, required) - one of `cost`, `latency`, `quality`
    - `priceCeiling` (number or null, required)
  - `resolvedInput` (object, required)
    - `ratio` (string, required)
    - `aspectRatio` (string, required)
    - `resolution` (string, required)
  - `estimatedCost` (object, required)
    - `credits` (number, required)
  - `capacityFallback` (object)
    - `skipped` (array of string, required)
    - `allExhausted` (boolean, required)

Other responses: `400`, `404`, `429`

### POST /v1/generate/audio

Routed audio generation

Start an audio generation task using a saved Model Router config instead of naming a model. Set input.type to speech to speak promptText verbatim, audio to generate audio described by promptText, or music to generate...

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `configId` (string, required) - The slug of a saved Model Router config to route this request with.
- `dryRun` (boolean) - When true, run the full routing pipeline and return the decision and estimated cost without generating. No task is created, nothing is billed, and no asset is produced.
- `input` (object, required) - Model-agnostic audio generation input. The router selects a model and maps these options to it.
  - `type` (string, required) - one of `speech`, `audio`, `music`. How promptText is interpreted: `speech` speaks it verbatim as a script; `audio` treats it as a description of the desired audio, which may combine speech, music, ambience, and sound effects; `music` treats it as a des...
  - `promptText` (string, required) - max length 5000. For `speech`, the words to speak. For `audio` and `music`, a description of the desired output.
  - `voice` (object) - The voice to speak with. When omitted, models that support a default voice remain eligible.
    - `type` (string, required) - one of `preset`, `reference-audio`
    - `presetId` (string) - one of `Maya`, `Arjun`, `Serene`, `Bernard`, `Billy`, `Mark`, `Clint`, `Mabel`, `Chad`, `Leslie`, `Eleanor`, `Elias`, `Elliot`, `Grungle`, `Brodie`, `Sandra`, `Kirk`, `Kylie`, `Lara`, `Lisa`, `Malachi`, `Marlene`, `Martin`, `Miriam`, `Monster`, `Paula`, `Pip`, `Rusty`, `Ragnar`, `Xylar`, `Maggie`, `Jack`, `Katie`, `Noah`, `James`, `Rina`, `Ella`, `Mariah`, `Frank`, `Claudia`, ... (49 total). A Runway preset voice id. Choosing a preset routes only to models that support preset voices.
    - `audioUri` (string) - A 1-30 second clip to clone the voice from.
  - `referenceAudios` (array of object) - max 3 items. Optional reference audio clips guiding `audio` generation, for models that support them. Reference each clip in promptText as @Audio1, @Audio2, and @Audio3 in order.
    - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
  - `duration` (number) - 0.5-600. Desired output duration in seconds: 0.5-30 for `audio`, or whole seconds from 3 to 600 for `music`. Models that cannot honor an explicit duration are excluded.
  - `loop` (boolean) - When true, the `audio` output is designed to loop seamlessly. Models without loop support are excluded.

Response 200:

- `dryRun` (boolean, required) - one of `false`, `true`
- `id` (string) - format uuid. The ID of the created task. Poll GET /v1/tasks/:id for the result.
- `routing` (object, required)
  - `model` (string, required)
  - `provider` (string, required)
  - `configId` (string, required)
  - `resolvedSettings` (object, required)
    - `optimizeFor` (string, required) - one of `cost`, `latency`, `quality`
    - `priceCeiling` (number or null, required)
  - `resolvedInput` (object, required)
    - `type` (string, required) - one of `speech`, `audio`, `music`
    - `voice` (string, required) - one of `preset`, `reference-audio`, `default`, `none`
  - `estimatedCost` (object, required)
    - `credits` (number, required)
  - `capacityFallback` (object)
    - `skipped` (array of string, required)
    - `allExhausted` (boolean, required)

Other responses: `400`, `404`, `429`

### GET /v1/routers

List Model Routers

List Model Router configurations for the authenticated organization with cursor-based pagination.

Parameters:

- `cursor` (query, string) - max length 1000. Cursor from a previous response for fetching the next page of results.
- `limit` (query, integer) - 1-100; default `50`. The maximum number of items to return per page.

Response 200:

- `data` (array of object, required) - The list of items for the current page.
  - `id` (string, required) - format uuid. The Model Router's primary key ID (UUID). Use it to manage this router via the API; use the slug to reference the router in generation requests.
  - `slug` (string, required) - Immutable slug used to reference this Model Router in generation requests (for example, production-video). Unique within the API project. The UUID id remains the canonical management identifier.
  - `name` (string, required) - max length 255. Human-friendly Model Router display name shown in the dev portal. Mutable, and not used to reference the router in requests.
  - `description` (string or null, required) - An optional Model Router description.
  - `version` (integer, required) - greater than 0. Current settings version. Increments when settings change; name and description updates do not create a new version.
  - `settings` (object, required)
    - `schemaVersion` (number, required) - one of `1`. Settings JSON schema version used when this snapshot was written.
    - `models` (object) - When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video, image, audio, or mesh model name (unknown ids are rejected on create/update).
      - `mode` (string, required) - one of `allow_new_except`, `allowlist_only`
      - `ids` (array of string, required)
    - `maxCreditsPerGeneration` (object) - Optional per-modality credit caps, applied per generated output. Models whose estimated per-output cost exceeds the cap are excluded.
      - `video` (integer) - greater than 0
      - `image` (integer) - greater than 0
      - `audio` (integer) - greater than 0
      - `mesh` (integer) - greater than 0
    - `optimizeFor` (string) - one of `cost`, `latency`, `quality`. Soft preference among eligible models: cost, latency, or quality.
    - `fallback` (object) - Opt-in behavior for what routing should do when the preferred model cannot start immediately.
      - `onCapacity` (boolean) - When true, if the account is at its concurrency limit on the preferred model, routing skips it and picks the next-best eligible model instead of queueing. If every eligible model is at its limit, the original best-ran...
  - `createdAt` (string, required) - format date-time. When the Model Router was created.
  - `updatedAt` (string, required) - format date-time. When the Model Router was last updated.
- `hasMore` (boolean, required) - Whether there are more items available after this page.
- `nextCursor` (string or null, required) - Cursor to use for fetching the next page, or null if there are no more pages.

### POST /v1/routers

Create Model Router

Create a Model Router configuration.

Request body:

- `slug` (string, required) - Immutable slug used to reference this Model Router in generation requests (for example, production-video). Unique within the API project. The UUID id remains the canonical management identifier.
- `name` (string) - max length 255. Optional human-readable display name for this router. Defaults to the slug when omitted.
- `description` (string) - max length 2000. An optional Model Router description.
- `settings` (object) - Model Router routing preferences. Defaults to cost-optimized allow-all when omitted. Modality is implied by the generate endpoint used with this Model Router.
  - `schemaVersion` (number) - one of `1`. Settings JSON schema version. Omit on write to use the current version; responses and stored snapshots always include it.
  - `models` (object) - When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video, image, audio, or mesh model name (unknown ids are rejected on create/update).
    - `mode` (string, required) - one of `allow_new_except`, `allowlist_only`
    - `ids` (array of string, required)
  - `maxCreditsPerGeneration` (object) - Optional per-modality credit caps, applied per generated output. Models whose estimated per-output cost exceeds the cap are excluded.
    - `video` (integer) - greater than 0
    - `image` (integer) - greater than 0
    - `audio` (integer) - greater than 0
    - `mesh` (integer) - greater than 0
  - `optimizeFor` (string) - one of `cost`, `latency`, `quality`. Soft preference among eligible models: cost, latency, or quality.
  - `fallback` (object) - Opt-in behavior for what routing should do when the preferred model cannot start immediately.
    - `onCapacity` (boolean) - When true, if the account is at its concurrency limit on the preferred model, routing skips it and picks the next-best eligible model instead of queueing. If every eligible model is at its limit, the original best-ran...

Response 200:

- `id` (string, required) - format uuid. The Model Router's primary key ID (UUID). Use it to manage this router via the API; use the slug to reference the router in generation requests.
- `slug` (string, required) - Immutable slug used to reference this Model Router in generation requests (for example, production-video). Unique within the API project. The UUID id remains the canonical management identifier.
- `name` (string, required) - max length 255. Human-friendly Model Router display name shown in the dev portal. Mutable, and not used to reference the router in requests.
- `description` (string or null, required) - An optional Model Router description.
- `version` (integer, required) - greater than 0. Current settings version. Increments when settings change; name and description updates do not create a new version.
- `settings` (object, required)
  - `schemaVersion` (number, required) - one of `1`. Settings JSON schema version used when this snapshot was written.
  - `models` (object) - When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video, image, audio, or mesh model name (unknown ids are rejected on create/update).
    - `mode` (string, required) - one of `allow_new_except`, `allowlist_only`
    - `ids` (array of string, required)
  - `maxCreditsPerGeneration` (object) - Optional per-modality credit caps, applied per generated output. Models whose estimated per-output cost exceeds the cap are excluded.
    - `video` (integer) - greater than 0
    - `image` (integer) - greater than 0
    - `audio` (integer) - greater than 0
    - `mesh` (integer) - greater than 0
  - `optimizeFor` (string) - one of `cost`, `latency`, `quality`. Soft preference among eligible models: cost, latency, or quality.
  - `fallback` (object) - Opt-in behavior for what routing should do when the preferred model cannot start immediately.
    - `onCapacity` (boolean) - When true, if the account is at its concurrency limit on the preferred model, routing skips it and picks the next-best eligible model instead of queueing. If every eligible model is at its limit, the original best-ran...
- `createdAt` (string, required) - format date-time. When the Model Router was created.
- `updatedAt` (string, required) - format date-time. When the Model Router was last updated.

### GET /v1/routers/{id}

Retrieve Model Router

Retrieve a Model Router configuration by ID.

Parameters:

- `id` (path, string, required) - format uuid. The Model Router's primary key ID (UUID).

Response 200:

- `id` (string, required) - format uuid. The Model Router's primary key ID (UUID). Use it to manage this router via the API; use the slug to reference the router in generation requests.
- `slug` (string, required) - Immutable slug used to reference this Model Router in generation requests (for example, production-video). Unique within the API project. The UUID id remains the canonical management identifier.
- `name` (string, required) - max length 255. Human-friendly Model Router display name shown in the dev portal. Mutable, and not used to reference the router in requests.
- `description` (string or null, required) - An optional Model Router description.
- `version` (integer, required) - greater than 0. Current settings version. Increments when settings change; name and description updates do not create a new version.
- `settings` (object, required)
  - `schemaVersion` (number, required) - one of `1`. Settings JSON schema version used when this snapshot was written.
  - `models` (object) - When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video, image, audio, or mesh model name (unknown ids are rejected on create/update).
    - `mode` (string, required) - one of `allow_new_except`, `allowlist_only`
    - `ids` (array of string, required)
  - `maxCreditsPerGeneration` (object) - Optional per-modality credit caps, applied per generated output. Models whose estimated per-output cost exceeds the cap are excluded.
    - `video` (integer) - greater than 0
    - `image` (integer) - greater than 0
    - `audio` (integer) - greater than 0
    - `mesh` (integer) - greater than 0
  - `optimizeFor` (string) - one of `cost`, `latency`, `quality`. Soft preference among eligible models: cost, latency, or quality.
  - `fallback` (object) - Opt-in behavior for what routing should do when the preferred model cannot start immediately.
    - `onCapacity` (boolean) - When true, if the account is at its concurrency limit on the preferred model, routing skips it and picks the next-best eligible model instead of queueing. If every eligible model is at its limit, the original best-ran...
- `createdAt` (string, required) - format date-time. When the Model Router was created.
- `updatedAt` (string, required) - format date-time. When the Model Router was last updated.

### PATCH /v1/routers/{id}

Update Model Router

Update a Model Router configuration. Settings changes append a new version; name and description updates do not. Settings are merged with the current snapshot - omitted fields keep their existing values.

Parameters:

- `id` (path, string, required) - format uuid. The Model Router's primary key ID (UUID).

Request body:

- `name` (string) - max length 255. Display name. The slug is immutable and cannot be changed after creation.
- `description` (string or null)
- `settings` (object) - Nested merge: omitted settings fields keep their current values. When models is present, omitted models.mode or models.ids are preserved (sending only optimizeFor does not clear the model allowlist or credit ceiling)....
  - `schemaVersion` (number) - one of `1`. Settings JSON schema version. Omit on write to use the current version; responses and stored snapshots always include it.
  - `models` (object) - When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video, image, audio, or mesh model name (unknown ids are rejected on create/update).
    - `mode` (string, required) - one of `allow_new_except`, `allowlist_only`
    - `ids` (array of string, required)
  - `maxCreditsPerGeneration` (object or null) - Per-modality credit caps to change. Set a modality to null to remove its cap, or set maxCreditsPerGeneration to null to remove every cap.
    - `video` (integer or null)
    - `image` (integer or null)
    - `audio` (integer or null)
    - `mesh` (integer or null)
  - `optimizeFor` (string) - one of `cost`, `latency`, `quality`. Soft preference among eligible models: cost, latency, or quality.
  - `fallback` (object) - Opt-in behavior for what routing should do when the preferred model cannot start immediately.
    - `onCapacity` (boolean) - When true, if the account is at its concurrency limit on the preferred model, routing skips it and picks the next-best eligible model instead of queueing. If every eligible model is at its limit, the original best-ran...

Response 200:

- `id` (string, required) - format uuid. The Model Router's primary key ID (UUID). Use it to manage this router via the API; use the slug to reference the router in generation requests.
- `slug` (string, required) - Immutable slug used to reference this Model Router in generation requests (for example, production-video). Unique within the API project. The UUID id remains the canonical management identifier.
- `name` (string, required) - max length 255. Human-friendly Model Router display name shown in the dev portal. Mutable, and not used to reference the router in requests.
- `description` (string or null, required) - An optional Model Router description.
- `version` (integer, required) - greater than 0. Current settings version. Increments when settings change; name and description updates do not create a new version.
- `settings` (object, required)
  - `schemaVersion` (number, required) - one of `1`. Settings JSON schema version used when this snapshot was written.
  - `models` (object) - When mode is allow_new_except, ids are excluded; when allowlist_only, ids are the only allowed values. Each id must be a known public video, image, audio, or mesh model name (unknown ids are rejected on create/update).
    - `mode` (string, required) - one of `allow_new_except`, `allowlist_only`
    - `ids` (array of string, required)
  - `maxCreditsPerGeneration` (object) - Optional per-modality credit caps, applied per generated output. Models whose estimated per-output cost exceeds the cap are excluded.
    - `video` (integer) - greater than 0
    - `image` (integer) - greater than 0
    - `audio` (integer) - greater than 0
    - `mesh` (integer) - greater than 0
  - `optimizeFor` (string) - one of `cost`, `latency`, `quality`. Soft preference among eligible models: cost, latency, or quality.
  - `fallback` (object) - Opt-in behavior for what routing should do when the preferred model cannot start immediately.
    - `onCapacity` (boolean) - When true, if the account is at its concurrency limit on the preferred model, routing skips it and picks the next-best eligible model instead of queueing. If every eligible model is at its limit, the original best-ran...
- `createdAt` (string, required) - format date-time. When the Model Router was created.
- `updatedAt` (string, required) - format date-time. When the Model Router was last updated.

### DELETE /v1/routers/{id}

Delete Model Router

Delete a Model Router configuration. Deleted Model Routers cannot be used for generation.

Parameters:

- `id` (path, string, required) - format uuid. The Model Router's primary key ID (UUID).

### GET /v1/routers/{id}/requests

List Model Router requests

Paginated routing history for live Model Router requests (successful routes and failures). Playground dry runs are not recorded.

Parameters:

- `id` (path, string, required) - format uuid. The Model Router's primary key ID (UUID).
- `cursor` (query, string) - max length 1000. Cursor from a previous response for fetching the next page of results.
- `limit` (query, integer) - 1-100; default `50`. The maximum number of items to return per page.

Response 200:

- `data` (array of object, required) - The list of items for the current page.
  - `id` (string, required) - format uuid
  - `requestId` (string, required)
  - `status` (string, required) - one of `routed`, `no_eligible_model`, `router_config_not_found`, `invalid_request`, `error`. How the routing attempt ended: routed (model selected), no_eligible_model (hard filters emptied the pool), router_config_not_found (same condition as the generate error of that name), invalid_request, or error.
  - `model` (string or null, required)
  - `provider` (string or null, required)
  - `reason` (string or null, required) - Free-text explanation of the pick. Written by the ranker, so treat it as prose for humans and group on reasonCode instead.
  - `reasonCode` (string or null, required) - Why the model won: lowest_cost, best_latency, best_quality, only_eligible_model, or filter_order_fallback (ranking was unavailable, so hard-filter order stood). Null when the request never reached ranking.
  - `estimatedCredits` (number or null, required)
  - `taskId` (string or null, required)
  - `createdAt` (string, required) - format date-time
  - `pipeline` (array of object, required) - Ordered routing story: hard-filter stages with surviving model ids, a capacity step when concurrency limits affected the pool, then rank step when selection reached ranking.
    - `type` (string, required) - one of `filter`, `capacity`, `rank`
    - `filter` (string) - one of `capability`, `prompt_length`, `input_support`, `allow_deny`, `price`. Hard-filter stage that ran: capability (modality/feature fit), prompt_length (prompt within model limits), input_support (requested inputs/assets), allow_deny (router model allowlist/denylist), or price (credit ceiling).
    - `models` (array of string) - Model IDs of the models that remained eligible after this filter stage.
    - `skipped` (array of string) - Model IDs that were eligible but passed over because the account was at its concurrency limit for them.
    - `allExhausted` (boolean) - True when every eligible model was at its limit, in which case none was skipped and the selected task queues.
    - `outcome` (string) - one of `cost`, `selected`, `fallback`, `single_candidate`. How the router chose among eligible models: cost (sorted by estimated credits), selected (preference ranking chose a model), fallback (preference ranking failed so the eligible models were left in filter order), or si...
  - `emptiedBy` (array of string, required) - The filter(s) that reduced the eligible pool to zero.
- `hasMore` (boolean, required) - Whether there are more items available after this page.
- `nextCursor` (string or null, required) - Cursor to use for fetching the next page, or null if there are no more pages.

