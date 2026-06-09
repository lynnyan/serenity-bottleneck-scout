# Serenity 综合研报包（Thesis Pack + Investment Ideas）— {{THEME}}

Date: {{DATE}}  
Market: {{MARKET}}  
Horizon: {{HORIZON}}  
Candidates: {{CANDIDATES}}  

> 写作规则（本 skill 强制）：
> - 研报正文以**中文**呈现。
> - 关键技术术语以**英文**呈现并全篇统一（例如：`chokepoint`、`bottleneck`、`lead time`、`qualification`、`integrated actuator`）。
> - 必须提供 **Glossary（术语表）**：用中文解释关键英文术语及其在本研报中的含义。
> - 最终交付必须包含：Markdown（事实源）+ PDF（渲染产物）。

## 0) 范围与假设（Scope & assumptions）

> 重要声明：
> - 本文为一般性研究，不构成个性化投资建议，不提供仓位/买卖点/适配性判断。
> - 合规/标准仅作为“市场准入/供给约束/地缘风险”的讨论材料；默认不把标准本身当作投资推荐的核心依据（除非你显式把主题设为“合规红利”）。

- What’s included/excluded:
- Key assumptions (mark inferences explicitly):
- What would change my mind (disconfirmers):

## Glossary（英文术语中文解释）

| Term (EN) | 中文解释（建议一句话） | Why it matters |
|---|---|---|
| chokepoint |  |  |
| bottleneck |  |  |
| lead time |  |  |
| qualification |  |  |
| integrated actuator |  |  |
| functional safety |  |  |

## 1) 供应链地图（Supply-chain map；必须物理闭环；PDF 对齐版）

Raw materials → substrates → devices → modules → systems → end customers

### 1.1 物理闭环（对齐表）

| Layer | What’s inside | Evidence / note |
|---|---|---|
| Raw materials |  |  |
| Devices / parts |  |  |
| Sensors / safety |  |  |
| Compute / AI |  |  |
| Subsystems |  |  |
| System & deployment |  |  |

### 1.2 “Must-pass gate” 列表（对齐表；VERIFIED vs HYPOTHESIS）

| Type | Gate | Why it is “must-pass” | Evidence / boundary |
|---|---|---|---|
| VERIFIED |  |  |  |
| HYPOTHESIS |  |  |  |

### 1.3 物理 bottleneck 候选（对齐表；必须可证伪）

| Candidate node | Status (Established / Hypothesis) | Evidence we have | Evidence missing (to upgrade) |
|---|---|---|---|
|  |  |  |  |

### 1.4 Geography / policy single points（对齐表）

| Region | Single point | Why it matters | Monitoring |
|---|---|---|---|
| CN |  |  |  |
| US |  |  |  |
| EU |  |  |  |
| Other |  |  |  |

### 1.5 交易所公告/披露线索捕捉（对齐表；避免漏掉 Tier-2 物理链接）

> 规则：
> - 任何“合作/JV/园区/海外布局/客户线索”优先回溯到交易所披露原文 PDF（SSE/SZSE/CNINFO/HKEX 等），并在 References 里放 **可分享 URL**。
> - 若只能从东方财富/同花顺/雪球看到转述，默认降级为 D（线索/导航），并写出“升级路径”。
> - **强制线索保全（不丢失线索）**：每次任务必须运行 `python3 assets/tools/you_search_api.py --query "..." --out reports/<company>/<date>/<run>/sources/leads/you_search/<slug>.md`，
>   并把“可行动线索”填入下表（`Evidence grade = D`），同时在附录/References 中保留原始搜索结果文件路径。

| Lead (what we saw) | Primary filing (shareable URL) | Why it matters to the map | Evidence grade | Upgrade path (what to fetch next) |
|---|---|---|---|---|
|  |  |  |  |  |

## 2) 候选标准字段表（Candidate table）

