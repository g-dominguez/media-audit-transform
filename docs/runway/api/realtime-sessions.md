## Realtime Sessions

### POST /v1/realtime_sessions

Create realtime session

Create a new realtime session with the specified model configuration. The returned ID is also the conversation ID used later to fetch transcripts and recordings from the avatar conversation endpoints.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 1 shape, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/realtime_sessions - model `gwm1_avatars`

- `model` (string, required) - one of `gwm1_avatars`. The realtime session model type.
- `avatar` (object, required) - The avatar configuration for the session.
  - `type` (string, required) - one of `runway-preset`, `custom`
  - `presetId` (string) - one of `game-character`, `music-superstar`, `game-character-man`, `cat-character`, `influencer`, `tennis-coach`, `human-resource`, `fashion-designer`, `cooking-teacher`. ID of a preset avatar.
  - `avatarId` (string) - format uuid. ID of a user-created avatar.
- `maxDuration` (integer) - 10-1800; default `300`. Maximum session duration in seconds.
- `personality` (string) - max length 10000. Override the avatar personality for this session. If not provided, uses the avatar default.
- `startScript` (string) - max length 2000. Override the avatar start script for this session. If not provided, uses the avatar default.
- `tools` (array of object) - max 20 items; default `[]`. Tools available to the avatar during the session.
  - `type` (string, required) - one of `client_event`, `backend_rpc`
  - `name` (string, required)
  - `description` (string, required)
  - `parameters` (array of object)
    - `name` (string, required)
    - `description` (string, required)
    - `required` (boolean)
    - `type` (string, required) - one of `string`, `integer`, `number`, `boolean`, `array`, `object`
    - `enum` (array of string)
    - `items` (object)
      - `type` (string, required) - one of `string`, `integer`, `number`, `boolean`
    - `properties` (array of unknown)
  - `timeoutSeconds` (number) - 1-8; default `4`. Maximum time to wait for the backend to respond.
- `integration` (object) - External integration. Runway renders the avatar; the integration owns conversation or audio.
  - `type` (string, required) - one of `elevenlabs`, `livekit`
  - `signedUrl` (string) - format uri. ConvAI signed WebSocket URL (~15 min lifetime). Must be a wss:// or https:// URL that resolves to a public host.
  - `url` (string) - format uri. WebSocket URL of the external LiveKit server the avatar worker should join. Must be a wss:// or https:// URL that resolves to a public host.
  - `token` (string) - max length 2048. LiveKit access token granting the avatar worker publish rights in the external room.
  - `roomName` (string) - max length 256. Name of the external LiveKit room.
  - `agentIdentity` (string) - max length 256. The participant identity of the customer agent already in the room. When provided, the avatar worker trusts audio published by this identity.
- `livekit` (object) - Use integration with type "livekit" instead.
  - `url` (string, required) - format uri. WebSocket URL of the external LiveKit server the avatar worker should join. Must be a wss:// or https:// URL that resolves to a public host.
  - `token` (string, required) - max length 2048. LiveKit access token granting the avatar worker publish rights in the external room.
  - `roomName` (string, required) - max length 256. Name of the external LiveKit room.
  - `agentIdentity` (string) - max length 256. The participant identity of the customer agent already in the room. When provided, the avatar worker trusts audio published by this identity.

Response 200:

- `id` (string, required) - format uuid. The ID of the created realtime session. This same value is later used as the conversation ID in the avatar conversation endpoints.

### GET /v1/realtime_sessions/{id}

Get realtime session

Get the status of a realtime session. This endpoint uses the same ID that the avatar conversation endpoints later expose as the conversation ID.

Parameters:

- `id` (path, string, required) - format uuid. The realtime session ID. This same value is later used as the conversation ID in the avatar conversation endpoints.

Response 200:

- `id` (string, required)
- `createdAt` (string, required)
- `status` (string, required) - one of `NOT_READY`, `READY`, `RUNNING`, `COMPLETED`, `FAILED`, `CANCELLED`
- `queued` (boolean) - When true, the session is waiting in a queue for available capacity. When false or absent, the session is actively being provisioned.
- `expiresAt` (string) - format date-time. When the session credentials expire.
- `sessionKey` (string) - Session key for authenticating the /consume endpoint. Use as Bearer token.
- `duration` (integer) - The session duration in seconds.
- `failure` (string) - A human-readable error message. This value is not stable and should not be matched against programmatically.
- `failureCode` (string) - A stable, machine-readable error code. See https://docs.dev.runwayml.com/errors/task-failures/ for more information.

### DELETE /v1/realtime_sessions/{id}

Cancel realtime session

Cancel an active realtime session.

Parameters:

- `id` (path, string, required) - format uuid. The realtime session ID. This same value is later used as the conversation ID in the avatar conversation endpoints.

