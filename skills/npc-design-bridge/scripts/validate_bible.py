#!/usr/bin/env python3
"""Validate an NPC Design Bible against the compact 3-layer template."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "NPC 基础身份",
    "NPC 涉及的剧情",
    "NPC 的功能",
    "设计校准",
]

REQUIRED_KEYWORDS = [
    "一句话定位",
    "身份摘要",
    "视觉识别点",
    "剧情位置",
    "玩家关系线",
    "功能声明",
    "互动规则",
    "删除测试",
]

PLACEHOLDER_PATTERNS = [
    r"\[[^\]]+\]",
]


def find_missing_sections(content: str) -> list[str]:
    missing = []
    for section in REQUIRED_SECTIONS:
        pattern = re.compile(rf"#+\s+.*{re.escape(section)}", re.IGNORECASE)
        if not pattern.search(content):
            missing.append(section)
    return missing


def find_missing_keywords(content: str) -> list[str]:
    return [keyword for keyword in REQUIRED_KEYWORDS if keyword not in content]


def find_placeholders(content: str) -> list[str]:
    placeholders: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        placeholders.extend(re.findall(pattern, content))
    return sorted(set(placeholders))


def count_markdown_tables(content: str) -> int:
    table_blocks = 0
    in_table = False
    for line in content.splitlines():
        is_table_line = line.strip().startswith("|") and line.strip().endswith("|")
        if is_table_line and not in_table:
            table_blocks += 1
            in_table = True
        elif not is_table_line:
            in_table = False
    return table_blocks


def validate_bible(filepath: Path) -> dict:
    result = {
        "file": str(filepath),
        "valid": True,
        "issues": [],
        "sections_missing": [],
        "keywords_missing": [],
        "placeholders_found": [],
        "table_count": 0,
    }

    if not filepath.exists():
        result["valid"] = False
        result["issues"].append("文件不存在")
        return result

    content = filepath.read_text(encoding="utf-8")

    result["sections_missing"] = find_missing_sections(content)
    for section in result["sections_missing"]:
        result["issues"].append(f"缺少章节: {section}")

    result["keywords_missing"] = find_missing_keywords(content)
    for keyword in result["keywords_missing"]:
        result["issues"].append(f"缺少关键字段: {keyword}")

    result["placeholders_found"] = find_placeholders(content)
    if result["placeholders_found"]:
        result["issues"].append("仍包含未替换占位符")

    result["table_count"] = count_markdown_tables(content)
    if result["table_count"] < 4:
        result["issues"].append("表格数量偏少，可能缺少快速索引、关系线、互动规则或校准表")

    if result["issues"]:
        result["valid"] = False

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate NPC Design Bible")
    parser.add_argument("input", type=Path, help="Input Markdown file")
    parser.add_argument("--json", "-j", action="store_true", help="Output JSON")
    parser.add_argument("--validate-only", action="store_true", help="Only validate")
    args = parser.parse_args()

    result = validate_bible(args.input)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif result["valid"]:
        print(f"OK: {args.input}")
    else:
        print(f"FAILED: {args.input}")
        for issue in result["issues"]:
            print(f"- {issue}")

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
