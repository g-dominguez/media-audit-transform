## Start generating

### POST /v1/text_to_image

Text/Image to Image

This endpoint will start a new task to generate images from text and/or image(s)

Parameters:

- `X-Runway-Tags` (header, string) - max length 1024. Comma-separated tags to attribute this generation's credit usage to, so you can filter and break down usage with `POST /v1/organization/usage`. Each tag is a plain label (`campaign-q4`) or a `key:value` pair (`team:gr...

Request body: one of 28 shapes, selected by `model`. Only the fields listed under a given `model` are valid.

#### POST /v1/text_to_image - model `gen4_image_turbo`

- `promptText` (string, required) - max length 1000. A non-empty string up to 1000 characters (measured in UTF-16 code units). This should describe in detail what should appear in the output.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `ratio` (string, required) - one of `1024:1024`, `1080:1080`, `1168:880`, `1360:768`, `1440:1080`, `1080:1440`, `1808:768`, `1920:1080`, `1080:1920`, `2112:912`, `1280:720`, `720:1280`, `720:720`, `960:720`, `720:960`, `1680:720`. The resolution of the output image.
- `referenceImages` (array of object, required) - min 1 items; max 3 items. An array of one to three images to be used as references for the generated image output.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. A tag to identify the reference image. This is used to reference the image in prompt text. Must be 3-16 characters, start with a letter, and use only letters, digits, and underscores (no hyphens or other punctuation).
- `contentModeration` (object) - Settings that affect the behavior of the content moderation system.
  - `publicFigureThreshold` (string) - one of `auto`, `low`. When set to `low`, the content moderation system will be less strict about preventing generations that include recognizable public figures.
- `model` (string, required) - one of `gen4_image_turbo`

#### POST /v1/text_to_image - model `gen4_image`

- `promptText` (string, required) - max length 1000. A non-empty string up to 1000 characters (measured in UTF-16 code units). This should describe in detail what should appear in the output.
- `seed` (integer) - 0-4294967295. If unspecified, a random number is chosen. Varying the seed integer is a way to get different results for the same other request parameters. Using the same seed integer for an identical request will produce similar re...
- `ratio` (string, required) - one of `1024:1024`, `1080:1080`, `1168:880`, `1360:768`, `1440:1080`, `1080:1440`, `1808:768`, `1920:1080`, `1080:1920`, `2112:912`, `1280:720`, `720:1280`, `720:720`, `960:720`, `720:960`, `1680:720`. The resolution of the output image.
- `referenceImages` (array of object) - max 3 items. An array of up to three images to be used as references for the generated image output.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. A tag to identify the reference image. This is used to reference the image in prompt text. Must be 3-16 characters, start with a letter, and use only letters, digits, and underscores (no hyphens or other punctuation).
- `contentModeration` (object) - Settings that affect the behavior of the content moderation system.
  - `publicFigureThreshold` (string) - one of `auto`, `low`. When set to `low`, the content moderation system will be less strict about preventing generations that include recognizable public figures.
- `model` (string, required) - one of `gen4_image`

#### POST /v1/text_to_image - model `gpt_image_2`

