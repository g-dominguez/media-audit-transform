## Voices

### GET /v1/voices

List voices

List custom voices for the authenticated organization with cursor-based pagination.

Parameters:

- `cursor` (query, string) - max length 1000. Cursor from a previous response for fetching the next page of results.
- `limit` (query, integer) - 1-100; default `50`. The maximum number of items to return per page.

Response 200:

- `data` (array of object, required) - The list of items for the current page.
  - `id` (string, required)
  - `name` (string, required)
  - `description` (string or null, required)
  - `createdAt` (string, required)
  - `status` (string, required) - one of `PROCESSING`, `READY`, `FAILED`
  - `previewUrl` (string or null) - A signed URL to an MP3 audio sample of the voice, or null if no sample is available.
  - `failureReason` (string) - A human-readable error message. This value is not stable and should not be matched against programmatically.
- `hasMore` (boolean, required) - Whether there are more items available after this page.
- `nextCursor` (string or null, required) - Cursor to use for fetching the next page, or null if there are no more pages.

### POST /v1/voices

Create a voice

Create a custom voice from a text description, or clone a voice from an audio sample.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `name` (string, required) - max length 100. A name for the voice.
- `description` (string or null) - An optional description of the voice.
- `from` (object, required)
  - `type` (string, required) - one of `audio`, `text`
  - `audio` (string) - Audio sample to clone the voice from. Must be between 10 seconds and 5 minutes long. At most 10MB as a URL or Runway upload URI; at most 5MB as an inline data URI. For best results, use a clear recording with minimal...
  - `prompt` (string) - max length 1000. A text description of the desired voice characteristics. Must be at least 20 characters.
  - `model` (string) - one of `eleven_ttv_v3`, `eleven_multilingual_ttv_v2`. The voice design model to use. Prefer eleven_ttv_v3 (latest); eleven_multilingual_ttv_v2 is the previous generation.

Response 200:

- `id` (string, required) - format uuid. The ID of the voice that was created.

### GET /v1/voices/{id}

Get a voice

Get details about a specific custom voice.

Parameters:

- `id` (path, string, required) - format uuid. The ID of the voice to retrieve.

Response 200:

- `id` (string, required)
- `name` (string, required)
- `description` (string or null, required)
- `createdAt` (string, required)
- `status` (string, required) - one of `PROCESSING`, `READY`, `FAILED`
- `previewUrl` (string or null) - A signed URL to an MP3 audio sample of the voice, or null if no sample is available.
- `failureReason` (string) - A human-readable error message. This value is not stable and should not be matched against programmatically.

### PATCH /v1/voices/{id}

Update a voice

Update the name and/or description of a custom voice.

Parameters:

- `id` (path, string, required) - format uuid. The ID of the voice to update.

Request body:

- `name` (string) - max length 100. A name for the voice.
- `description` (string or null) - An optional description of the voice.

Response 200:

- `id` (string, required)
- `name` (string, required)
- `description` (string or null, required)
- `createdAt` (string, required)
- `status` (string, required) - one of `PROCESSING`, `READY`, `FAILED`
- `previewUrl` (string or null) - A signed URL to an MP3 audio sample of the voice, or null if no sample is available.
- `failureReason` (string) - A human-readable error message. This value is not stable and should not be matched against programmatically.

### DELETE /v1/voices/{id}

Delete a voice

Delete a custom voice.

Parameters:

- `id` (path, string, required) - format uuid. The ID of the voice to delete.

### POST /v1/voices/preview

Preview a voice

Generate a short audio preview of a voice from a text description. Use this to audition a voice before creating it.

Request body:

- `prompt` (string, required) - max length 1000. A text description of the desired voice characteristics. Must be at least 20 characters.
- `model` (string, required) - one of `eleven_ttv_v3`, `eleven_multilingual_ttv_v2`. The voice design model to use. Prefer eleven_ttv_v3 (latest); eleven_multilingual_ttv_v2 is the previous generation.

Response 200:

- `url` (string, required) - format uri. A presigned URL to the audio preview. The URL expires after 24 hours.
- `durationSecs` (number, required) - Duration of the audio preview in seconds.

