# 从这里开始｜考研英语（一）讲义知识库

## 新会话阅读顺序
1. 读取 **CONTEXT_SNAPSHOT.md**、**AGENTS.md**、**docs/STUDENT_LESSON_STANDARD.md**。
2. 读取 **data/lessons.json**、**data/lexemes.json**、**data/exposures.json**，确认每册是否确实已发布、哪些词已经有主讲记录。
3. 读取相应教材单元的 **editorial/SOURCE_AUDIT.md**（L002源审计可能在教材根目录）。
4. 规划时运行 `python scripts/audit.py`、`python scripts/plan_next.py --lesson L003`；更新数据后运行 `python scripts/build_snapshot.py`。不能在本环境执行时须明确说明，不要虚构检查完成。

## 当前待办
- L002《环境与生态》本地46页XeLaTeX版，L003《工作与职业》本地50页XeLaTeX版都已在各自对话中交付，但其**最终完整PDF和源文件均尚未同步到GitHub**。当前远程保持 `planned`、主讲未登记，禁止提前计覆盖。
- L003已登记28项候选新词及5项跨册复习；L002已登记23项不重复新候选，regulate 属S001主讲词需复习。
- 逐项取得并核验2027官方完整大纲词表；目前没有可计算的官方覆盖率与个人掌握率。

## 核心质量要求
学生教材必须从学习者角度编排，并与元数据、GitHub提交报告、来源审计和词表数据库分开；所有原创英文练习须有放在答案章节**之后**的英中对照附录。不要用旧的9页L002工作稿作为样板。
