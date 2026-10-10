# CONTEXT SNAPSHOT | 考研英语（一）讲义知识库

> 自动从 data/*.json 生成；**不要手工修改本文件**。事实以原始数据和具体来源为准。

## 长期目标与边界

- 对象：考研英语（一）词汇与阅读讲义，重点是真题语境与迁移训练，而不是泛泛的英语素材。
- 主题组织：主题域 → 子议题 → 具体文章要解决的问题 → 语言素材。
- 同一词汇单位只安排一次主要精讲；再次出现记为复习或新义项扩展。
- 所有自编英文练习应配英中双语对照，附录集中置于答案之后。
- 真题、第三方转录、原始媒体题源、自编例句必须明确区分。
- 尚未完成2027官方完整词表导入：不得声称掌握了约5500词中的某个精确比例。

## 已完成内容（有文件证据）

- L001 / 第1册：教育与学习｜词汇与阅读；24项精讲。文件：`lessons/01-education-learning/lesson-01-bilingual.pdf`。

## 接下来要做

- **L002（planned）**：环境与生态｜保护政策与野火管理。真题：2024 English I Reading Text 4；2026 English I Reading Text 4。
  - 候选新词 24 项：filter, authority, regulate, scope, at odds with, repercussion, jurisdiction, shortsighted, transcend, runoff, call on, stakes, mandate, curb, peter out, compile, shortfall, suppression, testament, erode, ignite, prescribed, tactic, double-edged sword。
  - 复现词 2 项：resilient, subsequent。
  - 完成前必须复核真实试卷语境、选项与词义；候选词不代表已经教过。

## 覆盖指标（基于已登记的资料，不是考试得分）

- 已出版：1册；拟编：1册。
- 已主讲独立词汇单位：24；规划候选：24。
- 已覆盖主题域：1/10；已覆盖具体问题：2/4。
- 官方大纲完整覆盖率：**尚不可计算**（缺官方词表；或尚未完成逐项核验）。
- 个人掌握情况：**尚无测验数据**；不能用讲义覆盖数量代替掌握数量。

## 新会话启动操作

1. 阅读 `START_HERE.md`、本文件、`AGENTS.md`。
2. 读取 `data/lessons.json`、`data/exposures.json`；如需选词，读取 `data/lexemes.json`。
3. 规划前运行 `python scripts/audit.py` 与 `python scripts/plan_next.py`（在可执行的本地环境）。
4. 完成一册：更新词汇、主题、来源、课程和复现记录，运行检查、生成本摘要，再合并到主分支。

详细规则：`docs/WORKFLOW.md`，数据含义：`docs/DATA_MODEL.md`。