- `promptText` (string, required) - max length 32000. A non-empty string up to 32,000 characters describing the desired image.
- `ratio` (string, required) - one of `2048:880`, `1920:1088`, `1920:1280`, `1920:1440`, `1920:1536`, `1920:1920`, `1536:1920`, `1440:1920`, `1280:1920`, `1088:1920`, `2912:1248`, `2560:1440`, `2560:1712`, `2560:1920`, `2560:2048`, `2560:2560`, `2048:2560`, `1920:2560`, `1712:2560`, `1440:2560`, `3840:1648`, `3840:2160`, `3504:2336`, `3264:2448`, `3200:2560`, `2880:2880`, `2560:3200`, `2448:3264`, `2336:3504`, `2160:3840`, `auto`. The resolution of the output image, expressed as `<width>:<height>`. Use `auto` to let the model choose.
- `quality` (string) - one of `low`, `medium`, `high`, `auto`. Rendering quality. Higher qualities consume more credits. Defaults to `high`.
- `background` (string) - one of `transparent`, `opaque`, `auto`. Background treatment. Defaults to `auto`, which lets the model pick. Use `transparent` to generate a PNG with an alpha-channel background.
- `referenceImages` (array of object) - max 16 items. An array of up to 16 images to be used as references for the generated image output. No two images may share the same tag.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. An optional label for the reference image. Tags are not sent to the model and cannot be used to reference images in prompt text. Instead, refer to images by their order in this array (for example, "the first image" or...
- `outputCount` (integer) - 1-10. The number of images to generate (1-10). Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `gpt_image_2`

#### POST /v1/text_to_image - model `gemini_image3.1_flash`

- `promptText` (string, required) - max length 45000. This should describe in detail what should appear in the output.
- `ratio` (string, required) - one of `512:512`, `416:624`, `624:416`, `432:592`, `592:432`, `448:576`, `576:448`, `384:672`, `672:384`, `768:336`, `256:1024`, `1024:256`, `176:1408`, `1408:176`, `1024:1024`, `832:1248`, `1248:832`, `864:1184`, `1184:864`, `896:1152`, `1152:896`, `768:1344`, `1344:768`, `1536:672`, `512:2048`, `2048:512`, `352:2816`, `2816:352`, `2048:2048`, `1696:2528`, `2528:1696`, `1792:2400`, `2400:1792`, `1856:2304`, `2304:1856`, `1536:2752`, `2752:1536`, `3168:1344`, `1024:4096`, `4096:1024`, ... (56 total). The resolution of the output image.
- `referenceImages` (array of object) - max 14 items. An array of up to 14 images to be used as references for the generated image output. Up to five of those images can pass `subject: "human"` to maintain character consistency, and up to nine of those images can pass `s...
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. A tag to identify the reference image. This is used to reference the image in prompt text. Must be 3-16 characters, start with a letter, and use only letters, digits, and underscores (no hyphens or other punctuation).
  - `subject` (string) - one of `object`, `human`; default `object`. Whether this is a reference of a human subject (for character consistency) or an object that appears in the output.
- `outputCount` (number) - one of `1`, `4`. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation. Up to four images can be generated at once.
- `model` (string, required) - one of `gemini_image3.1_flash`

#### POST /v1/text_to_image - model `muse_image`

- `promptText` (string, required) - max length 4000. A non-empty text prompt describing what should appear in the output image.
- `ratio` (string, required) - one of `2352:1008`, `2016:1152`, `1920:1280`, `1792:1344`, `1600:1600`, `1344:1792`, `1280:1920`, `1152:2016`, `auto`. The resolution of the output image, expressed as `<width>:<height>`. Use `auto` to let the model choose the framing from the prompt.
- `outputFormat` (string) - one of `webp`, `png`, `jpeg`. The file format of the output image. Defaults to png.
- `referenceImages` (array of object) - max 10 items. Up to 10 images to guide the generation. When provided, the model edits and combines them as your prompt describes instead of generating from the prompt alone.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `outputCount` (integer) - 1-10. The number of images to generate. Each image costs 1 credit.
- `model` (string, required) - one of `muse_image`

#### POST /v1/text_to_image - model `seedream5_pro`

- `promptText` (string, required) - max length 4000. A non-empty string up to 4,000 characters describing the desired image.
- `ratio` (string, required) - one of `1024:1024`, `1184:896`, `896:1184`, `1376:768`, `768:1376`, `1296:864`, `864:1296`, `2048:2048`, `2304:1728`, `1728:2304`, `2720:1530`, `1530:2720`, `2496:1664`, `1664:2496`, `auto_1k`, `auto_2k`. The resolution of the output image, expressed as `<width>:<height>`. Use `auto_1k` or `auto_2k` to let the model pick aspect ratio at a fixed resolution tier.
- `outputFormat` (string) - one of `png`, `jpeg`. The file format of the output image. Defaults to png.
- `referenceImages` (array of object) - max 10 items. An array of reference images for multi-image fusion and interactive editing. Reference by upload order in prompt text (Figure 1, Figure 2, etc.).
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `outputCount` (integer) - 1-4. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation.
- `grounding` (boolean) - When true, enable live web search so the model can use current brand, trend, or event context. Default false for deterministic output.
- `model` (string, required) - one of `seedream5_pro`

#### POST /v1/text_to_image - model `seedream5_lite`

- `promptText` (string, required) - max length 4000. A non-empty string up to 4,000 characters describing the desired image.
- `ratio` (string, required) - The resolution of the output image, expressed as `<width>:<height>`. Also accepts freeform sizes whose width*height is between 3686400 and 16777216 pixels.
- `outputFormat` (string) - one of `png`, `jpeg`. The file format of the output image. Defaults to png.
- `referenceImages` (array of object) - max 14 items. An array of reference images for multi-image fusion and interactive editing. Reference by upload order in prompt text (Figure 1, Figure 2, etc.).
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `outputCount` (integer) - 1-4. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation.
- `grounding` (boolean) - When true, enable live web search so the model can use current brand, trend, or event context. Default false for deterministic output.
- `model` (string, required) - one of `seedream5_lite`

#### POST /v1/text_to_image - model `grok_imagine_image_2`

- `promptText` (string, required) - max length 2500. A non-empty text prompt describing what should appear in the output image.
- `ratio` (string, required) - one of `1024:1024`, `1280:720`, `720:1280`, `1152:864`, `864:1152`, `1248:832`, `832:1248`, `1248:576`, `576:1248`, `1280:576`, `576:1280`, `1408:704`, `704:1408`, `2048:2048`, `2816:1584`, `1584:2816`, `2368:1776`, `1776:2368`, `2496:1664`, `1664:2496`, `2912:1344`, `1344:2912`, `3200:1440`, `1440:3200`, `2912:1456`, `1456:2912`, `auto_1k`, `auto_2k`. The resolution of the output image, expressed as `<width>:<height>`. 2K ratios cost 2 additional credits per image. Use `auto_1k` or `auto_2k` to pick a resolution tier and let the model choose the framing from the pr...
- `quality` (string) - one of `low`, `medium`. How much rendering effort the model spends on the output. Defaults to `medium`; `low` is faster and costs 2 fewer credits per image.
- `edit` (boolean) - When true with exactly one reference image, edit that image directly instead of using it as a loose visual reference. With several reference images the prompt describes how they should be edited or combined. Requires...
- `referenceImages` (array of object) - max 3 items. Up to 3 images to guide the generation. Reference them from `promptText` to describe how each should be used. Each adds 1 credit to the generation.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `outputCount` (integer) - 1-4. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `grok_imagine_image_2`

#### POST /v1/text_to_image - model `gemini_image3.1_flash_lite`

- `promptText` (string, required) - max length 45000. This should describe in detail what should appear in the output.
- `ratio` (string, required) - one of `1024:1024`, `848:1264`, `1264:848`, `896:1200`, `1200:896`, `928:1152`, `1152:928`, `768:1376`, `1376:768`, `1584:672`. The resolution of the output image.
- `referenceImages` (array of object) - max 14 items. An array of up to 14 images to be used as references for the generated image output. Up to five can pass `subject: "human"` and up to nine can pass `subject: "object"`.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16
  - `subject` (string) - one of `object`, `human`; default `object`
- `outputCount` (number) - one of `1`, `4`. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation. Up to four images can be generated at once.
- `model` (string, required) - one of `gemini_image3.1_flash_lite`

#### POST /v1/text_to_image - model `gemini_image3_pro`

- `promptText` (string, required) - max length 45000. This should describe in detail what should appear in the output.
- `ratio` (string, required) - one of `1344:768`, `768:1344`, `1024:1024`, `1184:864`, `864:1184`, `1536:672`, `832:1248`, `1248:832`, `896:1152`, `1152:896`, `2048:2048`, `1696:2528`, `2528:1696`, `1792:2400`, `2400:1792`, `1856:2304`, `2304:1856`, `1536:2752`, `2752:1536`, `3168:1344`, `4096:4096`, `3392:5056`, `5056:3392`, `3584:4800`, `4800:3584`, `3712:4608`, `4608:3712`, `3072:5504`, `5504:3072`, `6336:2688`. The resolution of the output image.
- `referenceImages` (array of object) - max 14 items. An array of up to 14 images to be used as references for the generated image output. Up to five of those images can pass `subject: "human"` to maintain character consistency, and up to nine of those images can pass `s...
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. A tag to identify the reference image. This is used to reference the image in prompt text. Must be 3-16 characters, start with a letter, and use only letters, digits, and underscores (no hyphens or other punctuation).
  - `subject` (string) - one of `object`, `human`; default `object`. Whether this is a reference of a human subject (for character consistency) or an object that appears in the output.
- `outputCount` (number) - one of `1`, `4`. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation. Up to four images can be generated at once.
- `model` (string, required) - one of `gemini_image3_pro`

#### POST /v1/text_to_image - model `gpt_image_2_5_flare`

- `promptText` (string, required) - max length 32000. A non-empty string describing the desired image.
- `ratio` (string, required) - one of `2048:880`, `1920:1088`, `1920:1280`, `1920:1440`, `1920:1536`, `1920:1920`, `1536:1920`, `1440:1920`, `1280:1920`, `1088:1920`, `2912:1248`, `2560:1440`, `2560:1712`, `2560:1920`, `2560:2048`, `2560:2560`, `2048:2560`, `1920:2560`, `1712:2560`, `1440:2560`, `3840:1648`, `3840:2160`, `3504:2336`, `3264:2448`, `3200:2560`, `2880:2880`, `2560:3200`, `2448:3264`, `2336:3504`, `2160:3840`, `auto`. The resolution of the output image, expressed as `<width>:<height>`. Use `auto` to let the model choose.
- `quality` (string) - one of `low`, `medium`, `high`, `xhigh`, `max`. Rendering quality. Higher qualities consume more credits. Defaults to `high`.
- `background` (string) - one of `opaque`, `auto`. Background treatment. Defaults to `auto`, which lets the model pick.
- `referenceImages` (array of object) - max 16 items. An array of up to 16 images to be used as references for the generated image output. No two images may share the same tag. Each reference image adds 1 credit per generated image.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. An optional label for the reference image. Tags are not sent to the model and cannot be used to reference images in prompt text. Instead, refer to images by their order in this array (for example, "the first image" or...
- `outputCount` (integer) - 1-10. The number of images to generate (1-10). Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `gpt_image_2_5_flare`

#### POST /v1/text_to_image - model `gpt_image_2_5_sunburst`

- `promptText` (string, required) - max length 32000. A non-empty string describing the desired image.
- `ratio` (string, required) - one of `2048:880`, `1920:1088`, `1920:1280`, `1920:1440`, `1920:1536`, `1920:1920`, `1536:1920`, `1440:1920`, `1280:1920`, `1088:1920`, `2912:1248`, `2560:1440`, `2560:1712`, `2560:1920`, `2560:2048`, `2560:2560`, `2048:2560`, `1920:2560`, `1712:2560`, `1440:2560`, `3840:1648`, `3840:2160`, `3504:2336`, `3264:2448`, `3200:2560`, `2880:2880`, `2560:3200`, `2448:3264`, `2336:3504`, `2160:3840`, `auto`. The resolution of the output image, expressed as `<width>:<height>`. Use `auto` to let the model choose.
- `quality` (string) - one of `low`, `medium`, `high`, `xhigh`, `max`. Rendering quality. Higher qualities consume more credits. Defaults to `high`.
- `background` (string) - one of `transparent`, `opaque`, `auto`. Background treatment. Defaults to `auto`, which lets the model pick. Use `transparent` to generate a PNG with an alpha-channel background.
- `referenceImages` (array of object) - max 16 items. An array of up to 16 images to be used as references for the generated image output. No two images may share the same tag. Each reference image adds 1 credit per generated image.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. An optional label for the reference image. Tags are not sent to the model and cannot be used to reference images in prompt text. Instead, refer to images by their order in this array (for example, "the first image" or...
- `outputCount` (integer) - 1-10. The number of images to generate (1-10). Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `gpt_image_2_5_sunburst`

#### POST /v1/text_to_image - model `bria_fibo_1_5`

- `promptText` (string, required) - max length 10000. A non-empty text prompt describing what should appear in the output image.
- `ratio` (string, required) - one of `1024:1024`, `768:1152`, `1152:768`, `768:1024`, `1024:768`, `768:960`, `960:768`, `576:1024`, `1024:576`, `2048:2048`, `1536:2304`, `2304:1536`, `1536:2048`, `2048:1536`, `1536:1920`, `1920:1536`, `1152:2048`, `2048:1152`. The resolution of the output image, expressed as `<width>:<height>`. 1MP sizes cost 5 credits per image and 4MP sizes 10.
- `seed` (integer) - 0-2147483647. If unspecified, a random number is chosen. Using the same seed with an identical request reproduces the same image.
- `outputFormat` (string) - one of `png`, `jpeg`. The file format of the output image. Defaults to png.
- `referenceImages` (array of object) - max 1 items. Up to 1 image to guide the generation. The prompt describes how the output should build on it.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `model` (string, required) - one of `bria_fibo_1_5`

#### POST /v1/text_to_image - model `bria_fibo_edit_1_5`

- `promptText` (string, required) - max length 10000. An instruction describing how to edit the reference images.
- `seed` (integer) - 0-2147483647. If unspecified, a random number is chosen. Using the same seed with an identical request reproduces the same image.
- `outputFormat` (string) - one of `png`, `jpeg`. The file format of the output image. Defaults to png.
- `referenceImages` (array of object) - max 4 items. 1 to 4 images to edit. With several, the instruction describes how to combine them.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `ratio` (string) - one of `1024:1024`, `768:1152`, `1152:768`, `768:1024`, `1024:768`, `768:960`, `960:768`, `576:1024`, `1024:576`, `auto`. The resolution of the output image, expressed as `<width>:<height>`. Omit it or use `auto` to keep the framing of the first reference image. Choosing a size requires at least 2 reference images; a single image always...
- `model` (string, required) - one of `bria_fibo_edit_1_5`

#### POST /v1/text_to_image - model `ideogram_4_0`

- `promptText` (string, required) - max length 4000. Describe the image to generate, or how to remix the reference image.
- `quality` (string) - one of `low`, `medium`, `high`. How much rendering effort the model spends on each image. `low` costs 4 credits per image, `medium` 7 and `high` 11.
- `ratio` (string) - one of `2048:2048`, `2560:1440`, `1440:2560`, `2304:1728`, `1728:2304`, `2496:1664`, `1664:2496`, `3072:1280`, `1280:3072`. The resolution of the output image, expressed as `<width>:<height>`.
- `referenceImages` (array of object) - max 1 items. An image to remix. The prompt describes how the output should differ from it.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `outputCount` (integer) - 1-4. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `ideogram_4_0`

#### POST /v1/text_to_image - model `ideogram_4_5`

- `promptText` (string, required) - max length 10000. Describe the image to generate, or the changes to make to the reference images.
- `quality` (string) - one of `very_low`, `low`, `medium`, `high`. How much rendering effort the model spends on each image. Defaults to `medium` (8 credits per image) when generating from reference images and `high` (25 credits) otherwise, including `preciseEdit`. `low` costs 4 cred...
- `ratio` (string) - one of `1024:1024`, `1280:720`, `720:1280`, `1152:864`, `864:1152`, `1248:832`, `832:1248`, `1120:896`, `896:1120`, `1440:720`, `720:1440`, `2048:2048`, `2560:1440`, `1440:2560`, `2304:1728`, `1728:2304`, `2496:1664`, `1664:2496`, `2240:1792`, `1792:2240`, `2880:1440`, `1440:2880`, `1024:576`, `576:1024`, `1408:704`, `704:1408`, `auto`. The resolution of the output image, expressed as `<width>:<height>`. Omit it or use `auto` to let the model choose. With reference images, widescreen 1K sizes are `1024:576`, `576:1024`, `1408:704`, `704:1408` instead...
- `referenceImages` (array of object) - max 5 items. Up to 5 images to guide the generation. With `maskUri` or `preciseEdit`, the first image is the one being edited and the rest are references.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `preciseEdit` (boolean) - When true, edit the first reference image. Requires at least one reference image. Whole-image edits above 4,194,304 pixels are scaled down. Set contextWindow to edit a region at full source resolution; auto-fit may st...
- `contextWindow` (string) - Precise-edit region: none, auto (requires maskUri), or top,left,bottom,right in original-image pixels, with exclusive maximum edges. A manual region preserves full resolution and all pixels outside it. All masked edit...
- `maskUri` (string) - A black-and-white mask the same size as the first reference image. Black areas are edited and white areas are preserved. Supports up to 3 additional reference images.
- `outputCount` (integer) - 1-8. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `ideogram_4_5`

#### POST /v1/text_to_image - model `seedream5_flash`

- `promptText` (string, required) - max length 4000. A description of the image you want to generate.
- `ratio` (string, required) - one of `1024:1024`, `1184:896`, `896:1184`, `1376:768`, `768:1376`, `1248:832`, `832:1248`, `1568:672`, `2048:2048`, `2304:1728`, `1728:2304`, `2848:1600`, `1600:2848`, `2496:1664`, `1664:2496`, `3136:1344`, `auto_1k`, `auto_2k`. The resolution of the output image, expressed as `<width>:<height>`. Use `auto_1k` or `auto_2k` to let the model pick the aspect ratio at a fixed resolution tier.
- `outputFormat` (string) - one of `png`, `jpeg`. The file format of the output image. Defaults to png.
- `referenceImages` (array of object) - max 10 items. Images to edit or combine. Refer to them in the prompt by upload order (Figure 1, Figure 2, and so on).
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `outputCount` (integer) - 1-4. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `seedream5_flash`

#### POST /v1/text_to_image - model `nano_banana_2.1`

- `promptText` (string, required) - max length 45000. A description of the image you want to generate.
- `ratio` (string, required) - one of `1024:1024`, `848:1264`, `1264:848`, `896:1200`, `1200:896`, `928:1152`, `1152:928`, `768:1376`, `1376:768`, `1584:672`, `512:2064`, `2064:512`, `352:2928`, `2928:352`, `2048:2048`, `1696:2528`, `2528:1696`, `1792:2400`, `2400:1792`, `1856:2304`, `2304:1856`, `1536:2752`, `2752:1536`, `3168:1344`, `1024:4128`, `4128:1024`, `704:5856`, `5856:704`, `4096:4096`, `3392:5056`, `5056:3392`, `3584:4800`, `4800:3584`, `3712:4608`, `4608:3712`, `3072:5504`, `5504:3072`, `6336:2688`, `2048:8256`, `8256:2048`, ... (42 total). The resolution of the output image.
- `thinkingLevel` (string) - one of `minimal`, `medium`, `high`. How much the model reasons about the prompt before generating. Defaults to medium.
- `referenceImages` (array of object) - max 14 items. Up to 14 images to edit, combine, or use as references for the output.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. A tag to identify the reference image. This is used to reference the image in prompt text. Must be 3-16 characters, start with a letter, and use only letters, digits, and underscores.
- `outputCount` (integer) - 1-4. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `nano_banana_2.1`

#### POST /v1/text_to_image - model `recraft_v4_1_flash`

- `promptText` (string, required) - max length 10000. A description of the image you want to generate.
- `ratio` (string, required) - one of `1024:1024`, `1536:768`, `768:1536`, `1280:832`, `832:1280`, `1216:896`, `896:1216`, `1152:896`, `896:1152`, `832:1344`, `1280:896`, `896:1280`, `1344:768`, `768:1344`. The output dimensions, expressed as `<width>:<height>`.
- `seed` (integer) - 0-4294967295
- `outputFormat` (string) - one of `webp`, `png`. The output file format. Defaults to webp.
- `colors` (array of string) - max 10 items. Preferred colors as six-digit hex strings.
- `backgroundColor` (string) - A preferred background color as a six-digit hex string.
- `outputCount` (integer) - 1-6. The number of images to generate. Each image is billed separately.
- `model` (string, required) - one of `recraft_v4_1_flash`

#### POST /v1/text_to_image - model `recraft_v4_1_vector`

- `promptText` (string, required) - max length 10000. Describe the vector illustration you want to generate.
- `colors` (array of string) - max 10 items; default `[]`. Preferred colors as six-digit hex values, such as #FF8800.
- `backgroundColor` (string) - The preferred background color as a six-digit hex value. This is a generation hint, not an exact color constraint; the generated background may use a different shade.
- `ratio` (string) - one of `1024:1024`, `1216:896`, `896:1216`, `1344:768`, `768:1344`. The width and height declared by the output SVG. Vector artwork can be scaled after generation.
- `model` (string, required) - one of `recraft_v4_1_vector`

#### POST /v1/text_to_image - model `ideogram_vector`

- `promptText` (string, required) - max length 9500. Describe the vector illustration you want to generate.
- `quality` (string) - one of `low`, `medium`, `high`. Rendering quality. Higher quality costs more credits.
- `seed` (integer) - 0-2147483647
- `ratio` (string) - one of `auto`. Let the model choose the framing of the SVG.
- `referenceImages` (array of object) - max 5 items. Images to guide the illustration. To trace a source image, use image_to_vector instead.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `model` (string, required) - one of `ideogram_vector`

#### POST /v1/text_to_image - model `gpt_image_2_6_sunburst`

- `outputFormat` (string) - one of `png`, `jpeg`, `webp`, `gif`, `svg`; default `png`. Output format. Defaults to PNG. JPEG and WebP produce smaller files; JPEG cannot have a transparent background. GIF and SVG cannot use reference images; GIF requires ratio auto.
- `frameCount` (integer) - 2-16. Number of animation frames. Only supported for GIF output.
- `frameDurationMs` (integer) - 20-2000. Duration of each animation frame in milliseconds. Only supported for GIF output.
- `promptText` (string, required) - max length 32000. A non-empty string describing the desired image.
- `ratio` (string, required) - one of `2048:880`, `1920:1088`, `1920:1280`, `1920:1440`, `1920:1536`, `1920:1920`, `1536:1920`, `1440:1920`, `1280:1920`, `1088:1920`, `2912:1248`, `2560:1440`, `2560:1712`, `2560:1920`, `2560:2048`, `2560:2560`, `2048:2560`, `1920:2560`, `1712:2560`, `1440:2560`, `3840:1648`, `3840:2160`, `3504:2336`, `3264:2448`, `3200:2560`, `2880:2880`, `2560:3200`, `2448:3264`, `2336:3504`, `2160:3840`, `auto`. The resolution of the output image, expressed as `<width>:<height>`. Use `auto` to let the model choose.
- `quality` (string) - one of `low`, `medium`, `high`. Rendering quality. Higher qualities consume more credits. Defaults to `high`.
- `reasoningEffort` (string) - one of `low`, `medium`, `high`. How much reasoning to use before rendering. Defaults to `high`.
- `background` (string) - one of `transparent`, `opaque`, `auto`. Background treatment. Defaults to `auto`, which lets the model pick. Use `transparent` for an alpha-channel background, which `jpeg` output does not support.
- `referenceImages` (array of object) - max 16 items. An array of up to 16 images to be used as references for the generated image output. No two images may share the same tag. Each reference image adds 1 credit per generated image.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. An optional label for the reference image. Tags are not sent to the model and cannot be used to reference images in prompt text. Instead, refer to images by their order in this array (for example, "the first image" or...
- `outputCount` (integer) - 1-10. The number of images to generate (1-10). Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `gpt_image_2_6_sunburst`

#### POST /v1/text_to_image - model `gpt_image_2_6_flare`

- `outputFormat` (string) - one of `png`, `jpeg`, `webp`, `gif`, `svg`; default `png`. Output format. Defaults to PNG. JPEG and WebP produce smaller files; JPEG cannot have a transparent background. GIF and SVG cannot use reference images; GIF requires ratio auto.
- `frameCount` (integer) - 2-16. Number of animation frames. Only supported for GIF output.
- `frameDurationMs` (integer) - 20-2000. Duration of each animation frame in milliseconds. Only supported for GIF output.
- `promptText` (string, required) - max length 32000. A non-empty string describing the desired image.
- `ratio` (string, required) - one of `2048:880`, `1920:1088`, `1920:1280`, `1920:1440`, `1920:1536`, `1920:1920`, `1536:1920`, `1440:1920`, `1280:1920`, `1088:1920`, `2912:1248`, `2560:1440`, `2560:1712`, `2560:1920`, `2560:2048`, `2560:2560`, `2048:2560`, `1920:2560`, `1712:2560`, `1440:2560`, `3840:1648`, `3840:2160`, `3504:2336`, `3264:2448`, `3200:2560`, `2880:2880`, `2560:3200`, `2448:3264`, `2336:3504`, `2160:3840`, `auto`. The resolution of the output image, expressed as `<width>:<height>`. Use `auto` to let the model choose.
- `quality` (string) - one of `low`, `medium`, `high`. Rendering quality. Higher qualities consume more credits. Defaults to `high`.
- `reasoningEffort` (string) - one of `low`, `medium`, `high`. How much reasoning to use before rendering. Defaults to `high`.
- `background` (string) - one of `transparent`, `opaque`, `auto`. Background treatment. Defaults to `auto`, which lets the model pick. Use `transparent` for an alpha-channel background, which `jpeg` output does not support.
- `referenceImages` (array of object) - max 16 items. An array of up to 16 images to be used as references for the generated image output. No two images may share the same tag. Each reference image adds 1 credit per generated image.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. An optional label for the reference image. Tags are not sent to the model and cannot be used to reference images in prompt text. Instead, refer to images by their order in this array (for example, "the first image" or...
- `outputCount` (integer) - 1-10. The number of images to generate (1-10). Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `gpt_image_2_6_flare`

#### POST /v1/text_to_image - model `seedream5_pro_layers`

- `referenceImages` (array of object, required) - min 1 items; max 1 items. The image to split into editable layers. Layer ordering and positioning are returned in the completed task’s layers field.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `resolution` (string) - one of `auto`, `1k`, `1.5k`, `2k`. Output resolution tier. Defaults to auto, which adapts to the input image. The base image and layers preserve their respective aspect ratios.
- `outputFormat` (string) - one of `png`, `jpeg`. Base image format; defaults to png. Separated layers always use PNG with transparency.
- `optimizePromptMode` (string) - one of `standard`, `fast`. Prompt optimization: standard prioritizes quality; fast reduces generation time. Defaults to standard.
- `promptText` (string) - max length 4000. Optional instructions describing which elements to separate. Omit to split the image automatically.
- `model` (string, required) - one of `seedream5_pro_layers`

#### POST /v1/text_to_image - model `seedream5.5`

- `promptText` (string, required) - max length 4000. A description of the image you want to generate.
- `ratio` (string, required) - one of `1024:1024`, `1152:864`, `864:1152`, `1424:800`, `800:1424`, `1248:832`, `832:1248`, `1568:672`, `1536:1536`, `1792:1344`, `1344:1792`, `2048:1152`, `1152:2048`, `1872:1248`, `1248:1872`, `2352:1008`, `2048:2048`, `2368:1776`, `1776:2368`, `2816:1584`, `1584:2816`, `2496:1664`, `1664:2496`, `3136:1344`, `auto_1k`, `auto_1.5k`, `auto_2k`. The resolution of the output image, expressed as `<width>:<height>`. Use `auto_1k`, `auto_1.5k` or `auto_2k` to let the model pick the aspect ratio at a fixed resolution tier.
- `outputFormat` (string) - one of `png`, `jpeg`. The file format of the output image. Defaults to png.
- `background` (string) - one of `transparent`, `opaque`. Whether the image has a transparent or an opaque background. A transparent background needs the png output format. Omit to let the model decide from the prompt.
- `referenceImages` (array of object) - min 0 items; max 10 items. Images to edit or combine. Refer to them in the prompt by upload order (Figure 1, Figure 2, and so on).
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `outputCount` (integer) - 1-4. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `seedream5.5`

#### POST /v1/text_to_image - model `seedream5.5_layers`

- `referenceImages` (array of object, required) - min 1 items; max 1 items. The image to split into editable layers. Layer ordering and positioning are returned in the completed task’s layers field.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `resolution` (string) - one of `auto`, `1k`, `1.5k`, `2k`. Output resolution tier. Defaults to auto, which adapts to the input image. The base image and layers preserve their respective aspect ratios.
- `outputFormat` (string) - one of `png`, `jpeg`. Base image format; defaults to png. Separated layers always use PNG with transparency.
- `maxImages` (integer) - 2-100. The most images the task may return, counting the base image. Each returned image is billed separately. Defaults to 30.
- `promptText` (string) - max length 4000. Optional instructions describing which elements to separate. Omit to split the image automatically.
- `model` (string, required) - one of `seedream5.5_layers`

#### POST /v1/text_to_image - model `minimax_h3_image`

- `promptText` (string, required) - max length 32000. A non-empty text prompt describing what should appear in the output image.
- `ratio` (string, required) - one of `1024:1024`, `1152:928`, `928:1152`, `1184:896`, `896:1184`, `1248:832`, `832:1248`, `1376:768`, `768:1376`, `1440:736`, `736:1440`, `1568:672`, `672:1568`, `1760:576`, `576:1760`, `2048:2048`, `2304:1824`, `1824:2304`, `2368:1760`, `1760:2368`, `2496:1664`, `1664:2496`, `2720:1536`, `1536:2720`, `2912:1440`, `1440:2912`, `3136:1344`, `1344:3136`, `3552:1184`, `1184:3552`, `4096:4096`, `4576:3648`, `3648:4576`, `4736:3552`, `3552:4736`, `5024:3360`, `3360:5024`, `5472:3072`, `3072:5472`, `5792:2912`, ... (48 total). The resolution of the output image, expressed as `<width>:<height>`. 4K ratios cost more credits per image than 1K and 2K. Use `auto_1k`, `auto_2k` or `auto_4k` to pick a resolution tier and let the model choose the f...
- `highspeed` (boolean) - When true, generate with the faster MiniMax H3 Image Highspeed model, which costs more credits per image. Defaults to false.
- `referenceImages` (array of object) - min 0 items; max 16 items. Up to 16 images to edit or combine. Refer to them in the prompt by upload order (image 1, image 2, and so on). Each reference image adds to the credits per image.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
- `outputCount` (integer) - 1-10. The number of images to generate. Increasing this number will affect the number of credits consumed by the generation.
- `model` (string, required) - one of `minimax_h3_image`

#### POST /v1/text_to_image - model `gemini_2.5_flash`

- `promptText` (string, required) - max length 45000. This should describe in detail what should appear in the output.
- `ratio` (string, required) - one of `1344:768`, `768:1344`, `1024:1024`, `1184:864`, `864:1184`, `1536:672`, `832:1248`, `1248:832`, `896:1152`, `1152:896`. The resolution of the output image.
- `referenceImages` (array of object) - max 3 items. An array of up to three images to be used as references for the generated image output.
  - `uri` (string, required) - A HTTPS URL, Runway or data URI containing an encoded image. See [our docs](/assets/inputs#images) on image inputs for more information.
  - `tag` (string) - max length 16. A tag to identify the reference image. This is used to reference the image in prompt text. Must be 3-16 characters, start with a letter, and use only letters, digits, and underscores (no hyphens or other punctuation).
- `model` (string, required) - one of `gemini_2.5_flash`

Response 200:

- `id` (string, required) - format uuid. The ID of the task that was created. Use this to retrieve the task later.
- `estimatedCost` (object, required) - The maximum credits this task may charge. The final amount may be lower after the task completes.
  - `credits` (number, required) - Estimated cost of the generation in credits.

Other responses: `400`, `429`

