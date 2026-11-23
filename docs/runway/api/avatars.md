## Avatars

### GET /v1/avatars

List avatars

List avatars for the authenticated user with cursor-based pagination.

Parameters:

- `cursor` (query, string) - max length 1000. Cursor from a previous response for fetching the next page of results.
- `limit` (query, integer) - 1-100; default `50`. The maximum number of items to return per page.

Response 200:

- `data` (array of object, required) - The list of items for the current page.
  - `id` (string, required)
  - `name` (string, required)
  - `personality` (string, required)
  - `startScript` (string or null, required)
  - `voice` (object, required)
    - `type` (string, required) - one of `runway-live-preset`, `custom`
    - `presetId` (string) - one of `victoria`, `vincent`, `clara`, `drew`, `skye`, `max`, `morgan`, `felix`, `mia`, `marcus`, `summer`, `ruby`, `aurora`, `jasper`, `leo`, `adrian`, `nina`, `emma`, `blake`, `david`, `maya`, `nathan`, `sam`, `georgia`, `petra`, `adam`, `zach`, `violet`, `roman`, `luna`
    - `name` (string)
    - `description` (string or string or null)
    - `id` (string)
    - `deleted` (boolean)
  - `referenceImageUri` (string or null, required)
  - `processedImageUri` (string or null, required)
  - `documentIds` (array of string, required)
  - `createdAt` (string, required)
  - `updatedAt` (string, required)
  - `status` (string, required) - one of `PROCESSING`, `READY`, `FAILED`
  - `failureReason` (string) - A human-readable error message. This value is not stable and should not be matched against programmatically.
- `hasMore` (boolean, required) - Whether there are more items available after this page.
- `nextCursor` (string or null, required) - Cursor to use for fetching the next page, or null if there are no more pages.

### POST /v1/avatars

Create avatar

Create a new avatar with a reference image and voice.

Request body:

- `name` (string, required) - max length 50. The character name for the avatar.
- `referenceImage` (string, required) - A HTTPS URL, Runway URI, or data URI containing the avatar reference image. See [our docs](/assets/inputs#images) for supported formats.
- `personality` (string, required) - max length 10000. System prompt defining how the avatar should behave in conversations.
- `startScript` (string) - max length 2000. Optional opening message that the avatar will say when a session starts.
- `voice` (object, required) - The voice configuration for the avatar.
  - `type` (string, required) - one of `runway-live-preset`, `custom`
  - `presetId` (string) - one of `victoria`, `vincent`, `clara`, `drew`, `skye`, `max`, `morgan`, `felix`, `mia`, `marcus`, `summer`, `ruby`, `aurora`, `jasper`, `leo`, `adrian`, `nina`, `emma`, `blake`, `david`, `maya`, `nathan`, `sam`, `georgia`, `petra`, `adam`, `zach`, `violet`, `roman`, `luna`. The ID of a preset voice. Available voices: `victoria` (Victoria), `vincent` (Vincent), `clara` (Clara), `drew` (Drew), `skye` (Skye), `max` (Max), `morgan` (Morgan), `felix` (Felix), `mia` (Mia), `marcus` (Marcus), `...
  - `id` (string) - format uuid. The ID of a custom voice created via the Voices API.
- `documentIds` (array of string) - max 50 items. Optional list of knowledge document IDs to attach to this avatar. Documents provide additional context during conversations.
- `imageProcessing` (string) - one of `optimize`, `none`; default `optimize`. Controls image preprocessing. `optimize` improves the image for better avatar results. `none` uses the image as-is; quality not guaranteed.

Response 200:

- `id` (string, required)
- `name` (string, required)
- `personality` (string, required)
- `startScript` (string or null, required)
- `voice` (object, required)
  - `type` (string, required) - one of `runway-live-preset`, `custom`
  - `presetId` (string) - one of `victoria`, `vincent`, `clara`, `drew`, `skye`, `max`, `morgan`, `felix`, `mia`, `marcus`, `summer`, `ruby`, `aurora`, `jasper`, `leo`, `adrian`, `nina`, `emma`, `blake`, `david`, `maya`, `nathan`, `sam`, `georgia`, `petra`, `adam`, `zach`, `violet`, `roman`, `luna`
  - `name` (string)
  - `description` (string or string or null)
  - `id` (string)
  - `deleted` (boolean)
- `referenceImageUri` (string or null, required)
- `processedImageUri` (string or null, required)
- `documentIds` (array of string, required)
- `createdAt` (string, required)
- `updatedAt` (string, required)
- `status` (string, required) - one of `PROCESSING`, `READY`, `FAILED`
- `failureReason` (string) - A human-readable error message. This value is not stable and should not be matched against programmatically.

### GET /v1/avatar_conversations

List conversations

List realtime avatar conversations for the authenticated user with cursor-based pagination. Each conversation corresponds to a realtime session, and the conversation ID matches the realtime session ID. Pass `avatar` t...

Parameters:

- `cursor` (query, string) - max length 1000. Cursor from a previous response for fetching the next page of results.
- `limit` (query, integer) - 1-100; default `20`. The maximum number of items to return per page.
- `avatar` (query, string) - format uuid. Filter to conversations that used the given custom avatar.
- `startDate` (query, string) - format date-time. Filter conversations created on or after this timestamp (inclusive).
- `endDate` (query, string) - format date-time. Filter conversations created before this timestamp (exclusive).

Response 200:

- `data` (array of object, required) - Array of conversation summaries.
  - `id` (string, required) - format uuid. Unique conversation identifier. This is the same value as the realtime session ID for the call.
  - `name` (string, required) - Conversation name (auto-generated or user-provided).
  - `status` (string, required) - one of `in_progress`, `ended`, `failed`. The status of the conversation. `in_progress` means the session is active, `ended` means it completed successfully, `failed` means it ended due to an error.
  - `avatar` (object or null, required) - The avatar used in this conversation, or null if unavailable.
    - `type` (string, required) - one of `runway-preset`, `custom`
    - `presetId` (string) - The preset avatar ID.
    - `name` (string or string or null, required)
    - `id` (string or null) - The custom avatar ID, or null if deleted.
  - `createdAt` (string, required) - format date-time. When the conversation was created.
  - `duration` (integer or null, required) - Duration of the conversation in seconds, or null if not started.
  - `hasTools` (boolean, required) - Whether tools were configured for this conversation session.
- `hasMore` (boolean, required) - Whether there are more conversations to fetch.
- `nextCursor` (string or null, required) - Cursor to use for fetching the next page, or null if no more pages.

### GET /v1/avatar_usage

Get avatar usage

Get aggregate usage statistics for avatar conversations, including total duration, session counts, average duration, and a per-day breakdown. Per-day buckets are keyed by UTC calendar date. The date range must not exc...

Parameters:

- `startDate` (query, string, required) - format date-time. Start of the date range in UTC (inclusive). Required.
- `endDate` (query, string, required) - format date-time. End of the date range in UTC (exclusive). Required.

Response 200:

- `totalSeconds` (integer, required) - Total seconds across conversations with a measured duration in the date range.
- `totalSessions` (integer, required) - Number of conversations started in the date range. Includes unfinished and failed conversations.
- `avgDurationSeconds` (integer, required) - Average duration in seconds across conversations with a measured duration, or 0 if none completed. May not equal `totalSeconds / totalSessions` because unfinished conversations contribute to the session count but not...
- `byDay` (array of object, required) - Per-day usage across the date range. Days with no sessions are included with zeroes.
  - `date` (string, required) - format date. The UTC calendar date (YYYY-MM-DD).
  - `sessions` (integer, required) - Number of conversations started on this date.
  - `seconds` (integer, required) - Total seconds of measured conversation duration on this date.

### GET /v1/avatar_conversations/{id}

Get conversation

Get detailed information about a specific conversation, including the transcript and recording download URL when available. The conversation ID is the same value returned when the realtime session was created.

Parameters:

- `id` (path, string, required) - format uuid. The conversation ID. This is the same value as the realtime session ID for the call.

Response 200:

- `id` (string, required)
- `name` (string, required)
- `avatar` (object or null, required)
  - `type` (string, required) - one of `runway-preset`, `custom`
  - `presetId` (string)
  - `id` (string or null)
  - `name` (string or null)
  - `imageUrl` (string or null)
- `createdAt` (string, required)
- `maxDuration` (integer or null, required)
- `transcript` (array of object, required)
  - `role` (string, required) - one of `user`, `assistant`
  - `content` (string or null, required)
  - `timestamp` (string or null, required)
  - `toolCalls` (array of object)
    - `id` (string)
    - `name` (string, required)
    - `arguments` (object, required)
  - `toolResults` (array of object)
    - `id` (string)
    - `name` (string, required)
    - `result` (object or string or null)
    - `error` (string or null)
    - `durationMs` (number or null)
- `recordingUrl` (string or null, required)
- `tools` (array of object, required)
  - `type` (string, required) - one of `client_event`, `backend_rpc`
  - `name` (string, required)
  - `description` (string, required)
- `status` (string, required) - one of `in_progress`, `ended`, `failed`
- `startedAt` (string or null, required)
- `duration` (integer or null, required)
- `endedAt` (string or null)
- `failure` (string) - A human-friendly reason for the failure. We do not recommend returning this to users directly without adding context.
- `failureCode` (string) - A machine-readable error code for the failure. See https://docs.dev.runwayml.com/errors/task-failures/ for more information.

### DELETE /v1/avatar_conversations/{id}

Delete conversation

Permanently delete a conversation, including its transcript and recording.

Parameters:

- `id` (path, string, required) - format uuid. The conversation ID.

### GET /v1/avatars/{id}

Get avatar

Get details of a specific avatar.

Parameters:

- `id` (path, string, required) - format uuid

Response 200:

- `id` (string, required)
- `name` (string, required)
- `personality` (string, required)
- `startScript` (string or null, required)
- `voice` (object, required)
  - `type` (string, required) - one of `runway-live-preset`, `custom`
  - `presetId` (string) - one of `victoria`, `vincent`, `clara`, `drew`, `skye`, `max`, `morgan`, `felix`, `mia`, `marcus`, `summer`, `ruby`, `aurora`, `jasper`, `leo`, `adrian`, `nina`, `emma`, `blake`, `david`, `maya`, `nathan`, `sam`, `georgia`, `petra`, `adam`, `zach`, `violet`, `roman`, `luna`
  - `name` (string)
  - `description` (string or string or null)
  - `id` (string)
  - `deleted` (boolean)
- `referenceImageUri` (string or null, required)
- `processedImageUri` (string or null, required)
- `documentIds` (array of string, required)
- `createdAt` (string, required)
- `updatedAt` (string, required)
- `status` (string, required) - one of `PROCESSING`, `READY`, `FAILED`
- `failureReason` (string) - A human-readable error message. This value is not stable and should not be matched against programmatically.

### PATCH /v1/avatars/{id}

Update avatar

Update an existing avatar. At least one field must be provided.

Parameters:

- `id` (path, string, required) - format uuid

Request body:

- `name` (string) - max length 50. The character name for the avatar.
- `referenceImage` (string) - A HTTPS URL, Runway URI, or data URI containing the avatar reference image. See [our docs](/assets/inputs#images) for supported formats.
- `personality` (string) - max length 10000. System prompt defining how the avatar should behave in conversations.
- `startScript` (string or null) - Optional opening message that the avatar will say when a session starts. Set to null to clear.
- `voice` (object) - The voice configuration for the avatar.
  - `type` (string, required) - one of `runway-live-preset`, `custom`
  - `presetId` (string) - one of `victoria`, `vincent`, `clara`, `drew`, `skye`, `max`, `morgan`, `felix`, `mia`, `marcus`, `summer`, `ruby`, `aurora`, `jasper`, `leo`, `adrian`, `nina`, `emma`, `blake`, `david`, `maya`, `nathan`, `sam`, `georgia`, `petra`, `adam`, `zach`, `violet`, `roman`, `luna`. The ID of a preset voice. Available voices: `victoria` (Victoria), `vincent` (Vincent), `clara` (Clara), `drew` (Drew), `skye` (Skye), `max` (Max), `morgan` (Morgan), `felix` (Felix), `mia` (Mia), `marcus` (Marcus), `...
  - `id` (string) - format uuid. The ID of a custom voice created via the Voices API.
- `documentIds` (array of string) - max 50 items. List of knowledge document IDs to attach to this avatar. Replaces all current attachments. Documents provide additional context during conversations.
- `imageProcessing` (string) - one of `optimize`, `none`; default `optimize`. Controls image preprocessing. `optimize` improves the image for better avatar results. `none` uses the image as-is; quality not guaranteed.

Response 200:

- `id` (string, required)
- `name` (string, required)
- `personality` (string, required)
- `startScript` (string or null, required)
- `voice` (object, required)
  - `type` (string, required) - one of `runway-live-preset`, `custom`
  - `presetId` (string) - one of `victoria`, `vincent`, `clara`, `drew`, `skye`, `max`, `morgan`, `felix`, `mia`, `marcus`, `summer`, `ruby`, `aurora`, `jasper`, `leo`, `adrian`, `nina`, `emma`, `blake`, `david`, `maya`, `nathan`, `sam`, `georgia`, `petra`, `adam`, `zach`, `violet`, `roman`, `luna`
  - `name` (string)
  - `description` (string or string or null)
  - `id` (string)
  - `deleted` (boolean)
- `referenceImageUri` (string or null, required)
- `processedImageUri` (string or null, required)
- `documentIds` (array of string, required)
- `createdAt` (string, required)
- `updatedAt` (string, required)
- `status` (string, required) - one of `PROCESSING`, `READY`, `FAILED`
- `failureReason` (string) - A human-readable error message. This value is not stable and should not be matched against programmatically.

Other responses: `409`

### DELETE /v1/avatars/{id}

Delete avatar

Delete an avatar.

Parameters:

- `id` (path, string, required) - format uuid

