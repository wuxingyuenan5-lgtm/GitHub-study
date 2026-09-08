# V. 交易平台基础设施与跨市场开发

> 面向自建多市场交易平台的底层组件研究，重点覆盖：交易所统一接入、跨所执行、资金费率策略、实时数据、可观测性、链上分析和 AI Agent 开发辅助。
>
> 本分类不是“再找一套完整交易平台替换现有系统”，而是判断哪些开源组件适合直接接入、哪些适合拆源码借鉴、哪些只适合独立 Pilot。

**调研基准日期：2026-09-08**

---

## 一、对 Platform_Experiment 的直接结论

### 优先级

1. **CCXT：直接接入** —— 新增 Binance / OKX / Bitget / Gate / Hyperliquid 等 Venue（交易场所）时，优先作为统一 Adapter（适配器）层。
2. **Prometheus：直接接入** —— 给 execution-runtime、行情流、订单生命周期、资金费率数据建立 7×24 Metrics（指标）和告警。
3. **Hummingbot：重点拆源码借鉴** —— 研究跨所做市、套利、对冲、Executor 生命周期，不建议替换现有两腿执行内核。
4. **NautilusTrader：独立 Pilot** —— 评估未来统一 Crypto + IBKR / 美股 / 期货的事件驱动交易内核，不建议现在迁移主平台。
5. **Dune Skills：加密看板增强** —— 用于链上数据研究与 Agent 调用，不作为实时交易行情源。
6. **HiThink Financial-API：A股数据层补充** —— 更适合 A 股日线、财报、板块、指数、特色数据；采用增量同步+本地库，而不是策略高频直连。
7. **CryptoSkills：Codex/Agent 知识层** —— 选择性安装，不作为运行时依赖，也不能替代协议官方最新文档。
8. **Coinbase AgentKit：链上执行候选** —— 未来做钱包型 Agent、DEX / DeFi 自动化时再引入，当前 CEX 资金费率/跨所策略优先级低。

### 场景适配矩阵

| 项目 | 资金费率策略 | 跨所策略 | 加密看板 | 美股看板 | 平台角色 | 建议动作 |
|------|:------:|:------:|:------:|:------:|------|------|
| CCXT | ★★★★★ | ★★★★★ | ★★★★★ | ☆ | Exchange Abstraction（交易所抽象层） | **直接接入** |
| Hummingbot | ★★★★★ | ★★★★★ | ★★ | ☆ | Crypto Strategy / Execution 参考 | **拆源码借鉴** |
| NautilusTrader | ★★★★☆ | ★★★★★ | ★★★ | ★★★★☆ | 统一事件驱动交易内核 | **独立 Pilot** |
| Prometheus | ★★★ | ★★★★ | 运维 | 运维 | Observability（可观测性） | **直接接入** |
| Dune Skills | ★★ | ★★ | ★★★★★ | ☆ | On-chain Analytics（链上分析） | **看板增强** |
| HiThink Financial-API | ☆ | ☆ | ☆ | ☆ | A股数据服务 | **A股数据层** |
| CryptoSkills | ★ | ★ | ★★ | ☆ | Agent Knowledge（Agent 知识层） | **按需安装** |
| Coinbase AgentKit | ★ | ★★ | ★★★ | ☆ | On-chain Agent / Wallet | **以后再接** |

---

## 1. CCXT 🔥⭐ —— 多交易所统一接入的第一优先级

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/ccxt/ccxt |
| **Stars** | ~43.9k |
| **许可证** | MIT ✅ |
| **语言** | Python / TypeScript / JavaScript / C# / PHP / Go / Java / Rust |
| **定位** | 100+ Crypto Exchange / Prediction Market 的统一交易 API |

### 核心价值

CCXT 不是数据供应商，而是 **Exchange Abstraction Layer（交易所抽象层）**。它把 Binance、Bybit、OKX、Bitget、Hyperliquid 等底层不同 API 尽量标准化成统一接口，包括：

