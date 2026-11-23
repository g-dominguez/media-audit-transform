# Glossary

**Audit**:
A read-only scan of a folder of video that reports what each file is and what shape it is in. Never moves, changes, or deletes files, and never spends credits.

**Audit report**:
The CSV an Audit produces, one row per Source file. A person reviews it and fills in the Selection columns on the rows they want transformed; the same CSV is then the input to Transform.
_Avoid_: scan output

**Selection**:
The reviewer-filled columns on an Audit report row (in point, out point, prompt) that mark that row for Transform. A row with no Selection is skipped.

**Source file**:
A video file in the audited folder, as it exists on disk.
_Avoid_: clip (ambiguous)

**Clip**:
The segment of a Source file, between a Selection's in point and out point, that is prepared and sent for transformation.
_Avoid_: video, file

**Readiness**:
A Source file's verdict for Aleph: `ready`, `needs_prep` (with the specific Prep steps listed), or `unsupported` (not a video, unreadable, or shorter than Aleph's 2-second minimum, which no Prep can fix). A file is never `unsupported` just for being 4K or long.

**Prep**:
The local steps that make a Clip acceptable to Aleph: trim, rotate, downscale, frame-rate conversion.

**very_short**:
Flag on a Source file at or below a configurable duration (default 5 seconds). A hint that it may be unwanted, not a judgment about content. The Audit only flags it.
_Avoid_: junk

**Transform**:
Sending a prepared Clip to Runway Aleph 2.0 for a cartoon restyle.
