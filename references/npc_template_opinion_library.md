---
description: >
  15 个 NPC 模板的评估意见库。每个模板绑定相关术语、参考案例、主要风险
  和评估问题。用于 Skill 在推荐模板时提供透明、可追溯的依据。
source: >
  基于 interaction_design_template_library.md、game_npc_case_reference_library.md、
  interaction_terms_tips.md 和 design_roots.md 综合整理。
---

# NPC 模板评估意见库 / NPC Template Opinion Library

本文档为每个交互设计模板提供评估意见，包括术语关联、案例关联、风险标注和评估问题。

---

## T01 Guide NPC / 引导者 NPC

**related_terms**: Touchpoint, Cognitive Load, Progressive Disclosure
**reference_cases**: C008 Elden Ring Melina, C009 Alyx Vance
**reliability_level**: A

### 适合解决的问题
玩家在新环境/新系统中感觉迷失方向，需要指引而不被剥夺探索感。

### 设计根源
认知负荷理论——新玩家的工作记忆被新信息占据，需要一个外部导航来减少"保持方向"这个认知消耗。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Melina (Elden Ring) | 最小化存在，只在需要时出现 | FromSoftware 的"模糊叙事"不是所有游戏适用 |
| Alyx Vance (HL2) | 向前分配，引导方向 | Valve 的角色化程度需要大量交互点 |  

### 主要风险
- 太主动 → NPC 变成"提醒机器"
- 引导内容超过玩家认知负荷 → 玩家跳过
- 没有退出机制 → 玩家被强迫引导
- 引导结束后 NPC 消失 → 资源浪费

### 评估问题
1. 玩家可以拒绝引导吗？
2. 引导者在玩家熟练后会自然退场吗？
3. 引导者的存在降低了玩家的认知负荷还是增加了？

---

## T02 Pacing NPC / 节奏调节器 NPC

**related_terms**: Pacing, Feedback, Cognitive Load
**reference_cases**: C005 Merchant (RE4), C007 Trico (TLG), C010 Morte (PST)
**reliability_level**: A

### 适合解决的问题
玩家长期处于紧张/重复/疲劳状态，需要节奏缓冲点。

### 设计根源
Lazzaro (2004) 的 Four Keys —— 情绪体验需要差异化的节奏：紧张后的松弛让放松更有意义。没有节奏变化的游戏体验是平的。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| RE4 Merchant | 蓝火把 = Pacing 信号 | Merchant 也是商店接口 |
| Trico (TLG) | 互动节奏随信任提高而变化 | 延迟响应不是所有游戏可承受 |

### 主要风险
- 太被动 → 纯情绪装饰，无玩法功能
- 调节只改变情绪不改变行为
- 插入在错误的节奏点（正在高潮时打断）
- 玩家不知道 NPC 的节奏调节功能

### 评估问题
1. 这个 NPC 改变玩家行为还是只改变情绪？
2. 删除它后，核心循环的节奏感会变差吗？
3. 它是在正确的时间点提供缓冲吗？

---

## T03 Risk-Reward NPC / 风险交易者 NPC

**related_terms**: Mental Model, Feedback, Agency
**reference_cases**: C005 Merchant (RE4), C003 GLaDOS (Portal)
**reliability_level**: A

### 适合解决的问题
核心循环缺少有意义的资源决策，玩家的每次交易都缺少权重。

### 设计根源
Mental Model——玩家基于"公平交易"的预期进入交互。打破这个预期（制造信息不对称）产生张力，但不打破太多次（否则玩家不再信任交易）。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| RE4 Merchant | 升级 vs 新武器的取舍 | 不是所有游戏都有货币经济 |
| GLaDOS | 信息不对称设计 | GLaDOS 的欺诈性需要特定叙事支持 |

### 主要风险
- 总是最优选择 → 没有真正决策
- 风险不会实际出现 → 失去意义
- 玩家没有足够上下文判断风险 → 随机惩罚而非权衡
- 交易后没有恢复机制 → 单次失误代价过大

