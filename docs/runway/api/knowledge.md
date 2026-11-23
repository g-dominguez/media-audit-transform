## Knowledge

### GET /v1/documents

List documents

List knowledge documents for the authenticated user with cursor-based pagination.

Parameters:

- `cursor` (query, string) - max length 1000. Cursor from a previous response for fetching the next page of results.
- `limit` (query, integer) - 1-100; default `50`. The maximum number of items to return per page.
- `sort` (query, string) - one of `createdAt`, `updatedAt`; default `createdAt`. Field to sort results by.
- `order` (query, string) - one of `asc`, `desc`; default `desc`. Sort direction.

Response 200:

- `data` (array of object, required) - The list of items for the current page.
  - `id` (string, required) - format uuid. The unique identifier of the document.
  - `name` (string, required) - The name of the document.
  - `type` (string, required) - one of `text`, `file`. The type of document.
  - `usedBy` (array of object, required) - Avatars that use this document.
    - `id` (string, required) - format uuid. The avatar ID.
    - `name` (string, required) - The avatar name.
    - `imageUrl` (string or null, required) - URL to the avatar image, or null if not yet processed.
  - `createdAt` (string, required) - format date-time. When the document was created.
  - `updatedAt` (string, required) - format date-time. When the document was last updated.
- `hasMore` (boolean, required) - Whether there are more items available after this page.
- `nextCursor` (string or null, required) - Cursor to use for fetching the next page, or null if there are no more pages.

### POST /v1/documents

Create document

Create a new knowledge document. Documents can be attached to avatars to provide additional context during conversations.

Request body:

- `name` (string, required) - max length 255. A descriptive name for the document.
- `content` (string, required) - max length 200000. The markdown or plain text content of the document.

Response 200:

- `id` (string, required) - format uuid. The unique identifier of the document.
- `name` (string, required) - The name of the document.
- `type` (string, required) - one of `text`, `file`. The type of document.
- `usedBy` (array of object, required) - Avatars that use this document. Always empty for newly created documents.
  - `id` (string, required) - format uuid. The avatar ID.
  - `name` (string, required) - The avatar name.
  - `imageUrl` (string or null, required) - URL to the avatar image, or null if not yet processed.
- `content` (string, required) - The full content of the document.
- `createdAt` (string, required) - format date-time. When the document was created.
- `updatedAt` (string, required) - format date-time. When the document was last updated.

### GET /v1/documents/{id}

Get document

Get details of a specific knowledge document.

Parameters:

- `id` (path, string, required) - format uuid. The document ID.

Response 200:

- `id` (string, required) - format uuid. The unique identifier of the document.
- `name` (string, required) - The name of the document.
- `type` (string, required) - one of `text`, `file`. The type of document.
- `usedBy` (array of object, required) - Avatars that use this document.
  - `id` (string, required) - format uuid. The avatar ID.
  - `name` (string, required) - The avatar name.
  - `imageUrl` (string or null, required) - URL to the avatar image, or null if not yet processed.
- `content` (string, required) - The full content of the document.
- `createdAt` (string, required) - format date-time. When the document was created.
- `updatedAt` (string, required) - format date-time. When the document was last updated.

### PATCH /v1/documents/{id}

Update document

Update a knowledge document. At least one of `name` or `content` must be provided.

Parameters:

- `id` (path, string, required) - format uuid. The document ID.

Request body:

- `name` (string) - max length 255. A new name for the document.
- `content` (string) - max length 200000. New markdown or plain text content for the document.

### DELETE /v1/documents/{id}

Delete document

Delete a knowledge document. This also removes it from all avatars it was attached to.

Parameters:

- `id` (path, string, required) - format uuid. The document ID.

