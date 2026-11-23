import argparse
from datetime import date
from pathlib import Path

from media_audit.audit import DEFAULT_VERY_SHORT, run_audit, summarize


def main(argv=None):
    parser = argparse.ArgumentParser(prog="media-audit", description="Audit a folder of video into a CSV report.")
    sub = parser.add_subparsers(dest="command", required=True)
    audit = sub.add_parser("audit", help="scan a folder and write or update the audit report")
    audit.add_argument("folder", type=Path)
    audit.add_argument("-o", "--output", type=Path,
                       help="report path (default: <today>_audit.csv; pass an existing report to merge into it)")
    audit.add_argument("--very-short", type=float, default=DEFAULT_VERY_SHORT,
                       help="flag files at or below this many seconds (default: %(default)s)")
    tr = sub.add_parser("transform", help="prep and send rows marked send=y to Runway Aleph (dry run by default)")
    tr.add_argument("report", type=Path, help="audit report CSV with Selections filled in")
    tr.add_argument("--folder", type=Path, required=True, help="folder holding the source files")
    tr.add_argument("--run", action="store_true", help="actually upload and spend credits")
    tr.add_argument("--max-credits", type=int, default=300, help="refuse if the estimate is over this (default: %(default)s)")
    tr.add_argument("--allow-long", action="store_true", help="allow clips over 10s (30s is always the limit)")
    tr.add_argument("--force", action="store_true", help="resend rows that already have a task_id")
    tr.add_argument("--output-dir", type=Path, default=Path("output"))
    tr.add_argument("--tag", help="X-Runway-Tags value (default: project:<folder name>)")
    args = parser.parse_args(argv)

    if args.command == "transform":
        return _transform(parser, args)

    if args.output is None:
        args.output = Path(f"{date.today():%Y-%m-%d}_audit.csv")
    if not args.folder.is_dir():
        parser.error(f"not a folder: {args.folder}")
    written = run_audit(args.folder, args.output, very_short=args.very_short)
    if written != args.output:
        print(f"Existing {args.output} could not be merged; wrote {written} instead.")
    print(summarize(written))
    print(f"Report: {written}")


def _transform(parser, args):
    from media_audit.transform import SelectionError, plan, prep, run_jobs, select_jobs

    if not args.report.is_file():
        parser.error(f"report not found: {args.report}")
    if not args.folder.is_dir():
        parser.error(f"not a folder: {args.folder}")
    try:
        jobs, skipped = select_jobs(args.report, args.folder, force=args.force, allow_long=args.allow_long)
    except SelectionError as e:
        raise SystemExit(f"Nothing sent. {e}")
    for note in skipped:
        print(f"skipped {note}")
    if not jobs:
        print("No rows with send=y to process.")
        return
    print(plan(jobs, args.max_credits))

    if not args.run:
        for job in jobs:
            prep(job, args.output_dir / "prep")
        print(f"Dry run: clips prepared in {args.output_dir / 'prep'}; nothing uploaded or spent. Add --run to send.")
        return

    from runwayml import RunwayML

    tag = args.tag or f"project:{args.folder.resolve().name.lower()}"
    try:
        run_jobs(jobs, args.report, RunwayML(), args.output_dir, tag=tag, max_credits=args.max_credits)
    except SelectionError as e:
        raise SystemExit(f"Nothing sent. {e}")


if __name__ == "__main__":
    main()
