---
description: >
  9 个游戏设计理论来源及其在 NPC 设计中的转译。基于权威文献
  (MDA Framework, The Art of Game Design, Design of Everyday Things 等)
  和游戏设计学术界公认的理论体系。
source: >
  Robin Hunicke et al. (2004) AAAI; Jesse Schell (2008/2019) CRC Press;
  Ernest Adams (2014); Salen & Zimmerman (2004) MIT Press;
  Don Norman (1988/2013); Jakob Nielsen (1995); Janet Murray (1997);
  Celia Hodent (2017) CRC Press.
---

# 设计理论根源 / Design Roots

本文档收录 9 个游戏设计权威理论来源。每个条目将理论转译为 NPC 设计的可执行判断依据。

---

## MDA Framework — Mechanics, Dynamics, Aesthetics

**来源类型**: 游戏设计研究框架
**来源**: Robin Hunicke, Marc LeBlanc, Robert Zubek (2004, AAAI)

**核心观点**: 游戏可以从 Mechanics (机制)、Dynamics (动态)、Aesthetics (美学) 三层理解。设计者通过 Mechanics 影响 Dynamics，再形成 Aesthetics。玩家从 Aesthetics 出发，理解 Dynamics，推断 Mechanics。

**转译到 NPC 设计**: NPC 不能只看角色设定（Aesthetics/C 层），而要看她的行为机制（Mechanics/A 层）如何改变玩家动态（Dynamics/B 层），最终形成什么体验（Aesthetics/C 层）。NPC 设计的核心是从"她是谁"转为"她的机制如何改变玩家行为"。

**适用场景**: 核心循环分析、NPC 功能定位、删除测试、微型模拟游玩
**对应 Skill Step**: Step 4 核心循环、Step 5 功能定位、Step 9 作品集自检
**可靠性等级**: A — 学术界广泛引用，Game Developers Conference 验证

---

## The Art of Game Design: A Book of Lenses

**来源类型**: 游戏设计方法论
**来源**: Jesse Schell (2008/2019, CRC Press)

**核心观点**: 好的游戏设计需要从尽可能多的视角审视游戏。Schell 提供了 100+ 个"镜头"——每个镜头是一组问题，帮助设计师从不同角度审视设计。

**转译到 NPC 设计**: NPC 设计的每个决策可以拆解为不同"镜头"的提问：
- Essential Experience Lens: 这个 NPC 想要玩家体验什么？
- Endogenous Value Lens: NPC 提供的东西在游戏内有什么价值？
- Unification Lens: NPC 的行为是否和游戏整体体验一致？

**适用场景**: 全流程设计检查、设计决策验证、多角度评审
**对应 Skill Step**: Step 8 文档整合、Step 9 作品集自检
**可靠性等级**: A — 游戏设计领域的标准教材，CMU ETC 使用

---

## Fundamentals of Game Design

**来源类型**: 游戏设计教科书
**来源**: Ernest Adams (2014, 第三版)

**核心观点**: 游戏设计可以被分解为核心机制、叙事结构、用户体验、交互层和技术层五个相互关联的层面。每个层面都有可操作的设计标准和约束条件。

**转译到 NPC 设计**: NPC 是连接多个设计层面的节点——它同时属于核心机制（功能）、体验（叙事）、UX（交互方式）和技术（AI 行为）四个层面。在设计 NPC 时，必须在这四个层面的交叉处做决策。

**适用场景**: 架构设计、功能定位、技术约束评估
**对应 Skill Step**: Step 5 功能定位、Step 8 文档整合
**可靠性等级**: A — 标准教科书，多所大学使用

---

## Rules of Play: Game Design Fundamentals

**来源类型**: 游戏设计理论
**来源**: Katie Salen & Eric Zimmerman (2004, MIT Press)

**核心观点**: 游戏设计是"第二序设计"——设计者不直接创造玩家体验，而是创造规则，让玩家在规则中自行产生体验。这带来了游戏设计的核心挑战：Designer 只能控制规则，不能控制体验。

**转译到 NPC 设计**: NPC 是"第二序设计"的典型案例——你不能直接"让玩家感到温暖"，你只能设计 NPC 的行为规则，让玩家在规则交互中自行产生温暖感。这就是为什么行为规则表（Trigger → Response → Impact）比 NPC 的性格描述更接近游戏设计本质。

**适用场景**: 行为规则设计、玩家体验预测、设计验证
**对应 Skill Step**: Step 6 行为规则、Step 9 作品集自检
**可靠性等级**: A — 游戏研究领域的基础文献

---

## Nielsen's 10 Usability Heuristics

**来源类型**: 可用性工程
**来源**: Jakob Nielsen (1995, Nielsen Norman Group)

**核心观点**: 10 条启发式可用性评估标准，用于评估界面设计的易用性。虽然面向软件界面，但大部分启发式直接适用于游戏 UX。

