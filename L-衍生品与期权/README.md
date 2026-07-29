# L-衍生品与期权

> 本分类收录期权/期货定价、期权组合情景分析与收益归因相关的开源项目，从底层定价引擎到实战分析工具全覆盖。

---

## 项目列表

| # | 项目名称 | GitHub | Stars | 许可证 | 标签 |
|---|---------|--------|-------|--------|------|
| 1 | FinancePy | [domokane/FinancePy](https://github.com/domokane/FinancePy) | 较少 | — | 🧊 冷门 |
| 2 | Scenario-Analysis-of-Options-Trading | [Yuyang-Yao75/Scenario-Analysis-of-Options-Trading](https://github.com/Yuyang-Yao75/Scenario-Analysis-of-Options-Trading) | <10 | — | 🧊 极冷门实战 |
| 3 | Attribution-Analysis-of-Options-Trading | [Yuyang-Yao75/Attribution-Analysis-of-Options-Trading](https://github.com/Yuyang-Yao75/Attribution-Analysis-of-Options-Trading) | <10 | PolyForm Noncommercial ⚠️ | 🧊 极冷门实战 |

---

## 1. FinancePy — 期权/期货定价+Numba加速 🧊 冷门

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [domokane/FinancePy](https://github.com/domokane/FinancePy) |
| **Stars** | 较少（冷门项目） |
| **许可证** | 未标明 |

### 核心功能

FinancePy 是一个专业的衍生品定价库，专注于期权与期货的定价模型实现，通过Numba JIT编译达到接近C++的执行性能：

- **期权定价模型**：Black-Scholes、二叉树/三叉树、蒙特卡洛模拟、有限差分法（隐式/显式/Crank-Nicolson）
- **奇异期权**：障碍期权、亚式期权、回望期权、两值期权
- **利率模型**：Hull-White、Black-Karasinski等短期利率模型
- **信用衍生品**：CDS定价与信用曲线构建
- **Numba加速**：核心计算路径使用 `@njit` 装饰器编译为机器码，性能接近C++原生实现
- **曲线构建**：收益率曲线、波动率曲面校准

### 优点

- ✅ Numba JIT加速是核心亮点，无需编写C/C++代码即获得高性能
- ✅ 定价模型覆盖全面，从香草期权到奇异期权均有实现
- ✅ 代码结构清晰，适合学习和理解衍生品定价原理
- ✅ 纯Python实现，跨平台部署方便

### 缺点

- ❌ Stars极少，代码质量和数学正确性需自行验证
- ❌ 文档简陋，缺少系统性API参考和使用指南
- ❌ 与QuantLib等成熟C++库相比，功能覆盖仍有差距
- ❌ 无活跃社区，bug修复和问题解答响应慢
- ❌ 缺少中国市场特化功能（如上交所/深交所期权规则）

### 适用场景

- 衍生品定价的学习和教学
- 需要Python原生定价引擎的研究项目
- 对定价速度有要求但不想引入C++依赖的轻量场景

---

## 2. Scenario-Analysis-of-Options-Trading — 期权组合情景分析 🧊 极冷门实战

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [Yuyang-Yao75/Scenario-Analysis-of-Options-Trading](https://github.com/Yuyang-Yao75/Scenario-Analysis-of-Options-Trading) |
| **Stars** | <10 |
| **许可证** | 未标明 |

### 核心功能

该项目提供了期权组合的多维度情景分析工具，是国内极少见的聚焦A股期权实战分析的仓库：

- **二维P&L热力矩阵**：标的资产价格 × 隐含波动率变动的交叉情景下，计算期权组合的盈亏（P&L）热力图
- **双引擎隐含波动率**：
  - 欧式期权：Newton-Raphson迭代法
  - 美式期权（ETF期权）：Bisection二分法
- **A股期权保证金计算**：支持上交所（SSE）、深交所（SZSE）、中金所（CFFEX）三大交易所的保证金规则
- **Greeks热力矩阵**：与P&L矩阵类似，但展示各情景下Delta/Gamma/Vega/Theta/Rho的变化
- **可视化输出**：seaborn/matplotlib热力图直观呈现风险暴露

### 优点

- ✅ 极少数支持A股期权（ETF期权+股指期权）保证金计算的开源项目
- ✅ 二维P&L热力分析是专业期权交易者的核心需求，实战价值高
- ✅ 双引擎IV计算覆盖欧式和美式，场景完整
- ✅ 可视化热力图直观展示尾部风险

### 缺点

- ❌ Stars极少（<10），代码可靠性未经验证
- ❌ 缺少文档和示例，上手门槛高
- ❌ 依赖特定数据格式，数据源兼容性有限
- ❌ 未做实时行情对接，需手动准备输入数据
- ❌ 维护状态不明，长时间未更新

### 适用场景

- A股期权交易者在建仓前进行情景压力测试
- 期权策略设计中评估标的价格+波动率同时变化的联合风险
- 理解和计算A股三大交易所的保证金规则
- **极冷门但实战价值高**，值得关注和试用

---

## 3. Attribution-Analysis-of-Options-Trading — 期权组合收益归因 🧊 极冷门实战 ⚠️ PolyForm Noncommercial

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [Yuyang-Yao75/Attribution-Analysis-of-Options-Trading](https://github.com/Yuyang-Yao75/Attribution-Analysis-of-Options-Trading) |
| **Stars** | <10 |
| **许可证** | **PolyForm Noncommercial** ⚠️（仅非商业用途） |

### 核心功能

该项目将期权组合的每日盈亏精确分解为各希腊值（Greeks）的贡献，是专业期权交易归因分析的稀有开源实现：

- **Greeks收益归因分解**：将期权组合日收益拆解为：
  - Delta贡献（标的方向性收益）
  - Gamma贡献（凸性收益）
  - Vega贡献（波动率变化收益）
  - Theta贡献（时间衰减收益）
  - 其他项（高阶项+Rho+交互项）
- **历史时间序列分析**：支持多日连续分析，追踪各风险因子贡献的时序变化
- **Excel多Sheet输出**：自动生成格式化的xlsx报告，每个分析维度独立Sheet
- **可视化**：堆叠柱状图展示每日各Greeks收益贡献

### 优点

- ✅ 期权收益归因是非常专业的领域，开源实现极其稀少
- ✅ 五因子分解（Delta/Gamma/Vega/Theta/其他）逻辑完整
- ✅ Excel输出方便分享和报告
- ✅ 时间序列分析可追踪策略风格漂移

### 缺点

- ❌ Stars极少（<10），代码正确性未经验证
- ❌ **PolyForm Noncommercial 许可证**，仅限非商业用途，限制较大 ⚠️
- ❌ 缺少文档，需要深入阅读源码才能理解使用方法
- ❌ 无持续维护迹象
- ❌ 输入数据格式要求未文档化

### 适用场景

- 期权交易者进行持仓PL归因分析，理解盈亏来源
- 监控策略是否偏离设计意图（如Delta对冲是否有效）
- 学术研究中期权组合收益分解的方法参考
- **注意**：不可用于商业目的 ⚠️

---

## 本分类总结

| 维度 | FinancePy | Scenario-Analysis | Attribution-Analysis |
|------|:---:|:---:|:---:|
| 方向 | 定价引擎 | 情景分析 | 收益归因 |
| 实战价值 | ★★★☆☆ | ★★★★☆ | ★★★★☆ |
| A股适配 | ❌ | ✅（保证金） | ❌ |
| 许可证风险 | — | — | ⚠️ 非商业 |
| Stars | 少 | 极少 | 极少 |
| 推荐优先级 | 3 | **1** | 2（注意许可） |

**注意**：本分类三个项目均为冷门仓库，适合研究和学习参考，实盘使用需谨慎验证。Scenario-Analysis 对A股期权交易者有独特价值。
