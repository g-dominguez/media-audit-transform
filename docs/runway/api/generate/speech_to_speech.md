## Start generating

### POST /v1/speech_to_speech

Speech to speech

This endpoint will start a new task to convert speech from one voice to another in audio or video.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 1 shape, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/speech_to_speech - model `eleven_multilingual_sts_v2`

- `removeBackgroundNoise` (boolean) - Whether to remove background noise from the generated speech.
- `media` (object, required)
  - `type` (string, required) - one of `audio`, `video`
  - `uri` (string, required)
- `voice` (object, required) - The voice to use for the generated speech.
  - `type` (string, required) - one of `runway-preset`
  - `presetId` (string, required) - one of `Maya`, `Arjun`, `Serene`, `Bernard`, `Billy`, `Mark`, `Clint`, `Mabel`, `Chad`, `Leslie`, `Eleanor`, `Elias`, `Elliot`, `Grungle`, `Brodie`, `Sandra`, `Kirk`, `Kylie`, `Lara`, `Lisa`, `Malachi`, `Marlene`, `Martin`, `Miriam`, `Monster`, `Paula`, `Pip`, `Rusty`, `Ragnar`, `Xylar`, `Maggie`, `Jack`, `Katie`, `Noah`, `James`, `Rina`, `Ella`, `Mariah`, `Frank`, `Claudia`, ... (49 total). The preset voice ID to use for the generated speech.
- `model` (string, required) - one of `eleven_multilingual_sts_v2`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

