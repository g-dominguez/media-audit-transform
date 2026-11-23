## Uploads

Endpoints for uploading media files.

### POST /v1/uploads

Upload a file

Uploads a temporary media file that can be referenced in API generation requests. The uploaded files will be automatically expired and deleted after a period of time. It is strongly recommended to use our SDKs for thi...

Request body:

- `filename` (string, required) - max length 255. The filename of the file to upload. Must have a valid extension and be a supported media type (image, video, or audio).
- `type` (string, required) - one of `ephemeral`. The type of upload to create

Response 200:

- `uploadUrl` (string, required) - format uri. The URL to upload your media file to with a POST request.
- `fields` (object, required) - Fields that must be included in the file upload request as form data.
- `runwayUri` (string, required) - The Runway upload URI to use in other API generation requests

Other responses: `429`

