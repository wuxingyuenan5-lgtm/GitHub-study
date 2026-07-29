# Q-AFAC2025比赛方案

> 本分类收录AFAC2025金融算法挑战赛相关的高质量比赛方案仓库，涵盖基金申赎预测、金融长思维链压缩等赛题的获奖方案。

---

## 项目列表

| # | 项目名称 | GitHub | Stars | 许可证 | 标签 |
|---|---------|--------|-------|--------|------|
| 1 | Menu-RAG | 已在A类介绍 | — | — | 赛题四三等奖 |
| 2 | tianchi_AFAC_AGENT | 已在A类介绍 | — | — | 赛题四前百 |
| 3 | AFAC2025赛题一Top2方案 | [fengmaochairman/AFAC2025_Track1](https://github.com/fengmaochairman/AFAC2025_Track1_Forecast-of-fund-subscription-and-redemption) | 较少 | — | 🧊 冷门比赛 |
| 4 | AFAC2025赛题三冠军方案 | [shinsonwu/AFAC2025-Challenge-Compression](https://github.com/shinsonwu/AFAC2025-Challenge-Compression-of-Long-Thinking-Chains-in-the-Financial-Field-Gold-Medal-Solution) | 较少 | — | 🧊 冷门比赛 |

---

## 1 & 2. Menu-RAG 与 tianchi_AFAC_AGENT

> 这两个项目已在前面分类中详细介绍，此处仅做索引。

### Menu-RAG
- **赛题**：AFAC2025 赛题四（金融研报/公告智能问答）
- **成绩**：三等奖
- **核心方案**：RAG + 多级菜单式检索
- **详见**：相关A类分类目录

### tianchi_AFAC_AGENT
- **赛题**：AFAC2025 赛题四
- **成绩**：前百
- **核心方案**：LLM Agent协作框架
- **详见**：相关A类分类目录

---

## 3. AFAC2025赛题一Top2方案 — 基金申赎预测 🧊 冷门比赛

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [fengmaochairman/AFAC2025_Track1_Forecast-of-fund-subscription-and-redemption](https://github.com/fengmaochairman/AFAC2025_Track1_Forecast-of-fund-subscription-and-redemption) |
| **Stars** | 较少（比赛方案） |
| **许可证** | 未标明 |

### 核心功能

该仓库展示了AFAC2025赛题一「基金申购赎回预测」的Top2获奖方案，技术路线清晰且有系统性：

- **赛题背景**：预测公募基金的每日申购/赎回金额，是基金流动性管理的核心问题
- **双模型融合**：
  - 两个 LightGBM 模型分别训练后融合，利用差异提升鲁棒性
  - 融合策略（平均/加权/Stacking）经过对比实验选择
- **大模型特征工程**：
  - 利用LLM提取新闻/公告的文本特征
  - 将非结构化信息转化为结构化特征输入模型
- **时序特征工程**：
  - 滞后期特征（t-1, t-2, ..., t-n）
  - 滚动统计特征（均值/标准差/极值）
  - 周期性特征（周内效应/月度效应/节假日效应）
- **数据清洗**：缺失值处理、异常值检测、分布对齐

### 优点

- ✅ 双LightGBM融合+大模型特征的技术路线清晰合理
- ✅ Top2方案经过了充分的交叉验证和线上测试
- ✅ 大模型特征工程是亮点，将NLP能力引入传统表格预测
- ✅ 代码和思路完整可复现

### 缺点

- ❌ 比赛方案针对特定赛题和数据集，泛化到真实业务需要适配
- ❌ 对比赛数据集的强依赖和可能的过拟合
- ❌ LightGBM方案在超大规模数据下性能有瓶颈
- ❌ 大模型特征提取的延迟和成本在实时场景中需优化

### 适用场景

- 基金公司流动性管理的技术方案参考
- 比赛型时序预测（表格数据+NLP特征融合）的方法论参考
- 学习Top级比赛的特征工程和模型融合策略

---

## 4. AFAC2025赛题三冠军方案 — 金融长思维链压缩 🧊 冷门比赛

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [shinsonwu/AFAC2025-Challenge-Compression-of-Long-Thinking-Chains-in-the-Financial-Field-Gold-Medal-Solution](https://github.com/shinsonwu/AFAC2025-Challenge-Compression-of-Long-Thinking-Chains-in-the-Financial-Field-Gold-Medal-Solution) |
| **Stars** | 较少（比赛方案） |
| **许可证** | 未标明 |

### 核心功能

这是AFAC2025赛题三「金融领域长思维链压缩」冠军方案，解决金融推理大模型推理链过长导致的效率和成本问题：

- **赛题背景**：金融推理大模型（如o1风格）的思维链通常过长，影响推理速度和成本，需要在保持推理质量的同时压缩链长度
- **核心技术一：自一致性偏置解码（Self-Consistency Biased Decoding）**
  - 在多个采样结果中寻找一致性高、冗余度低的推理路径
  - 偏置解码策略引导模型生成更紧凑的推理链
- **核心技术二：多温度交叉推理（Multi-Temperature Cross Inference）**
  - 使用不同温度参数并行推理，捕捉不同粒度的推理模式
  - 低温推理保证准确性，高温推理探索压缩空间
- **LLaMA-Factory LoRA微调**：
  - 使用LLaMA-Factory框架对基座模型进行LoRA微调
  - 训练模型学习高效推理路径
- **压缩率 vs 质量权衡**：在保证推理准确率的前提下，实现显著的推理链压缩

### 优点

- ✅ 冠军方案，经过了激烈的比赛验证，技术方案可靠
- ✅ 自一致性偏置解码+多温度交叉推理方法创新性强
- ✅ LLaMA-Factory LoRA微调降低了训练门槛
- ✅ 对金融大模型的效率优化有重要参考价值
- ✅ 方案完整可复现

### 缺点

- ❌ 比赛方案针对特定评测指标，真实场景效果需验证
- ❌ 自一致性需多次采样，总计算量可能不减反增
- ❌ 多温度推理的工程实现相对复杂
- ❌ 推理链压缩可能在某些极端case下丢失关键信息

### 适用场景

- 金融大模型推理效率优化的前沿技术参考
- 思考链压缩/蒸馏方向的学术研究
- 金融LLM部署中降低推理延迟和成本的技术探索

---

## 本分类总结

| 维度 | 赛题一Top2 | 赛题三冠军 |
|------|:---:|:---:|
| 赛题类型 | 表格预测（基金申赎） | NLP推理优化 |
| 核心技术 | LightGBM×2 + LLM特征 | 自一致性 + 多温度推理 |
| 方法论价值 | ★★★★☆ | ★★★★★ |
| 工程价值 | ★★★★☆ | ★★★☆☆ |
| 推荐优先级 | 1 | 1 |

**特别说明**：比赛方案的价值在于方法论参考和技术思路借鉴，不能直接等同于生产环境方案。赛题三冠军方案对关注金融大模型效率优化的同学有极高的技术参考价值。
