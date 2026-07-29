# G - 强化学习交易

> 用深度强化学习算法训练交易策略，覆盖从经典DRL到高频交易的多种RL方法。

---

## 1. FinRL ⭐

| 属性 | 详情 |
|------|------|
| GitHub | [AI4Finance-Foundation/FinRL](https://github.com/AI4Finance-Foundation/FinRL) |
| Stars | 14k |
| 许可证 | Apache-2.0 |
| 定位 | 第一个开源金融RL框架 |

**核心功能**：金融深度强化学习框架，支持**DQN/DDPG/PPO/A2C/SAC/TD3**等主流DRL算法，多资产（股票/加密/期货）多时间尺度训练，提供从数据获取→环境建模→策略训练→回测评估→实盘部署的完整Pipeline。

✅ 优点：
- **生态最成熟**：14k Stars，社区活跃，文档完善，教程丰富
- 算法覆盖全面：DQN/DDPG/PPO/A2C/SAC/TD3 一站式选择
- 多资产多时间尺度，灵活度高
- Apache-2.0 许可证，商业友好
- 配套FinRL-Meta（元学习）和FinRL-Tutorials，学习曲线平滑
- 有实盘对接案例（Alpaca等）

❌ 缺点：
- 框架偏"学术示范"，生产级稳定性需自行加固
- RL策略过拟合风险高，回测表现≠实盘表现
- 环境建模依赖外部数据源，数据质量直接影响训练效果
- 超参数敏感，调参成本高

适用场景：**RL交易策略研究入门**，适合第一次尝试用RL做交易的开发者/研究者；多资产策略开发；RL算法对比实验。

---

## 2. TradeMaster 🧊 ⭐ 推荐关注

| 属性 | 详情 |
|------|------|
| GitHub | [TradeMaster-NTU/TradeMaster](https://github.com/TradeMaster-NTU/TradeMaster) |
| Stars | ~2.9k |
| 许可证 | — |
| 学术背景 | NeurIPS 2023 / KDD 2024 / AAAI 2024 / WWW 2024 |

**核心功能**：南洋理工大学AMI实验室出品，**15种RL算法**覆盖从低频到高频：DeepScalper/OPD/DeepTrader/SARL/EIIE等。独有**PRUDEX-Compass评估工具箱**，全面量化RL策略表现。MacroHFT支持高频交易，EarnHFT实现层级RL。

✅ 优点：
- **算法数量最多**：15种RL算法，涵盖经典和前沿方法
- 多篇顶会论文支撑（NeurIPS/KDD/AAAI/WWW），学术质量高
- PRUDEX-Compass评估工具箱是亮点，比单纯看收益更全面
- MacroHFT/EarnHFT深入高频交易，比FinRL更细
- 代码结构清晰，算法独立封装，便于替换和扩展

❌ 缺点：
- 🧊 学术项目，社区规模远小于FinRL
- 文档以论文为导向，工程化使用需自行摸索
- 高频交易部分依赖特定数据格式，适配成本较高
- 部分算法仅提供论文实现，缺少完整训练Pipeline

适用场景：**前沿RL交易研究**，适合需要多种RL算法对比的研究者；高频交易策略探索；RL策略评估方法论研究。

---

## 分类总结

| 项目 | Stars | 许可证 | 推荐度 | 关键词 |
|------|-------|--------|--------|--------|
| FinRL | 14k | Apache-2.0 | ⭐ | 最成熟生态、主流DRL算法全覆盖 |
| TradeMaster | ~2.9k | — | 🧊⭐ | 15种算法、顶会支撑、PRUDEX评估、高频交易 |

**入门推荐**：FinRL — 生态最成熟，文档最完善，RL交易入门首选。

**研究推荐**：TradeMaster — 算法更前沿、评估更科学、高频交易更深入，适合已有RL基础需要深入探索的研究者。

> ⚠️ **重要提醒**：RL交易策略的回测表现与实盘表现之间存在显著Gap。所有RL框架产出的策略，务必经过充分的前向测试和风控验证后方可考虑实盘部署。RL不是"黑盒赚钱机器"。
