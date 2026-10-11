import argparse
from common import plan
parser = argparse.ArgumentParser()
parser.add_argument("--lesson", default="L002")
args = parser.parse_args()
lesson, new, repeated, review = plan(args.lesson)
print(lesson["id"], lesson["title"])
print("Candidate words without prior primary teaching:", len(new))
print(", ".join(w["text"] for w in new))
print("Previously taught candidates; use review or verified sense extension:", len(repeated))
for word in repeated:
    print("  ", word["text"], "->", word["primary_lesson"])
print("Already planned review:", ", ".join(w["text"] for w in review))
print("Lesson status:", lesson["status"])
if lesson["candidate_words"]:
    print("Candidates are not published primary records; consult the source and vocabulary audits.")
else:
    print("No pending candidate words in this lesson; consult primary/review records for published teaching.")

