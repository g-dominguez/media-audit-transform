## Start generating

### POST /v1/sound_effect

Generate sound effects

This endpoint will start a new task to generate sound effects from a text description.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 3 shapes, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/sound_effect - model `seed_audio`

- `promptText` (string, required) - max length 2048. A non-empty text prompt. For text-to-speech, the words to speak. For text-to-audio, a scene description that can include voice direction, dialogue, music, and sound effects.
- `referenceAudios` (array of string) - max 3 items. Up to three reference audio clips. When provided, reference them in promptText as @Audio1, @Audio2, and @Audio3 in order.
- `speechRate` (integer) - -50-100. Relative speech speed. Negative is slower, positive is faster; 0 is normal.
- `loudnessRate` (integer) - -50-100. Relative output loudness. Negative is quieter, positive is louder; 0 is normal.
- `pitchRate` (integer) - -12-12. Pitch shift in semitones. Negative lowers, positive raises; 0 is unchanged.
- `sampleRate` (number) - one of `8000`, `16000`, `24000`, `32000`, `44100`, `48000`. Output sample rate in Hz.
- `outputFormat` (string) - one of `wav`, `mp3`, `ogg_opus`. Output audio container/format.
- `model` (string, required) - one of `seed_audio`

#### POST /v1/sound_effect - model `mirelo_sfx_2_0`

- `duration` (number, required) - 0.1-600. The duration of the generated audio in seconds.
- `negativePrompt` (string) - max length 1000. Sounds to avoid in the generated audio.
- `numVariants` (integer) - 1-4; default `1`. The number of audio variations to generate.
- `format` (string) - one of `mp3`, `wav`, `flac`; default `mp3`. The format of the generated audio.
- `seed` (integer) - 0-4294967295. A seed for reproducible generation.
- `promptText` (string, required) - max length 2000. A description of the sound effects to generate.
- `model` (string, required) - one of `mirelo_sfx_2_0`

#### POST /v1/sound_effect - model `eleven_text_to_sound_v2`

- `promptText` (string, required) - max length 3000. A text description of the sound effect to generate.
- `duration` (number) - 0.5-30. The duration of the sound effect in seconds, between 0.5 and 30 seconds. If not provided, the duration will be determined automatically based on the text description.
- `loop` (boolean) - default `false`. Whether the output sound effect should be designed to loop seamlessly.
- `model` (string, required) - one of `eleven_text_to_sound_v2`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

