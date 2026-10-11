# 数据契约 v0.1.0

contracts使用JSON Schema 2020-12，引用由本地校验器解析，不从远端下载Schema。Schema标识URL只是标识符，不代表已部署网站。仅确认结构与必要字段；不能证明内容医学正确、完成脱敏或授权者身份真实。

| 契约 | 约束 |
|---|---|
| [member](../contracts/member.schema.json) | 随机代号、主库、阶段及来源；身份映射另存 |
| [source](../contracts/source.schema.json) | 文档/用户陈述/医生原记录/AI分析来源，核对及中性位置 |
| [observation](../contracts/observation.schema.json) | 原文、数值/null、单位/null、时间精度、来源、人工核对 |
| [clinical-entry](../contracts/clinical-entry.schema.json) | 类型、主库、版本、确认人/时间、来源、更正链及敏感类别 |
| [task](../contracts/task.schema.json) | 来源类型、负责人、日期/null、状态、默认提醒关闭 |
| [context](../contracts/context.schema.json) | 已核对必要事实、授权引用、事实快照版本 |
| [exchange](../contracts/exchange.schema.json) | 接收库、授权类型/类别、来源、记录版本、完整性字段 |
| [room-output](../contracts/room-output.schema.json) | 六室统一候选输出 |
| [source-register](../contracts/source-register.schema.json) | 来源发现、审阅、适用范围及引入状态 |

未知日期/单位保留null；只有日期不造时分。数值保留原文、原单位与报告范围。单位换算须另外保存依据，不覆盖原值。不把空白当正常或0。

clinical-entry用于已确认记录；AI分析可确认保存，但record_type仍为ai_analysis。clinician_diagnosis/order必须指向clinician_document；用户转述保持user_report。report事实仍是报告事实，不能因报告结论自动变确诊。来源自述类型和true标记只是可追溯约定，不能替代实际人工核对。

revision=1的supersedes=null；更正使用同record_id的直接前一revision。更正链、原子写入、并发检查、备份与Markdown视图是未来记录服务职责，当前契约校验不实施事务。

交换包的fixture_type=contract_fixture表明它是虚构契约夹具，不可作为真实导入包。本基线计算了虚构包SHA256以校验一致性；摘要是去掉integrity字段后，JSON按键排序、无额外空白、UTF-8、非ASCII字符保留的字节串。哈希不提供身份认证或传输加密。

接口签名、模型/本地边界、失败状态见 [工具契约](tool-contracts.md)。示例在 [examples](../examples/README.md)，不得据样例存在宣称服务实现。
