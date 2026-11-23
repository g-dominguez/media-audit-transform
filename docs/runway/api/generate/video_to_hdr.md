## Start generating

### POST /v1/video_to_hdr

Video to HDR

This endpoint starts a task to upconvert an SDR video to true HDR with Ruby, Runway's HDR grading model. The output keeps the source's own pixels - luma and color are extended into the HDR range, nothing is re-synthes...

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 1 shape, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/video_to_hdr - model `ruby`

- `videoUri` (string, required) - The SDR input video to upconvert. Must be 30 seconds or shorter.
- `outputFormat` (string) - one of `hdr10`, `hlg`, `hdr_prores`, `hdr_exr_sequence`, `hdr_exr_acescg_sequence_1_3`, `hdr_exr_acescg_sequence_2_0`. The HDR delivery profile of the output. `hdr10` (default) returns an HEVC Main 10, BT.2020 + PQ .mp4; `hlg` returns an HEVC Main 10, BT.2020 + HLG .mp4; `hdr_prores` returns a BT.2020 + PQ ProRes .mov editorial mezzan...
- `proresProfile` (string) - one of `422`, `4444`, `422 HQ`. The ProRes tier of the `hdr_prores` mezzanine. Only valid when `outputFormat` is `hdr_prores`. Defaults to `422 HQ`. A source with an alpha channel is always delivered as `4444`, the only tier with an alpha plane, wha...
- `model` (string, required) - one of `ruby`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

