# CONTEXT SNAPSHOT | 考研英语（一）讲义知识库

> 从 data/*.json 生成。修改原始数据后运行 python scripts/build_snapshot.py，不手工编辑本文件。

## 当前已归档

- 正式讲义：1 册；L001 教育与学习，23页双语PDF，24项主讲词。
- 历史样章：1 册；S001 科技与规制，12页，14项主讲词，保留去重。
- 累计登记主讲词汇单位：38 项；不是个人掌握数量。
- 原PDF已导入；本次只核对词汇索引等选定页面，未全面重审答案及旧文中的论断。

## 本次进展（2026-10-10）

- L002 2024与2026英语一 Text 4 的语境、36–40题选项与非官方参考答案已交叉核对，见 `lessons/02-environment-ecology/SOURCE_AUDIT.md`。
- GitHub 已保存简版可编辑工作稿 `lessons/02-environment-ecology/LESSON_DRAFT.md`；完整Markdown与9页PDF在当前聊天中生成，**未同步仓库**。
- L002依旧为 `planned`；23项候选新词无任何 primary 记录；旧S001的 `regulate` 与L001的 `resilient`、`subsequent` 只能作为复习。
- 完整资料入仓库后，需运行审计、人工检查PDF，再更新出版与曝光记录。不能推算官方大纲覆盖率、个人掌握率。

## 下一步：L002 环境与生态

- 候选真题：2024 English I Reading Text 4；2026 English I Reading Text 4。
- 原快照24个候选中，未发现历史主讲的 23 项：
  filter, authority, scope, at odds with, repercussion, jurisdiction, shortsighted, transcend, runoff, call on, stakes, mandate, curb, peter out, compile, shortfall, suppression, testament, erode, ignite, prescribed, tactic, double-edged sword。
- 候选重复 1 项：regulate（已在S001主讲）。
- 原计划复现：resilient, subsequent。
- 原文、选项及语境已初步交叉核验（来源审计见L002）；所有候选仍未计入已教。regulate 应改复习。

## 长期规则

- 以具体真题文章问题组织讲义，避免受旧聊天题材框架干扰。
- 同一词汇单位主要精讲一次；复习、新义项分开记录。
- 自编英文练习配英中双语，对照附录放在答案后。
- 真题原卷、第三方转录、媒体题源、词典、自编内容分别标注。
- 官方完整词表尚未导入/逐项核验，官方大纲覆盖率不可计算。
- 个人测验记录：0 条；没有数据不得推断掌握率。

## 接续

读取 START_HERE.md、AGENTS.md、data/lessons.json、data/lexemes.json、data/exposures.json。
运行 python scripts/audit.py 和 python scripts/plan_next.py。
ChatGPT 接续提示见 CHAT_HANDOFF.md；保存与上传必须以实际文件、commit 为证据。