- Ticker / Order Book / Trades / OHLCV
- Funding Rate / Funding History
- Open Interest
- Balance / Position
- Create / Cancel / Fetch Orders
- REST + WebSocket（CCXT Pro 已并入 ccxt 包）
- 内置 Rate Limiter（限流器）和 Endpoint Cost（接口权重）

### 对资金费率策略的价值

建议用 CCXT 构建统一 Funding Collector（资金费率采集器），标准化：

```text
funding_rate
funding_interval
next_funding_time
mark_price
index_price
perp_bid / perp_ask
spot_bid / spot_ask
open_interest
volume
contract_size
tick_size
qty_step
```

真正策略信号不应只比较 Funding Rate，而应计算：

```text
Net Carry
= Funding Spread
- Trading Fee
- Slippage
- Borrow Cost
- Basis Risk
- Capital Cost
```

### 对现有平台的建议

**不要把现有成熟 Bybit Native Adapter（原生适配器）替换掉。**

更合理的结构：

```text
execution-runtime
├─ Bybit Native Adapter      ← 保留
├─ MT5 Native Adapter        ← 保留
└─ CCXT Adapter
   ├─ Binance
   ├─ OKX
   ├─ Bitget
   ├─ Gate
   └─ Hyperliquid
```

核心 Venue（交易场所）或特殊订单能力继续走 Native API；新交易所先通过 CCXT 快速接入，验证后再决定是否原生化。

### 风险/缺点

- 统一 API 必然是 Lowest Common Denominator（最低公共能力集），特殊订单/保证金模式可能仍需 Native API。
- CCXT 不提供长期历史数据库，历史深度仍由各交易所决定。
- 不适合微秒级 HFT（高频交易）核心执行路径。

**结论：当前最值得直接引入 Platform_Experiment 的项目。**

---

## 2. Hummingbot 🔥⭐ —— 资金费率与跨所策略最值得“抄作业”的源码

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/hummingbot/hummingbot |
| **Stars** | ~19.9k |
| **许可证** | Apache-2.0 ✅ |
| **语言** | Python / Cython |
| **定位** | Crypto Market Making / Arbitrage / Execution Framework |

### 最值得研究的模块

- Connector（交易所连接器）
- Controller（策略控制器）
- Executor（执行器）
- Cross-Exchange Market Making（跨所做市）
- Spot-Perpetual Arbitrage（现货-永续套利）
- Hedging（对冲）
- Inventory Management（库存管理）
- Dynamic Spread（动态价差）
- Order Refresh / Cancel / Repost（订单刷新/撤挂）

### 为什么和现有平台高度相关

现有 Platform_Experiment 已经有两腿执行、成交确认、部分对冲、Private Stream（私有流）、Reconciliation（对账恢复）等基础。Hummingbot 的价值不是替换这套系统，而是对照它成熟的 Maker/Taker（挂单方/吃单方）和 Hedge（对冲）逻辑，补强：

- 何时先挂哪条腿
- 最低盈利阈值
- Maker 成交后 Taker 对冲策略
- Partial Fill（部分成交）的残余敞口处理
- Slippage Buffer（滑点缓冲）
- Inventory Bias（库存偏置）
- Executor 生命周期与状态机

### 建议

**研究源码，不整套嵌入主 Runtime。**

如果直接引入 Hummingbot 作为第二套执行内核，会与现有 orchestration / risk / reconciliation 职责重复，增加复杂度。

---

## 3. NautilusTrader 🔥⭐⚠️ —— 最像未来“统一跨资产交易内核”的项目

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/nautechsystems/nautilus_trader |
| **Stars** | ~28.6k |
| **许可证** | LGPL-3.0 ⚠️ |
| **核心语言** | Rust + Python |
| **定位** | Production-grade Event-Driven Trading Engine（生产级事件驱动交易引擎） |

### 核心架构

```text
Market Data
    ↓
Data Engine
    ↓
Strategy
    ↓
Risk Engine
    ↓
Execution Engine
    ↓
Venue Adapter
```

