# CONTEXT SNAPSHOT | 考研英语（一）词汇与阅读

> 由 scripts/build_snapshot.py 根据 data/*.json 生成；不要手工维护统计数字。

## 远程仓库已确认的事实

- 正式已归档/已发布讲义：1 册；历史样章：1 册。
- 已登记首次主讲的不同词汇单位：38 项。含历史样章；**不等于已掌握词数**。
- 学习者测验记录：0 条。未经测验不能推算个人掌握率。
- 大纲完整覆盖率：不可计算（官方全词表尚未导入并逐项核对）。

## 已归档讲义

- L001｜教育与学习｜词汇与阅读；状态 `imported`；登记主讲 24 项；PDF `lessons/01-education-learning/lesson-01-bilingual.pdf`。
- S001｜历史样章：科技、创新与规制；状态 `archived_sample`；登记主讲 14 项；PDF `lessons/00-legacy-sample/vocabulary-sample.pdf`。

## 待发布讲义（计划词不计已教）

- **L002｜环境与生态｜保护政策与野火管理**：新候选 23 项；历史已讲候选 0 项；已安排复习 3 项；当前未登记任何主讲。
  - 候选：filter, authority, scope, at odds with, repercussion, jurisdiction, shortsighted, transcend, runoff, call on, stakes, mandate, curb, peter out, compile, shortfall, suppression, testament, erode, ignite, prescribed, tactic, double-edged sword。
  - 复习/去重：regulate（S001）, resilient（L001）, subsequent（L001）。
  - 来源审校：lessons/02-environment-ecology/editorial/SOURCE_AUDIT.md。
  - 注：完整学生版已恢复并审校，本地53页PDF与可编辑LaTeX已验证。此内容提交仍保持planned；待推送远端校验后另行登记published和23项primary。
- **L003｜工作与职业｜学历信号与劳动保障**：新候选 28 项；历史已讲候选 0 项；已安排复习 5 项；当前未登记任何主讲。
  - 候选：weigh up, be found wanting, devalue, social mobility, inevitable, predecessor, committed, scrap, generalist, postgraduate, upskill, employable, trajectory, fulfillment, grievance, provision, dismissal, justify, procedural, safeguard, arbitrary, constrain, productivity, paradoxically, marginal, stringent, threshold, unwieldy。
  - 复习/去重：qualified（L001）, transition（L001）, incentive（L001）, regulate（S001）, consequence（S001）。
  - 来源审校：lessons/03-work-career/editorial/SOURCE_AUDIT.md。
  - 注：2022英语（一）Text 2与Text 4 已核验；本次本地生成50页XeLaTeX学生教材与完整可编辑源码，完整文件尚未远程存储，故暂维持planned；28项新候选未计主讲，5项旧词为复习，不推算大纲覆盖或个人掌握。

## 新会话读取与编写规则

1. 先读 START_HERE.md、AGENTS.md、docs/STUDENT_LESSON_STANDARD.md、本快照。
2. 再读 data/lessons.json、data/lexemes.json、data/exposures.json、对应册次的独立来源审计。
3. 真题、媒体题源、第三方转录、自编练习必须区分。原创英文练习必须有英中对照附录，位于答案之后。
4. 学生版不得混入版本、JSON、仓库操作等编辑资料；候选词不能预记主讲。
5. 如需更新：运行 python scripts/audit.py、python scripts/plan_next.py --lesson <ID>、python scripts/build_snapshot.py 并报告真实提交。
6. 只有远程仓库实际保存了完整教材源文件和PDF后，才能登记其出版状态；不能把本地生成等同于GitHub已发布。
