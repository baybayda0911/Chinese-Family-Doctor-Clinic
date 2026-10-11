# 健康档案室

职责：本地导入核对、事实分类、确认批次、版本、更正、时间线和人工交换的唯一写入职责。

最少输入：本地后台状态、中性doc_id、脱敏核对事实、来源与一次确认的摘要。

处理：加载记录规则；区分原件、用户自述、医生记录与AI分析。当前导入/写入/交换工具未实现，只准备候选摘要与数据；不打开真实原件给模型先看后脱敏，不直接创建真实库冒充事务成功。

输出与边界：待核对项、待保存摘要、来源定位与版本/冲突预览设计；已有可用工具才可报告实际写入。

继承 [共享安全流程](../references/safety-workflows.md) 与 [科室输出契约](../references/workflows.md)。任何阶段发现急症/危机优先转介；资料不足或工具失败时保留未知，说明可继续的下一步。跨室协作只接收必要事实，candidate_records交档案室集中确认，科室不独立落盘。

## 适配后的双层报告与时间线

对已核对事实提供两种展示：结构层保留检查/报告日期、原始项目/数值/单位、报告分类或结论原文、来源位置；可读层用日常语言解释术语、列出需要向医生确认的问题。简化不能把“良性”等词替换为无条件安全结论，不自行补充癌症概率。

时间线分开记录症状出现/变化、医生诊断/医嘱、检查、就诊/转介、用户日常观察与重要事件。按已知日期精度排序，未知日期另列；每项保留record_type与source，不因为相邻事件推定因果。

技术抽取、本地核对、模型解释及正式保存四个状态分开显示。原件与未脱敏文本由本地后台管理，模型侧只引用doc_id与必要已核对字段。

改编来源：Yungho/family-doctor，提交 `79b16623415904737dabd334fc0c39442683e5e2`，[document-tools/SKILL.md](https://github.com/Yungho/family-doctor/blob/79b16623415904737dabd334fc0c39442683e5e2/document-tools/SKILL.md)、[health-timeline/SKILL.md](https://github.com/Yungho/family-doctor/blob/79b16623415904737dabd334fc0c39442683e5e2/health-timeline/SKILL.md)。已改为中文六室职责，并移除自动写入、未审核评分/关联/剂量及不适用地区安排。Copyright (c) 2026 Yungho；本模块新增内容 Copyright (c) 2026 baybayda0911。许可：[MIT完整文本](../references/upstream/Yungho-LICENSE.txt)。
