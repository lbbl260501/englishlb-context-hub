# 数据含义

所有数据为 UTF-8 JSON。

- lessons.json：课程 ID、状态、主题、问题、PDF 路径、主讲/候选/复习词 ID、来源。imported 表示实际旧资料已导入；archived_sample 是保留去重的历史样章；planned 不计完成。
- lexemes.json：词或词块 ID、text、primary_lesson、syllabus_status、mastery_status、senses。词族和不同词形不自动合并；匹配需证据。
- exposures.json：已发生的讲义记录。kind 为 primary/review/sense_extension；扩展必须有 sense_note。不得从讲义记录推断个人掌握。
- themes.json、problems.json：教学组织框架及具体阅读问题，不代表官方分类或真题频率统计。
- sources.json：证据类型、路径/定位和核验状态。文件存在、聊天报道、候选来源必须分开。
- artifacts.json：实际导入二进制文件的字节数、SHA-256 和页数，便于检测意外改动。
- assessments.json：真实测验记录，空表表示没有测验，不表示零分。
- syllabus.json：完整官方词表导入/核验状态，未完成时 denominator 为 null。
- sessions.json：工作交接与未解决项，不存无关完整聊天。

候选重复由规划脚本提示，不静默删除。新的主讲重复在 audit 中报错。

