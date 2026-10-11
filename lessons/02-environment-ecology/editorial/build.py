#!/usr/bin/env python3
"""Rebuild the learner-facing LaTeX PDF from L002 student Markdown.

Keeps editable LaTeX output; source Markdown is bundled for reproducibility.
Requires Pandoc and XeLaTeX with xeCJK and tcolorbox; Noto CJK and TeX Gyre fonts.
"""
from pathlib import Path
import subprocess
import re

BASE = Path(__file__).resolve().parent
MD = BASE / 'lesson.md'
TEMPLATE = BASE / 'template.tex'
import tempfile
TMP = tempfile.TemporaryDirectory()
BODY = Path(TMP.name) / 'body.tex'
OUTPUT = BASE.parent / 'student' / 'L002_student.tex'
PDF = BASE.parent / 'student' / 'L002_student.pdf'

s=MD.read_text(encoding='utf-8')
lines=s.splitlines()
assert lines[0].strip() == '# 环境与生态', 'Unexpected source title'
assert lines[2].strip() == '## 保护政策与野火管理', 'Unexpected subtitle'
assert len(re.findall(r'^###\s+\d{2}\s{2,}.+\s{2,}.+$',s, flags=re.M))==23
# Keep introductory text (not title repetition); retitle its chapter for natural course flow
start = next(i for i,line in enumerate(lines) if line.startswith('## 写在开始之前'))
newlines=[]
# Let Pandoc parse all paragraphs as Markdown. Wrap vocabulary profiles
# only in the *generated* LaTeX; raw LaTeX environments inserted directly
# into Markdown suppress markdown interpretation in Pandoc.
for i,line in enumerate(lines[start:]):
    if i == 0:
        line='# 导读｜开始学习之前'
    if line.startswith('**读题提醒**'):
        line=line.replace('**读题提醒**',r'\emphasislabel{读题提醒}',1)
    if line.startswith('**最容易读错的地方**'):
        line=line.replace('**最容易读错的地方**',r'\emphasislabel{最容易读错的地方}',1)
    # XeLaTeX Noto Serif has no default math-symbol font fallback.
    line=line.replace('→', r'$\rightarrow$').replace('≠',r'$\neq$')
    newlines.append(line)
processed=Path(TMP.name)/'_pandoc_input.md'
processed.write_text('\n'.join(newlines)+'\n',encoding='utf-8')

cmd=["pandoc",str(processed),"-f","markdown+raw_tex","-t","latex","--top-level-division=chapter","--wrap=none","--toc-depth=1","-o",str(BODY)]
subprocess.run(cmd,check=True)
body=BODY.read_text(encoding='utf-8')
# Pandoc 2 wraps headings in hypertarget; unwrap before inserting environments.
body=re.sub(r'\\hypertarget\{[^}]+\}\{%\n([^\n]+)\n', lambda m: m[1][:-1]+'\n', body)

# Format the 23 lexical subsections as genuine *breakable LaTeX boxes*.
# The body contents have already been translated to LaTeX by Pandoc.
profiles=[]
for n,word,pos in re.findall(r'^###\s+(\d{2})\s{2,}(.+?)\s{2,}(.+?)\s*$',s,flags=re.M):
    profiles.append((n,word,pos))
assert len(profiles)==23
for n,word,pos in profiles:
    pat=re.compile(r'\\subsection\{'+re.escape(f"{n} {word} {pos.replace('. ', '.~')}")+r'\}\\label\{[^}]+\}')
    body,k=pat.subn(lambda _: f'\\begin{{vocabbox}}{{{n}}}{{{word}}}{{{pos}}}',body,count=1)
    if k!=1:raise RuntimeError(f'Missing profile header: {n} {word} {pos}')
# Close a lexical profile before the next sectional heading.
for n,word,pos in reversed(profiles):
    opening=f'\\begin{{vocabbox}}{{{n}}}{{{word}}}{{{pos}}}'
    ix=body.index(opening)+len(opening)
    match=re.search(r'(?m)^\\(?:section|subsection|chapter)\{|^\\begin\{vocabbox\}',body[ix:])
    if not match:raise RuntimeError('Cannot locate the end of '+word)
    j=ix+match.start()
    body=body[:j]+'\\end{vocabbox}\n\n'+body[j:]
# The source appendix uses hard linebreak + a blockquote marker for translations.
# Pandoc correctly escapes the marker literally in that construction: reformat
# it as a subtle bilingual translation line instead of printing a stray >.
body,k=re.subn(r'(?m)^\\textgreater\{\} (.+)$',lambda m:r'\zhline{'+m.group(1)+'}',body)
assert k>=90, f'expected translations, got {k}'
assert '**这篇文章中的意思**' not in body
# Pandoc will render :: as ordinary punctuation. Typeset hyperlinked chapter/section only.
# Protect exercise block headings and ensure no giant whitespace caused by automatic top-level.
body=body.replace('\\hypertarget{', '\\hypertarget{')
# Keep a question stem with its answer choices; separate diagnostic work from guide.
body=body.replace(r'\section{开始前的4道小测}', r'\clearpage'+'\n'+r'\section{开始前的4道小测}')
body=re.sub(r'(?m)^(\\textbf\{(?:D\d{2}|[ABC][1-5]|M\d{2}|I\d{2})\.\})', lambda m:r'\Needspace{10\baselineskip}'+'\n'+m[1], body)
# Preserve each English/Chinese pair as one reading unit.
body=re.sub(r'(?m)^([^\n]+\\\\\n\\zhline\{[^\n]+\})$', lambda m:r'\begin{samepage}'+'\n'+m[1]+'\n'+r'\par\end{samepage}',body)
# A vocabulary heading must stay with its first bilingual example.
body=re.sub(r'(?m)^(\\textbf\{\d{2} [a-z][^}]*\})',lambda m:r'\Needspace{5\baselineskip}'+'\n'+m[1],body)
template=TEMPLATE.read_text(encoding='utf-8')
assert '@@BODY@@' in template
full=template.replace('@@BODY@@',body)
OUTPUT.write_text(full,encoding='utf-8')
(BASE.parent / 'student' / 'L002_student.md').write_text(s, encoding='utf-8')
print(f'Built {OUTPUT} (body {len(body)} chars)')
