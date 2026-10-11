# 编译两册重塑版 LaTeX 学生讲义

本文件是**编辑/编译说明**，不是学生教材。学生版不得插入 GitHub 状态、来源审计或编译工具说明。

## 可编辑全量源码（已入GitHub并用本地Git blob哈希核对）

| 课程 | XeLaTeX 完整源码 | Markdown 完整学习正文 | 本地PDF |
|---|---|---|---|
| L002 环境与生态 | [L002 tex](../lessons/02-environment-ecology/student/L002_rebuilt_2026.tex) | [L002 Markdown](../lessons/02-environment-ecology/student/L002_rebuilt_2026.md) | 36页；尚未提交新版PDF二进制 |
| L003 工作与职业 | [L003 tex](../lessons/03-work-career/student/L003_rebuilt_2026.tex) | [L003 Markdown](../lessons/03-work-career/student/L003_rebuilt_2026.md) | 39页；尚未提交新版PDF二进制 |

L002 旧版53页 PDF **仍然是仓库里当前正式发布的二进制文件**，不得误认为已经由新36页PDF取代。L003 状态为 planned，28项新词尚未登记为主讲或掌握。

## 本地编译

两份源码是**完整独立可编译的 .tex 文件**，无需回到 Markdown/Pandoc 重新生成。推荐 XeLaTeX / latexmk，系统需要 TeX Live 的 CTeX、xeCJK、tcolorbox、titlesec、fancyhdr、geometry 等 LaTeX 宏包，以及 Noto Serif / Noto Sans / Noto Serif CJK SC / Noto Sans CJK SC 字体。

在仓库根目录运行：

```bash
mkdir -p /tmp/english1-rebuilt
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/english1-rebuilt \
  lessons/02-environment-ecology/student/L002_rebuilt_2026.tex

latexmk -xelatex -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/english1-rebuilt \
  lessons/03-work-career/student/L003_rebuilt_2026.tex
```

输出会分别生成 `L002_rebuilt_2026.pdf` 和 `L003_rebuilt_2026.pdf`。不建议用普通pdflatex编译含中文正文的文档。

## 版本与核验

本次聊天本地构建的PDF SHA-256：
- L002 36页：`82436c3ca99694c3f062da3eff801c90c17224b73ecda193cf501ed1ab9247df`
- L003 39页：`63c8dd633629434c8a9df84f90a39b9a2694a8839fd02116572ab32c91e56528`

不同 TeX Live 引擎、字体版本或PDF元信息可能导致**输出二进制哈希不完全一致**，因此比较哈希不是对其他运行环境的绝对要求；应另行检查文本、页数、缺字、链接、练习答案和中译。内部原编译版未发现严重overfull或字体缺字警告，本地QA通过，但仍需教师审校和真实学习者试用。

**工作流程**：改正文→本地编译→渲染检查→核对来源与答案→保存新源代码→实际上传PDF二进制并核验→才考虑更新正式发布状态和词汇曝光记录。见 [编辑档案](REBUILD_L002_L003_2026-10-11.md)。
