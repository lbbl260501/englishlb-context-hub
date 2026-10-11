"""Export inspectable teaching records from the canonical editorial Markdown."""
import json,re
from pathlib import Path
BASE=Path(__file__).resolve().parent
s=(BASE/'lesson.md').read_text(encoding='utf-8')
body,answers=s.split('# 答案与解析',1)
answer_text,appendix=answers.split('# 英中双语对照附录',1)
profiles=[]
for n,w,pos,content in re.findall(r'^### (\d{2})  (.+?)  (.+?)\n(.*?)(?=^### |^## |\Z)',body,re.M|re.S):
    fields=dict(re.findall(r'^\*\*(.*?)\*\*　(.*)$',content,re.M))
    examples=[]
    for j in (1,2):
        key=f'{n}-{j}'
        en=fields[f'例句 {key}']
        match=re.search(r'^\*\*'+key+r'\*\*　(.+?)  \n> (.+)$',appendix,re.M)
        assert match and match[1]==en,(key,'example/translation drift')
        examples.append({'id':key,'en':en,'zh':match[2]})
    profiles.append({'number':n,'headword':w,'pos':pos,'meaning':fields['这篇文章中的意思'],'location':fields['在真题里'],'collocations':fields['常用搭配'],'contrast':fields['义项辨析'],'reading_note':fields['读题提醒'],'usage':fields['用法再进一层'],'examples':examples})
assert len(profiles)==23
questions=[]
for m in re.finditer(r'^\*\*((?:D|V|M|I|T|P)\d{2}|[ABC][1-5])\.\*\*\s*(.*?)(?=^\*\*(?:(?:D|V|M|I|T|P)\d{2}|[ABC][1-5])\.\*\*|^#{1,3} |\Z)',body,re.M|re.S):
    q=m[1]
    ans=re.search(r'^\*\*'+q+r'(?: → ([A-D]))?\*\*　(.+)$',answer_text,re.M)
    assert ans,('missing answer',q)
    questions.append({'id':q,'question_markdown':m[2].strip(),'answer_letter':ans[1],'answer_and_explanation_zh':ans[2]})
assert len(questions)==56,len(questions)
sections=[]
for m in re.finditer(r'^(#{1,3}) (.+)\n(.*?)(?=^#{1,3} |\Z)',s,re.M|re.S):
    sections.append({'level':len(m[1]),'title':m[2],'body_markdown':m[3].strip()})
def save(name,data):
    (BASE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
save('vocabulary_profiles.json',profiles)
save('exercises.json',questions)
save('lesson_content.json',{'schema_version':1,'canonical_source':'lesson.md','material_boundary':'Exam commentary and links; original examples and exercises. No full exam republication.','sections':sections})
print('Exported 23 vocabulary profiles, 46 bilingual examples, 56 numbered exercises and full lesson sections.')
