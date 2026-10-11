# 多格式录入与OCR

以下是P1实现要求，目前适配器和本地核对界面尚未实现。

| 格式 | 路线与重点 |
|---|---|
| 文字/TXT/Markdown | 本地读取与编码、段落/行定位 |
| CSV/XLSX | 工作表/行列、单位/日期、合并单元格及公式缓存 |
| DOCX | 段落、表格、页眉页脚、内嵌图片按需OCR |
| DOC | 可信本地Office/LibreOffice转换，不启用宏/外链，核对完整性 |
| 文字PDF | 有效文字层优先，保留页/块/表格及被遗漏图片 |
| 扫描PDF | 本地逐页渲染、中文OCR、方向/版面/表格及关键字段核对 |
| 混合PDF | 按页/区域识别，文字层与OCR去重不漏 |
| PNG/JPEG/TIFF等 | 解码、方向、反光/截断/模糊、逐帧及页序核对 |

原始医学影像诊断不在首版范围，影像报告文字可走输入流程。手写或低置信字段进入人工更正，不猜数字。图片和扫描件通道缺失属于首版阻塞；不能降为要求用户自行录入并宣称完成。

管线：received → classified → extracted → redacted → reviewed → analysis_ready → awaiting_save_confirmation → saved。位置/关键字段校对与新增记录保存确认是不同目的，可以集中批次进行；保存拒绝不影响已核对事实的解释。重大新变更另建确认批次。

获取顺序：可用Codex插件/现有本地工具 → 必要时GitHub开源项目 → 相同虚构报告在各设备比较。插件存在不代表本地数据流合格；本地MCP也需暂存、脱敏与核对层。

| 候选 | 调查依据 | 比较方向 |
|---|---|---|
| [RapidOCR](https://github.com/RapidAI/RapidOCR) | 本地中文OCR及ONNX等路线 | 基础识别、CPU部署、单位/数字、坐标 |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/integrations/mcp_server.md) | 官方MCP有本地推理，PP-StructureV3版面/表格 | 表格列对应、复杂布局、耗时/内存、Codex适配 |
| [Docling](https://github.com/docling-project/docling) | 多格式本地解析、OCR、JSON/Markdown | 统一导入、中文配置、页序和图片覆盖 |
| [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) | 离线桌面、图片/PDF、CLI/HTTP | 人工核对入口、本地桥接、位置输出；CSV不等于表格结构恢复 |

以上为资料调查与拟评估角色，没有本项目速度/准确率排名，未选定或安装。各设备的操作系统、资源与依赖分别验证。源码、权重、转换模型、附带运行库的许可分别登记；启动自检不能省略中文模型和失败恢复检查。

脱敏覆盖姓名/证件/联系方式/地址、文件名、元数据、页眉、图中标识及条码/二维码。必要年龄/孕周等仍是敏感信息，不宣称完全匿名。关键数字、小数、负号、单位、日期、否定词、左右侧及医嘱原文逐项对照原件。OCR成功不等于完成脱敏或具备医疗有效性。
