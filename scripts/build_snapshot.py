"""Generate a neutral, lesson-agnostic cross-chat project snapshot from data/*.json.

Never count candidate teaching as primary exposure; do not infer learner mastery.
Run audit before writing, so any broken references or artifact hashes fail closed.
"""
from common import load, plan, write_text
from audit import audit

errors = audit()
if errors:
    raise SystemExit("\n".join(errors))

lessons = load("lessons")
lexemes = load("lexemes")
assessments = load("assessments")
syllabus = load("syllabus")
primary = [w for w in lexemes if w.get("primary_lesson")]
published = [l for l in lessons if l["status"] in ("imported", "published")]
legacy = [l for l in lessons if l["status"] == "archived_sample"]
pending = [l for l in lessons if l["status"] == "planned"]

lines = [
    "# CONTEXT SNAPSHOT | 考研英语（一）词汇与阅读",
    "",
    "> 由 scripts/build_snapshot.py 根据 data/*.json 生成；不要手工维护统计数字。",
    "",
    "## 远程仓库已确认的事实",
    "",
    f"- 正式已归档/已发布讲义：{len(published)} 册；历史样章：{len(legacy)} 册。",
    f"- 已登记首次主讲的不同词汇单位：{len(primary)} 项。含历史样章；**不等于已掌握词数**。",
    f"- 学习者测验记录：{len(assessments)} 条。未经测验不能推算个人掌握率。",
    "- 大纲完整覆盖率：" + ("需后续审计后使用" if syllabus.get("official_list_imported") and syllabus.get("item_mapping_verified") else "不可计算（官方全词表尚未导入并逐项核对）。"),
    "",
    "## 已归档讲义",
    "",
]
for l in published + legacy:
    lines.append(f"- {l['id']}｜{l['title']}；状态 `{l['status']}`；登记主讲 {len(l['primary_words'])} 项；PDF `{l.get('pdf') or '未登记'}`。")

lines.extend(["", "## 待发布讲义（计划词不计已教）", ""])
for l in pending:
    _, new, repeated, review = plan(l["id"])
    lines.append(
        f"- **{l['id']}｜{l['title']}**：新候选 {len(new)} 项；历史已讲候选 {len(repeated)} 项；已安排复习 {len(review)} 项；当前未登记任何主讲。"
    )
    if new:
        lines.append("  - 候选：" + ", ".join(w["text"] for w in new) + "。")
    if repeated or review:
        seen = []
        for w in repeated + review:
            if w["id"] not in [x["id"] for x in seen]:
                seen.append(w)
        lines.append("  - 复习/去重：" + ", ".join(w["text"] + "（" + str(w["primary_lesson"]) + "）" for w in seen) + "。")
    if l.get("source_audit"):
        lines.append("  - 来源审校：" + l["source_audit"] + "。")
    if l.get("note"):
        lines.append("  - 注：" + l["note"])

lines.extend(["", "## 重塑版源文件（与现行教材发布记录分开）", ""])
for lesson in lessons:
    rebuilt = lesson.get("rebuilt_edition")
    if rebuilt:
        lines.append(
            f"- {lesson['id']}：学生可编辑源文件 `{rebuilt['tex']}` / `{rebuilt['markdown']}` 已入库核验；"
            f"重塑版PDF {rebuilt['local_pdf_pages']}页，目前**尚未入库**；"
            f"该册的正式发布状态仍为 `{lesson['status']}`。"
        )

lines += [
    "",
    "## 新会话读取与编写规则",
    "",
    "1. 先读 START_HERE.md、AGENTS.md、docs/STUDENT_LESSON_STANDARD.md、本快照。",
    "2. 再读 data/lessons.json、data/lexemes.json、data/exposures.json、对应册次的独立来源审计。",
    "3. 真题、媒体题源、第三方转录、自编练习必须区分。原创英文练习必须有英中对照附录，位于答案之后。",
    "4. 学生版不得混入版本、JSON、仓库操作等编辑资料；候选词不能预记主讲。",
    "5. 如需更新：运行 python scripts/audit.py、python scripts/plan_next.py --lesson <ID>、python scripts/build_snapshot.py 并报告真实提交。",
    "6. 只有远程仓库实际保存了完整教材源文件和PDF后，才能登记其出版状态；不能把本地生成等同于GitHub已发布。",
    "",
]

write_text("CONTEXT_SNAPSHOT.md", "\n".join(lines))
print("Generated CONTEXT_SNAPSHOT.md for", len(lessons), "lessons")
