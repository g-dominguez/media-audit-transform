## Start generating

### POST /v1/character_performance

Control a character

This endpoint will start a new task to control a character's facial expressions and body movements using a reference video.

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 1 shape, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/character_performance - model `act_two`

- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `character` (object, required) - The character to control. You can either provide a video or an image. A visually recognizable face must be visible and stay within the frame.
  - `type` (string, required) - one of `image`, `video`
  - `uri` (string, required)
- `reference` (object, required) - The reference video containing the performance to apply to the character.
  - `type` (string, required) - one of `video`
  - `uri` (string, required) - A video of a person performing in the manner that you would like your character to perform. The video must be between 3 and 30 seconds in duration. See [our docs](/assets/inputs#videos) on video inputs for more inform...
- `bodyControl` (boolean) - A boolean indicating whether to enable body control. When enabled, non-facial movements and gestures will be applied to the character in addition to facial expressions.
- `expressionIntensity` (integer) - 1-5; default `3`. An integer between 1 and 5 (inclusive). A larger value increases the intensity of the character's expression.
- `ratio` (string) - one of `1280:720`, `720:1280`, `960:960`, `1104:832`, `832:1104`, `1584:672`. The resolution of the output video.
- `contentModeration` (object) - Settings that affect the behavior of the content moderation system.
  - `publicFigureThreshold` (string) - one of `auto`, `low`. When set to `low`, the content moderation system will be less strict about preventing generations that include recognizable public figures.
- `model` (string, required) - one of `act_two`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