Backtest / Paper / Live 尽量共享同一套事件模型，这是它相较多数 Python Bot Framework（机器人框架）最重要的优势。

### 对你的特殊价值

它不仅做 Crypto，也适合未来统一：

```text
Crypto                 TradFi
Binance / Bybit        IBKR
OKX / ...              US Equity / Futures / Options
        \              /
         Unified Event Model
                ↓
             Strategy
                ↓
          Risk / Execution
```

这对未来“加密看板 + 美股看板 + 策略 + 实盘”统一平台很有吸引力。

### 当前建议

不要迁移现有 Platform_Experiment；单独建立：

```text
research-lab/nautilus-pilot/
```

先验证：

1. Binance / Bybit Perpetual 数据与交易；
2. IBKR 美股数据与交易；
3. Funding / Mark / Index 的统一事件；
4. Backtest→Paper→Live 的一致性；
5. 与现有 Platform API / Risk / Accounting 的边界。

如果 Pilot 显著减少跨资产重复代码，再考虑 Platform 2.0。

### 风险

- LGPL-3.0 需要明确动态链接、修改库本身和分发边界。
- Rust + Python 双栈学习成本高。
- 架构很完整，容易诱发“为了框架重写现有系统”的过度工程。

---

## 4. Prometheus 🔥⭐ —— 交易平台最应该尽快补的可观测性

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/prometheus/prometheus |
| **Stars** | ~66k |
| **许可证** | Apache-2.0 ✅ |
| **语言** | Go |
| **定位** | Monitoring + Time Series Database（监控 + 时序数据库） |

### 适合 Platform_Experiment 的 Metrics

```text
exchange_ws_connected
exchange_ws_age_ms
market_data_age_ms
funding_data_age_ms
order_submit_latency_ms
order_ack_latency_ms
fill_latency_ms
order_reject_total
cancel_failure_total
partial_hedge_total
reconciliation_pending_total
position_mismatch
api_429_total
strategy_pnl
strategy_drawdown
```

### 最有价值的告警

```text
Bybit/Binance WebSocket > 5s 无数据
Funding 数据 stale > 30s
partially_hedged 状态持续 > 10s
position mismatch != 0
连续出现 429 / order reject
Execution Runtime heartbeat 丢失
```

### 推荐架构

```text
Execution Runtime / Data Service
             ↓
        Prometheus
             ↓
          Grafana
             ↓
       Alertmanager
```

**结论：不是“量化策略项目”，但对 7×24 多交易所系统的实际价值非常高，优先级应高于继续堆交易所。**

---

## 5. Dune Skills 🧊⭐ —— 加密看板的链上分析增强层

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/duneanalytics/skills |
| **Stars** | ~49 |
| **许可证** | MIT ✅ |
| **定位** | Dune 官方 Agent Skills（智能体技能） |

### 正确定位

Dune Skills 不是实时行情源，而是让 Codex / Claude / Cursor 更方便调用 Dune 的链上查询能力。

适合补充加密看板中的：

- Exchange Inflow / Outflow（交易所流入流出）
- Stablecoin Flow（稳定币流量）
- DEX Volume（去中心化交易所成交量）
- Protocol TVL
- Holder Distribution（持币分布）
- Whale / Smart Money 行为
- DeFi Position（链上头寸）

推荐组合：

```text
Crypto Dashboard
├─ Exchange / Derivatives → CCXT
└─ On-chain              → Dune
```

**不要用 Dune 替代 WebSocket / Order Book / Funding 实时数据。**

---

## 6. HiThink Financial-API ⭐ —— A股数据层的重要补充

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/HiThink-Tech/Financial-API |
| **Stars** | ~2.8k |
| **许可证** | MIT ✅（客户端/接入代码） |
| **定位** | 同花顺官方 A 股金融数据服务 |

### 适合的数据

