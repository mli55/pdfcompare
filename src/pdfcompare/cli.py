from __future__ import annotations

import argparse
from pathlib import Path

from .annotate import apply_annotations
from .compare import compare_documents
from .extract import extract_document


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdfcompare",
        description="Compare two born-digital PDFs and write highlights back to original PDFs.",
    )
    parser.add_argument("old_pdf", help="old/original PDF")
    parser.add_argument("new_pdf", help="new/revised PDF")
    parser.add_argument("--old-out", default="old_marked.pdf", help="output annotated old PDF")
    parser.add_argument("--new-out", default="new_marked.pdf", help="output annotated new PDF")
    parser.add_argument("--opacity", type=float, default=0.35, help="annotation opacity")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    old_pdf = str(Path(args.old_pdf))
    new_pdf = str(Path(args.new_pdf))

    old_pages = extract_document(old_pdf)
    new_pages = extract_document(new_pdf)

    old_rects, new_rects = compare_documents(old_pages, new_pages)

    apply_annotations(
        input_pdf=old_pdf,
        output_pdf=args.old_out,
        page_to_rects=old_rects,
        color=(1.0, 0.0, 0.0),
        opacity=args.opacity,
    )

    apply_annotations(
        input_pdf=new_pdf,
        output_pdf=args.new_out,
        page_to_rects=new_rects,
        color=(0.0, 1.0, 0.0),
        opacity=args.opacity,
    )

    old_count = sum(len(v) for v in old_rects.values())
    new_count = sum(len(v) for v in new_rects.values())

    print(f"Done.")
    print(f"Old annotations: {old_count}")
    print(f"New annotations: {new_count}")
    print(f"Wrote: {args.old_out}")
    print(f"Wrote: {args.new_out}")


if __name__ == "__main__":
    main()