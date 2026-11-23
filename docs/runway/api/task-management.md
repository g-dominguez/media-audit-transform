## Task management

Endpoints for managing tasks that have been submitted.

### GET /v1/tasks/{id}

Get task detail

Return details about a task. Consumers of this API should not expect updates more frequent than once every five seconds for a given task.

Parameters:

- `id` (path, string, required) - format uuid. The ID of a previously-submitted task that has not been canceled or deleted.

Response 200:

- `id` (string, required)
- `createdAt` (string, required)
- `status` (string, required) - one of `PENDING`, `THROTTLED`, `CANCELLED`, `RUNNING`, `FAILED`, `SUCCEEDED`
- `estimatedCost` (object)
  - `credits` (number, required)
- `cost` (object)
  - `credits` (integer, required)
- `progress` (number) - 0-1
- `failure` (string) - A human-friendly reason for the failure. We do not recommend returning this to users directly without adding context.
- `failureCode` (string) - A machine-readable error code for the failure. See https://docs.dev.runwayml.com/errors/task-failures/ for more information.
- `output` (array of string) - An array of URLs that return the output of the task. These URLs will expire within 24-48 hours; fetch the task again to get fresh URLs. It is expected that you download the assets at these URLs and store them in your...
- `layers` (array of object) - Layer details for successful Seedream layer decomposition tasks. Each URI matches the output URL at the same index.
  - `uri` (string, required) - format uri. An ephemeral URL for this layer, matching output at the same index.
  - `name` (string) - The layer filename.
  - `zIndex` (number) - The layer stacking order returned by the model provider.
  - `boundingBox` (object) - The layer bounds in absolute and normalized coordinates, when returned by the model provider.
    - `absolute` (array of number, required)
    - `normalized` (array of number, required)

Other responses: `404`

### DELETE /v1/tasks/{id}

Cancel or delete a task

Tasks that are running, pending, or throttled can be canceled by invoking this method. Invoking this method for other tasks will delete them. Refund eligibility is based on the task status observed by the server durin...

Parameters:

- `id` (path, string, required) - format uuid. The ID of a previously-submitted task that has not been canceled or deleted.

