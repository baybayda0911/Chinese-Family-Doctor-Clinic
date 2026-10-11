# 虚构契约夹具

这里的成员、报告、记录、授权、库和任务均为合成。所有JSON带synthetic=true，交换包另带fixture_type=contract_fixture；它们用于结构/约束测试，不是已实现导入服务的运行包。

示例契约覆盖member、observation、clinical-entry、task、context、exchange、room-output。原件、影像与OCR图片夹具将在P1/P4添加；当前没有这些格式的运行验收。

交换包仅计算合成内容的完整性摘要以演示算法，不提供发送者认证。用户若自行改动内容，应重新生成摘要；测试校验会拒绝不一致的哈希。不会将任何示例写入真实档案库。