### 评估问题
1. 这个 NPC 的每个交易是否都有明确的取舍？
2. 玩家是否可以预判风险而不只是承受风险？
3. 如果玩家永远选择最安全的交易，这个 NPC 还有意义吗？

---

## T04 Relationship NPC / 关系推进者 NPC

**related_terms**: User Journey, Agency, Feedback
**reference_cases**: C002 Ellie (TLOU), C004 Wheatley (Portal 2), C008 Elden Ring Ranni
**reliability_level**: A

### 适合解决的问题
玩家与游戏世界缺少情感连接点——角色仅仅是功能提供者，缺少持续的关系变化。

### 设计根源
渐进关系设计：时间（持续暴露→情感积累）、互惠（双方有来有往→关系强化）、变化（关系有节点有波动→不是静态）。三个条件缺一不可。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Ellie | 关系的渐进推进，从不信任到信任 | Naughty Dog 的面部动画和表演投资巨大 |
| Wheatley | 完整的关系弧线（朋友→背叛） | "朋友变敌人"需要足够篇幅建立信任 baseline |
| Ranni (Elden Ring) | 分布式、跨区域的 NPC 支线 | 线性游戏中无法实现 |

### 主要风险
- 关系变化只体现在对话中（玩家行为没有被改变）
- 选择没有可感知的分支后果（伪 choice）
- 关系推进与核心玩法无关
- 推进太快（玩家还没建立连接关系已满级）

### 评估问题
1. 关系的变化能被玩家在游戏行为中感知（不仅是对话文本）吗？
2. 玩家有机会破坏/放弃这段关系吗？
3. 删除 NPC 后核心循环中情感部分损失了什么？

---

## T05 Lore Gateway NPC / 世界观入口 NPC

**related_terms**: Progressive Disclosure, Cognitive Load, Readability
**reference_cases**: C008 Elden Ring NPCs, C010 Morte (PST)
**reliability_level**: A

### 适合解决的问题
世界观信息量太大或散落在各处，玩家难以系统理解。

### 设计根源
Progressive Disclosure——信息分层释放。玩家每次接触 NPC 时只获得该阶段需要的信息，剩余信息在后续条件满足时解锁。防止一次性认知超载。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Elden Ring NPCs | 信息碎片化 + 环境线索 | 信息过于模糊可能让玩家困惑 |
| Morte (PST) | 对话深度分级 | PST 的文字量非常大 |

### 主要风险
- 一次性倾倒世界观信息 → 玩家记不住
- 信息触发条件过于苛刻 → 玩家错过
- 信息揭示和玩家进度脱钩 → 玩家觉得没意义
- NPC 只是"有声百科全书" → 失去角色感

### 评估问题
1. 玩家的进度是否影响 NPC 愿意说多少？
2. 世界观信息是否与玩家当前行为相关？
3. 信息揭示是否有节奏感而不只是进度解锁？

---

## T06 Gatekeeper NPC / 阻碍者 NPC

**related_terms**: Pacing, Cognitive Load, Feedback
**reference_cases**: C006 Xenomorph (Alien Isolation), C003 GLaDOS (Portal)
**reliability_level**: A

### 适合解决的问题
玩家进展太快，或缺少有意义的非战斗挑战。需要制造"通过的价值"。

### 设计根源
Pacing——内容的推进需要"快-慢-快"的节奏。Gatekeeper 在玩家和下一阶段之间制造缓冲区，让"通过"时的价值感大于直接放行。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Xenomorph | 作为流程中始终存在的"Gate" | 非恐怖项目中过度压迫 |
| GLaDOS | 测试室是 gate，完成才进入下一阶段 | 测试室结构需要大量关卡开发 | 

### 主要风险
- 阻碍理由牵强 → 玩家觉得"设计者故意拖时间"
- 只有一种通过方式 → 强行让玩家做某事
- Gatekeeper 被通过后不再有互动 → NPC 变成一次性锁
- 玩家备感挫折而非成就感

