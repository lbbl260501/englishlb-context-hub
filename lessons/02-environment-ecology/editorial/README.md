# L002 编辑与构建

学生成品是 `../student/L002_student.pdf`，可直接编辑的完整LaTeX为 `../student/L002_student.tex`；同目录也提供学生Markdown。

## 内容来源与修改入口

`lesson.md`是教材正文的权威编辑底本。`build.py`配合`template.tex`生成独立、完整的学生LaTeX和Markdown。词汇、练习及全章节JSON由`export_content.py`提取，避免英文例句和中译分别修改后漂移。`reading_c.json`单独保留新增阅读的逐段双语及题目字段；修改C时须同步此文件。管理数据不参与编译。

## 编译

依赖Python 3、Pandoc、XeLaTeX、xeCJK、tcolorbox、enumitem、titlesec、fancyhdr、hyperref等常用TeX包，中文字体Noto Serif CJK SC与Noto Sans CJK SC，西文字体Latin Modern。TeX Live完整版配合上述字体即可。Linux可安装texlive-xetex、texlive-lang-chinese、texlive-latex-extra、fonts-noto-cjk；具体包名依系统而异。Overleaf须选择XeLaTeX并配置相同字体，未在Overleaf实测。

从仓库根目录运行：

```sh
python lessons/02-environment-ecology/editorial/export_content.py
python lessons/02-environment-ecology/editorial/build.py
mkdir -p build/L002
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build/L002 lessons/02-environment-ecology/student/L002_student.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build/L002 lessons/02-environment-ecology/student/L002_student.tex
cp build/L002/L002_student.pdf lessons/02-environment-ecology/student/L002_student.pdf
python scripts/audit.py
python scripts/plan_next.py
python scripts/build_snapshot.py
```

本次环境为TeX Live 2023、Pandoc 2；缺少的xeCJK 3.9.1与Noto字体从其上游Git仓库取得，只用于本地编译，没有将第三方依赖源码打包入本仓库。PDF字体已嵌入。模板使用标准report+xeCJK，避免要求某一特定ctex文类版本。

直接修改学生`.tex`也可编译，但再次运行build.py将覆盖它；长期维护应先改`lesson.md`/`template.tex`。生成PDF后须重新检查分页、文字溢出及对应答案；`export_content.py`不是语言答案正确性的自动证明。QA见`QA.md`。
