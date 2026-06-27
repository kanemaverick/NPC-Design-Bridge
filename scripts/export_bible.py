#!/usr/bin/env python3
"""export_bible.py — 将 NPC Design Bible 的 Markdown 输出整理为格式化文档。

用法:
    python scripts/export_bible.py <input.md> [--output <output.md>] [--format plain|markdown]

如果未指定 --output，输出到 stdout。
"""

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "Project Experience Goal",
    "NPC One-Line Pitch",
    "Character Concept Card",
    "Player Touchpoint Map",
    "Core Gameplay Loop",
    "NPC Gameplay Function",
    "Behavior & State Rules",
    "Dialogue Samples",
    "Remove-Test Results",
    "Anti-Trope Check",
    "Micro Playtest Results",
    "Design Decisions & Iteration Log",
    "Portfolio Review Score",
]


def validate_bible(content: str) -> list[str]:
    """检查 NPC Design Bible 是否包含所有必填章节。"""
    missing = []
    for section in REQUIRED_SECTIONS:
        pattern = re.compile(rf"#+\s+.*{re.escape(section)}", re.IGNORECASE)
        if not pattern.search(content):
            missing.append(section)
    return missing


def clean_markdown(content: str) -> str:
    """清理和标准化 Markdown 格式。"""
    lines = content.split("\n")
    cleaned = []
    in_code_block = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block

        if in_code_block:
            cleaned.append(line)
            continue

        stripped = line.rstrip()
        cleaned.append(stripped)

    text = "\n".join(cleaned)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip() + "\n"

    return text


def main():
    parser = argparse.ArgumentParser(description="Export NPC Design Bible to formatted document")
    parser.add_argument("input", type=Path, help="Input Markdown file")
    parser.add_argument("--output", "-o", type=Path, default=None, help="Output file path")
    parser.add_argument("--format", "-f", choices=["plain", "markdown"], default="markdown",
                        help="Output format (default: markdown)")
    parser.add_argument("--validate-only", action="store_true",
                        help="Only validate, don't export")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"错误：输入文件不存在 — {args.input}", file=sys.stderr)
        sys.exit(1)

    content = args.input.read_text(encoding="utf-8")

    missing = validate_bible(content)
    if missing:
        print("⚠️ 验证警告 — 以下章节缺失：")
        for s in missing:
            print(f"  - {s}")
        if args.validate_only:
            sys.exit(1)
    else:
        print("✅ 所有必填章节已存在")

    if args.validate_only:
        sys.exit(0)

    output = clean_markdown(content)

    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"✅ 导出完成 → {args.output}")
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
