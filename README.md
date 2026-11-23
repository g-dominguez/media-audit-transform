# media-audit-transform

Audit a folder of video, pick clips from the report, and turn them into cartoon-style versions with Runway Aleph 2.0.

Before footage goes into an AI pipeline you need to know what you have: which files are ready, which need fixing first, and what an action would cost before anything is spent. Nothing is spent or changed without approval.

## How it works

1. **Audit** (built): scan a folder with `ffprobe` and write a CSV report (default `YYYY-MM-DD_audit.csv`), one row per file. It covers real orientation (including the rotation flag), length, size, fps, codec, audio, flags such as `very_short` and `possible_duplicate`, and a readiness verdict (`ready`, `needs_prep`, `unsupported`). Read-only; no Runway calls, no credits.
2. **Review**: open the CSV and fill in `send`, `in`, `out`, and optionally `prompt` and `seed` on the rows you want transformed.
3. **Transform** (built): validate every row marked `send=y`, prepare each clip locally (frame-accurate trim, bake in rotation, cap at 1080p and 30 fps), run it through Aleph 2.0, download the result, and write `status`, `task_id`, `output_path` and `credits` back into the CSV. Every run is also logged to `output/runs.jsonl`. Aleph keeps the clip's original audio. Dry run by default; `--run` spends credits, capped by `--max-credits` (default 300) and your balance. Rows that already have a `task_id` are skipped unless you pass `--force`.

Re-running the audit merges into an existing report and keeps your selections.

## Usage

```
python3 -m venv .venv && .venv/bin/pip install -e . pytest
brew install ffmpeg

.venv/bin/media-audit audit path/to/folder [-o report.csv] [--very-short 5]
.venv/bin/media-audit transform 2026-11-22_audit.csv --folder path/to/folder          # dry run: plan, cost, local prep
.venv/bin/media-audit transform 2026-11-22_audit.csv --folder path/to/folder --run    # upload and spend credits
.venv/bin/pytest
```

`in` and `out` take seconds (`12.5`), `m:ss` or `h:mm:ss`. Clips must be 2–10 seconds (`--allow-long` allows up to 30). A blank `prompt` uses the default cartoon prompt; a blank `seed` lets Runway pick one. `--run` needs `RUNWAYML_API_SECRET` set in your environment.

If you edit the CSV in Google Sheets, type in/out points as plain seconds: Sheets turns `0:12` into twelve minutes. Download it back as CSV before running.

`--very-short` sets the length (seconds) at or below which a file gets the `very_short` flag. It only labels files.

## Docs

- [GLOSSARY.md](GLOSSARY.md): project terms.
- [Media_Audit_Scoping_Brief.md](Media_Audit_Scoping_Brief.md): original scoping brief.
- [docs/runway/](docs/runway/README.md): saved Runway API docs.

Video files, `output/`, and audit CSVs are gitignored so footage and filenames are not committed.
