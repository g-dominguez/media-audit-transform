# Runway Dev context

A condensed primer for agents and language models working with Runway Dev. It covers
authentication, the task lifecycle, the complete endpoint surface, and the mistakes that most often
break a first integration.

If you need exact request fields and their allowed values, read
[/api.md](https://docs.dev.runwayml.com/api.md) next. Everything in this file is also documented at
length across <https://docs.dev.runwayml.com>, where every page is available as raw Markdown by
appending `.md` to its path.

## The essentials

- Base URL: `https://api.dev.runwayml.com`
- Authentication: `Authorization: Bearer <your API secret>`
- Required on every request: `X-Runway-Version: 2024-11-06`
- Get a key from the Developer Portal at <https://dev.runway.com>. The SDKs read it from the
  `RUNWAYML_API_SECRET` environment variable.

Official SDKs are `@runwayml/sdk` for Node and `runwayml` for Python. Prefer them over hand-rolled
HTTP calls: they handle the version header, retries, and task polling for you.

## Generation is asynchronous

This is the single most important thing to internalise. With few exceptions, you do not get output
back from the request that starts the work.

1. Send a generation request, for example `POST /v1/text_to_video`.
2. Receive `{ "id": "<uuid>" }`.
3. Poll `GET /v1/tasks/{id}` until `status` is terminal.
4. Read the output URLs from `output` on a successful task.

`status` is one of `PENDING`, `THROTTLED`, `RUNNING`, `SUCCEEDED`, `FAILED`, or `CANCELLED`. Only
`SUCCEEDED` carries an `output` array. `FAILED` carries `failure` (human-readable) and `failureCode`
(machine-readable). `THROTTLED` is not an error; the task is queued behind your rate limit and will
proceed on its own.

`DELETE /v1/tasks/{id}` cancels an in-progress task or deletes a finished one.

Poll with backoff rather than a tight loop, and treat generation as a job that takes anywhere from
seconds to minutes depending on the model and duration. In the SDKs, `waitForTaskOutput()` (Node) and
`wait_for_task_output()` (Python) do this correctly, including raising a distinct
`TaskFailedError` you can catch:

```ts
import RunwayML, { TaskFailedError } from "@runwayml/sdk";

const client = new RunwayML();

try {
  const task = await client.textToVideo
    .create({
      model: "seedance2_5",
      promptText: "A timelapse on a sunny day with clouds flying by",
      ratio: "1280:720",
      duration: 5,
    })
    .waitForTaskOutput();

  console.log(task.output[0]);
} catch (error) {
  if (error instanceof TaskFailedError) {
    console.error(error.taskDetails);
  } else {
    throw error;
  }
}
```

Output URLs are temporary. Download and store anything you intend to keep. See
<https://docs.dev.runwayml.com/assets/outputs.md>.

## Request bodies are per-model, not per-endpoint

The mistake that breaks most integrations: on generation endpoints the request body is almost always a
discriminated union keyed on `model`. The valid `ratio` values, the allowed `duration` values, the
prompt length limit, and which optional fields exist **all change depending on the model you pick**.

For example, on `POST /v1/text_to_video`:

- `gen4.5` accepts `ratio` of `1280:720` or `720:1280`, any integer `duration` from 2 to 10, and a
  1,000 character prompt. Both `ratio` and `duration` are required.
- `gemini_omni_flash` accepts the same two ratios, but `duration` from 3 to 10 and a 4,000 character
  prompt, and requires neither `ratio` nor `duration`.
- `seedance2` accepts 24 ratios up to 4K, `duration` from 4 to 15, a 3,500 character prompt, and adds
  `audio`, `references`, `referenceVideos`, and `referenceAudio`.

Note that the first two share an identical `ratio` set yet differ on everything else, including which
fields are required. So never carry a `ratio` or `duration` from one model to another, and never
guess. Look up the exact model in [/api.md](https://docs.dev.runwayml.com/api.md), which lists every
field for every model variant, or in [/openapi.json](https://docs.dev.runwayml.com/openapi.json).

These three are illustrations of how much varies between models, not recommendations. Choose a model
from [/guides/models.md](https://docs.dev.runwayml.com/guides/models.md), which describes what each
one is actually good at.

## Capability map

Thirteen endpoint groups, 58 operations. Each links to a task-scoped documentation bundle you can load
in full. The same grouping, generated from the spec, opens
[/api.md](https://docs.dev.runwayml.com/api.md).

### Generation

- **Start generating** (12 endpoints) — the core generative surface:
  `/v1/text_to_video`, `/v1/image_to_video`, `/v1/video_to_video`, `/v1/text_to_image`,
  `/v1/image_upscale`, `/v1/video_upscale`, `/v1/character_performance`, `/v1/text_to_speech`,
  `/v1/speech_to_speech`, `/v1/sound_effect`, `/v1/voice_dubbing`, `/v1/voice_isolation`.
- **Task management** (2 endpoints) — `GET` and `DELETE /v1/tasks/{id}`. Every generation flows
  through here.
- **Uploads** (1 endpoint) — `POST /v1/uploads` creates an ephemeral upload for local files.

Details: <https://docs.dev.runwayml.com/_llms-txt/core-api.txt>

### Recipes

**Recipes** (7 endpoints) are prebuilt multi-step workflows that wrap several generations behind a
single call, so you do not have to orchestrate the steps yourself:
`/v1/recipes/product_ad`, `/v1/recipes/product_swap`, `/v1/recipes/product_ugc`,
`/v1/recipes/multi_shot_video`, `/v1/recipes/ad_localization`,
`/v1/recipes/marketing_stock_image`, `/v1/recipes/product_campaign_image`.

They return a task and follow the same contract as any other generation. In the SDKs, chain
`waitForTaskOutput()` / `wait_for_task_output()` on the recipe call. With HTTP, poll
`GET /v1/tasks/{id}`. Reference media has its own guidelines, at
<https://docs.dev.runwayml.com/recipes/reference-media.md>.

Details: <https://docs.dev.runwayml.com/_llms-txt/recipes.txt>

### Model Router

- **Model Router** (5 endpoints, `/v1/routers`) lets you save a routing configuration once and
  reference it by `configId` instead of naming a model. The router narrows to eligible models and
  picks one based on your optimization preference — cost, latency, or quality. You can set model
  allow and deny lists, per-modality credit ceilings, and preview a decision with `dryRun` before
  committing.
- **Generate** (1 endpoint) — `POST /v1/generate/video` runs a generation through a saved router.
  Send a `configId` and an `input` rather than a `model`. This is a separate group from Model Router,
  which only manages the configurations.

Use these when you would otherwise hardcode a model identifier that will age.

Details: <https://docs.dev.runwayml.com/_llms-txt/model-routers.txt>

### Characters

Real-time conversational characters. An **Avatar** is the reusable configuration — reference image,
voice, personality, knowledge — and a **Session** is one live conversation.

- **Avatars** (9 endpoints, `/v1/avatars` and `/v1/avatar_conversations`) — create and manage
  Avatars, list conversations, read usage.
- **Avatar Videos** (1 endpoint, `/v1/avatar_videos`) — render a video from an Avatar rather than
  holding a live Session.
- **Realtime Sessions** (3 endpoints, `/v1/realtime_sessions`) — open, inspect, and end a live
  conversation.
- **Knowledge** (5 endpoints, `/v1/documents`) — Documents you attach to an Avatar so it can answer
  from your own material.
- **Voices** (6 endpoints, `/v1/voices`) — designed and cloned custom voices, plus previews. Once `READY`, use a voice's ID with `/v1/text_to_speech` (`eleven_v4`, `eleven_v3`, or `eleven_multilingual_v2`) as `voice: {type: "custom", id: "…"}`, or assign it to an Avatar. The voice and request must belong to the same API project. See <https://docs.dev.runwayml.com/characters/custom-voice>.

Characters also support tool calling, so an Avatar can invoke your functions mid-conversation, on the
client or on your server. There is a React SDK at
<https://github.com/runwayml/avatar-sdk-react> and a framework-agnostic package,
`@runwayml/avatars`. Component props and current examples live in those READMEs rather than in the
docs site. An embedded widget is configured in the Developer Portal under the Embed tab and mounted
with a `data-pub-key` attribute.

Details: <https://docs.dev.runwayml.com/_llms-txt/characters.txt>

### Workflows

**Workflows** (4 endpoints) are node-graph pipelines you build in the Runway app and publish to your
Runway Dev project. Each publish is a version with its own ID, and a version keeps running the graph
it was published with.

- `GET /v1/workflows` lists published Workflows and their versions. `GET /v1/workflows/{id}` returns a
  version's graph; an input is exposed unless marked `exposedToApp: false`.
- `POST /v1/workflows/{id}` starts an invocation. Set inputs in `nodeOutputs`, keyed by node ID and
  then output key (`prompt` for text inputs; `image`, `video`, or `audio` for media inputs).
- Poll `GET /v1/workflow_invocations/{id}`, not `GET /v1/tasks/{id}`. In the SDKs,
  call `workflows.run()` for the ID, then `workflowInvocations.retrieve(id).waitForTaskOutput()` /
  `workflow_invocations.retrieve(id=…).wait_for_task_output()`. `run()` has no wait helper.

Inputs you leave out use the saved value; unknown node IDs or keys are ignored silently. A `400` on
run can mean a node uses a retired model: replace it in the Runway app and publish a new version. A
`404` can mean the API key belongs to a different project than the one the Workflow was published to.

A `SUCCEEDED` invocation can still contain failed or skipped nodes: check `nodeErrors` and that
`output` (node IDs to URL arrays, exposed outputs only) has every node you expect. Cancel a `RUNNING`
invocation with `DELETE /v1/tasks/{id}` using the invocation ID; started and queued nodes still run.

Details: <https://docs.dev.runwayml.com/_llms-txt/workflows.txt>

### Organization

- **Organization** (2 endpoints, `/v1/organization`) — credit balance, usage tier, and credit usage
  for the project that owns the API key. Enterprise organizations can also export per-generation usage and audit logs.

## Supplying input media

Three ways to pass an image, video, or audio file. All are described at
<https://docs.dev.runwayml.com/assets/inputs.md>.

1. **HTTPS URL** — simplest, and the best default when your media is already hosted. The URL must be
   publicly reachable.
2. **Data URI** — base64 inline. Convenient for small files, but it inflates the request body and
   counts against size limits, so avoid it for video.
3. **Ephemeral upload** — `POST /v1/uploads` with a `filename` and `type: "ephemeral"` returns a
   Runway URI you pass in place of a URL. Use this for local files you do not want to host.

Inputs are auto-cropped to the target aspect ratio when they do not match, which can silently change
your composition. Check the aspect ratio guidance before assuming a crop is safe.

## When things fail

- **Content moderation** surfaces as a task with `status: "FAILED"` — not as an HTTP error. Inspect
  `failure` and `failureCode`. Moderated generations cost the same as successful ones, and repeated
  moderated requests can suspend an account. Each call defaults to `auto` moderation; the optional
  `contentModeration.publicFigureThreshold` field can be set to `low` to be less strict about
  recognizable public figures. See <https://docs.dev.runwayml.com/api-details/moderation.md>.
- **HTTP errors** and their meanings: <https://docs.dev.runwayml.com/errors/errors.md>
- **Task failure codes**: <https://docs.dev.runwayml.com/errors/task-failures.md>
- **Rate limits** are per usage tier. A `THROTTLED` task is queued, not rejected. Tiers are at
  <https://docs.dev.runwayml.com/usage/tiers.md>.

## Pitfalls to avoid

- **Do not invent model identifiers.** Use only what is listed in
  <https://docs.dev.runwayml.com/guides/models.md> or `/api.md`. Retired identifiers fail outright:
  `gen3a_turbo` and `gen4_aleph` were removed and their requests now error. Replace `gen3a_turbo`
  with `gen4.5` or `gen4_turbo`, and `gen4_aleph` with `aleph2`.
- **Do not state or estimate credit costs.** Pricing lives only at
  <https://docs.dev.runwayml.com/guides/pricing.md> and changes independently of everything else.
- **Do not reuse a `ratio` or `duration` across models.** See the per-model section above.
- **Do not treat the create response as the result.** It only contains a task id.
- **Do not skip the `X-Runway-Version` header.** Requests without it fail.
- **Do not assume output URLs persist.** Download what you need.
- **Do not poll in a tight loop.** Use backoff, or the SDK helper.

## Where to go next

| Resource | Contents |
| --- | --- |
| <https://docs.dev.runwayml.com/api.md> | Every endpoint, with per-model request fields and allowed values |
| <https://docs.dev.runwayml.com/openapi.json> | Machine-readable OpenAPI 3.1 specification |
| <https://docs.dev.runwayml.com/llms.txt> | Index of all documentation bundles |
| <https://docs.dev.runwayml.com/llms-full.txt> | Complete documentation as one file |
| <https://docs.dev.runwayml.com/guides/using-the-api.md> | Worked examples in Node, Python, and HTTP |
| <https://docs.dev.runwayml.com/guides/models.md> | Current models and their capabilities |
| <https://docs.dev.runwayml.com/guides/professional-outputs.md> | HDR and pipeline formats from Gen-4.5 and Aleph 2.0, plus resolution, frame rate, and SDR-to-HDR conversion |
| <https://docs.dev.runwayml.com/guides/pricing.md> | Credit costs, the single source of truth |
| <https://docs.dev.runwayml.com/guides/go-live.md> | Checklist before shipping to production |
| <https://docs.dev.runwayml.com/changelog.md> | What changed and when |

Any documentation page can be read as Markdown by appending `.md` to its path.
