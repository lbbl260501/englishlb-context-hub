# 从这里开始｜考研英语（一）讲义知识库

## 新会话阅读顺序
1. 读取 **CONTEXT_SNAPSHOT.md**、**AGENTS.md**、**docs/STUDENT_LESSON_STANDARD.md**。
2. 读取 **data/lessons.json**、**data/lexemes.json**、**data/exposures.json**，确认每册是否确实已发布、哪些词已经有主讲记录。
3. 读取相应教材单元的 **editorial/SOURCE_AUDIT.md**。
4. 规划时运行 `python scripts/audit.py`、`python scripts/plan_next.py --lesson L003`；更新数据后运行 `python scripts/build_snapshot.py`。不能在本环境执行时须明确说明，不要虚构检查完成。

## 当前待办
- L002《环境与生态》53页学生版PDF、LaTeX和Markdown已入库并回读核验，状态为 `published`。外部教师二审、学习者试用和实体打印仍待完成。
- L003《工作与职业》此前对话记载本地50页XeLaTeX版；完整PDF与源文件仍未入库，保持 `planned`，不得预先登记主讲。
- L003已登记28项候选新词及5项跨册复习；L002已登记23项不重复主讲和3项复习（regulate、resilient、subsequent）。
- 逐项取得并核验2027官方完整大纲词表；目前没有可计算的官方覆盖率与个人掌握率。

## 核心质量要求
学生教材必须从学习者角度编排，并与元数据、GitHub提交报告、来源审计和词表数据库分开；所有原创英文练习须有放在答案章节**之后**的英中对照附录。不要用旧的9页L002工作稿作为样板。

## 编写逻辑（优先）

教材创作开始前必须阅读 `docs/ENGLISH_I_EDITORIAL_BLUEPRINT.md`，再读 `docs/STUDENT_LESSON_STANDARD.md`。新纲领为全考研英语（一）的英语能力 × 文章理解 × 可观察命题考查逻辑，不应误读为“全部靠阅读技巧”。

## 2026-10-11 两册新源码已入库

L002与L003重塑版完整XeLaTeX/Markdown源码已经GitHub远程blob哈希核验，分别参见 `lessons/02-environment-ecology/student/L002_rebuilt_2026.tex` 与 `lessons/03-work-career/student/L003_rebuilt_2026.tex`。新PDF（36/39页）目前只有ChatGPT对话本地交付，GitHub未存新版PDF。L002原53页正式发布版保持不变，L003暂不发布也不计28候选词主讲。详情见 `docs/REBUILD_L002_L003_2026-10-11.md`。
