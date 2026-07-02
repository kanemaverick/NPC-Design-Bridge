# Step 5-7 Expert Loop Design

## Background

NPC Design Bridge currently asks users for Step 5-7 content and then accepts it directly into the skill output:

- Step 5: NPC gameplay function and remove-test results
- Step 6: behavior and state rules
- Step 7: dialogue samples

This can create intent drift. A user may provide a rough fragment, but the agent may silently treat it as final design intent. The skill also needs more visible TT expert integration for competition evaluation.

## Design

Add a visible clarification loop to Step 5-7:

1. The user provides a fragment.
2. The main agent asks a subagent or expert-review pass to refine the fragment while preserving intent.
3. The main agent presents a "current understanding" draft.
4. The draft includes a visible `TT Expert Review | Liu Zhejun AI Perspective` card.
5. The user either confirms or requests changes.
6. The loop repeats until the user confirms the understanding is correct.

The expert is visible, but does not take over the conversation. NPC Design Bridge remains the host and uses one consistent teaching-assistant voice.

## Expert Role

Use Liu Zhejun's AI perspective as a TT expert layer based on the provided expert plugin. The skill must describe this as an AI perspective based on public materials, not as the real person speaking.

The expert layer contributes:

- Step 5: game design education and core-loop necessity review
- Step 6: playable prototype and trigger/response feasibility review
- Step 7: gameplay-functional dialogue review
- Step 8-9: final collaboration notes for portfolio presentation

## UX Rules

- Keep each review card short: 2-4 bullets.
- Separate user-stated intent from expert inference.
- Mark uncertain additions with `[待确认]`.
- Ask for confirmation before treating Step 5, 6, or 7 as final.
- Let the user reject expert suggestions without penalty.

## Files To Update

- `SKILL.md`: add the general clarification-loop protocol, update Step 5-7, and make TT expert collaboration explicit.
- `prompts/system_prompt.md`: add global confirmation-loop and expert-card rules.
- `prompts/step_05_function_anchor.md`: add the Step 5 loop and expert review card.
- `prompts/step_06_behavior_rules.md`: add the Step 6 loop and expert review card.
- `prompts/step_07_dialogue_samples.md`: add the Step 7 loop and expert review card.
- `prompts/step_08_bible_assembly.md`: include TT expert collaboration notes in the final Bible.
- `templates/npc_design_bible_template.md`: add a collaboration-notes section.
- `docs/tt_collaboration_log.md`: replace the old "pending interface" with the new visible review-card protocol.
- `examples/tea_grandma_cozy_sim/skill_conversation.md`: show the loop in the example.
- `tests/edge_cases.md` and `tests/golden_cases.md`: document expected loop behavior.

## Success Criteria

- Step 5-7 no longer finalize rough user fragments without a confirmation turn.
- The TT expert integration is visible in interaction and final documentation.
- The expert is framed compliantly as "Liu Zhejun AI Perspective".
- Existing Bible validation still passes for the example.
