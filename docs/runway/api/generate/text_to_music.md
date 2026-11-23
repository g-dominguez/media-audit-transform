## Start generating

### POST /v1/text_to_music

Generate music

This endpoint will start a new task to generate a song or instrumental track from a text description.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 1 shape, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/text_to_music - model `eleven_music_v2_5`

- `promptText` (string, required) - max length 4100. A description of the track to generate, such as its genre, mood, instruments, and vocals. Prompts that name specific artists or songs are rejected.
- `duration` (integer) - 3-600; default `30`. The length of the track in whole seconds. You are billed for the requested length.
- `instrumental` (boolean) - When true, the track has no vocals. When omitted, the model decides from the prompt.
- `model` (string, required) - one of `eleven_music_v2_5`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

