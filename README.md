# media-audit-transform

Audit a folder of video, pick clips from the report, and turn them into cartoon-style versions with Runway Aleph 2.0.

Before footage goes into an AI pipeline you need to know what you have: which files are ready, which need fixing first, and what an action would cost before anything is spent. Nothing is spent or changed without approval.

## How it works

1. **Audit** (built): scan a folder with `ffprobe` and write a CSV report, one row per file. It covers real orientation (including the rotation flag), length, size, fps, codec, audio, flags such as `very_short` and `possible_duplicate`, and a readiness verdict (`ready`, `needs_prep`, `unsupported`). Read-only; no Runway calls, no credits.
2. **Review**: open the CSV and fill in `send`, `in`, `out`, and optionally `prompt` and `seed` on the rows you want transformed.
3. **Transform** (planned): prepare each selected clip locally (trim, bake in rotation, downscale to 1080p), run it through Aleph 2.0, and log the result. Dry run by default, with a credit cap.

Re-running the audit merges into an existing report and keeps your selections.

## Usage

```
python3 -m venv .venv && .venv/bin/pip install -e . pytest
brew install ffmpeg

.venv/bin/media-audit audit path/to/folder -o audit.csv [--very-short 5]
.venv/bin/pytest
```

`--very-short` sets the length (seconds) at or below which a file gets the `very_short` flag. It only labels files.

## Docs

- [GLOSSARY.md](GLOSSARY.md): project terms.
- [Media_Audit_Scoping_Brief.md](Media_Audit_Scoping_Brief.md): original scoping brief.
- [docs/runway/](docs/runway/README.md): saved Runway API docs.

Video files, `output/`, and audit CSVs are gitignored so footage and filenames are not committed.
