# J-组合优化与风控

> 本分类收录组合构建、风险度量与绩效分析相关的开源项目，覆盖从均值-方差优化到量化绩效报告的全流程工具。

---

## 项目列表

| # | 项目名称 | GitHub | Stars | 许可证 | 标签 |
|---|---------|--------|-------|--------|------|
| 1 | Riskfolio-Lib | [dcajasn/Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | ~2k | MIT | — |
| 2 | QuantStats | [ranaroussi/quantstats](https://github.com/ranaroussi/quantstats) | ~7.5k | MIT | — |
| 3 | ML-Portfolio-Optimization | [Gouldh/ML-Portfolio-Optimization](https://github.com/Gouldh/ML-Portfolio-Optimization) | 较少 | — | 🧊 冷门 |

---

## 1. Riskfolio-Lib — 专业组合构建与风险管理

### 核心属��

| 属性 | 内容 |
|------|------|
| **GitHub** | [dcajasn/Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) |
| **Stars** | ~2,000 |
| **许可证** | MIT |

### 核心功能

Riskfolio-Lib 是当前最全面的开源投资组合优化库之一，提供多达 **24种风险度量**，覆盖从经典均值-方差到现代风险管理的完整工具链：

- **均值-风险优化（Mean-Risk Optimization）**：支持方差、半方差、MAD、CVaR、CDaR、最大回撤（Max Drawdown）等多种风险度量
- **风险平价（Risk Parity）**：等风险贡献（ERC）及其多种变体，支持分层风险平价（HRP）
- **风险预算（Risk Budgeting）**：灵活分配各资产的风险预算权重
- **Black-Litterman 模型**：融合主观观点的贝叶斯优化框架
- **约束处理**：支持上下界约束、组约束、换手率约束、因子暴露约束
- **内置可视化**：饼图、风险贡献图、有效前沿绘制

### 优点

- ✅ 支持24种风险度量，覆盖全面，远超同类开源工具
- ✅ API设计清晰，与Pandas无缝集成，学习曲线平缓
- ✅ 文档丰富，配有详细教程和Jupyter Notebook示例
- ✅ 活跃维护，持续更新新功能和Bug修复
- ✅ 学术界和业界均有使用案例，可靠性有保障

### 缺点

- ❌ 纯优化库，不包含数据获取和回测功能，需搭配其他工具
- ❌ 大规模资产下（>1000只）求解速度下降，需配合HRP等近似方法
- ❌ 未内置因子模型，需自行构建因子暴露矩阵
- ❌ 对极值依赖的风险度量（如CVaR），样本量不足时估计不稳定

### 适用场景

- 机构投资者构建多资产配置方案
- 量化研究员验证新型风险度量或优化算法
- 学术研究中对比不同风险度量下的最优组合差异
- PMS（投资组合管理系统）的风险分析模块原型开发

---

## 2. QuantStats — 组合绩效分析报告一键生成

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [ranaroussi/quantstats](https://github.com/ranaroussi/quantstats) |
| **Stars** | ~7,500 |
| **许可证** | MIT |

### 核心功能

QuantStats 是 Python 生态中最流行的投资组合绩效分析库，以「一行代码生成完整分析报告」著称：

- **核心指标**：Sharpe 比率、Sortino 比率、Calmar 比率、最大回撤（MDD）、年化收益、波动率
- **高级分析**：滚动指标（滚动 Sharpe、滚动波动率）、VaR/CVaR、最大回撤持续期
- **一键报告**：`qs.reports.html(returns)` 生成包含图表和指标的完整 HTML 报告
- **基准对比**：支持与任意基准（如 S&P 500）的多维度对比分析
- **展示优化**：Treemap 收益分布、月度收益热力图、水下曲线图（Underwater Plot）等丰富可视化

### 优点

- ✅ 上手极快，核心API仅3-5个函数即可完成完整分析
- ✅ 生成的HTML报告美观专业，可直接用于客户展示
- ✅ 与 `bt`、`ffn` 等库配合使用效果更佳，生态兼容性好
- ✅ 指标计算符合GIPS等行业标准
- ✅ Stars高，社区活跃，问题响应及时

### 缺点

- ❌ 专注绩效分析，不包含组合优化和回测功能
- ❌ 依赖 Matplotlib/Plotly，报告渲染在无GUI服务器上需额外配置
- ❌ 大规模回测数据（>10万行）下报告生成较慢
- ❌ 自定义程度有限，深度定制需修改源码
- ❌ 部分高级统计检验（如Bootstrap置信区间）需自行实现

### 适用场景

- 量化策略回测后的快速绩效评估
- 向客户或投资人展示策略表现，生成专业报告
- 多策略对比分析，筛选最优策略
- 学术论文中的量化策略绩效表格与图表输出

---

## 3. ML-Portfolio-Optimization — ML+金融理论的组合优化 🧊 冷门

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [Gouldh/ML-Portfolio-Optimization](https://github.com/Gouldh/ML-Portfolio-Optimization) |
| **Stars** | 较少（冷门项目） |
| **许可证** | 未标明 |

### 核心功能

该项目将机器学习技术与经典金融组合理论结合，提供了一种创新的组合优化思路：

- **因子分析**：利用ML方法提取和筛选有效因子，构建因子模型
- **Black-Litterman 集成**：将因子信号的置信度编码为BL模型的主观观点
- **ML预测**：使用回归/分类模型预测资产收益，作为优化器的输入
- **实验对比**：提供ML增强组合 vs 传统等权/市值加权组合的对比实验

### 优点

- ✅ 将ML预测与BL理论框架结合的方法论有新意
- ✅ 提供了从因子提取到组合构建的完整pipeline参考
- ✅ 对理解ML在组合优化中的应用有教学价值

### 缺点

- ❌ Stars极少，代码质量和稳定性未经充分验证
- ❌ 文档简陋，缺少详细使用说明和API文档
- ❌ 长时间未更新，可能存在依赖兼容性问题
- ❌ 未做充分的样本外测试和过拟合防范
- ❌ 仅适用于研究参考，不建议直接用于实盘

### 适用场景

- 学术研究中探索ML+组合优化的结合方式
- 量化研究者寻找因子模型与Black-Litterman的技术参考
- 课程项目中学习组合优化的进阶实现

---

## 本分类总结

| 维度 | Riskfolio-Lib | QuantStats | ML-Portfolio-Optimization |
|------|:---:|:---:|:---:|
| 成熟度 | ★★★★☆ | ★★★★★ | ★★☆☆☆ |
| 学习曲线 | 中等 | 极低 | 较高 |
| 实盘可用 | ✅ | ✅ | ❌ |
| 推荐优先级 | 1 | 1 | 3 |

**推荐组合**：Riskfolio-Lib（构建组合）+ QuantStats（分析绩效）= 完整的组合管理工具链。
