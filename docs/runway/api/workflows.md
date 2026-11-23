## Workflows

### GET /v1/workflows/{id}

Get workflow details

Returns details about a specific published workflow, including its graph schema.

Parameters:

- `id` (path, string, required) - format uuid. The ID of the published workflow to run. You can copy this value from the developer portal.

Response 200:

- `id` (string, required) - format uuid. The globally unique ID of the published workflow.
- `name` (string, required) - The name of the published workflow.
- `description` (string or null, required) - The description of the published workflow.
- `version` (integer, required) - minimum 1. A monotonically increasing version number. Each workflow version for the same published workflow has a unique version number.
- `createdAt` (string, required) - format date-time. When this version was published
- `updatedAt` (string, required) - format date-time. When this version was last updated
- `graph` (object, required) - The workflow graph definition.
  - `nodes` (array of unknown, required) - The list of nodes in the workflow graph.
  - `edges` (array of unknown, required) - The list of edges connecting nodes in the workflow graph.
  - `version` (integer, required) - minimum 1. The schema version of the workflow graph format.

Other responses: `404`

### POST /v1/workflows/{id}

Run a published workflow

Start a new task to execute a published workflow. You can optionally provide custom input values via `nodeOutputs` to override the defaults defined in the workflow graph.

Parameters:

- `id` (path, string, required) - format uuid. The ID of the published workflow to run. You can copy this value from the developer portal.
- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body:

- `nodeOutputs` (object) - Optional node outputs to override default values. Keys are node IDs from the workflow graph, values are objects mapping output keys to typed values.

Response 200:

- `id` (string, required) - format uuid. The ID of the workflow invocation that was created.

Other responses: `404`

### GET /v1/workflows

List published workflows

Returns a list of all published workflows for the authenticated user, grouped by source workflow with their published versions.

Response 200:

- `data` (array of object, required) - A list of published workflows grouped by source workflow.
  - `name` (string, required) - The name of the published workflow.
  - `versions` (array of object, required) - The published versions of this workflow, newest first.
    - `id` (string, required) - format uuid. The globally unique ID of this published workflow version.
    - `version` (integer, required) - minimum 1. A monotonically increasing version number. Each workflow version for the same published workflow has a unique version number.
    - `createdAt` (string, required) - format date-time. When this version was published

### GET /v1/workflow_invocations/{id}

Get workflow invocation detail

Return details about a workflow invocation. Consumers of this API should not expect updates more frequent than once every five seconds for a given workflow invocation. A `SUCCEEDED` invocation may still have had indiv...

Parameters:

- `id` (path, string, required) - format uuid. The ID of a previously-submitted workflow invocation that has not been canceled or deleted.

Response 200:

- `id` (string, required)
- `createdAt` (string, required)
- `status` (string, required) - one of `PENDING`, `THROTTLED`, `CANCELLED`, `RUNNING`, `FAILED`, `SUCCEEDED`
- `progress` (number) - 0-1. A number between 0 and 1 representing the overall workflow execution progress.
- `output` (object)
- `nodeErrors` (object)
- `failure` (string) - A human-friendly reason for the failure. We do not recommend returning this to users directly without adding context.
- `failureCode` (string) - A machine-readable error code for the failure. See https://docs.dev.runwayml.com/errors/task-failures/ for more information.
- `cost` (object)
  - `credits` (integer, required)

Other responses: `404`
