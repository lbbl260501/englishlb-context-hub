# English I Context Hub

远程仓库：https://github.com/lbbl260501/englishlb-context-hub

用途：个人考研英语学习与讲义编写。仓库保持公开，公开内容限于讲义、课程进度和项目规则；不保存私人测验明细、聊天标识或凭据。

考研英语（一）词汇与阅读讲义的长期上下文仓库。先读 [START_HERE.md](START_HERE.md)，再读 [CONTEXT_SNAPSHOT.md](CONTEXT_SNAPSHOT.md)。

本仓库从用户提供的快照、相关 ChatGPT 历史和下载目录中的实际 PDF 整理。保留出处，不把聊天中的结论自动当作已核验事实。

- 第一册：教育与学习，23 页双语 PDF，24 项主讲词。
- 历史样章：科技与规制，12 页 PDF，14 项主讲词，纳入去重。
- 第二册：环境生态，24 项原候选、2 项复现；其中 regulate 已在历史样章精讲。
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

L002 旧九页稿已被学习者指出内容与组织问题，故不作为后续教材的质量范本。修订学生版在确认完整源文件与成品实际上传仓库以前，L002 仍然保留 planned，历史38项主讲统计不变。
