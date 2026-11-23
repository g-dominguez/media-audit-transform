---
title: Handle Task Failures
description: Troubleshoot task failures on Runway Dev. Learn about common generation errors, retry strategies and how to handle failed AI video requests.
---

When a task fails, the [Get Task endpoint](/api/#tag/Task-management/paths/~1v1~1tasks~1%7Bid%7D/get)
endpoint returns a `failureCode` indicating the problem that occurred during processing.

# `SAFETY` failures

Failure codes that start with `SAFETY.` indicate that the task was rejected because of content
moderation. Content moderation is performed on both task inputs as well as outputs.

When a failure code is in the form `SAFETY.INPUT.*`, it indicates that one of the inputs
contained content that was deemed unsupportable. When in the form `SAFETY.OUTPUT.*`, it
indicates that content moderation rejected the output of the task.

The end of the failure code indicates the likely source of rejection. `SAFETY.INPUT.TEXT`,
for instance, indicates that prompt text was rejected. If multiple inputs would be rejected,
you will receive a failure for the first one that was tested.

While we make a best-effort attempt to ensure the accuracy of the third component of these
failure codes, they may not correspond exactly to inputs. You may, for instance, receive
a `SAFETY.INPUT.TEXT` failure on a task that provides no `promptText` argument. You should
treat these as diagnostic messages only rather than exposing them to users.

:::note
Unlike other failures, credits are not refunded for `SAFETY.INPUT.*` failures.
:::

You should not retry these generations.

# `INTERNAL.BAD_OUTPUT` failures

Failure codes in the form `INTERNAL.BAD_OUTPUT.*` represent generations that were rejected
by our internal systems for quality or system error reasons.

The most common failure of this category is `INTERNAL.BAD_OUTPUT.01`. Common causes for this error include:

* Logos, watermarks, or overlaid text in input media
* Prompt including explicit text generation requests
* Prompt requested that a media generation prompt be written rather than provided directly (e.g. "write a prompt for...")

You may retry these generations, they may succeed if corrections were made to prompts based on the above common errors.

# `INPUT_PREPROCESSING.SAFETY.TEXT`

This failure code indicates that input prompt text was rejected for content moderation reasons.

You should not retry these generations.

# `INPUT_PREPROCESSING.INTERNAL`

This failure code indicates that there was a problem performing content moderation.

You may retry these generations, but you should add a delay.

# `ASSET.INVALID`

One of the inputs that you provided (an image, video, etc.) is not acceptable for the type of task that you ran. This often indicates a problem with the dimensions, duration, or other properties of the media you provided.

You should not retry these errors, as they indicate a problem with your inputs.

# `THIRD_PARTY.UNAVAILABLE`

When invoking a generation with a model that's provided by a third party, it's possible for the third party to fail to provide an output due to unavailability (e.g., an outage, load shedding, etc.).

You should not retry these errors immediately as they are unlikely to succeed. You may wait and retry the generations.

# `INTERNAL` or a `null` value

`INTERNAL` or an undefined or null value indicates that there was an internal problem
processing the task.

You may retry these generations, but you should add a delay.
