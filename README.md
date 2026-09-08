# 二级市场开源项目研究库

> 系统整理二级市场分析、交易相关的开源项目，含详细评估、优缺点分析、项目地址索引

## 📋 目录结构

| 分类 | 项目数 | 说明 |
|------|:------:|------|
| [A-研报撰写与AI投研](A-研报撰写与AI投研/README.md) | 12 | 一键生成专业金融研究报告的AI系统 |
| [B-AI投研Agent与大师模拟](B-AI投研Agent与大师模拟/README.md) | 10 | 多智能体协作金融研究系统 |
| [C-量化交易框架](C-量化交易框架/README.md) | 6 | 策略开发到实盘交易的完整框架 |
| [D-回测引擎](D-回测引擎/README.md) | 5 | 纯回测工具，策略验证 |
| [E-决策仪表盘与信息聚合](E-决策仪表盘与信息聚合/README.md) | 8 | 每日推送、热榜聚合、实时盯盘 |
| [F-因子挖掘与选股](F-因子挖掘与选股/README.md) | 8 | Alpha因子自动挖掘、AI选股 |
| [G-强化学习交易](G-强化学习交易/README.md) | 2 | RL算法在金融中的应用 |
| [H-实盘交易工具](H-实盘交易工具/README.md) | 5 | 券商对接、自动下单 |
| [I-数据获取](I-数据获取/README.md) | 10 | 金融数据免费获取 |
| [J-组合优化与风控](J-组合优化与风控/README.md) | 3 | 组合构建、风险管理 |
| [K-策略分析与回测](K-策略分析与回测/README.md) | 6 | 交易策略开发与回测 |
| [L-衍生品与期权](L-衍生品与期权/README.md) | 3 | 期权定价、情景分析 |
| [M-舆情分析与情绪因子](M-舆情分析与情绪因子/README.md) | 5 | 新闻情绪→择时信号 |
| [N-知识图谱与产业链](N-知识图谱与产业链/README.md) | 3 | 产业链关系可视化 |
| [O-技术形态与缠论与实战工具](O-技术形态与缠论与实战工具/README.md) | 5 | 缠论、战法、涨停预测 |
| [P-金融大模型](P-金融大模型/README.md) | 3 | 金融专用LLM |
| [Q-AFAC2025比赛方案](Q-AFAC2025比赛方案/README.md) | 4 | 金融AI比赛方案合集 |
| [R-上财FinClaw](R-上财FinClaw/README.md) | 1 | 金融Skills平台 |
| [S-期权错定价套利](S-期权错定价套利/README.md) | 1 | 期权套利策略 |
| [T-量化学习资源与导航](T-量化学习资源与导航/README.md) | 4 | 教程、书籍、资源清单 |
| [U-其他关注清单](U-其他关注清单/README.md) | 41 | 通用AI、编程、生产力、学习资源（用户Stars） |
| [V-交易平台基础设施与跨市场开发](V-交易平台基础设施与跨市场开发/README.md) | 8 | CCXT、跨所执行、可观测性、链上分析与平台底层组件 |

**共 153 个项目，22 个分类**

## ⚠️ 许可证说明

| 许可证 | 含义 | 涉及项目 |
|--------|------|----------|
| **MIT** | 最自由，随便改随便商用 | 大多数项目 |
| **Apache-2.0** | 较自由，需保留版权声明 | FinRobot, FinRL, FinGPT, FinX1, global-stock-data, a-stock-data, Hummingbot, Prometheus, Coinbase AgentKit, CryptoSkills |
| **LGPL-3.0** ⚠️ | 弱传染性，修改库本身与分发边界需重点评估 | NautilusTrader |
| **GPL-3.0** ⚠️ | 传染性，修改分发必须开源 | FinSight, freqtrade, abu量化, PandaAI-Quantflow |
| **AGPL-3.0** ⚠️ | 强传染性，网络服务也触发开源义务 | OpenBB, OpenAlice, OpenStock |
| **PolyForm Noncommercial** ⚠️ | 仅非商业用途 | Attribution-Analysis-of-Options |
| **CC BY-NC-SA 4.0** ⚠️ | 仅非商业，需署名+相同方式共享 | ai-quant-book, xquant-beginner（书稿部分） |
| **未标注** | 需查看项目LICENSE文件 | 冷门项目居多 |

## 🧊 冷门项目标注

- 🧊 = 冷门项目（Stars < 500）
- ⭐ = 推荐关注（冷门但高价值）
- 🔥 = 热门项目（Stars > 5k）
- ⚠️ = 许可证有约束

## 🔗 项目地址索引

完整 153 个项目 GitHub 地址、Stars、许可证、一句话说明见：

👉 **[项目索引.md](项目索引.md)**

> 说明：源码备份体积过大且维护成本高，本库仅保留调研评估与地址索引。如需使用请直接访问原始仓库。

## 📐 仓库架构

本仓库是**策展型索引库**，不是源码镜像站。设计原则：
- **不备份源码**，只保留地址链接 + 评估说明
- **元数据驱动**：`metadata/projects.yaml` 是数据源，`scripts/generate_index.py` 生成索引
- **稳定 ID**：项目 ID 格式为 `<分类>-<序号>`，新增项目不再大规模重排

详见：[ARCHITECTURE.md](ARCHITECTURE.md) | [docs/维护指南.md](docs/维护指南.md)

## 📚 扩展阅读

- **[collections/用户精选清单.md](collections/用户精选清单.md)**：用户提供的项目线索及纳入/排除说明

## 🔍 研究方法

搜集渠道：GitHub搜索 + 学术论文代码仓库 + AFAC比赛方案 + 知乎/Gitee推荐 + arXiv论文跟踪 + 用户个人收藏
核心需求：二级市场分析、交易（信息整理、研报撰写、策略分析、实盘交易）