### 评估问题
1. 是否有至少 2 种通过 Gatekeeper 的方式？
2. 通过 Gatekeeper 后的"价值感"是否大于"直接放行"？
3. Gatekeeper 被通过后是否还有角色意义？

---

## T07 Merchant NPC / 资源交换者 NPC

**related_terms**: Mental Model, Feedback, Player Burden
**reference_cases**: C005 Merchant (RE4)
**reliability_level**: A

### 适合解决的问题
商店功能需要角色化，交易过程需要创造体验而非只是 UI 界面。

### 设计根源
Mental Model——玩家对"商人"已经有成熟心智模型。需要利用这个模型降低学习成本，但加入一个反差点制造独特性（如 RE4 Merchant 的和敌人同款眼睛）。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| RE4 Merchant | 安全区信号+个性+经济系统 | 交易品必须有取舍不是"越贵越好" |

### 主要风险
- 完全等价于 UI 商店 → NPC 没有存在价值
- 交易品没有取舍 → 玩家不做决策
- NPC 个性与游戏基调不符
- 商人位置太安全 → 失去了"危险状态下到达安全点"的奖励感

### 评估问题
1. 如果 NPC 被 UI 商店完全替代，玩家会损失什么体验？
2. 每次交易是否有取舍？
3. NPC 是否在正确的地点出现（与探索奖励挂钩）？

---

## T08 Silent Guide NPC / 非语言引导者 NPC

**related_terms**: Signifier, Affordance, Readability
**reference_cases**: C007 Trico (TLG), C012 Companion Cube (Portal)
**reliability_level**: A

### 适合解决的问题
需要非语言的引导方式，因为 NPC 不能说话（物种/设定/设计约束）。

### 设计根源
Affordance + Signifier——NPC 的动作本身成为信号：视线方向=玩家方向、后退=危险、放松=安全。玩家通过观察而不是听取来获得信息，保全了 player agency（玩家自己得出的结论）。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Trico (TLG) | 跨物种非语言信号系统 | 信任建立周期很长 |
| Companion Cube | 无反应的"角色"如何承载情感 | 需要特定的叙事框架支持 |

### 主要风险
- 信号太弱 → 玩家完全错过 NPC 的意图
- 信号噪音 → 玩家无法准确理解 NPC
- 玩家需要"学习"信号系统但没有足够教学场景
- 在快节奏场景中非语言信号失效

### 评估问题
1. 玩家需要多久学会 NPC 的信号系统？有没有低风险教学场景？
2. 非语言信号在游戏的嘈杂环境中是否仍然可见？
3. 是否有辅助手段（如环境提示）增强 NPC 的信号？

---

## T09 Companion NPC / 伙伴型 NPC

**related_terms**: Agency, Player Burden, Complementary Ability, Environmental Reactivity
**reference_cases**: C001 Elizabeth (BioShock Infinite), C002 Ellie (TLOU), C009 Alyx Vance (HL2)
**reliability_level**: A

### 适合解决的问题
长期流程需要陪伴、情绪连接和低干扰支持。但伙伴不能成为负担或替玩家完成游戏。

### 设计根源
Three Key Problems of Companions: (1) Player Burden——不能给玩家增加任务、(2) Player Agency——不能替代玩家决策、(3) Environmental Fit——不能破坏关卡/战斗设计。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Elizabeth | 补充性帮助 + 环境反馈 | 13 人跨职能团队不是标准配置 |
| Ellie | 从不 burden 玩家的跟随设计 | 需要大量 animation 和 navmesh 投资 |
| Alyx Vance | 向前分配 + 独立行动 | 主动型 NPC 需要关卡配合 |

### 主要风险
- NPC 太强 → 玩家觉得自己是旁观者
- NPC 太弱 → 只是跟随的挂件
- NPC 太吵 → 破坏探索节奏
- NPC 需要频繁保护 → 变成玩家负担
- NPC 没有删除价值 → 去掉不影响游戏

