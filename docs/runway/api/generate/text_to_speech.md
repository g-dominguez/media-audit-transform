## Start generating

### POST /v1/text_to_speech

Text to speech

This endpoint will start a new task to generate speech from text. ElevenLabs models accept preset voices or custom voices created via the Voices API. Seed Audio accepts a reference audio clip.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 6 shapes, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/text_to_speech - model `seed_audio`

- `promptText` (string, required) - max length 2048. A non-empty text prompt. For text-to-speech, the words to speak. For text-to-audio, a scene description that can include voice direction, dialogue, music, and sound effects.
- `voice` (object) - The voice to use for text-to-speech generation. If omitted, a default voice is used.
  - `type` (string, required) - one of `reference-audio`
  - `audioUri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
- `speechRate` (integer) - -50-100. Relative speech speed. Negative is slower, positive is faster; 0 is normal.
- `loudnessRate` (integer) - -50-100. Relative output loudness. Negative is quieter, positive is louder; 0 is normal.
- `pitchRate` (integer) - -12-12. Pitch shift in semitones. Negative lowers, positive raises; 0 is unchanged.
- `sampleRate` (number) - one of `8000`, `16000`, `24000`, `32000`, `44100`, `48000`. Output sample rate in Hz.
- `outputFormat` (string) - one of `wav`, `mp3`, `ogg_opus`. Output audio container/format.
- `model` (string, required) - one of `seed_audio`

#### POST /v1/text_to_speech - model `eleven_v4`

- `promptText` (string, required) - The text to convert to speech. You can include expressive audio tags like [laughs], [whispers], or [pause] in the script.
- `voice` (object, required) - The voice to use for the generated speech.
  - `type` (string, required) - one of `runway-preset`, `custom`
  - `presetId` (string) - one of `Maya`, `Arjun`, `Serene`, `Bernard`, `Billy`, `Mark`, `Clint`, `Mabel`, `Chad`, `Leslie`, `Eleanor`, `Elias`, `Elliot`, `Grungle`, `Brodie`, `Sandra`, `Kirk`, `Kylie`, `Lara`, `Lisa`, `Malachi`, `Marlene`, `Martin`, `Miriam`, `Monster`, `Paula`, `Pip`, `Rusty`, `Ragnar`, `Xylar`, `Maggie`, `Jack`, `Katie`, `Noah`, `James`, `Rina`, `Ella`, `Mariah`, `Frank`, `Claudia`, ... (49 total). The preset voice ID to use for the generated speech.
  - `id` (string) - format uuid. The ID of a custom voice created via the Voices API.
- `stability` (number) - 0-1. Voice stability. Lower values allow broader emotional range; higher values are steadier.
- `similarityBoost` (number) - 0-1. How closely the output tracks the original speaker.
- `style` (number) - 0-1. Style exaggeration. Higher values amplify the speaker style.
- `speed` (number) - 0.7-1.2. Speech speed multiplier. Values below 1 slow the speech down, and values above 1 speed it up.
- `useSpeakerBoost` (boolean) - Boost similarity to the original speaker at a small latency cost.
- `languageCode` (string) - max length 16. Language code to enforce pronunciation, such as "en" or "pt". A regional code such as "pt-BR" is read as its language.
- `previousText` (string) - Text that comes before this request, so the speech can continue from an earlier generation.
- `nextText` (string) - Text that comes after this request, so the speech can lead into a later generation.
- `seed` (integer) - 0-4294967295. Optional seed for more consistent output. The same seed and settings tend to sound alike, but it is not guaranteed.
- `model` (string, required) - one of `eleven_v4`

#### POST /v1/text_to_speech - model `gemini_3.8_flash_tts`

- `voiceIds` (array of string, required) - min 1 items; max 2 items. The Google voice for each speaker, such as "Kore" or "Puck". Pass one voice for a single speaker, or two for a dialogue.
- `turns` (array of object, required) - min 1 items; max 100 items. The script, in the order it is spoken. Use one turn for a single speaker, or alternate speakers across turns for a dialogue.
  - `text` (string, required) - The words to speak in this turn.
  - `style` (string) - max length 200. How this turn should be delivered, such as "calm and reassuring". It guides the delivery and is not read aloud.
  - `speaker` (integer) - 0-1. The position in `voiceIds` of the voice that speaks this turn. Defaults to the first voice.
- `languageCode` (string) - max length 16. The language of the script, such as "en-US". When omitted, the model detects it.
- `model` (string, required) - one of `gemini_3.8_flash_tts`

#### POST /v1/text_to_speech - model `gemini_3.8_flash_lite_tts`

- `voiceIds` (array of string, required) - min 1 items; max 2 items. The Google voice for each speaker, such as "Kore" or "Puck". Pass one voice for a single speaker, or two for a dialogue.
- `turns` (array of object, required) - min 1 items; max 100 items. The script, in the order it is spoken. Use one turn for a single speaker, or alternate speakers across turns for a dialogue.
  - `text` (string, required) - The words to speak in this turn.
  - `style` (string) - max length 200. How this turn should be delivered, such as "calm and reassuring". It guides the delivery and is not read aloud.
  - `speaker` (integer) - 0-1. The position in `voiceIds` of the voice that speaks this turn. Defaults to the first voice.
- `languageCode` (string) - max length 16. The language of the script, such as "en-US". When omitted, the model detects it.
- `model` (string, required) - one of `gemini_3.8_flash_lite_tts`

#### POST /v1/text_to_speech - model `eleven_multilingual_v2`

- `promptText` (string, required) - max length 1000. A non-empty string up to 1000 characters (measured in UTF-16 code units). This should describe in detail what should appear in the output.
- `voice` (object, required) - The voice to use for the generated speech.
  - `type` (string, required) - one of `runway-preset`, `custom`
  - `presetId` (string) - one of `Maya`, `Arjun`, `Serene`, `Bernard`, `Billy`, `Mark`, `Clint`, `Mabel`, `Chad`, `Leslie`, `Eleanor`, `Elias`, `Elliot`, `Grungle`, `Brodie`, `Sandra`, `Kirk`, `Kylie`, `Lara`, `Lisa`, `Malachi`, `Marlene`, `Martin`, `Miriam`, `Monster`, `Paula`, `Pip`, `Rusty`, `Ragnar`, `Xylar`, `Maggie`, `Jack`, `Katie`, `Noah`, `James`, `Rina`, `Ella`, `Mariah`, `Frank`, `Claudia`, ... (49 total). The preset voice ID to use for the generated speech.
  - `id` (string) - format uuid. The ID of a custom voice created via the Voices API.
- `model` (string, required) - one of `eleven_multilingual_v2`

#### POST /v1/text_to_speech - model `eleven_v3`

- `promptText` (string, required) - max length 5000. The text to convert to speech. You can include expressive audio tags like [laughs] or [whispers] in the script.
- `voice` (object, required) - The voice to use for the generated speech.
  - `type` (string, required) - one of `runway-preset`, `custom`
  - `presetId` (string) - one of `Maya`, `Arjun`, `Serene`, `Bernard`, `Billy`, `Mark`, `Clint`, `Mabel`, `Chad`, `Leslie`, `Eleanor`, `Elias`, `Elliot`, `Grungle`, `Brodie`, `Sandra`, `Kirk`, `Kylie`, `Lara`, `Lisa`, `Malachi`, `Marlene`, `Martin`, `Miriam`, `Monster`, `Paula`, `Pip`, `Rusty`, `Ragnar`, `Xylar`, `Maggie`, `Jack`, `Katie`, `Noah`, `James`, `Rina`, `Ella`, `Mariah`, `Frank`, `Claudia`, ... (49 total). The preset voice ID to use for the generated speech.
  - `id` (string) - format uuid. The ID of a custom voice created via the Voices API.
- `stability` (number) - 0-1. Voice stability (0-1). Lower values allow broader emotional range; higher values are steadier.
- `similarityBoost` (number) - 0-1. How closely the output tracks the original speaker (0-1). Maps to ElevenLabs similarity_boost.
- `style` (number) - 0-1. Style exaggeration (0-1). Higher values amplify the speaker style.
- `speed` (number) - 0.7-1.2. Speech speed multiplier (0.7-1.2). 1.0 is default; values below slow down and above speed up.
- `useSpeakerBoost` (boolean) - Boost similarity to the original speaker at a small latency cost.
- `languageCode` (string) - max length 16. ISO 639-1 language code to enforce pronunciation and normalization.
- `applyTextNormalization` (string) - one of `auto`, `on`, `off`. Text normalization mode: 'auto', 'on', or 'off' (e.g. spelling out numbers).
- `seed` (integer) - 0-4294967295. Optional seed for more deterministic output (0-4294967295). Not guaranteed.
- `model` (string, required) - one of `eleven_v3`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

