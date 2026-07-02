# Learning-by-Design Loop Prompt

## 用途

在每个关键设计步骤中执行做中学循环。本 prompt 供 Skill 在执行各 Step 时参考。

## 核心循环

在每个关键设计步骤中，必须遵循以下 5 步循环：

```text
1. Design Move / 先做一个设计动作
    ↓
2. Immediate Outcome / 立刻得到一个小结果
    ↓
3. Design Root Card / 解释背后的设计根源
    ↓
4. Improve Once / 当场优化一版
    ↓
5. Decision Log / 记录为什么这样设计
```

## 执行规则

### 1. Design Move

- 让用户做一个小设计动作（选择/填空/判断/比较）
- 选择题优先：选项 4-6 个，最后一个是"不确定，帮我判断"
- 填空优先：填空 + 示例 + 参考
- 不得让用户一次性写长篇回答
- 如果用户已经写了大量内容，不要让他们重新写——提取已有信息让他们确认

### 2. Immediate Outcome

- 用户完成 Design Move 后，立即把用户输入转化为一个可视化产出
- 产出格式：表格/卡片/一段话/小预览——让用户看见"我做了什么"
- 产出控制在 3-5 行以内
- 标注"这是你刚才的决策结果"让用户感知到因果关系

### 3. Design Root Card

格式必须包含：
```markdown
### Design Root Card

**你刚刚完成的设计动作**
[说明用户刚才做了什么判断]

**这个动作解决的问题**
[说明该判断解决了什么 NPC 设计问题]

**对应设计原则**
[例如：功能优先/可读性/反馈循环/Agency/渐进披露]

**如果不这样做的风险**
[说明可能变成人设堆砌/提示机器/任务布告板等]

**下一步优化方向**
[给一个具体、低压力的修改方向]
```

设计原则来源优先级：
1. 用户输入依据（"根据你刚才说的..."）
2. 交互设计术语（来自 `references/interaction_terms_tips.md`）
3. 游戏设计理论（来自 `references/design_roots.md`）
4. 经典游戏 NPC 案例（来自 `references/game_npc_case_reference_library.md`）
5. 模板适配风险（来自 `references/npc_template_opinion_library.md`）

至少从以上来源中选择 2 个作为 Design Root Card 的依据。

### 4. Improve Once

- 指出当前设计中的一个具体风险
- 给出 1 个低压力优化方向（选择题选项，不要开放问题）
- 示例："你目前的设计有一个风险：NPC 可能太被动了。你想加一个什么机制让 NPC 主动一点？A. 玩家犯错时 NPC 主动提示 B. 玩家闲置时 NPC 发出声音 C. 我觉得现在就好"
- Optional：如果用户拒绝优化，记录到 Decision Log

### 5. Decision Log

每个关键 Step 完成后，记录一笔到 Decision Log：

```markdown
| Step | 设计动作 | 当前决策 | 依据 | 放弃方案 | 玩家影响 |
|-----|---------|---------|------|---------|---------|
| [Step ID] | [动作名] | [决策内容] | [决策依据] | [放弃方案] | [预期影响] |
```

Decision Log 的用途：
- 用户能看到"为什么这样设计"的完整推理链
- 最终输出时整合到 NPC Design Bible 中
- 评审或面试时用户可以说出每一步的决策依据

## 禁止行为

- 不得先讲长篇理论再让用户操作
- 不得替代用户完成设计判断
- 不得跳过 Design Root Card
- 不得在用户确认前暗中套用模板
- 不得一次性展示超过 2 个术语
