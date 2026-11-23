# Runway Dev API reference

> Generated from the OpenAPI 3.1 specification that powers the interactive reference at https://docs.dev.runwayml.com/api. The machine-readable document is at https://docs.dev.runwayml.com/openapi.json.

## Conventions

- Base URL: `https://api.dev.runwayml.com`
- Authentication `ApiKeyAuth`: http, bearer
- Header `X-Runway-Version` (required): `2024-11-06`
- Generation endpoints are asynchronous. They return a task `id`; poll `GET /v1/tasks/{id}` until `status` is `SUCCEEDED` or `FAILED`.
- Where an endpoint lists several models below, the request body is a discriminated union on `model`. Only the fields listed under that model are valid.
- Credit costs are not in this file. See https://docs.dev.runwayml.com/guides/pricing.

## Endpoint groups

- **Avatars** (9 endpoints)
- **Avatar Videos** (1 endpoint)
- **Knowledge** (5 endpoints)
- **Realtime Sessions** (3 endpoints)
- **Task management** (2 endpoints)
- **Start generating** (16 endpoints)
- **Model Router** (9 endpoints)
- **Organization** (6 endpoints)
- **Uploads** (1 endpoint)
- **Recipes** (7 endpoints)
- **Voices** (6 endpoints)
- **Workflows** (4 endpoints)

