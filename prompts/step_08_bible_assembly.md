# Step 08: 文档整合 (Bible Assembly)

## 目标

将 Step 1-7 的产出按 NPC Design Bible 固定结构合并，生成完整的可展示文档。

## 执行流程

### 合并操作

Skill 自动从 Step 1-7 的产出中提取内容，填入 NPC Design Bible 模板：

```markdown
# NPC Design Bible: [NPC 名称]

## 1. Project Experience Goal
[来自 Step 1 的体验目标句 + 游戏类型]

## 2. NPC One-Line Pitch
[自动生成一句话介绍：角色 + 游戏类型 + 核心功能]
> 示例：温柔老奶奶是治愈经营类游戏中的"节奏调节器"型 NPC，她在玩家迷失目标时通过对话和小任务帮助玩家重新找到方向。

## 3. Character Concept Card
[来自 Step 2 的三格概念卡]

## 4. Player Touchpoint Map
[来自 Step 3 的接触点地图]

## 5. Core Gameplay Loop
[来自 Step 4 的核心循环描述]

## 6. NPC Gameplay Function
[来自 Step 5 的功能声明 + 删除测试结果]

## 7. Behavior & State Rules
[来自 Step 6 的行为规则表]

## 8. Dialogue Samples
[来自 Step 7 的对话样例]

## 9. Design Decisions & Iteration Log
[Skill 自动记录的设计决策汇总]
```

### 确认与调整

> 以上是完整的 NPC Design Bible 初稿。浏览一下，有什么地方需要修改吗？
> 你可以：
> - 修改任何章节的内容
> - 补充遗漏的细节
> - 调整顺序
> - 没有问题，进入下一步

## 输出格式

完整的 NPC Design Bible Markdown 文档。

## 通过标准

- 所有来自 Step 1-7 的必填字段已填入
- 文档能被他人独立阅读和理解
- 用户确认了内容或提出了修改

## 不通过处理

- 如果有步骤缺失 → 回到对应步骤补充：
  > [X 章节] 目前还缺少 [Y 内容]。要不要回到对应步骤补充一下？或者我根据已有内容帮你推断一个初稿，你再修改？