**转译到 NPC 设计**:
- **系统状态可见性 (Visibility of System Status)** → NPC 需要在交互后提供即时反馈
- **用户控制和自由 (User Control and Freedom)** → 玩家可以取消/避免 NPC 交互
- **一致性和标准 (Consistency and Standards)** → 同类型 NPC 的行为逻辑一致
- **识别而非回忆 (Recognition rather than Recall)** → NPC 的功能应该被看到而非被记住
- **错误预防 (Error Prevention)** → NPC 不应该让玩家进入不可挽回的错误状态
- **帮助和文档 (Help and Documentation)** → NPC 本身应该提供帮助而非需要查外部文档

**适用场景**: NPC UX 评估、交互设计检查
**对应 Skill Step**: Step 3 接触点地图、Step 6 行为规则、Step 9 作品集自检
**可靠性等级**: A — HCI 和 UX 领域的标准规范

---

## Affordance & Signifier (The Design of Everyday Things)

**来源类型**: 交互设计理论
**来源**: Don Norman (1988/2013, Basic Books)

**核心观点**: Affordance（可供性）是指一个对象可以提供的交互可能性。Signifier（示能符号）是指示 affordance 存在的视觉/行为信号。两者共同作用是良好交互设计的核心。Perceived Affordance（用户认为自己能做的）比实际 affordance 更重要。

**转译到 NPC 设计**: 玩家看到一个 NPC 时，它在视觉、位置和行为上"看起来能做什么"决定了玩家是否愿意交互。一个 NPC 如果没有清晰的 signifier（发光、特殊音效、独特站位），玩家会把它当背景。一个 NPC 如果有 signifier 但没有可交互的 affordance，玩家会失望。

**适用场景**: 角色概念设计、接触点设计、可读性评估
**对应 Skill Step**: Step 2 角色概念卡、Step 3 接触点地图
**可靠性等级**: A — 交互设计的奠基理论

---

## Player Agency (Hamlet on the Holodeck)

**来源类型**: 互动叙事理论
**来源**: Janet Murray (1997, MIT Press)

**核心观点**: Agency 是用户在交互式环境中做出有意义的选择并看到这些选择产生可感知后果的能力。这是互动媒体区别于线性媒体的核心特征。Agency ≠ interactivity；interactivity 是"按按钮有响应"，agency 是"我的选择造成了可感知的不同结果"。

**转译到 NPC 设计**: NPC 是 agency 最容易受侵蚀的环节。当玩家被迫接受一个 NPC（不可拒绝）、被 NPC 替做决定（功能覆盖）、或选择没有可感知影响（伪 choice）时，player agency 就会被侵蚀。Guard: 不剥夺玩家决策权（玩家可以拒绝 NPC）、选择有可感知后果、"NPC 可以帮你但不能替你"。

**适用场景**: 功能定位评估、关系推进设计、选择后果设计
**对应 Skill Step**: Step 5 功能定位、Step 6 行为规则、Step 9 作品集自检
**可靠性等级**: A — 互动叙事领域的经典理论框架

---

## Progressive Disclosure

**来源类型**: UX 设计模式
**来源**: Nielsen Norman Group (2006); Sweller Cognitive Load Theory (1988)

**核心观点**: 将信息分层展示，先提供最必要的信息，进阶细节在用户需要时再展开。初次用户只看到"摘要"，高级用户看到"全部"。核心目标是将用户的认知负荷降低到工作记忆容量（~4 chunks）以下。

**转译到 NPC 设计**: NPC 的信息、功能和情感深度不应该在第一次见面时全部展示。玩家的每次交互应该揭示下一层：第 1 次见面→核心功能；第 2-3 次→角色背景；第 4-5 次→隐藏深度；条件达成→特殊回应。分层释放比一次性倾倒更容易让玩家记住，也创造了"发现"的乐趣。

**适用场景**: 对话设计、世界观揭示、功能释放节奏
**对应 Skill Step**: Step 3 接触点地图、Step 7 对话样例、Step 5 功能定位
**可靠性等级**: A — UX 设计和认知科学的标准工作方式

---

## The Gamer's Brain: How Neuroscience and UX Design Impact Game Design

**来源类型**: 游戏 UX 认知科学
**来源**: Celia Hodent (2017, CRC Press)

**核心观点**: 游戏体验本质上受限于人类大脑的工作方式。具体有三个关键瓶颈：Perception（玩家看到了吗？）、Attention（玩家注意到了吗？）、Memory（玩家记住了吗？）。游戏的 UX 和教程设计必须在这三个认知层面的约束下工作。

**转译到 NPC 设计**: NPC 的教学/引导功能必须遵循感知-注意-记忆的认知路径。不要假设玩家自动感知到 NPC（用 signifier 解决）、不要假设玩家会注意 NPC（用位置和行为引导注意力）、不要假设玩家记住了 NPC 的功能（用渐进式重复强化记忆）。在 NPC 首次出现时，应该在低认知负荷环境中让玩家学习如何与其互动。

**适用场景**: 新手引导、NPC 教程功能、接触点密度优化
**对应 Skill Step**: Step 1 体验定锚、Step 4 核心循环、Step 9 作品集自检
**可靠性等级**: A — 认知科学和游戏 UX 交叉领域的体系化理论
