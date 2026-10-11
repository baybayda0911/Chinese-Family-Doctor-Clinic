# 基线使用与本地配置

本仓库包含项目级Skill及开发校验资料，业务服务尚未开发。主入口在[SKILL.md](../.agents/skills/chinese-family-doctor-clinic/SKILL.md)。在Codex打开仓库后选择该Skill；若未显示，按[官方说明](https://learn.chatgpt.com/docs/build-skills)检查项目级发现目录或重新加载。当前不改用户级全局Skill或MCP配置。

本地配置样式见[config.example.json](../config.example.json)。复制为config.local.json后只在本机填入知识仓库路径；该文件已被忽略。当前配置供Skill和后续实现参考，不存在已运行的自动配置加载服务。clinical_data_root、local_identity_root和vault_id初始为null，不自动建立真实库。

知识源路径与健康资料路径分开。当前设备已克隆的上游可在本地config.local.json查看。其他设备须自行克隆并分别配置，不能复制本机绝对路径。TCM可选工作流适用非商业许可，禁用该选项时核心模块仍可进行一般信息整理。nihaixia默认关闭，用户选择流派时再启用本地参考；family-doctor-zh无许可证，当前只外置。

使用虚构或已经本地脱敏、核对的信息演练。图片和扫描PDF导入、正式保存及交换尚不可用，不通过直接读真实原件或手动写库冒充完成。后续安装OCR与运行工具依P1/P2任务实施。

开发校验环境由requirements-dev.lock固定，只安装JSON Schema/YAML校验依赖；不包含OCR、模型、知识库或付费API。README列出检查入口，锁文件记录本次平台，其他平台需验证兼容性。
