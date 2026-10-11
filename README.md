# English I Context Hub

远程仓库：https://github.com/lbbl260501/englishlb-context-hub

用途：个人考研英语学习与讲义编写。仓库保持公开，公开内容限于讲义、课程进度和项目规则；不保存私人测验明细、聊天标识或凭据。

考研英语（一）词汇与阅读讲义的长期上下文仓库。先读 [START_HERE.md](START_HERE.md)，再读 [CONTEXT_SNAPSHOT.md](CONTEXT_SNAPSHOT.md)。

本仓库从用户提供的快照、相关 ChatGPT 历史和下载目录中的实际 PDF 整理。保留出处，不把聊天中的结论自动当作已核验事实。

- 第一册：教育与学习，23 页双语 PDF，24 项主讲词。
- 历史样章：科技与规制，12 页 PDF，14 项主讲词，纳入去重。
- 第二册：环境生态，[53页双语PDF](lessons/02-environment-ecology/student/L002_student.pdf)及[可编辑LaTeX](lessons/02-environment-ecology/student/L002_student.tex)已发布；23项主讲、3项复习，3篇原创阅读和56道编号练习。
- 官方完整词表尚未导入；覆盖率和个人掌握率均不可计算。

## 继续使用

```sh
python scripts/audit.py
python scripts/plan_next.py
python scripts/build_snapshot.py
```

以上脚本只依赖 Python 3 标准库。PDF 原文件保持不变；没有替用户生成任何学习成绩。

ChatGPT 接续文案见 [CHAT_HANDOFF.md](CHAT_HANDOFF.md)，协作规则见 [AGENTS.md](AGENTS.md)，证据边界见 [docs/PROVENANCE.md](docs/PROVENANCE.md)。

## 讲义正文与编辑档案

学生教材只承担学习：背景、真题阅读任务、词汇、句法、练习、详解、答案后双语对照。项目工作记录、数据索引、核验说明置于仓库独立文档，不编译进学生讲义。见 [学生讲义标准](docs/STUDENT_LESSON_STANDARD.md)。

L002 旧九页稿已被学习者指出内容与组织问题，故不作为后续教材的质量范本。修订学生版已于2026-10-11完成远端文件回读核验并登记 published；全库61项已主讲词汇单位，不代表大纲覆盖或个人掌握。教师二审、学习者试用及实体打印仍待完成。

## L003｜工作与职业（2026-10-11）
已核验 2022 英语（一）Text 2（学历与职业发展）与Text 4（解雇保护与生产率），并建立 [独立来源审计](lessons/03-work-career/editorial/SOURCE_AUDIT.md)。
本次对话已本地编译50页学生用XeLaTeX讲义，含完整源文件及双语附录；**远程仓库尚未上传完整版PDF与.tex**。本仓库已登记28项待主讲新候选词、5项旧词复习，L003维持 `planned`，不能将候选误算为已教。具体状态见 [CONTEXT_SNAPSHOT.md](CONTEXT_SNAPSHOT.md)。
