#!/usr/bin/env python3
"""Generate a high-fidelity NPC card page from the bundled prototype assets."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REQUIRED = [
    SKILL_DIR / "npc-card-prototype.html",
    SKILL_DIR / "assets" / "images" / "card" / "card_bg.png",
    SKILL_DIR / "assets" / "images" / "card" / "synchro_border.png",
    SKILL_DIR / "assets" / "fonts" / "Pretendard-Bold.ttf",
    SKILL_DIR / "scripts" / "card.js",
]


def require_assets() -> None:
    missing = [path for path in REQUIRED if not path.exists()]
    if missing:
        formatted = "\n".join(f"- {path}" for path in missing)
        raise SystemExit(f"Missing required npc-card-generator assets:\n{formatted}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_name(content: str, fallback: str) -> str:
    match = re.search(r"#\s+NPC Design Bible:\s*(.+)", content)
    if match:
        return match.group(1).strip()
    return fallback


def infer_data(content: str, overrides: dict) -> dict:
    name = overrides.get("name") or extract_name(content, "未命名NPC")
    text = content

    rarity = overrides.get("rarity") or ("ssr" if "核心" in text or "主" in text else "sr")
    class_name = overrides.get("class") or "supporter"
    element = overrides.get("element") or ("wind" if any(key in text for key in ["冷", "克制", "冷静"]) else "water")
    weapon = overrides.get("weapon") or ("sr" if any(key in text for key in ["精准", "品鉴", "参数"]) else "ar")
    burst = overrides.get("burst") or ("02" if "示范" in text else "03")
    color = overrides.get("color") or ("#8A79D6" if element == "wind" else "#2ced73")

    data = {
        "name": name,
        "rarity": rarity,
        "class": class_name,
        "element": element,
        "weapon": weapon,
        "burst": burst,
        "copies": int(overrides.get("copies", 3)),
        "level": int(overrides.get("level", 100)),
        "borderType": overrides.get("borderType", "synchro"),
        "color": color,
        "quote": overrides.get("quote", "看清楚。我只做一遍。"),
        "title": overrides.get("title", "冷感示范型导师"),
    }
    if overrides.get("portrait"):
        data["portrait"] = overrides["portrait"]
    return data


def patch_prototype(html: str, data: dict) -> str:
    html = re.sub(r"<title>.*?</title>", f"<title>NPC 角色卡牌生成器 — {data['name']}</title>", html, flags=re.S)
    html = html.replace("<h1>NPC 角色卡牌 — 飞飞</h1>", f"<h1>NPC 角色卡牌 — {data['name']}</h1>")
    html = html.replace('id="input-name" value="飞飞"', f'id="input-name" value="{data["name"]}"')
    html = html.replace('let curName = "飞飞";', f'let curName = "{data["name"]}";')
    html = html.replace('<span class="info-value">飞飞</span>', f'<span class="info-value">{data["name"]}</span>')
    html = html.replace(
        '<input type="file" id="input-upload" accept="image/*">',
        '<input type="file" id="input-upload" accept="image/*"><span style="font-size:12px;color:#f4d259;margin-left:8px;">没有形象图时在这里上传</span>'
    )
    html = html.replace(
        '<div class="controls-panel">',
        '<div class="info-panel" style="border-color:rgba(244,210,89,.35);"><strong>角色图</strong>：当前未检测到本 NPC 的 Step 2 / Step 8 形象图时，卡面会显示占位。请在下方“图片位置”区域点击“上传图片”选择角色立绘。</div>\n\n    <div class="controls-panel">'
    )
    inject = f"""
    <script>
    window.NPC_CARD_PRESET = {json.dumps(data, ensure_ascii=False, indent=2)};
    document.addEventListener('DOMContentLoaded', () => {{
      const d = window.NPC_CARD_PRESET;
      const setValue = (id, value) => {{
        const el = document.getElementById(id);
        if (el) {{
          el.value = value;
          el.dispatchEvent(new Event('input', {{ bubbles: true }}));
          el.dispatchEvent(new Event('change', {{ bubbles: true }}));
        }}
      }};
      document.title = `NPC 角色卡牌生成器 — ${{d.name}}`;
      const h1 = document.querySelector('h1');
      if (h1) h1.textContent = `NPC 角色卡牌 — ${{d.name}}`;
      setValue('input-name', d.name);
      setValue('input-level', d.level);
      setValue('input-copies', d.copies);
      setValue('input-color', d.color);
      setValue('input-element', d.element);
      setValue('input-weapon', d.weapon);
      setValue('input-burst', d.burst);
      setValue('input-class', d.class);
      setValue('input-border', d.borderType);
      document.querySelectorAll('[data-rarity]').forEach(btn => {{
        if (btn.dataset.rarity === d.rarity) btn.click();
      }});
      const infoValues = document.querySelectorAll('.info-value');
      const infoText = [
        d.name,
        `${{d.rarity.toUpperCase()}} (核心角色)`,
        d.class === 'supporter' ? '关系推进者 / 支援者' : d.class,
        d.element === 'wind' ? '冷静克制 (Wind)' : d.element,
        d.weapon === 'sr' ? '精准品鉴 (SR)' : d.weapon,
        d.burst === '02' ? '失败后示范 (II)' : d.burst,
        `${{d.copies}} / 3 星`,
        `LV. ${{d.level}}`,
        d.borderType === 'synchro' ? 'Synchro (已解锁)' : d.borderType,
        d.color
      ];
      infoValues.forEach((el, idx) => {{
        if (idx < infoText.length) el.textContent = infoText[idx];
        if (idx === 9) el.style.color = d.color;
      }});
      if (d.portrait) {{
        window.applyCardData && window.applyCardData(d);
      }}
    }});
    </script>
    """
    return html.replace("</body>", inject + "\n</body>")


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def copy_required_assets(out_dir: Path) -> None:
    assets_dir = out_dir / "assets"
    if assets_dir.exists():
        shutil.rmtree(assets_dir)
    (assets_dir / "images").mkdir(parents=True, exist_ok=True)
    copy_tree(SKILL_DIR / "assets" / "images" / "card", assets_dir / "images" / "card")
    copy_tree(SKILL_DIR / "assets" / "fonts", assets_dir / "fonts")


def find_portrait(bible: Path, npc_name: str) -> Path | None:
    search_dir = bible.parent
    safe_name = re.sub(r'[\\/:*?"<>|]', "", npc_name)
    patterns = [
        f"portrait-{safe_name}.*",
        f"{safe_name}-portrait.*",
        f"{safe_name}_portrait.*",
        f"{safe_name}立绘.*",
        f"{safe_name}形象图.*",
        f"{safe_name}*.png",
        f"{safe_name}*.jpg",
        f"{safe_name}*.jpeg",
        f"{safe_name}*.webp",
    ]
    image_exts = {".png", ".jpg", ".jpeg", ".webp"}
    for pattern in patterns:
        for candidate in search_dir.glob(pattern):
            if candidate.is_file() and candidate.suffix.lower() in image_exts:
                return candidate
    return None


def attach_portrait(data: dict, bible: Path, explicit_portrait: Path | None, out_dir: Path) -> None:
    portrait = explicit_portrait if explicit_portrait and explicit_portrait.exists() else find_portrait(bible, data["name"])
    if not portrait:
        return
    dest = out_dir / "assets" / "portrait.png"
    shutil.copy2(portrait, dest)
    data["portrait"] = "./assets/portrait.png"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate high-fidelity NPC card from Bible")
    parser.add_argument("bible", type=Path, help="NPC Design Bible markdown")
    parser.add_argument("--out-dir", type=Path, required=True, help="Output card directory")
    parser.add_argument("--data", type=Path, help="Optional JSON overrides")
    parser.add_argument("--portrait", type=Path, help="Optional current NPC portrait generated by Step 2/Step 8")
    args = parser.parse_args()

    require_assets()
    if not args.bible.exists():
        raise SystemExit(f"Bible not found: {args.bible}")

    overrides = {}
    if args.data and args.data.exists():
        overrides = json.loads(read_text(args.data))

    content = read_text(args.bible)
    data = infer_data(content, overrides)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    copy_required_assets(args.out_dir)
    attach_portrait(data, args.bible, args.portrait, args.out_dir)
    copy_tree(SKILL_DIR / "scripts", args.out_dir / "scripts")
    html = patch_prototype(read_text(SKILL_DIR / "npc-card-prototype.html"), data)
    (args.out_dir / "npc-card.html").write_text(html, encoding="utf-8")
    (args.out_dir / "npc-card-data.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated: {args.out_dir / 'npc-card.html'}")


if __name__ == "__main__":
    main()
