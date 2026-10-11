# CONTEXT SNAPSHOT | 考研英语（一）词汇与阅读

本文件是依据最新 `data/*.json` 记录整理的接续摘要；`scripts/build_snapshot.py` 已改为遍历全部讲义。需要在完整克隆的仓库执行该脚本再次生成并校验。

## 远程仓库已确认的事实

- 正式已归档/已发布讲义：1 册；历史样章：1 册。
- 已登记首次主讲的不同词汇单位：38 项。包含历史样章，不等于已掌握词数。
- 学习者测验记录：0 条；未经测验不推算掌握率。
- 官方完整词表：尚未导入；不能计算大纲精确覆盖率。

## 已归档讲义

- L001｜教育与学习｜词汇与阅读；状态 `imported`；登记主讲 24 项；PDF `lessons/01-education-learning/lesson-01-bilingual.pdf`。
- S001｜历史样章：科技、创新与规制；状态 `archived_sample`；登记主讲 14 项；PDF `lessons/00-legacy-sample/vocabulary-sample.pdf`。

## 待发布讲义（候选词不计已教）

- **L002｜环境与生态｜保护政策与野火管理**：新候选 23 项；已讲候选 1 项；额外安排复习 2 项；无本册主讲记录。
  - 新候选：filter, authority, scope, at odds with, repercussion, jurisdiction, shortsighted, transcend, runoff, call on, stakes, mandate, curb, peter out, compile, shortfall, suppression, testament, erode, ignite, prescribed, tactic, double-edged sword。
  - 复习/去重：regulate（S001）, resilient（L001）, subsequent（L001）。
  - 试卷与题源核验：`lessons/02-environment-ecology/SOURCE_AUDIT.md`。
  - 真题、答案、选词和题源交叉核验记录已入仓库；23项候选新词均未登记主讲，regulate 已在 S001 主讲应复习。完整Markdown与9页PDF在本次会话文件中生成，尚未同步GitHub；仓库仅有简版工作稿，status仍为planned。
- **L003｜工作与职业｜学历信号与劳动保障**：新候选 28 项；已讲候选 0 项；额外安排复习 5 项；无本册主讲记录。
  - 新候选：weigh up, be found wanting, devalue, social mobility, inevitable, predecessor, committed, scrap, generalist, postgraduate, upskill, employable, trajectory, fulfillment, grievance, provision, dismissal, justify, procedural, safeguard, arbitrary, constrain, productivity, paradoxically, marginal, stringent, threshold, unwieldy。
  - 复习/去重：qualified（L001）, transition（L001）, incentive（L001）, regulate（S001）, consequence（S001）。
  - 试卷与题源核验：`lessons/03-work-career/editorial/SOURCE_AUDIT.md`。
  - 2022英语（一）Text 2与Text 4 已核验；本次本地生成50页XeLaTeX学生教材与完整可编辑源码，完整文件尚未远程存储，故暂维持planned；28项新候选未计主讲，5项旧词为复习，不推算大纲覆盖或个人掌握。

## 编辑与学习的长期规则

1. 学生讲义必须独立成教材：真题伴读、词汇精讲、句法、原创阅读、训练、答案以及放在答案后的英中对照附录。
2. 原卷、第三方转录、原刊题源与原创内容分别标明；教学不依赖以往聊天的未经验证判断。
3. 已归档主讲词、计划新词、复习词严格分离；发布前不增加 primary exposures；无真实测验不得推算个人掌握。
4. 规划或修改前先读本文件与 `data/lessons.json` / `data/lexemes.json` / `data/exposures.json`，后读 `docs/STUDENT_LESSON_STANDARD.md`。
5. 在完整仓库执行 `python scripts/audit.py`、`python scripts/plan_next.py --lesson L003`、`python scripts/build_snapshot.py`，并确认 PDF/source 远程文件存在后才能记为发布。
6. L002已有46页本地 LaTeX 版，L003已有50页本地 LaTeX 版；**截至本次修改，两份最终 PDF/.tex 均尚未写入 GitHub 仓库**，不能将其视为远程已归档教材。
