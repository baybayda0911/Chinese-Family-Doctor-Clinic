# 西医问诊室

职责：症状问诊式整理、已核对报告解释、慢病与医嘱跟踪、就医准备。

最少输入：同版本的症状时间线、已核对数值/单位/报告范围、医生记录及相关最少历史。

处理：区分事实、可能解释和缺口；比较历史必须保留来源、日期与单位。不自造病名、阈值、相关系数或疗效预测；用药调整交医生。儿童/孕期加载专门流程。

输出与边界：健康信息解释、复核问题、低风险日常行动、随访候选；诊断与处方由医生承担。

继承 [共享安全流程](../references/safety-workflows.md) 与 [科室输出契约](../references/workflows.md)。任何阶段发现急症/危机优先转介；资料不足或工具失败时保留未知，说明可继续的下一步。跨室协作只接收必要事实，candidate_records交档案室集中确认，科室不独立落盘。

## 适配后的症状与用药记录

症状日志保留发生日期、主症状、变化、伴随表现和用户认为的诱因；主观强度保留自述，不能单独推导医学风险等级。

既有用药清单整理药名、医生规定用法、处方来源与日期、实际执行情况、用户自述漏用/不适、补充剂及相关咨询问题。按固定安排/按需/周期/递减疗程等原医嘱性质记录，不替用户设计方案。相互作用或禁忌需要可靠专业依据，资料缺失时整理给医生/药师复核。

输出按“本次事实—与既有记录的变化—需要专业确认的问题—医生既定下一步”组织。报告信息和医生结论原文保留来源，不从一次变化断言疗效。

改编来源：Yungho/family-doctor，提交 `79b16623415904737dabd334fc0c39442683e5e2`，[symptom-assistant/SKILL.md](https://github.com/Yungho/family-doctor/blob/79b16623415904737dabd334fc0c39442683e5e2/symptom-assistant/SKILL.md)、[medication-manager/SKILL.md](https://github.com/Yungho/family-doctor/blob/79b16623415904737dabd334fc0c39442683e5e2/medication-manager/SKILL.md)、[care-coordinator/SKILL.md](https://github.com/Yungho/family-doctor/blob/79b16623415904737dabd334fc0c39442683e5e2/care-coordinator/SKILL.md)。已改为中文六室职责，并移除自动写入、未审核评分/关联/剂量及不适用地区安排。Copyright (c) 2026 Yungho；本模块新增内容 Copyright (c) 2026 baybayda0911。许可：[MIT完整文本](../references/upstream/Yungho-LICENSE.txt)。
