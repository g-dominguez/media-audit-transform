## Start generating

### POST /v1/voice_dubbing

Voice dubbing

This endpoint will start a new task to dub audio content to a target language.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 1 shape, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/voice_dubbing - model `eleven_voice_dubbing`

- `audioUri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `targetLang` (string, required) - one of `en`, `hi`, `pt`, `zh`, `es`, `fr`, `de`, `ja`, `ar`, `ru`, `ko`, `id`, `it`, `nl`, `tr`, `pl`, `sv`, `fil`, `ms`, `ro`, `uk`, `el`, `cs`, `da`, `fi`, `bg`, `hr`, `sk`, `ta`. The target language code to dub the audio to (e.g., "es" for Spanish, "fr" for French).
- `disableVoiceCloning` (boolean) - Whether to disable voice cloning and use a generic voice instead.
- `dropBackgroundAudio` (boolean) - Whether to remove background audio from the dubbed output.
- `numSpeakers` (integer) - greater than 0. The number of speakers in the audio. If not provided, it will be detected automatically.
- `model` (string, required) - one of `eleven_voice_dubbing`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

