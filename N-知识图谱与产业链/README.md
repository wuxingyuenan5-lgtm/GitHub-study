# N-知识图谱与产业链

> 本分类收录金融知识图谱构建、产业链关系挖掘和知识驱动的问答系统项目，覆盖从自动ETL到图可视化的全流程方案。

---

## 项目列表

| # | 项目名称 | GitHub | Stars | 许可证 | 标签 |
|---|---------|--------|-------|--------|------|
| 1 | stock-knowledge-graph（Obsidian版） | [wanghsinche/stock-knowledge-graph](https://github.com/wanghsinche/stock-knowledge-graph) | ~50 | MIT | 🧊 冷门 ⭐ 推荐 |
| 2 | FinKnowledgeGraph | [XuekaiChen/FinKnowledgeGraph](https://github.com/XuekaiChen/FinKnowledgeGraph) | 67 | MIT | 🧊 冷门 |
| 3 | financial_stock_knowledge_graph | [aihomo/financial_stock_knowledge_graph](https://github.com/aihomo/financial_stock_knowledge_graph) | 较少 | — | 🧊 冷门 |

---

## 1. stock-knowledge-graph（Obsidian版）— AI+自动ETL+双向链接 🧊 冷门 ⭐ 推荐

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [wanghsinche/stock-knowledge-graph](https://github.com/wanghsinche/stock-knowledge-graph) |
| **Stars** | ~50 |
| **许可证** | **MIT** |

### 核心功能

该项目将知识图谱技术与 Obsidian 笔记软件的「双向链接」机制结合，通过GitHub Actions每日自动更新数据，是一个设计极具巧思的创新型项目：

- **GitHub Actions 自动触发**：每日美股收盘后自动运行，无需手动操作，全流程无人值守
- **TradingView Most Active**：自动获取TradingView上最活跃的美股列表
- **AI产业链提取**：利用AI模型自动提取上市公司间的供应链/竞争/合作等产业链关系
- **JSON + Markdown 双格式**：
  - JSON：结构化图数据，可用图数据库处理
  - Markdown：适配 Obsidian 笔记，每个公司一个 `.md` 文件
- **Obsidian双向链接**：在 Obsidian 中打开即可实现 `[[TSMC]]` 自动链接 `[[NVDA]]`，形成可视化的知识网络
- **链路追溯**：一键查看从上游原材料到下游客户的完整产业链条

### 优点

- ✅ 设计极具巧思：GitHub Actions自动化 + Obsidian双向链接 + AI提取，产品思维突出
- ✅ MIT许可证，商业使用和二次开发友好
- ✅ 零成本运行：完全依赖免费基础设施（GitHub Actions + Obsidian免费版）
- ✅ 每日自动更新，信息时效性有保障
- ✅ Obsidian双向链接的图可视化效果专业直观

### 缺点

- ❌ 仅覆盖美股（TradingView Most Active），不涉及A股/港股
- ❌ AI提取的产业链关系可能存在误差，需人工校验
- ❌ 依赖GitHub Actions和外部API，服务中断会影响更新
- ❌ Stars极少，社区反馈有限

### 适用场景

- 美股投资者的产业链研究工具
- 建立个人化的上市公司知识库/产业链笔记体系
- 自动化ETL+知识图谱+可视化的技术方案参考
- **强烈推荐** Obsidian用户尝试

---

## 2. FinKnowledgeGraph — Neo4j金融知识图谱+问答系统 🧊 冷门

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [XuekaiChen/FinKnowledgeGraph](https://github.com/XuekaiChen/FinKnowledgeGraph) |
| **Stars** | 67 |
| **许可证** | **MIT** |

### 核心功能

这是国内较完整的基于Neo4j的金融知识图谱项目，包含从数据获取到智能问答的完整实现：

- **多源数据采集**：
  - 爬取上交所（SSE）上市公司数据
  - Tushare API 获取A股基本面数据
- **三元组构建**：将结构化数据转化为（实体）-[关系]->（实体）三元组
- **Neo4j图谱存储**：使用Neo4j图数据库存储和管理图谱
- **智能问答系统**：
  - 支持自然语言问句解析
  - 基于图谱的多轮对话式查询
  - 问句→Cypher查询→结果展示的完整流程
- **可视化**：Neo4j Browser自动可视化图结构

### 优点

- ✅ 完整的知识图谱构建流程：数据→抽取→存储→查询→问答
- ✅ Neo4j方案成熟稳定，适合生产环境
- ✅ 多轮问答增加了交互实用性
- ✅ MIT许可证，商业友好

### 缺点

- ❌ Tushare API需要积分/付费，数据获取有门槛
- ❌ 图谱规模有限，主要基于上交所公开数据
- ❌ 问答系统的问题覆盖范围受限，需定制Cypher模板
- ❌ Neo4j部署维护有一定成本
- ❌ 长时间未更新，可能不适配新版API

### 适用场景

- 企业级金融知识图谱搭建的参考原型
- 知识图谱驱动的金融问答系统MVP开发
- 学习Neo4j在金融领域的应用实践

---

## 3. financial_stock_knowledge_graph — A股基于Tushare的图谱教程 🧊 冷门

### 核心属性

| 属性 | 内容 |
|------|------|
| **GitHub** | [aihomo/financial_stock_knowledge_graph](https://github.com/aihomo/financial_stock_knowledge_graph) |
| **Stars** | 较少（冷门项目） |
| **许可证** | 未标明 |

### 核心功能

该项目以Jupyter Notebook的形式提供了一个循序渐进的A股证券知识图谱构建教程：

- **Jupyter Notebook 教程**：7步完整教程，从搭建到更新的闭环
  1. 环境配置与数据库初始化
  2. Tushare数据获取（个股信息/财务数据/股东关系）
  3. 实体识别与关系抽取
  4. 三元组构建与清洗
  5. 图数据库导入
  6. 图谱查询与分析
  7. 数据更新与维护
- **Tushare数据源**：基于Tushare的A股数据体系
- **查询示例**：产业链查询、股东穿透、同业竞争分析

### 优点

- ✅ 7步教程设计清晰，适合零基础学习者
- ✅ Jupyter Notebook形式便于交互式学习
- ✅ 覆盖从搭建到更新的完整生命周期
- ✅ 对理解图数据库在金融领域的应用有教育价值

### 缺点

- ❌ Tushare积分要求是学习门槛
- ❌ 教学性质为主，工程化程度不高
- ❌ 缺少可视化方案
- ❌ 维护状态不明，可能与新版Tushare API不兼容

### 适用场景

- 金融知识图谱的入门学习
- 高校金融科技课程的实践项目参考
- 快速验证图数据库在特定金融分析场景的可行性

---

## 本分类总结

| 维度 | stock-KG (Obsidian) | FinKnowledgeGraph | financial_stock_KG |
|------|:---:|:---:|:---:|
| 创新性 | ★★★★★ | ★★★☆☆ | ★★☆☆☆ |
| 产品化 | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ |
| 学习价值 | ★★★★☆ | ★★★★☆ | ★★★★★ |
| A股覆盖 | ❌（美股） | ✅ | ✅ |
| 推荐优先级 | **1** ⭐（美股） | 2 | 2（学习） |

**推荐路径**：学习知识图谱基础 → financial_stock_knowledge_graph（Jupyter教程）→ 进阶实战 → FinKnowledgeGraph（Neo4j+问答）；美股投资者 → stock-knowledge-graph（Obsidian版）。
