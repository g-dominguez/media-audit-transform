# Runway Dev docs (local copy)

Official Runway Dev documentation, downloaded **2026-11-22** from https://docs.dev.runwayml.com. These are Runway's own Markdown files, unedited. Runway changes model names and prices often, so check the live docs before relying on anything here for more than a few days.

## Read in this order

1. **[ai-context.md](ai-context.md)**: one-page primer. Authentication, how tasks work, every endpoint group, common mistakes. Read this first.
2. **[api/00-conventions.md](api/00-conventions.md)**: base URL, required `X-Runway-Version` header, task polling.
3. The **one endpoint file** your project uses, from `api/` below.
4. **[models.md](models.md)** for current model names, and **[pricing.md](pricing.md)** before spending credits.

Load only what the task needs. The full API reference is about 314 KB, which is why it's split up.

## Files

| File | What it covers | Source |
|---|---|---|
| [ai-context.md](ai-context.md) | Primer: auth, task lifecycle, capability map, pitfalls | `/ai-context.md` |
| [models.md](models.md) | Current model identifiers and what each does | `/guides/models.md` |
| [pricing.md](pricing.md) | Credit costs. The only official source for pricing | `/guides/pricing.md` |
| [professional-outputs.md](professional-outputs.md) | ProRes, HDR, SDR-to-HDR (Ruby), upscaling, frame rate | `/guides/professional-outputs.md` |
| [inputs.md](inputs.md) | Passing media: URL, data URI, or upload; size and duration limits | `/assets/inputs.md` |
| [task-failures.md](task-failures.md) | Task failure codes | `/errors/task-failures.md` |
| [go-live.md](go-live.md) | Checklist before shipping to production | `/guides/go-live.md` |
| [api/](api/) | The API reference (`/api.md`), split into one file per endpoint group | `/api.md` |
| [api/generate/](api/generate/) | One file per generation endpoint, e.g. `text_to_video.md`, `video_to_hdr.md` | `/api.md`, "Start generating" |

## API reference files

- `api/00-conventions.md`: conventions and the list of endpoint groups
- `api/task-management.md`: `GET` / `DELETE /v1/tasks/{id}`
- `api/uploads.md`: `POST /v1/uploads` for local files
- `api/generate/*.md`: one per endpoint (text_to_video, image_to_video, video_to_video, text_to_image, video_upscale, video_to_hdr, image_upscale, audio endpoints, and more)
- `api/recipes.md`, `api/workflows.md`, `api/model-router.md`
- `api/avatars.md`, `api/avatar-videos.md`, `api/realtime-sessions.md`, `api/knowledge.md`, `api/voices.md` (Characters)
- `api/organization.md`: credit balance and usage

## Refreshing

Any docs page is available as Markdown by adding `.md` to its URL. The index of everything is https://docs.dev.runwayml.com/llms.txt. To refresh the API split, download `/api.md` again and split it on `## ` headings (and `### ` headings inside "Start generating").
