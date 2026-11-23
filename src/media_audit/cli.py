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
    args = parser.parse_args(argv)

    if args.output is None:
        args.output = Path(f"{date.today():%Y-%m-%d}_audit.csv")
    if not args.folder.is_dir():
        parser.error(f"not a folder: {args.folder}")
    written = run_audit(args.folder, args.output, very_short=args.very_short)
    if written != args.output:
        print(f"Existing {args.output} could not be merged; wrote {written} instead.")
    print(summarize(written))
    print(f"Report: {written}")


if __name__ == "__main__":
    main()
