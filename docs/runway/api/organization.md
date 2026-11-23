## Organization

### GET /v1/organization/webapp/usage

List linked workspace usage

List per-generation credit-usage rows for the linked Runway workspaces you administer, newest first. Unlike `/v1/organization/usage` (this API project's own usage), this reports usage from the workspace linked to this...

Parameters:

- `cursor` (query, string) - max length 1000. Cursor from a previous response for fetching the next page of results.
- `limit` (query, integer) - 1-100; default `50`. The maximum number of items to return per page.
- `from` (query, string, required) - Start of the time window (inclusive), ISO-8601 datetime or date. A date means midnight UTC.
- `to` (query, string, required) - End of the time window (exclusive), ISO-8601 datetime or date. A date means midnight UTC, so `to=2026-08-01` covers all of July 31. A `cursor` can only narrow this window, never extend it past `to`.
- `organizationId` (query, string) - format uuid. Organization to report on. Optional when this API project is linked to a single organization; required when it is linked to more than one. If it is missing then, the 400 response lists the IDs and names of the linked...
- `workspaceIds` (query, string) - Restrict results to these workspace IDs, as a comma-separated list. Defaults to every workspace you administer in the organization.

Response 200:

- `data` (array of object, required) - The list of items for the current page.
  - `transactionId` (string, required) - Unique ID of the credit transaction behind this row. Stable across requests, so use it to deduplicate overlapping pulls.
  - `taskId` (string or null, required) - ID of the generation this row belongs to. A charge and its refunds share it. `null` for App Studio usage, which has no generation.
  - `status` (string or null, required) - Current status of the generation when you request it, so it can change between pulls (upsert on `transactionId`). A refund row doesn't mean the generation failed. `null` when `taskId` is null or the generation no long...
  - `outputType` (string or null, required) - Media type of the generation's output: one of the listed values, which won't be remapped. Agent sandbox sessions report `file`. `null` when `taskId` is null, the generation no longer exists, or the type wasn't recorded.
  - `outputCount` (integer or null, required) - Number of output files the generation returned, including ones the user later deleted and excluding attachments such as playable proxies. Copying an output into a project can raise it. 0 when it returned no files, for...
  - `timestamp` (string, required) - format date-time. When the generation was charged.
  - `userId` (integer, required) - ID of the user who generated.
  - `email` (string, required) - Email of the user who generated.
  - `workspaceId` (integer, required) - ID of the owning workspace.
  - `workspaceName` (string, required) - Name of the owning workspace.
  - `projectId` (string or null, required) - ID of the Runway web app project the generation was made in (not this API project). `null` when no project is recorded for it, which includes generations made outside a project, generations made before project trackin...
  - `projectName` (string or null, required) - Current name of that project, so it changes when the project is renamed (group by `projectId`). Still returned after the project is archived or deleted. `null` when `projectId` is null.
  - `tool` (string, required) - Model/task display name for the generation.
  - `credits` (number, required) - Credits charged for this generation.
  - `unit` (string, required) - one of `credits`. Unit of `credits`. Always `credits`.
  - `type` (string, required) - one of `charge`, `refund`. Whether the row is a credit charge for a generation or a task refund (negative credits).
- `hasMore` (boolean, required) - Whether there are more items available after this page.
- `nextCursor` (string or null, required) - Cursor to use for fetching the next page, or null if there are no more pages.

### GET /v1/organization/webapp/audit_logs

List linked workspace audit logs

List audit log entries for the linked Runway workspaces you administer, newest first. Authorized via the account link between this API project and the workspace.

Parameters:

- `cursor` (query, string) - max length 1000. Cursor from a previous response for fetching the next page of results.
- `limit` (query, integer) - 1-100; default `50`. The maximum number of items to return per page.
- `organizationId` (query, string) - format uuid. Organization to report on. Optional when this API project is linked to a single organization; required when it is linked to more than one. If it is missing then, the 400 response lists the IDs and names of the linked...
- `workspaceIds` (query, string) - Restrict results to these workspace IDs, as a comma-separated list of up to 50 IDs. Defaults to every workspace you administer in the organization.
- `actions` (query, string) - Restrict results to these audit log actions, as a comma-separated list of up to 50 actions. Allowed values: `AgentArtifactCommentCreated`, `AgentArtifactCreated`, `AgentArtifactVersionSaved`, `AgentArtifactSessionAtta...
- `actorEmails` (query, string) - Restrict results to entries performed by the users with these emails, as a comma-separated list of up to 50 emails.
- `from` (query, string) - format date-time. Start of the time window (inclusive), ISO-8601 datetime.
- `to` (query, string) - format date-time. End of the time window (exclusive), ISO-8601 datetime.

Response 200:

- `data` (array of object, required) - The list of items for the current page.
  - `eventId` (string, required) - format uuid. Unique identifier of the entry.
  - `timestamp` (string, required) - format date-time. When the action occurred.
  - `action` (string, required) - one of `AgentArtifactCommentCreated`, `AgentArtifactCreated`, `AgentArtifactVersionSaved`, `AgentArtifactSessionAttached`, `AgentArtifactSessionDetached`, `UserLogin`, `PasswordChanged`, `EmailChangeRequested`, `EmailChanged`, `UserRegistered`, `UserAccountDeleted`, `WorkspaceCreated`, `WorkspaceDeleted`, `MemberInvited`, `MemberInviteReminderSent`, `MemberRemoved`, `MemberRoleChanged`, `InviteAccepted`, `MemberJoinedViaDomain`, `TeamSettingsUpdated`, `InviteLinkToggled`, `UserGroupCreated`, `UserGroupUpdated`, `UserGroupDeleted`, `UserGroupArchived`, `UserGroupRestored`, `UserGroupMemberAdded`, `UserGroupMemberRemoved`, `UserGroupCreditCapUpdated`, `UserGroupVisibilityUpdated`, `SSOLogin`, `SSOUserProvisioned`, `SSOConfigCreated`, `SSOUserAutoAddedToTeam`, `SSODomainRegistrationCloned`, `AssetCreated`, `AssetUpdated`, `AssetDeleted`, `AssetDownloaded`, `AssetShared`, ... (137 total). The action performed.
  - `actorUsername` (string or null, required) - Username of the user who performed the action.
  - `actorEmail` (string or null, required) - Email of the user who performed the action.
  - `actorDeleted` (boolean, required) - Whether the acting user has since been deleted.
  - `workspaceId` (integer, required) - ID of the owning workspace.
  - `workspaceName` (string, required) - Name of the owning workspace.
  - `metadata` (object, required) - Action-specific details.
    - `Workspace` (string or null)
    - `Invited member` (string)
    - `Removed member` (string)
    - `Added member` (string)
    - `Target member` (string or null)
    - `Member email` (string)
    - `Accepted by` (string)
    - `New email` (string)
    - `Previous email` (string)
    - `Requested via` (array of string)
    - `Previous role` (string or null)
    - `New role` (string)
    - `Role` (string)
    - `Login method` (string)
    - `Method` (string)
    - `Platform` (string)
    - `Application` (string)
    - `Plan` (string)
    - `Amount` (number)
    - `Promotion` (string)
    - `New User` (boolean)
    - `Group name` (string)
    - `Project ID` (string)
    - `Language model or provider` (string)
    - `Model` (string)
    - `Operation` (string)
    - `Asset name` (string)
    - `Asset type` (string)
    - `Filename` (string)
    - `Downloaded by owner` (boolean)
    - `Anonymous` (boolean)
    - `Watermarked` (boolean)
    - `Updated fields` (array of string)
    - `Source application` (string)
    - `Source` (string)
    - `Task ID` (string)
    - `Comment ID` (string)
    - `Comment target type` (string)
    - `Comment target ID` (string)
    - `Mentions` (number)
    - `Comment text` (string)
    - `Previous text` (string)
    - `New text` (string)
    - `Agent tagged` (boolean)
    - `Agent session ID` (string)
    - `Connector` (string)
    - `Tool` (string)
    - `Read or write` (string)
    - `Result` (string)
    - `Outcome` (string)
    - `Error code` (string)
    - `Reason` (string or null)
    - `Tag name` (string)
    - `Tag color` (string)
    - `Workspace ID` (number)
    - `From workspace ID` (number)
    - `To workspace ID` (number)
    - `Email domain` (string)
    - `Automatic` (boolean)
    - `Join policy` (string)
    - `Enabled` (boolean)
    - `Link type` (string)
    - `Workspace name` (string or null)
    - `Workspace picture` (string or null)
    - `Workspace description` (string or null)
    - `Default task name template` (string or null)
    - `Default project discoverability` (string)
    - `Setting` (string)
    - `Previous value` (string or number or boolean or object or null)
    - `New value` (string or number or boolean or object or null)
    - `Shared with workspace` (boolean)
    - `Shared in project` (string or null)
    - `Shared with projects` (array of string)
    - `Brand kit ID` (string)
    - `Source category ID` (string)
    - `Destination category ID` (string)
    - `Hard spend cap` (boolean)
    - `Spend cap` (number)
    - `Spend cap change` (number)
    - `Previous project credit cap` (number or null)
    - `Project credit cap` (number or null)
    - `Credits used` (number)
    - `Spend cap (USD cents)` (number)
    - `Recharge amount (USD cents)` (number)
    - `Recharge below (credits)` (number)
    - `Cancels at period end` (boolean)
    - `API account` (string)
    - `API project ID` (string)
    - `Organization` (string)
    - `AWS license` (string)
    - `Direction` (string)
    - `Amount received` (number)
    - `Asset ID` (string)
    - `Source version asset ID` (string)
    - `Root asset ID` (string)
    - `Media included` (boolean)
    - `Via public API` (boolean)
    - `Provider` (string)
    - `Selected` (boolean)
    - `Result metric ID` (string or null)
    - `Ad account ID` (string)
    - `Ad sync run ID` (string)
    - `Ad sync start date` (string)
    - `Ad sync end date` (string)
    - `Ads onboarding answers` (array of string)
    - `Ads onboarding completed` (boolean)
    - `Ad creative ID` (string)
    - `Ad review request ID` (string)
    - `Ad review batch ID` (string)
    - `Submitted via` (string)
    - `Review decision` (string)
    - `Ad publish batch ID` (string)
    - `Platform ad account ID` (string)
    - `Into a new test ad set` (boolean)
    - `Creatives queued` (number)
    - `Creatives cancelled` (number)
    - `Creatives retried` (number)
    - `Ads created as` (string)
    - `Ad level` (string)
    - `Status before` (string)
    - `Status after` (string)
    - `Platform object ID` (string)
    - `Campaign setup ID` (string)
    - `Campaign setup type` (string)
    - `Campaign setup version` (number)
    - `App Studio app` (string or null)
    - `App Studio session` (string)
    - `App Studio app ID` (string)
    - `Secret name` (string)
    - `App Studio deploy` (string)
    - `Files moved` (number)
    - `Previously shared in project` (string or null)
- `hasMore` (boolean, required) - Whether there are more items available after this page.
- `nextCursor` (string or null, required) - Cursor to use for fetching the next page, or null if there are no more pages.

### GET /v1/organization/webapp/audit_logs/{eventId}

Get a linked workspace audit log entry

Get a single audit log entry, including its metadata and forensic details, for a linked Runway workspace you administer. Authorized via the account link between this API project and the workspace.

Parameters:

- `eventId` (path, string, required) - format uuid. The `eventId` of an entry returned by the list endpoint.
- `organizationId` (query, string) - format uuid. Organization to report on. Optional when this API project is linked to a single organization; required when it is linked to more than one. If it is missing then, the 400 response lists the IDs and names of the linked...

Response 200:

- `eventId` (string, required) - format uuid. Unique identifier of the entry.
- `timestamp` (string, required) - format date-time. When the action occurred.
- `action` (string, required) - one of `AgentArtifactCommentCreated`, `AgentArtifactCreated`, `AgentArtifactVersionSaved`, `AgentArtifactSessionAttached`, `AgentArtifactSessionDetached`, `UserLogin`, `PasswordChanged`, `EmailChangeRequested`, `EmailChanged`, `UserRegistered`, `UserAccountDeleted`, `WorkspaceCreated`, `WorkspaceDeleted`, `MemberInvited`, `MemberInviteReminderSent`, `MemberRemoved`, `MemberRoleChanged`, `InviteAccepted`, `MemberJoinedViaDomain`, `TeamSettingsUpdated`, `InviteLinkToggled`, `UserGroupCreated`, `UserGroupUpdated`, `UserGroupDeleted`, `UserGroupArchived`, `UserGroupRestored`, `UserGroupMemberAdded`, `UserGroupMemberRemoved`, `UserGroupCreditCapUpdated`, `UserGroupVisibilityUpdated`, `SSOLogin`, `SSOUserProvisioned`, `SSOConfigCreated`, `SSOUserAutoAddedToTeam`, `SSODomainRegistrationCloned`, `AssetCreated`, `AssetUpdated`, `AssetDeleted`, `AssetDownloaded`, `AssetShared`, ... (137 total). The action performed.
- `actorUsername` (string or null, required) - Username of the user who performed the action.
- `actorEmail` (string or null, required) - Email of the user who performed the action.
- `actorDeleted` (boolean, required) - Whether the acting user has since been deleted.
- `workspaceId` (integer, required) - ID of the owning workspace.
- `workspaceName` (string, required) - Name of the owning workspace.
- `metadata` (object, required) - Action-specific details.
  - `Workspace` (string or null)
  - `Invited member` (string)
  - `Removed member` (string)
  - `Added member` (string)
  - `Target member` (string or null)
  - `Member email` (string)
  - `Accepted by` (string)
  - `New email` (string)
  - `Previous email` (string)
  - `Requested via` (array of string)
  - `Previous role` (string or null)
  - `New role` (string)
  - `Role` (string)
  - `Login method` (string)
  - `Method` (string)
  - `Platform` (string)
  - `Application` (string)
  - `Plan` (string)
  - `Amount` (number)
  - `Promotion` (string)
  - `New User` (boolean)
  - `Group name` (string)
  - `Project ID` (string)
  - `Language model or provider` (string)
  - `Model` (string)
  - `Operation` (string)
  - `Asset name` (string)
  - `Asset type` (string)
  - `Filename` (string)
  - `Downloaded by owner` (boolean)
  - `Anonymous` (boolean)
  - `Watermarked` (boolean)
  - `Updated fields` (array of string)
  - `Source application` (string)
  - `Source` (string)
  - `Task ID` (string)
  - `Comment ID` (string)
  - `Comment target type` (string)
  - `Comment target ID` (string)
  - `Mentions` (number)
  - `Comment text` (string)
  - `Previous text` (string)
  - `New text` (string)
  - `Agent tagged` (boolean)
  - `Agent session ID` (string)
  - `Connector` (string)
  - `Tool` (string)
  - `Read or write` (string)
  - `Result` (string)
  - `Outcome` (string)
  - `Error code` (string)
  - `Reason` (string or null)
  - `Tag name` (string)
  - `Tag color` (string)
  - `Workspace ID` (number)
  - `From workspace ID` (number)
  - `To workspace ID` (number)
  - `Email domain` (string)
  - `Automatic` (boolean)
  - `Join policy` (string)
  - `Enabled` (boolean)
  - `Link type` (string)
  - `Workspace name` (string or null)
  - `Workspace picture` (string or null)
  - `Workspace description` (string or null)
  - `Default task name template` (string or null)
  - `Default project discoverability` (string)
  - `Setting` (string)
  - `Previous value` (string or number or boolean or object or null)
  - `New value` (string or number or boolean or object or null)
  - `Shared with workspace` (boolean)
  - `Shared in project` (string or null)
  - `Shared with projects` (array of string)
  - `Brand kit ID` (string)
  - `Source category ID` (string)
  - `Destination category ID` (string)
  - `Hard spend cap` (boolean)
  - `Spend cap` (number)
  - `Spend cap change` (number)
  - `Previous project credit cap` (number or null)
  - `Project credit cap` (number or null)
  - `Credits used` (number)
  - `Spend cap (USD cents)` (number)
  - `Recharge amount (USD cents)` (number)
  - `Recharge below (credits)` (number)
  - `Cancels at period end` (boolean)
  - `API account` (string)
  - `API project ID` (string)
  - `Organization` (string)
  - `AWS license` (string)
  - `Direction` (string)
  - `Amount received` (number)
  - `Asset ID` (string)
  - `Source version asset ID` (string)
  - `Root asset ID` (string)
  - `Media included` (boolean)
  - `Via public API` (boolean)
  - `Provider` (string)
  - `Selected` (boolean)
  - `Result metric ID` (string or null)
  - `Ad account ID` (string)
  - `Ad sync run ID` (string)
  - `Ad sync start date` (string)
  - `Ad sync end date` (string)
  - `Ads onboarding answers` (array of string)
  - `Ads onboarding completed` (boolean)
  - `Ad creative ID` (string)
  - `Ad review request ID` (string)
  - `Ad review batch ID` (string)
  - `Submitted via` (string)
  - `Review decision` (string)
  - `Ad publish batch ID` (string)
  - `Platform ad account ID` (string)
  - `Into a new test ad set` (boolean)
  - `Creatives queued` (number)
  - `Creatives cancelled` (number)
  - `Creatives retried` (number)
  - `Ads created as` (string)
  - `Ad level` (string)
  - `Status before` (string)
  - `Status after` (string)
  - `Platform object ID` (string)
  - `Campaign setup ID` (string)
  - `Campaign setup type` (string)
  - `Campaign setup version` (number)
  - `App Studio app` (string or null)
  - `App Studio session` (string)
  - `App Studio app ID` (string)
  - `Secret name` (string)
  - `App Studio deploy` (string)
  - `Files moved` (number)
  - `Previously shared in project` (string or null)
- `resourceType` (string or null, required) - Type of the affected resource, if any. Currently one of `account_link`, `agent_custom_skill`, `asset`, `brand_kit`, `generation`, `invite_link`, `membership`, `organization`, `permission`, `promotion`, `session`, `sha...
- `resourceId` (string or null, required) - ID of the affected resource, if any.
- `clientIpAddress` (string, required) - IP address of the client that performed the action.
- `userAgent` (string or null, required) - User-Agent header of the client request.
- `requestId` (string or null, required) - Request ID for correlation with other logs.

Other responses: `404`

### GET /v1/organization/webapp/members

List linked workspace members

List the members of the linked Runway workspaces you administer, one row per member per workspace, including pending invites and members who were removed. Ordered by `membershipId`. Authorized via the account link bet...

Parameters:

- `cursor` (query, string) - max length 1000. Cursor from a previous response for fetching the next page of results.
- `limit` (query, integer) - 1-100; default `50`. The maximum number of items to return per page.
- `organizationId` (query, string) - format uuid. Organization to report on. Optional when this API project is linked to a single organization; required when it is linked to more than one. If it is missing then, the 400 response lists the IDs and names of the linked...
- `workspaceIds` (query, string) - Restrict results to these workspace IDs, as a comma-separated list of up to 50 IDs. Defaults to every workspace you administer in the organization.

Response 200:

- `data` (array of object, required) - The list of items for the current page.
  - `membershipId` (integer, required) - Unique ID of the membership. Stable across requests, so use it to update a member's row between pulls.
  - `userId` (integer or null, required) - ID of the member's Runway user. It doesn't change when their email does. `null` for an invite to an email with no Runway account yet.
  - `email` (string, required) - Email of the member, or the email the invite was sent to.
  - `role` (string, required) - one of `viewer`, `editor`, `admin`, `non-generating-admin`. Role in the workspace. `non-generating-admin` is a Billing Admin.
  - `status` (string, required) - one of `active`, `invited`, `deactivated`. `active`: a member of the workspace. `invited`: invited, and the invite is not accepted yet. `deactivated`: no longer a member; `deactivationReason` says why.
  - `deactivationReason` (string or null, required) - Why the membership is `deactivated`. `removed`: the member was removed from the workspace. `invite_ended`: the invite was declined or revoked, which are recorded the same way. `suspended`: the user is suspended. `null...
  - `provisionedAt` (string, required) - format date-time. When the member was added, or when the invite was sent.
  - `deprovisionedAt` (string or null, required) - Approximately when the member was removed, or the invite was declined or revoked: the membership's last change. `null` when the membership was not ended, including for a suspended user.
  - `lastActiveDate` (string or null, required) - Last UTC date the member used Runway, on the web or mobile app and in any workspace. `null` when they never accepted the invite or have no recorded activity.
  - `workspaceId` (integer, required) - ID of the workspace.
  - `workspaceName` (string, required) - Name of the workspace.
- `hasMore` (boolean, required) - Whether there are more items available after this page.
- `nextCursor` (string or null, required) - Cursor to use for fetching the next page, or null if there are no more pages.

### GET /v1/organization

Get organization information

Get usage tier and credit balance information about the organization associated with the API key used to make the request.

Response 200:

- `tier` (object, required) - Limits associated with the organization's tier.
  - `maxMonthlyCreditSpend` (integer, required) - minimum 0. The maximum number of credits that can be purchased in a month.
  - `models` (object, required) - An object containing model-specific limits. Each key represents a model.
- `creditBalance` (integer, required) - minimum 0. The number of credits remaining in the organization account.
- `usage` (object, required) - Usage data for the organization.
  - `models` (object, required)

### POST /v1/organization/usage

Query credit usage

Fetch credit usage data broken down by model and day for the organization associated with the API key used to make the request. Up to 90 days of data can be queried at a time. Usage updates hourly; recent activity may...

Request body:

- `startDate` (string) - format date. The start date of the usage data in ISO-8601 format (YYYY-MM-DD). If unspecified, it will default to 30 days before the current date. All dates are in UTC.
- `beforeDate` (string) - format date. The end date of the usage data in ISO-8601 format (YYYY-MM-DD), not inclusive. If unspecified, it will default to thirty days after the start date. Must be less than or equal to 90 days after the start date. All dates...
- `tags` (array of string) - min 1 items. Only count generations that were created with every one of these tags in the `X-Runway-Tags` header. Tags are case-insensitive. Up to 10 tags.
- `groupBy` (string) - Also break usage down by tag in `resultsByTag`. `"tag"` gives one bucket per tag; a generation with several tags counts toward each of them. `"tag:<key>"` (for example `"tag:team"`) gives one bucket per value of that...

Response 200:

- `results` (array of object, required)
  - `date` (string, required) - format date. The date of the usage data in ISO-8601 format (YYYY-MM-DD). All dates are in UTC.
  - `usedCredits` (array of object, required) - The credits used per model for the given date.
    - `model` (string, required) - one of `gen4.5`, `gen3a_turbo`, `gen4_turbo`, `ideogram_vector`, `recraft_v4_1_vector`, `gen4_image`, `gen4_image_turbo`, `gpt_image_2`, `gpt_image_2_5_flare`, `gpt_image_2_5_sunburst`, `gpt_image_2_6_flare`, `gpt_image_2_6_sunburst`, `act_two`, `gen4_aleph`, `veo3`, `veo3.1`, `veo3.1_fast`, `gemini_2.5_flash`, `gemini_image3_pro`, `gemini_image3.1_flash`, `gemini_image3.1_flash_lite`, `nano_banana_2.1`, `recraft_v4_1_flash`, `seedream5_pro_layers`, `seedream5_pro`, `seedream5_flash`, `seedream5.5`, `seedream5.5_layers`, `seedream5_lite`, `gemini_omni_flash`, `gemini_omni_flash_1.2`, `gemini_omni_flash_1.1`, `eleven_multilingual_v2`, `seed_audio`, `eleven_v3`, `eleven_v4`, `gemini_3.8_flash_tts`, `gemini_3.8_flash_lite_tts`, `eleven_text_to_sound_v2`, `mirelo_sfx_2_0`, ... (91 total). The model that credits were spent on.
    - `amount` (integer, required) - The net number of credits spent on the model. May be negative if refunds exceeded charges on this day.
- `models` (array of string, required) - The list of models with usage during the queried time range.
- `apiKeys` (array of string) - Reserved for future use.
- `resultsByApiKey` (array of object) - Reserved for future use.
  - `date` (string, required) - format date
  - `usedCredits` (array of object, required)
    - `apiKeyId` (string, required) - format uuid
    - `amount` (integer, required)
- `resultsByTag` (array of object) - Credit usage broken down by tag, present when `groupBy` is set. With `groupBy: "tag"`, a generation with several tags counts toward each of them, so the buckets can add up to more than the total. With `groupBy: "tag:<...
  - `date` (string, required) - format date. The date of the usage data in ISO-8601 format (YYYY-MM-DD). All dates are in UTC.
  - `usedCredits` (array of object, required) - The credits used per tag for the date.
    - `tag` (string or null, required) - The tag that credits were spent under, or null for usage without a matching tag.
    - `amount` (integer, required) - The net number of credits spent under the tag. May be negative if refunds exceeded charges on this day.
- `tags` (array of string) - The tags on usage in the queried time range, sorted alphabetically, present when `tags` or `groupBy` is set. Lists at most the 1,000 tags with the most credits.

