#!/usr/bin/env python3
"""validate_bible.py — 验证 NPC Design Bible 的完整性和质量。

用法:
    python scripts/validate_bible.py <input.md> [--verbose] [--json]

检查项:
    1. 13 个必填章节是否存在
    2. 关键字段是否有实质内容（非占位符）
    3. 表格行数是否满足最低要求
"""

import argparse
import json
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

# 不应出现在最终文档中的占位符
PLACEHOLDER_PATTERNS = [
    r"\[NPC 名称\]",
    r"\[一句话介绍",
    r"\[最突出的视觉特征\]",
    r"\[语速、语气、口头禅\]",
    r"\[一句话比喻\]",
    r"\[时刻 \d\]",
    r"\[交互内容\]",
    r"\[玩家获得\]",
    r"\[做 X\]",
    r"\[Y\]",
    r"\[Z\]",
]


def validate_bible(filepath: Path, verbose: bool = False) -> dict:
    """验证 NPC Design Bible 的完整性。"""
    result = {
        "file": str(filepath),
        "valid": True,
        "issues": [],
        "sections_found": [],
        "sections_missing": [],
        "placeholders_found": [],
    }

    if not filepath.exists():
        result["valid"] = False
        result["issues"].append("文件不存在")
        return result

    content = filepath.read_text(encoding="utf-8")

    for section in REQUIRED_SECTIONS:
        pattern = re.compile(rf"#+\s+.*{re.escape(section)}", re.IGNORECASE)
        if pattern.search(content):
            result["sections_found"].append(section)
        else:
            result["sections_missing"].append(section)
            result["issues"].append(f"缺少章节: {section}")

    for pattern in PLACEHOLDER_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            result["placeholders_found"].extend(matches)
            result["issues"].append(f"发现未替换的占位符: {matches[0]}")

    # 检查表格最低行数
    touchpoint_rows = len(re.findall(r"^\|.+\|$", content, re.MULTILINE))
    if touchpoint_rows < 3:
        result["issues"].append(f"接触点地图表格行数不足 (当前: {touchpoint_rows}, 最低: 3)")

    # 检查删除测试
    if "删除" not in content and "Remove" not in content:
        result["issues"].append("未找到删除测试内容")

    if result["issues"]:
        result["valid"] = False

    return result


def main():
    parser = argparse.ArgumentParser(description="Validate NPC Design Bible")
    parser.add_argument("input", type=Path, help="Input Markdown file")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    parser.add_argument("--json", "-j", action="store_true", help="JSON 格式输出")
    args = parser.parse_args()

    result = validate_bible(args.input, verbose=args.verbose)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if result["valid"]:
            print(f"✅ 验证通过 — {args.input}")
            if args.verbose:
                print(f"   找到章节: {len(result['sections_found'])}/13")
                for s in result["sections_found"]:
                    print(f"   ✓ {s}")
        else:
            print(f"❌ 验证未通过 — {args.input}")
            for issue in result["issues"]:
                print(f"   ✗ {issue}")

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
