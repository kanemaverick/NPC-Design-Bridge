# Step 5-7 Expert Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add visible TT expert review and user-confirmation loops to Step 5-7 of NPC Design Bridge.

**Architecture:** Keep NPC Design Bridge as the single user-facing host. Add a reusable "intent-preserving expert review loop" protocol, then specialize it in Step 5, Step 6, and Step 7. Surface Liu Zhejun as an AI expert review card, and record expert collaboration in the final Bible.

**Tech Stack:** Markdown skill package, Python validation scripts already present in `scripts/`.

---

## File Structure

- `SKILL.md`: canonical skill workflow and TT collaboration protocol.
- `prompts/system_prompt.md`: global runtime rules for confirmation loops and expert cards.
- `prompts/step_05_function_anchor.md`: Step 5 loop details.
- `prompts/step_06_behavior_rules.md`: Step 6 loop details.
- `prompts/step_07_dialogue_samples.md`: Step 7 loop details.
- `prompts/step_08_bible_assembly.md`: final assembly instructions.
- `templates/npc_design_bible_template.md`: output schema section.
- `docs/tt_collaboration_log.md`: competition-facing collaboration explanation.
- `examples/tea_grandma_cozy_sim/skill_conversation.md`: sample interaction update.
- `tests/edge_cases.md`: expected behavior for user dissatisfaction and expert disagreement.
- `tests/golden_cases.md`: golden-case expectation update.

---

### Task 1: Add Global Loop And Expert Protocol

**Files:**
- Modify: `SKILL.md`
- Modify: `prompts/system_prompt.md`
- Modify: `docs/tt_collaboration_log.md`

- [x] **Step 1: Add reusable loop rules**

Add a short section defining the Step 5-7 loop: user fragment, subagent/expert refinement, current understanding, visible expert card, user confirmation, repeat if needed.

- [x] **Step 2: Add expert visibility rules**

State that the review card title is `TT专家审校｜柳喆俊 AI 视角`, and that the skill must not claim the real Liu Zhejun participated.

- [x] **Step 3: Update collaboration log**

Replace the pending pseudo-interface with the implemented review-card protocol and explain why it supports competition scoring.

### Task 2: Specialize Step 5-7 Prompts

**Files:**
- Modify: `prompts/step_05_function_anchor.md`
- Modify: `prompts/step_06_behavior_rules.md`
- Modify: `prompts/step_07_dialogue_samples.md`
- Modify: `SKILL.md`

- [x] **Step 1: Update Step 5**

Add confirmation before finalizing the function statement and remove-test result. The expert card checks core-loop necessity, delete-test strength, and whether inferred content is marked.

- [x] **Step 2: Update Step 6**

Add confirmation before finalizing behavior rules. The expert card checks trigger specificity, response feasibility, and player impact.

- [x] **Step 3: Update Step 7**

Add confirmation before finalizing dialogue samples. The expert card checks whether each line carries gameplay function, whether voice matches the NPC concept, and whether player next action is clear.

### Task 3: Add Final Collaboration Notes

**Files:**
- Modify: `prompts/step_08_bible_assembly.md`
- Modify: `templates/npc_design_bible_template.md`

- [x] **Step 1: Add Bible section**

Add `TT Expert Collaboration Notes` to final output guidance. Include Step 5-7 notes and accepted/rejected expert suggestions.

- [x] **Step 2: Preserve validator compatibility**

Do not remove or rename the 13 required sections validated by `scripts/validate_bible.py`.

### Task 4: Update Examples And Tests

**Files:**
- Modify: `examples/tea_grandma_cozy_sim/skill_conversation.md`
- Modify: `tests/edge_cases.md`
- Modify: `tests/golden_cases.md`

- [x] **Step 1: Update example conversation**

Show one pass through the Step 5-7 loop with visible expert review cards and user confirmation.

- [x] **Step 2: Update expected behavior docs**

Add cases for user dissatisfaction, expert suggestion rejection, and rough fragments that require `[待确认]` markers.

### Task 5: Validate

**Files:**
- Run only.

- [x] **Step 1: Run Python validation**

Run: `$env:PYTHONUTF8='1'; python scripts\validate_bible.py examples\tea_grandma_cozy_sim\npc_design_bible_output.md --verbose`

Expected: validation passes with 13/13 required sections.

- [x] **Step 2: Run Python compile check**

Run: `python -m py_compile scripts\validate_bible.py scripts\export_bible.py`

Expected: no output and exit code 0.
