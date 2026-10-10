from common import load, plan, write_text
from audit import audit
errors = audit()
if errors:
    raise SystemExit("\n".join(errors))
lessons = load("lessons")
words = load("lexemes")
completed = [x for x in lessons if x["status"] in ("imported", "published")]
legacy = [x for x in lessons if x["status"] == "archived_sample"]
primary = [w for w in words if w["primary_lesson"]]
_, new, repeated, review = plan()
snapshot = f"""# CONTEXT SNAPSHOT | 考研英语（一）讲义知识库

> 从 data/*.json 生成。修改原始数据后运行 python scripts/build_snapshot.py，不手工编辑本文件。

## 当前已归档

- 正式讲义：{len(completed)} 册；L001 教育与学习，23页双语PDF，24项主讲词。
- 历史样章：{len(legacy)} 册；S001 科技与规制，12页，14项主讲词，保留去重。
- 累计登记主讲词汇单位：{len(primary)} 项；不是个人掌握数量。
- 原PDF已导入；本次只核对词汇索引等选定页面，未全面重审答案及旧文中的论断。

## 下一步：L002 环境与生态

- 候选真题：2024 English I Reading Text 4；2026 English I Reading Text 4。
- 原快照24个候选中，未发现历史主讲的 {len(new)} 项：
  {", ".join(x["text"] for x in new)}。
- 候选重复 {len(repeated)} 项：{", ".join(x["text"] + "（已在" + x["primary_lesson"] + "主讲）" for x in repeated)}。
- 原计划复现：{", ".join(x["text"] for x in review)}。
- 先核对原文、选项及词义；所有候选均未计入已教。regulate 应改复习或有证据的新义项扩展。

## 长期规则

- 以具体真题文章问题组织讲义，避免受旧聊天题材框架干扰。
- 同一词汇单位主要精讲一次；复习、新义项分开记录。
- 自编英文练习配英中双语，对照附录放在答案后。
- 真题原卷、第三方转录、媒体题源、词典、自编内容分别标注。
- 官方完整词表尚未导入/逐项核验，官方大纲覆盖率不可计算。
- 个人测验记录：{len(load("assessments"))} 条；没有数据不得推断掌握率。

## 接续

读取 START_HERE.md、AGENTS.md、data/lessons.json、data/lexemes.json、data/exposures.json。
运行 python scripts/audit.py 和 python scripts/plan_next.py。
ChatGPT 接续提示见 CHAT_HANDOFF.md；保存与上传必须以实际文件、commit 为证据。
"""
write_text("CONTEXT_SNAPSHOT.md", snapshot)
print("Generated CONTEXT_SNAPSHOT.md")

