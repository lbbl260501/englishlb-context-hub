"""Check references, duplicate primary teaching, artifacts and coverage prerequisites."""
import hashlib
import sys
from collections import Counter
from common import ROOT, load

def audit():
    errors = []
    tables = {n: load(n) for n in ("lessons", "lexemes", "themes", "problems", "sources")}
    for name, rows in tables.items():
        ids = [x["id"] for x in rows]
        if len(set(ids)) != len(ids):
            errors.append(f"Duplicate IDs: {name}")
    lessons = {x["id"]: x for x in tables["lessons"]}
    words = {x["id"]: x for x in tables["lexemes"]}
    sources = {x["id"] for x in tables["sources"]}
    themes = {x["id"] for x in tables["themes"]}
    problems = {x["id"] for x in tables["problems"]}
    primary = []
    for lesson in lessons.values():
        if lesson["theme"] not in themes:
            errors.append(f"Unknown theme: {lesson['id']}")
        if not set(lesson["source_ids"]) <= sources or not set(lesson["problem_ids"]) <= problems:
            errors.append(f"Unknown source/problem: {lesson['id']}")
        for field in ("primary_words", "candidate_words", "review_words"):
            if not set(lesson[field]) <= words.keys():
                errors.append(f"Unknown word: {lesson['id']}/{field}")
            if len(set(lesson[field])) != len(lesson[field]):
                errors.append(f"Duplicate word: {lesson['id']}/{field}")
        if lesson["status"] == "planned" and lesson["primary_words"]:
            errors.append(f"Planned lesson marked taught: {lesson['id']}")
        if lesson["pdf"] and not (ROOT / lesson["pdf"]).is_file():
            errors.append(f"Missing PDF: {lesson['pdf']}")
        for wid in lesson["primary_words"]:
            primary.append((lesson["id"], wid))
            if wid in words and words[wid]["primary_lesson"] != lesson["id"]:
                errors.append(f"Inconsistent primary assignment: {wid}")
    for wid, count in Counter(w for _, w in primary).items():
        if count > 1:
            errors.append(f"Duplicate primary teaching: {wid}")
    recorded = []
    for exp in load("exposures"):
        if exp["lesson_id"] not in lessons or exp["lexeme_id"] not in words:
            errors.append("Unknown exposure reference")
        if exp["kind"] not in ("primary", "review", "sense_extension"):
            errors.append("Invalid exposure kind")
        if exp["kind"] == "sense_extension" and not exp.get("sense_note"):
            errors.append("Sense extension requires sense_note")
        if exp["kind"] == "primary":
            recorded.append((exp["lesson_id"], exp["lexeme_id"]))
        if exp.get("mastery_inferred"):
            errors.append("Teaching does not establish mastery")
    if Counter(recorded) != Counter(primary):
        errors.append("Primary exposures disagree with lessons")
    for word in words.values():
        if word["primary_lesson"] and (word["primary_lesson"], word["id"]) not in primary:
            errors.append(f"Unbacked primary assignment: {word['id']}")
    for item in load("artifacts"):
        path = ROOT / item["path"]
        if not path.is_file():
            errors.append(f"Missing artifact: {item['path']}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            errors.append(f"Artifact changed: {item['path']}")
    syllabus = load("syllabus")
    if syllabus["denominator"] is not None and not (
        syllabus["official_list_imported"] and syllabus["item_mapping_verified"]
        and syllabus["denominator"] == len(syllabus["entries"])
    ):
        errors.append("Unsupported official syllabus denominator")
    return errors

if __name__ == "__main__":
    errors = audit()
    for error in errors:
        print("ERROR:", error)
    if not errors:
        print("PASS: references, primary teaching records, PDF hashes and coverage prerequisites")
    sys.exit(bool(errors))

