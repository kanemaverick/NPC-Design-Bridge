#!/usr/bin/env python3
"""Export and lightly validate an NPC Design Bible Markdown document."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "NPC 基础身份",
    "NPC 涉及的剧情",
    "NPC 的功能",
    "设计校准",
]


def validate_bible(content: str) -> list[str]:
    missing = []
    for section in REQUIRED_SECTIONS:
        pattern = re.compile(rf"#+\s+.*{re.escape(section)}", re.IGNORECASE)
        if not pattern.search(content):
            missing.append(section)
    return missing


def clean_markdown(content: str) -> str:
    lines = content.splitlines()
    cleaned = []
    in_code_block = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        cleaned.append(line if in_code_block else line.rstrip())

    text = "\n".join(cleaned)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Export NPC Design Bible")
    parser.add_argument("input", type=Path, help="Input Markdown file")
    parser.add_argument("--output", "-o", type=Path, help="Output file path")
    parser.add_argument("--validate-only", action="store_true", help="Only validate")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: input file does not exist: {args.input}", file=sys.stderr)
        sys.exit(1)

    content = args.input.read_text(encoding="utf-8")
    missing = validate_bible(content)

    if missing:
        print("Validation warning: missing sections")
        for section in missing:
            print(f"- {section}")
        if args.validate_only:
            sys.exit(1)
    else:
        print("OK: all required sections exist")

    if args.validate_only:
        sys.exit(0)

    output = clean_markdown(content)
    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"Exported: {args.output}")
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
