# M-舆情分析与情绪因子

> 本分类收录金融文本情感分析、新闻情绪信号提取、社交媒体舆情因子构建相关的开源项目，覆盖从词典法到LLM的多层次NLP情绪分析方案。

---

## 项目列表

| # | 项目名称 | GitHub | Stars | 许可证 | 标签 |
|---|---------|--------|-------|--------|------|
| 1 | FinNews-Sentiment2Signal | [PandOvo/FinNews-Sentiment2Signal](https://github.com/PandOvo/FinNews-Sentiment2Signal) | <20 | — | 🧊 冷门 ⭐ 推荐关注 |
| 2 | 情绪增强反转交易策略 | [mukongshan/research-on-reversal-trading-strategies-incorporating-emotional-factors](https://github.com/mukongshan/research-on-reversal-trading-strategies-incorporating-emotional-factors) | <10 | — | 🧊 极冷门学术 ⭐ 推荐关注 |
| 3 | Stock-Market-Sentiment-Analysis | [ZijianWang1125/Stock-Market-Sentiment-Analysis](https://github.com/ZijianWang1125/Stock-Market-Sentiment-Analysis) | <50 | — | 🧊 冷门 |
| 4 | LLM_based_stock_sentiment | [24mlight/LLM_based_stock_sentiment](https://github.com/24mlight/LLM_based_stock_sentiment) | 42 | — | 🧊 冷门 |
| 5 | FinSight-NLP-Financial-Literacy-Agent | [wintershock/FinSight--An-NLP-based-Financial-Literacy-Agent](https://github.com/wintershock/FinSight--An-NLP-based-Financial-Literacy-Agent) | <5 | — | 🧊 极冷门 |

---

## 1. FinNews-Sentiment2Signal — 金融新闻情感→择时策略 🧊 冷门 ⭐ 推荐关注

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [PandOvo/FinNews-Sentiment2Signal](https://github.com/PandOvo/FinNews-Sentiment2Signal) |
| **Stars** | <20 |
| **许可证** | 未标明 |

### 核心功能

该项目提供了一个从金融新闻到交易信号的完整可复现pipeline，支持三层NLP方案按需切换：

- **三层情感分析方案（可切换）**：
  - **Tier 1 — 词典法**：金融情感词典快速打分，适合大规模粗筛
  - **Tier 2 — Transformers**：FinBERT等预训练模型，精度更高
  - **Tier 3 — LLM**：GPT/Claude等大语言模型，处理复杂语义
- **日度情绪指数**：将新闻情感聚合成每日连续情绪指标
- **择时策略回测**：基于情绪指数构建择时信号，包含完整回测检验
- **时间对齐**：强调新闻发布时间与交易日的时间对齐，避免前瞻偏差
- **可复现性**：完整的实验配置和数据版本管理

### 优点

- ✅ 三层方案切换设计优秀，平衡成本与精度
- ✅ 强调时间对齐和可复现性，学术研究价值高
- ✅ Pipeline完整：新闻→情感→信号→回测
- ✅ 架构灵活，便于替换各层组件

### 缺���

- ❌ Stars极少，代码稳定性未知
- ❌ 默认词典法对金融领域特化不够，可能漏判
- ❌ LLM方案成本高（API调用），大规模使用受限
- ❌ 仅支持英文新闻，不适用于A股中文舆情

### 适用场景

- 量化研究者构建基于新闻情绪的市场择时策略
- 对比词典法/Transformers/LLM情感分析效果的实验
- 可复现的量化研究项目参考

---

## 2. 情绪增强反转交易策略 — 年化47.63%/Sharpe 1.46 🧊 极冷门学术 ⭐ 推荐关注

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [mukongshan/research-on-reversal-trading-strategies-incorporating-emotional-factors](https://github.com/mukongshan/research-on-reversal-trading-strategies-incorporating-emotional-factors) |
| **Stars** | <10 |
| **许可证** | 未标明 |

### 核心功能

这是南京大学大创项目的开源仓库，将社交媒体情绪因子嵌入经典反转策略，取得了亮眼的回测结果：

- **数据源**：东方财富股吧评论爬取（A股散户情绪天然数据源）
- **多任务NLP语义建模**：同时处理情感和主题，提取更丰富的文本语义
- **LightGBM因子模型**：以NLP特征为输入，训练个股情绪因子预测模型
- **反转策略增强**：将情绪因子嵌入传统反转策略的信号框架：

  > 经典反转：R_t = α + β·R_{t-1} + ε
  > 情绪增强：R_t = α + β₁·R_{t-1} + β₂·Sentiment_t + ε

- **回测结果**：

  | 指标 | 数值 |
  |------|------|
  | **年化收益** | 47.63% |
  | **Sharpe比率** | 1.46 |
  | **最大回撤** | — |

### 优点

- ✅ 回测结果亮眼（年化47.63%，Sharpe 1.46），方法论有参考价值
- ✅ 东方财富股吧+多任务NLP+LightGBM的技术路线完整
- ✅ 情绪因子嵌入反转策略的做法有学术创新性
- ✅ 完整的研究流程和代码可供复现

### 缺点

- ❌ 学术项目，回测结果可能过于乐观（样本选择偏差/过拟合）
- ❌ 缺少样本外测试和实盘验证
- ❌ Stars极少，代码可能存在硬编码问题
- ❌ 文档以论文为主，代码可读性一般
- ❌ 股吧数据爬取受网站反爬策略影响，数据持续性存疑

### 适用场景

- 学术研究者探索情绪因子与反转策略的结合
- 量化学生参考其NLP+ML的技术路线设计
- **注意**：回测结果不代表实盘表现，需审慎对待

---

## 3. Stock-Market-Sentiment-Analysis — 股吧评论+ELECTRA微调 🧊 冷门

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [ZijianWang1125/Stock-Market-Sentiment-Analysis](https://github.com/ZijianWang1125/Stock-Market-Sentiment-Analysis) |
| **Stars** | <50 |
| **许可证** | 未标明 |

### 核心功能

这是一个面向A股市场的中文金融情感分析项目，数据规模和模型选择都较为扎实：

- **数据爬取**：从东方财富股吧爬取 **71,888条帖子**，构建大规模中文金融语料
- **中文ELECTRA微调**：使用哈工大中文ELECTRA预训练模型在金融语料上微调，实现三分类（正面/中性/负面）
- **滚动情绪指数**：基于时间窗口构建滚动情绪指数，追踪市场情绪变化
- **数据标注**：包含人工标注流程和标注质量说明

### 优点

- ✅ 中文ELECTRA微调三分类，对中文金融文本理解较好
- ✅ 71,888条帖子规模在类似项目中较大，数据量有保证
- ✅ 滚动情绪指数比单日情绪更平滑稳定
- ✅ 针对A股的解决方案

### 缺点

- ❌ 三分类粒度较粗，无法捕捉微妙的情感差异
- ❌ ELECTRA模型较老（vs 当前主流LLM方案）
- ❌ 股吧帖子质量参差不齐，噪声较大
- ❌ 缺少将情绪指数转化为交易策略的回测闭环

### 适用场景

- 需要A股中文情感分析 baseline 的研究项目
- 了解中文金融NLP微调流程的学习参考
- 构建A股市场情绪指数的入门项目

---

## 4. LLM_based_stock_sentiment — Gemini API+前后端完整方案 🧊 冷门

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [24mlight/LLM_based_stock_sentiment](https://github.com/24mlight/LLM_based_stock_sentiment) |
| **Stars** | 42 |
| **许可证** | 未标明 |

### 核心功能

该项目提供了一个完整的LLM驱动情感分析Web应用，从数据到展示形成完整产品：

- **LLM分析**：使用 Google Gemini API 分析A股新闻情感
- **完整前后端**：
  - 后端：FastAPI
  - 前端：Vue.js + ECharts
- **可视化仪表盘**：情感趋势图、个股情感排名、热点事件提取
- **数据源**：A股新闻抓取和预处理

### 优点

- ✅ 有完整前后端，是最接近产品化形态的情感分析项目
- ✅ Gemini API相比传统NLP模型有更好的语义理解能力
- ✅ ECharts可视化仪表盘专业美观
- ✅ FastAPI+Vue.js技术栈现代，便于二次开发

### 缺点

- ❌ 依赖Gemini API，网络和配额限制影响可用性
- ❌ Stars较少，社区反馈有限
- ❌ 缺少回测验证，情感分析结果的金融有效性未证明
- ❌ 未考虑延迟（新闻→情感→信号的时序对齐）

### 适用场景

- 搭建金融舆情监控看板的原型参考
- 使用LLM进行金融情感分析的技术可行性验证
- 学习FastAPI+Vue.js金融应用的架构设计

---

## 5. FinSight-NLP-Financial-Literacy-Agent — 股票+新闻+情感分析 🧊 极冷门

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [wintershock/FinSight--An-NLP-based-Financial-Literacy-Agent](https://github.com/wintershock/FinSight--An-NLP-based-Financial-Literacy-Agent) |
| **Stars** | <5 |
| **许可证** | 未标明 |

### 核心功能

这是一个多功能的金融信息Agent，整合了技术指标分析、新闻抓取和中文情感分析：

- **技术指标分析**：计算和展示常用股票技术指标
- **新闻爬取**：使用 Playwright 浏览器抓取东方财富财经早餐等金融新闻
- **中文情感分析**：SnowNLP + 自定义金融词典增强
- **数据整合**：将技术面数据与新闻面情感结合

### 优点

- ✅ 整合了技术面+消息面的信息
- ✅ Playwright实现可靠的动态页面抓取
- ✅ 自定义词典可增强SnowNLP在金融领域的表现

### 缺点

- ❌ Stars极少，代码质量未知
- ❌ SnowNLP的金融情感分析精度有限（基础模型非金融特化）
- ❌ 更像是一个拼凑的工具集，缺少系统性设计
- ❌ 文档和注释极少

### 适用场景

- 个人学习金融数据抓取和情感分析的入门参考
- 需要快速搭建简易金融信息聚合工具的参考代码

---

## 本分类总结

| 维度 | FinNews-S2S | 情绪反转策略 | Stock-Sentiment | LLM-Sentiment | FinSight |
|------|:---:|:---:|:---:|:---:|:---:|
| NLP层次 | 词典/Transformers/LLM | 多任务NLP+LightGBM | 中文ELECTRA | Gemini LLM | SnowNLP |
| 策略闭环 | ✅ | ✅（亮眼） | ⚠️ 半闭环 | ❌ | ❌ |
| 产品化程度 | 低 | 低 | 低 | ★★★★☆ | 低 |
| 研究价值 | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★★☆☆ | ★★☆☆☆ |
| 推荐优先级 | **1** ⭐ | **1** ⭐ | 2 | 2 | 3 |

**推荐路径**：研究情绪→策略转化 → 首选 FinNews-Sentiment2Signal + 情绪增强反转策略；产品化舆情监控看板 → 参考 LLM_based_stock_sentiment 的前后端架构。
