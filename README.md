# Chinese-Family-Doctor-Clinic

面向中文家庭的 AI 健康助手，以中国大陆为默认服务环境，通过一个 Codex 主 Skill 串联六个科室，服务成人、老人、儿童与孕妇的日常健康管理。提供健康信息整理、风险提示和就医准备；诊断、处方及专业判断由执业专业人员承担。

**当前阶段：实施基线 v0.1.0。** 主入口和六室说明、共享工作流、数据契约、虚构样例、开发与验收文件已经建立。OCR、资料导入界面、档案事务、跨设备交换、提醒、自动多 Agent 编排及医学规则引擎尚未实现。项目尚未完成医学或临床验证。版本说明见 [CHANGELOG](CHANGELOG.md)。

## 组织与使用场景

| 科室 | 主要职责 |
|---|---|
| 导诊台 | 风险优先、必要信息收集、分流和汇总 |
| 西医问诊室 | 已有症状/报告/医嘱的信息整理，慢病跟踪与就医准备 |
| 中医问诊室 | 中医知识及既有处方的信息解释，分别标明教材、经典与流派来源 |
| 心理健康管理室 | 支持、健康教育、自愿初筛准备及专业求助衔接 |
| 家庭健康管理室 | 家庭任务、生活方式、儿童/孕期/老人日常管理；自选“命理风水咨询” |
| 健康档案室 | 资料核对、来源、确认批次、版本和人工摘要交换规范 |

首版产品目标有三条流程：症状咨询与就医分流、多格式报告整理、慢病与家庭日常健康管理。文字、Word、图片、文字型/扫描型/混合型 PDF 均为首版验收要求；目前不宣称这些导入通道已实现。

## 使用主 Skill

在 Codex 中打开本仓库，选择或输入 `$chinese-family-doctor-clinic`。项目入口位于 [.agents/skills/chinese-family-doctor-clinic/SKILL.md](.agents/skills/chinese-family-doctor-clinic/SKILL.md)。项目级发现目录依据 [Codex 官方说明](https://learn.chatgpt.com/docs/build-skills)。当前仅完成文件与契约校验，尚未验证各版本 Codex 的交互表现。

可用虚构内容演练：“请使用家庭医生诊所，为 demo-member-001 整理已经核对的体重记录，列出就医沟通问题和随访任务。只演练，不写入档案。” 初次使用只用虚构或已脱敏、核对的信息。

Skill 是工作指导，不能自行获得 OCR、数据库、账户隔离或临床能力。原件须先经本地解析、脱敏与人工核对；未来对模型暴露的工具只返回必要事实。本地档案也不意味着模型分析全程离线。

## 开发与验证

基线检查使用 Python 3.11+；开发校验依赖见 [requirements-dev.lock](requirements-dev.lock)。在仓库根目录执行：

```text
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements-dev.lock
.venv/Scripts/python scripts/validate_project.py
.venv/Scripts/python -m unittest discover -s tests -v
```

macOS/Linux 将 Python 路径换成 `.venv/bin/python`。校验仅验证 Skill 元数据、内部链接、JSON Schema 和虚构样例；不是 OCR、医疗判断、记录写入或两机同步验收。实际结果见 [验证记录](docs/validation.md)。

## 实施资料

- [基线使用与配置](docs/setup.md)、[架构与工作流](docs/architecture.md)、[产品决策](docs/decisions.md)
- [数据契约](docs/data-contracts.md)、[多格式录入与 OCR](docs/ingestion.md)
- [隐私与双设备协作](docs/privacy.md)、[医学来源审阅](docs/clinical-review.md)
- [开发任务与完成条件](docs/roadmap.md)、[28 个验收场景](docs/acceptance.md)
- [当前能力清单](capabilities.json)、[贡献约定](CONTRIBUTING.md)

真实健康资料、身份映射、原件、导出包、缓存和备份存于源码仓库之外；仓库示例全部为虚构。目录约定和 .gitignore 不提供强隔离或自动脱敏保障。

## 许可证与参考项目

主框架与原创内容采用已有 [MIT 许可证](LICENSE)，第三方部分按[分层许可](docs/licensing.md)管理。本基线已适配Yungho的部分工作流，并保留其MIT声明；可选TCM工作流改编单独标注CC BY-NC。教材原文、完整知识库和上游运行代码未打包或安装。Yungho/family-doctor 为主要架构参考，TCM.Skill 与 nihaixia 为中医参考来源；后两者的知识资料分发有额外许可与版权条件。详见 [第三方声明](THIRD_PARTY_NOTICES.md) 与 [复用登记](docs/upstream-reuse.md)。本项目 MIT 许可证不覆盖外部资料。
