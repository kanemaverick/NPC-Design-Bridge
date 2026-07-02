# NPC Card Generator Implementation Notes

## Current bundled implementation

This skill is bundled with a high-fidelity NIKKE-style card prototype:

- `npc-card-prototype.html`
- `assets/images/card/`
- `assets/fonts/`
- `scripts/generate_card_from_bible.py`

## Non-negotiable behavior

- Use `npc-card-prototype.html` as the source template.
- Do not hand-write a simplified replacement card.
- Do not copy or display any sample character portrait by default.
- If the current NPC has no Step 2 / Step 8 portrait, the card must show an empty placeholder and the upload control.
- Uploaded or injected portraits must be clipped inside the card art frame.
- The current mask is defined in canvas coordinates:
  - `(18, 164)`
  - `(292, 115)`
  - `(292, 542)`
  - `(18, 542)`

## Generator

Run:

```bash
python scripts/generate_card_from_bible.py path/to/npc-design-bible-NAME.md --out-dir path/to/NAME-card
```

Optional:

```bash
python scripts/generate_card_from_bible.py path/to/npc-design-bible-NAME.md --portrait path/to/portrait.png --out-dir path/to/NAME-card
```

The generator copies only required card assets and fonts. It intentionally does not copy prototype sample portraits.
