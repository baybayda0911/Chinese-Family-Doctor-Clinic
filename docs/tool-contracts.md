# 待实现工具契约

全部下列接口仍为设计合同。没有工具服务器、业务CLI或医疗评分算法；项目校验脚本仅检查开发材料。

| 层/接口 | 输入 | 预期输出与退出 |
|---|---|---|
| 本地 inspect_input | local_file_ref | 文件类型/页数/损坏/加密，失败说明；原路径只在本地 |
| 本地 extract_local | doc_id, parser_config | 页/块/表格、原文、质量与错误，本地暂存 |
| 本地 prepare_review | doc_id, redaction_policy | 本地对照预览、脱敏候选、关键字段 |
| 本地 confirm_review | reviewed_fields, confirmation_batch_id | 已核对事实、来源；不等同保存同意 |
| 模型入口 ingest_status | doc_id | 中性状态与下一步，不返回原件或原文 |
| 模型 prepare_context | member_id, task_scope, grant_ref | 最少核对事实与snapshot_revision |
| get_rule | rule_id, population, region, as_of | 审核/适用状态；未批准或范围不符阻止自动规则用途 |
| search_public | generic_query, source_scope | 通用公开资料与日期，不发送原件 |
| route_task | intent, facts_snapshot, safety_state | 主责/协作/缺失/转介，风险优先中断 |
| stage_records | encounter, candidate_records, expected_revision | 一份新增/更正摘要与差异 |
| commit_records | confirmation_batch_id, expected_revision | 串行版本检查、备份、原子提交、审计与Markdown视图 |
| export_summary | member_id, selected_records, receiver_vault_id, grant_ref | 一次授权预览、最小包、指纹 |
| import_summary | package, member_mapping, expected_revision | 重复/新增/冲突预览，确认后主库合入 |
| restore_snapshot | backup_ref, expected_schema | 恢复预览，先保留有效库，失败不损坏 |
| build_followup | confirmed_actions | 来源明确任务，reminder_enabled=false |

授权预留 authorize(actor_id, member_id, purpose, fields, expires_at)、revoke_grant(grant_id)、test_isolation(actor, member_scope)。grant_ref首版可以指本次受控授权确认；不是强认证凭据。export_summary统一使用grant_ref。

本地内部接口不直接全部暴露为MCP工具。对模型的调用入口不能接收真实原件路径或返回未经核对的识别全文；需本地选择器/后台绑定中性ID。原始文件接收与人工核对需要本地界面，不让模型“先看后脱敏”。

实现先验证错误与中断：blocked_dependency、needs_password、needs_conversion、needs_manual_correction、failed；失败不得编造分析完成或写入成功。