### 评估问题
1. 它是否有玩家没有的补充性能力？
2. 它是否保留了玩家的决策权？
3. 它是否改变玩家行为而不仅是剧情气氛？
4. 删除它后核心循环是否受损？

---

## T10 Environmental Reactor NPC / 环境反应型 NPC

**related_terms**: Environmental Reactivity, Feedback, Touchpoint
**reference_cases**: C001 Elizabeth (BioShock Infinite), C010 Morte (PST)
**reliability_level**: B

### 适合解决的问题
游戏世界缺少对玩家的"回应感"——玩家的行动没有在周围角色身上产生变化。

### 设计根源
Environmental Reactivity——NPC 对至少三类变化做出响应：环境变化（天气/时间/事件）、玩家行为（战斗/探索/对话）、游戏进度（主线/支线推进）。响应不必总是交互，有时"被看见"已经足够。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Elizabeth | 对环境的观察和反应 | 需要大量"标记点"系统支持 |
| Morte (PST) | 对不同场景有不同的对话反应 | 大量文字内容 |

### 主要风险
- 反应太弱 → 玩家注意不到
- 触发点太少 → 和静态 NPC 没区别
- 反应和 NPC 角色设定不一致
- 性能成本（过多的环境检测和行为切换）

### 评估问题
1. NPC 至少对多少种环境变化做出响应？
2. 玩家能否感知到 NPC 的变化（不是系统后台完成了）？
3. 响应是否增强了 NPC 的角色一致性？

---

## T11 Trickster NPC / 欺骗者 NPC

**related_terms**: Mental Model, Agency, Feedback, Error Recovery
**reference_cases**: C003 GLaDOS (Portal), C004 Wheatley (Portal 2)
**reliability_level**: B

### 适合解决的问题
玩家在可预测的安全交互中建立了信任，需要一个打破信任模式的事件来制造张力。

### 设计根源
Trust Baseline 理论——玩家与 NPC 建立信任需要 2-3 次一致的可预测交互。信任打破只需要 1 次。欺骗者的效力来源于信任 baseline 的高度，所以在游戏中期/后期才有效。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| GLaDOS | 信息不完整的持续张力 | 需要验证信息的机制 |
| Wheatley | 朋友→背叛的完整弧线 | 背叛需要玩家"共谋感" |

### 主要风险
- 欺骗没有可预测的模式 → 玩家觉得不公平
- 没有线索暗示背叛 → 玩家感到被"剧情杀死"
- 背叛发生在信任建立之前 → 没有 impact

### 评估问题
1. 欺骗发生前玩家是否有获得暗示的机会？
2. 如果玩家足够警觉，能否提前应对背叛？
3. 背叛后是否有恢复/追责选项？

---

## T12 Echo NPC / 回音 NPC

**related_terms**: Feedback, User Journey, Touchpoint
**reference_cases**: C008 Elden Ring Melina, C010 Morte (PST)
**reliability_level**: B

### 适合解决的问题
长时间游戏流程中玩家感觉不到自己的成长和变化。

### 设计根源
Feedback——玩家需要外部参照物来感知变化。Echo NPC 通过在不同时间点说不同的话来反映玩家状态变化。核心不是新信息，而是"看，你已经变了"的确认。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Melina (Elden Ring) | 只在玩家到达关键节点时出现 | 过于稀疏可能让玩家忘记 NPC |
| Morte (PST) | 对话深度随进程增加 | 需要大量对话内容投资 |

### 主要风险
- 出现间隔太长 → 玩家忘记 NPC
- 出现间隔太短 → 变得重复
- 对话内容不反映玩家实际选择 → 感觉模板化
- 回音 NPC 的功能完全可以被 UI 替代

### 评估问题
1. NPC 每次出现时是否有不同的内容而非模板填空？
2. 回音是否真的反映了玩家的变化？
3. 删除 NPC 后玩家是否缺少"进步感"？