- A股实时快照
- 日线历史行情
- 财务报表 / 财务指标
- 估值
- 指数 / 板块
- 涨跌停 / 炸板 / 连板
- 龙虎榜 / 热榜 / 异动
- 公募基金

### 用量特点

公开说明是**不设累计调用次数上限**，但服务端存在动态限流，应控制短时间高并发。全市场或长时间数据更适合 Market Dumps（市场数据文件）+ 本地 DuckDB。

### 对平台的正确架构

```text
HiThink API
    ↓
Daily Incremental Sync（日度增量同步）
    ↓
DuckDB / PostgreSQL
    ↓
Unified Data Layer
    ↓
A股看板 / 因子 / 策略 / 研究
```

不建议策略页面每次打开都直接大量打远端 API。

---

## 7. CryptoSkills 🧊⭐ —— Crypto Vibe Coding 的知识库，不是交易基础设施

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/andresdefi/cryptoskills |
| **Stars** | ~4 |
| **许可证** | Apache-2.0 ✅ |
| **定位** | Crypto Agent Skills 知识库 |

### 覆盖内容

Uniswap、Aave、Pendle、Hyperliquid、Polymarket、Jupiter、Drift、Foundry、viem、ethers.js、Solidity Security 等大量协议和工具。

### 优点

- 给 Codex / Cursor / Claude 提供协议级上下文；
- 比模型纯训练记忆更接近实际 SDK / API 用法；
- 适合快速生成 DeFi / EVM / Solana 原型代码。

### 主要风险

- 项目内容更新速度可能落后于 Crypto 协议变化；
- Skill 中存在钱包、Signer（签名器）、Private Key（私钥）相关示例，生产环境必须隔离权限；
- 文档/示例不能视为 Production Runtime（生产运行时）。

### 建议

不要 `install --all`。只在对应任务中按需安装，例如：

```text
hyperliquid
polymarket
coingecko
viem
ethers-js
foundry
solidity-security
```

并在上线前重新核对协议官方最新文档。

---

## 8. Coinbase AgentKit ⭐ —— 未来链上 Agent / 钱包自动化候选

| 属性 | 详情 |
|------|------|
| **GitHub** | https://github.com/coinbase/agentkit |
| **Stars** | ~1.3k |
| **许可证** | Apache-2.0 ✅ |
| **语言** | TypeScript |
| **定位** | 给 AI Agent 提供 Wallet（钱包）和 On-chain Actions（链上操作） |

### 适合的未来方向

- DEX Swap
- DeFi Lending / Borrowing
- Token Transfer
- Wallet Management
- On-chain Agent
- 链上再平衡 / 自动化资金管理

### 当前为什么不优先

你现在更核心的需求是：

```text
Funding
CEX Cross-Venue
Crypto Dashboard
US Stock Dashboard
```

这些首先需要 CCXT、Market Data、Execution、Observability，而不是让 Agent 直接持有钱包执行链上交易。

**结论：保留观察，等 onchain-lab 独立模块成型后再接。**

---

## 二、仓库中已有项目的重新定位

以下项目已经在主索引中，不重复新增 ID，但结合 Platform_Experiment 应重新理解：

### freqtrade（H-03）

适合借鉴：

- Funding Rate 历史数据处理
- Futures Backtest（期货/永续回测）
- Hyperopt（参数优化）
- Look-ahead Bias Detection（前视偏差检测）

不建议替换现有 Execution Runtime（执行运行时）。GPL-3.0 也不适合作为商业平台核心依赖的首选。

### TradingAgents（B-07）

适合美股看板的 AI Research Layer（AI 研究层），尤其是 Fundamental / Technical / News / Sentiment / Risk 多 Agent 汇总。

**适合做研究综合，不适合把最终 Buy/Sell 当作自动交易信号。**

### global-stock-data（I-07）+ fred-us-macro-open-data（I-09）

可继续承担美股看板的低成本研究数据补充：

```text
US Stock Dashboard
├─ Price / Market Data
├─ Fundamental / SEC
├─ Options / FINRA
└─ Macro / FRED
```

