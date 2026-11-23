## Start generating

### POST /v1/video_to_audio

Generate audio from a video

Generate synchronized sound effects for a video, optionally guided by a text description. Returns audio, not a video with a replacement soundtrack.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 1 shape, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/video_to_audio - model `mirelo_sfx_2_0`

- `duration` (number, required) - 1-600
- `negativePrompt` (string) - max length 1000. Sounds to avoid in the generated audio.
- `numVariants` (integer) - 1-4; default `1`. The number of audio variations to generate.
- `format` (string) - one of `mp3`, `wav`, `flac`; default `mp3`. The format of the generated audio.
- `seed` (integer) - 0-4294967295. A seed for reproducible generation.
- `promptText` (string) - max length 2000. A description of the sound effects to generate.
- `videoUri` (string, required) - The video to generate synchronized sound effects for. The output is audio only.
- `preserveSpeech` (boolean) - Whether to preserve dialogue from the input video. Disabling this does not guarantee speech-free output.
- `model` (string, required) - one of `mirelo_sfx_2_0`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