---

## T13 Burden NPC / 负担型 NPC

**related_terms**: Player Burden, Agency, Feedback
**reference_cases**: C007 Trico (TLG), C012 Companion Cube (Portal)
**reliability_level**: B

### 适合解决的问题
在过度安全的游戏环境中，玩家需要"在乎的东西"和"失去的恐惧"。

### 设计根源
Ueda (Fumito Ueda, genDESIGN) 的设计原则："游戏的程序是规则，主角与负担型角色之间的互动才是情感载体。"负担不是疲劳——负担是可承受的压力，失去负担的恐惧大于负担本身。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Trico | 不完全服从创造了真实的关系感 | 不全服从的"度"很难把控制 |
| Companion Cube | 非角色的情感投射 | 6 条情感设计规则（Portal 设计） |

### 主要风险
- 负担太重 → 玩家想放弃 NPC
- 负担太轻 → 玩家不在乎 NPC
- 保护 NPC 的机制让人沮丧
- 没有"独立时刻"→ 负担必须伴随全程

### 评估问题
1. NPC 需要被保护的理由是否被玩家所接受？
2. 如果玩家选择放弃保护 NPC，游戏是否继续（而不是 game over）？
3. 负担是否在某个时间点减轻/解除？

---

## T14 Mirror NPC / 镜子型 NPC

**related_terms**: Feedback, Agency, User Journey
**reference_cases**: C010 Morte (PST), C011 HK-47 (KOTOR)
**reliability_level**: B

### 适合解决的问题
玩家做出的选择缺少总结和确认——没有外部参照让玩家"看到自己"。

### 设计根源
Feedback + Self-Reflection——玩家需要外部视角来认识自己的选择。Mirror NPC 不做价值判断，而是通过呈现玩家的行为模式让玩家自行反思。不是道德裁判，而是行为记录者。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Morte (PST) | 引导玩家反思的选择方式 | 需要大量分支对话支持 |
| HK-47 (KOTOR) | 用独特世界观反映玩家行为 | 极端立场需要幽默缓冲 |

### 主要风险
- 评价过于直白 → 说教感
- 评价不反映玩家实际选择 → 模板化
- 没有功能性影响 → 觉得不重要

### 评估问题
1. Mirror NPC 的反映是否基于玩家的实际行为数据？
2. 玩家是否可以选择不接受 Mirror NPC 的"反映"？
3. 除了对话中的信息提供以外，这个 NPC 还有别的作用吗？

---

## T15 Mentor NPC / 导师型 NPC

**related_terms**: Cognitive Load, Progressive Disclosure, Mental Model
**reference_cases**: C002 Ellie (TLOU), C009 Alyx Vance (HL2)
**reliability_level**: B

### 适合解决的问题
玩家需要掌握新技能/系统，但没有导师的教程体验是干涩的。

### 设计根源
Celia Hodent (2017) 的认知三阶段学习模型：(1) 无意识无能力——需要引导、(2) 有意识无能力——需要练习机会、(3) 有意识有能力——需要减少提示。导师的职责是帮助玩家从 1 走向 3，然后退场。

### 可参考案例
| 案例 | 可参考点 | 不应照抄 |
|------|---------|---------|
| Ellie (TLOU) | 教学与叙事整合 | 教学内容和角色深度绑定的成本 |
| Alyx Vance (HL2) | 在安全环境中演示新功能 | 纯粹的 demo + 独立练习模式 |

### 主要风险
- 导师在教学完成后仍存在 → 玩家不毕业
- 导师替玩家执行核心动作 → 玩家学不会
- 教学内容不是"通过做"而是"通过听"
- 导师存在时间和篇幅过长

### 评估问题
1. 导师是否在玩家掌握技能后自然退场/减少现身？
2. 教学方式是否以"玩家操作"而非"玩家阅读"为主？
3. 如果玩家已经是老手，导师的反应是否不同？