| Field | Content |
|---|---|
| Theme | |
| Industry layer | raw material / device / module / system / end |
| Core product (choke node) | |
| Downstream must-pass customers | |
| Alternatives / supplier count | |
| Bottleneck evidence (lead time, price, sold-out, financing) | |
| Value capture evidence (mix, GM, ASP, backlog) | |
| Geography & policy | |
| Catalysts (3–9m hard; 12–18m confirm) | |
| Bear case | |
| Time window (3/6/12/24m) | |

## 3) 评分（Scoring；100分制）

Weights:
- Demand certainty: 20
- Supply concentration: 20
- Chokepoint property: 20
- Bottleneck strength: 15
- Value capture: 15
- Catalyst distance: 10

| Item | Score | Notes |
|---|---:|---|
| Demand certainty (20) |  |  |
| Supply concentration (20) |  |  |
| Chokepoint property (20) |  |  |
| Bottleneck strength (15) |  |  |
| Value capture (15) |  |  |
| Catalyst distance (10) |  |  |
| **Total (100)** |  |  |

## 4) 证据表（Evidence table；claims 必须可证伪）

| Claim (must be true) | Evidence channel | Primary source link/quote | Disconfirmers | Confidence |
|---|---|---|---|---|
|  |  |  |  |  |

## 5) 投资建议（Investment ideas；明确公司建议；非个性化）

> 方法：
> - 不把“谁是某单一客户（如 Tesla）的供应商”当作默认前提；除非有一手确认。
> - 倾向选择：attach rate 高 + 规格固化 + qualification 长 + 扩产周期长 的部件节点。

### 5.1 候选分层（Tier A/B/C）

| Tier | Definition |
|---|---|
| Tier A | 核心推荐：强相关 + 价值捕获更可验证 |
| Tier B | 次级推荐：相关但周期/分散度更高，需要更严格验证 |
| Tier C | 仅线索池：证据弱或主要来自传闻/聚合平台 |

### 5.2 公司建议表（必须带 Evidence grade）

Evidence grade（论据可靠性分级）：
- A：监管披露/年报/电话会逐字稿/IR deck
- B：公司 IR 新闻稿/公司综合报告/政府官网政策
- C：公司官网新闻/产品页（营销口径）
- D：媒体/第三方聚合（雪球/东方财富/同花顺等默认 D；只作线索/导航）

| Node | Company (Ticker) | Market | Recommendation (A/B/C) | Key evidence grade | Why it matters | What must be true (checklist) |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 6) 催化剂时钟（Catalyst clock）

- Hard catalysts (3–9m; must be calendarable):
- Confirmation catalysts (12–18m):

## 7) 风险与反证（Risks & disconfirming evidence）

- Substitution:
- Policy/geography:
- Cycle/valuation/liquidity:
- Execution/quality:

## 8) 审判结论（Judge verdict；需跑 verifier agent）

- Verdict:
- Required revisions:
- Top disconfirmers to monitor:

## References（论据引用；支持 PDF 内跳转与外链；可分享优先）

说明：
- 正文引用请使用 `[[R#]](#R#)`，以便在 PDF 内跳转到本节条目。
- **可分享优先**：References 里尽量只放可公开访问的 URL；避免 `sources/`、`Local snapshot`、本地磁盘路径。
- 中文财经平台（雪球/东方财富/同花顺）建议作为“补充源/导航”，不替代原文：优先回溯到交易所公告/公司年报/监管披露。

- <a id="R1"></a>**[R1]** [Title](https://example.com)
- <a id="R2"></a>**[R2]** [Title](https://example.com)
- <a id="R3"></a>**[R3]** [Title](https://example.com)
- <a id="R20"></a>**[R20]** [东方财富（公告/研报/聚合）](https://data.eastmoney.com/)
- <a id="R21"></a>**[R21]** [雪球（新闻/讨论聚合）](https://xueqiu.com/)
- <a id="R22"></a>**[R22]** [同花顺（公告/新闻聚合）](https://www.10jqka.com.cn/)
