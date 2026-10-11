# 第三方声明与许可范围

根[LICENSE](LICENSE)为主框架及原创内容的MIT许可。适配部分保留上游许可，完整清单在[reuse-register.json](third_party/reuse-register.json)。完整教材、讲义、医案、模型权重和上游运行代码未打包。

## Yungho/family-doctor（MIT）

Copyright (c) 2026 Yungho。已基于提交 `79b16623415904737dabd334fc0c39442683e5e2` 适配导诊、西医、心理、家庭、档案的部分流程/记录模板；源文件逐项列在清单中。改为中文六室协作与受控最少上下文，移除上游自动写入、固定评分/关联、示例药物和不适用地区安排。[完整MIT许可副本](.agents/skills/chinese-family-doctor-clinic/references/upstream/Yungho-LICENSE.txt)。

## TCM.Skill（可选工作流，CC BY-NC 4.0）

来源YuanZHAO321/TCM.Skill，提交 `966a88acf942b6b8684575db3d1d3f261442b8a4`。仅从SKILL.md问题分流、检索与就医准备流程改编[可选工作流](.agents/skills/chinese-family-doctor-clinic/references/upstream/tcm-workflow.cc-by-nc.md)，2026-10-11修改。该文件单独适用[CC BY-NC完整许可](.agents/skills/chinese-family-doctor-clinic/references/upstream/TCM.Skill-LICENSE.txt)，保留署名、非商业条件及修改标注，不属于根MIT授权范围。

知识库/教材原文仍为本地外部资料，许可不自动覆盖其所有第三方作品。已改编工作流不代表中医诊疗、禁忌或剂量规则审核通过。

## 外部参考、未打包

- [nihaixia](https://github.com/jangviktor-web/nihaixia)：README声明MulanPSL-2.0，完整许可文件和教材等资料授权链待核实。现阶段外置。
- [family-doctor-zh](https://github.com/yiyanli123/family-doctor-skills)：该仓库中文模块，未发现明确许可。现阶段外置，不复制其文本发行。
- RapidOCR、PaddleOCR、Docling、Umi-OCR：候选方案，未引入/安装；模型、源码及运行库许可后续分开核验。
- 开发校验依赖：按requirements-dev.lock固定，依各包许可证使用，不将开发虚拟环境作为发行内容。

知识包如新增实际资料，逐文件登记版本、权利、修改和发行条件后再发布。详见[分层许可](docs/licensing.md)与[来源复用](docs/upstream-reuse.md)。
