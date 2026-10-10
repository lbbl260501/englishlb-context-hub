import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def load(name):
    return json.loads((ROOT / "data" / (name + ".json")).read_text(encoding="utf-8"))
def write_text(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")
def plan(lesson_id="L002"):
    lesson = next(x for x in load("lessons") if x["id"] == lesson_id)
    words = {x["id"]: x for x in load("lexemes")}
    new, repeated = [], []
    for wid in lesson["candidate_words"]:
        word = words[wid]
        (repeated if word["primary_lesson"] else new).append(word)
    return lesson, new, repeated, [words[x] for x in lesson["review_words"]]

