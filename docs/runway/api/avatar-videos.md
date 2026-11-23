## Avatar Videos

### POST /v1/avatar_videos

Generate avatar video from audio or text

Start an asynchronous task to generate a video of an avatar speaking. Provide `speech` with `type: "audio"` (audio file) or `type: "text"` (text script for TTS). Poll `GET /v1/tasks/:id` to check progress and retrieve...

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `model` (string, required) - one of `gwm1_avatars`. The model to use for avatar video generation.
- `avatar` (object, required) - The avatar configuration for the session.
  - `type` (string, required) - one of `runway-preset`, `custom`
  - `presetId` (string) - one of `game-character`, `music-superstar`, `game-character-man`, `cat-character`, `influencer`, `tennis-coach`, `human-resource`, `fashion-designer`, `cooking-teacher`. ID of a preset avatar.
  - `avatarId` (string) - format uuid. ID of a user-created avatar.
- `speech` (object, required) - The speech source for avatar video generation. Either an audio file or text script.
  - `type` (string, required) - one of `audio`, `text`
  - `audio` (string) - A HTTPS URL, Runway or data URI containing an encoded audio. See [our docs](/assets/inputs#audio) on audio inputs for more information.
  - `text` (string) - max length 5000. Text script for speech-driven video generation.
  - `voice` (object) - Optional voice override for TTS. If not provided, the avatar's configured voice is used.
    - `type` (string, required) - one of `preset`, `custom`
    - `presetId` (string) - one of `victoria`, `vincent`, `clara`, `drew`, `skye`, `max`, `morgan`, `felix`, `mia`, `marcus`, `summer`, `ruby`, `aurora`, `jasper`, `leo`, `adrian`, `nina`, `emma`, `blake`, `david`, `maya`, `nathan`, `sam`, `georgia`, `petra`, `adam`, `zach`, `violet`, `roman`, `luna`
    - `id` (string) - format uuid

Response 200:

- `id` (string, required) - format uuid. The ID of the avatar video task. Use `GET /v1/tasks/:id` to poll for status and output.