后续若进入正式实时行情与实盘，应再评估 Alpaca / Massive / IBKR 等官方数据与交易通道。

---

## 三、从 X 帖子中暂不进入主索引的候选

| 项目方向 | 当前处理 | 原因 |
|----------|----------|------|
| Foundry / viem / ethers.js | 暂不单独收录到本分类 | 通用 Web3 开发基础库，等链上模块启动时再拆专题 |
| EVM Agent Skills | 观察 | 对当前 CEX Funding / Cross-Venue 直接价值低 |
| EVM Cortex | 观察 | 更偏 Ethereum 协议工程环境，容易让主平台变重 |
| Awesome Crypto Skills | 仅资源发现 | 目录型项目，不应替代具体基础设施评估 |
| Jesse | 暂不新增 | 与现有回测框架 / Freqtrade 研究用途重叠，边际价值较低 |

---

## 四、建议的 Platform_Experiment 技术版图

```text
                         Platform Web
                              │
                        Platform API
               Strategy / Risk / Accounting
                        Orchestration
                              │
                       Runtime Contract
                              ↓
                     Execution Runtime
            ┌─────────────────┼─────────────────┐
            ↓                 ↓                 ↓
      Bybit Native          MT5 Native       CCXT Adapter
                                                 │
                                   ┌─────────────┼─────────────┐
                                   ↓             ↓             ↓
                                Binance         OKX          Bitget ...

                         Platform Data
                              │
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
           Crypto          On-chain          A股 / US
             ↓                ↓                ↓
          CCXT Pro           Dune       HiThink / US Data

                         Research Lab
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
         Hummingbot       Freqtrade      NautilusTrader
       源码/策略参考       回测研究             Pilot

                      AI Research Layer
                              ↓
                        TradingAgents

                        Observability
                              ↓
                         Prometheus
                              ↓
                    Grafana / Alertmanager
```

---

## 五、推荐实施顺序

### Phase 1 —— 直接增强现有系统

1. CCXT 接入统一 Crypto Market Data / Funding；
2. 新增 Binance / OKX / Bitget Adapter；
3. Prometheus 接 execution-runtime 和 data service。

### Phase 2 —— 资金费率/跨所策略增强

1. 统一 Funding Opportunity Model；
2. 加入 Fee / Slippage / Borrow / Basis / Capacity；
3. 拆解 Hummingbot XEMM / Spot-Perp / Hedge 逻辑；
4. 补齐回测中的 Funding Event 时间一致性。

### Phase 3 —— 看板

1. Crypto：CCXT + Dune；
2. A股：HiThink + 本地数据库；
3. 美股：现有 global-stock-data / FRED 先补研究层，正式实时行情再接官方 Provider；
4. TradingAgents 只作为 AI 研究综合层。

### Phase 4 —— 下一代交易内核验证

建立 NautilusTrader Pilot，验证 Crypto + IBKR / US Equity 的统一事件模型；通过后再讨论 Platform 2.0，而不是现在重写。

---

## 六、最终评级

| 项目 | 技术质量 | 对当前平台价值 | 接入紧迫度 | 最终建议 |
|------|:------:|:------:|:------:|------|
| CCXT | 9/10 | 10/10 | **P0** | 直接接入 |
| Prometheus | 10/10 | 9/10 | **P0** | 直接接入 |
| Hummingbot | 9/10 | 9/10 | **P1** | 拆源码 |
| NautilusTrader | 9.5/10 | 8.5/10 | **P2** | Pilot |
| Dune Skills | 8/10 | 7/10 | P2 | 加密看板增强 |
| HiThink Financial-API | 8.5/10 | 8/10 | P1 | A股数据层 |
| CryptoSkills | 7/10 | 5/10 | P3 | Agent 按需安装 |
| Coinbase AgentKit | 8/10 | 4/10 | P3 | 链上阶段再接 |

**核心原则：优先吸收组件能力，不要为了“用了知名框架”而引入第二套完整 Runtime。**
