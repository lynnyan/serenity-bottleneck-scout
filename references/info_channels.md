# 信息渠道与获取方式（按 Serenity report 整理）

本文件用于：当你需要“去哪找证据、找哪些字段、如何把碎片证据拼成一张地图”时打开。

## 1) 公司 IR / 财报 / 电话会（第一优先级）

要抓的字段：
- 收入分项/业务结构、毛利率、ASP、backlog、订单质量
- 扩产/资本开支/融资、产能利用率、交付约束措辞
- 地理暴露（工厂/原料/客户），出口许可/制裁/关税风险

为什么重要：
- 用来确认“需求是否真的传导到公司层”，以及是否有价值捕获迹象。

可半自动化：
- US 公司：`assets/tools/sec_edgar.py` 拉取 10-K/10-Q/8-K 并定位风险因素/业务结构等段落。
- 抽取关键段落（risk/backlog/capex/geo）：先用 `assets/tools/sec_edgar.py --download` 下载 primary doc，再用 `assets/tools/extract_filing_snippets.py --in <file>` 输出 `filing_snippets.md` 供快速定位。

## 2) 伙伴合作与客户 PR（验证生态位的最强证据之一）

要抓的字段：
- 客户名/伙伴名、路线图、平台接入、联合开发、量产时间线
- 关键技术词：MSA/PDK/qualification/design-in/production ramp

为什么重要：
- 用来证明“chokepoint 是否已被主流生态接入”，避免凭空推演。

可半自动化：
- 订阅公司新闻/RSS：`assets/tools/rss_watch.py`
- 对关键伙伴/客户做交叉验证（同一合作是否被双方公开确认）。

## 3) 行业会议与展示（OFC/APEC/Analyst day/资本市场日）

要抓的字段：
- 展示了什么 demo、谁在台上联合发布、是否出现“客户带站台”
- 新标准、新 MSA、新平台/PDK 的发布时间点

为什么重要：
- 很多“瓶颈”先在行业会被验证，后才在财报中被市场理解。

操作建议：
- 建一个“会议-日期-公司-关键词”表；把它纳入 catalyst clock。

## 3.5) 创始人 / 权威人士的公开表述（CEO/CTO/首席科学家/项目负责人）

要抓的字段：
- 关键判断：量产时间线、产能目标、成本/良率瓶颈、关键零部件自研 vs 外购策略、供应链约束措辞
- 可核验细节：具体数量、里程碑、地点/产线、交付/认证状态（避免纯愿景叙事）
- 明确“范围”：是个人观点、媒体转述、还是公司正式口径（记录来源与场景）

为什么重要：
- 在很多新产业（如机器人/AI 供应链）里，**最早的“硬信息”**往往先出现在核心负责人公开表述里，晚于此才进入财报口径。

证据分级（强 → 弱）：
1) **公司官方渠道**：财报电话会/官方文字纪要、IR 日/资本市场日官方稿、官网新闻稿/演讲稿（可视作高质量二手或准一手）。
2) **权威媒体原文采访**：有原始录音/视频/逐字稿可回溯（必须保留原链接/时间戳）。
3) **第三方纪要/转述**：券商/自媒体整理（只能作为 Rumor/线索，不能直接当作 Anchor-confirmed）。

操作规范（避免“口径污染”）：
- 必须写清：日期、场景（电话会/采访/路演）、发言人身份、原文引用（≤25 字）或可定位段落。
- 如果只有“转述”，默认降级为 **Rumor**，并在研报中写出“升级路径”（需要哪份一手文件确认）。

## 4) Lead time / 交付周期（bottleneck 强度的硬抓手）

要抓的字段：
- sold out/供不应求/交付受限措辞
- 交期周数、设备安装周期、资格认证周期

为什么重要：
- bottleneck 的核心是交付/价格控制权，而不是“产业链位置高”。

操作建议：
- 对每个节点建立 lead time 时间序列（即便是手工记录）。

## 5) 产能与工厂地理（政策/地缘风险与单点故障）

要抓的字段：
- fab/工厂地点、关键原料来源、是否单厂、是否跨境审批
- 供应链持股/垂直整合（例如原料股权）

为什么重要：
- 物理点位决定政策风险与扩产速度，也决定“供给紧张”是否由政策驱动。

## 6) 技术标准 / 平台入口（PDK/MSA/兼容性/设计流）

要抓的字段：
- 是否进入某平台/PDK、是否成为标准接口的一部分、兼容性/生态绑定

为什么重要：
- chokepoint 往往是“标准化入口”，不是单一产品参数。

## 7) 历史股价与成交量（交易性脉冲 vs 经营验证）

要抓的字段：
- 价格与成交量异常是否先于财务兑现
- 是否被社媒放大（事件驱动），还是基本面逐季确认

为什么重要：
- 把“交易催化”和“经营验证”分开评分，避免叙事领先过多导致回撤。

可半自动化：
- `assets/tools/price_ohlcv.py` 拉取 OHLCV 并输出 CSV。

## 7.5) 主流财经平台（东方财富 / 同花顺 / 雪球）

用途定位（默认 T3/T4，不做一手证据）：
- 用来捕捉 **市场叙事、传闻（Rumor）、券商/媒体转述、事件脉冲**，以及定位进一步核验的一手入口（公告 PDF、交易所披露、公司官网 IR）。
- 规则：这些平台的内容**默认不能用于 Anchor-confirmed**；除非它们提供的是“官方文件的原始 PDF/链接”，且你最终引用到原始文件本身。

### 东方财富（Eastmoney）

常见入口：
- 公告/披露聚合（常指向交易所/CNINFO 的 PDF）：`https://data.eastmoney.com/notices/`\n- 财富号（用户/机构号文章，强烈建议降级为 Rumor/T4）：`https://caifuhao.eastmoney.com/`\n- 研报/机构观点聚合（通常为二手总结）：`https://report.eastmoney.com/`

抓取建议：
- 优先抓“公告 PDF”的原始链接（CNINFO / SSE / SZSE / HKEX），把 PDF 存到任务目录 `sources/`。\n- 对财富号等 UGC：只作为 Rumor 线索，需同时记录“升级路径”（要什么一手材料才能确认）。

### 同花顺（10jqka）

常见入口：
- 公告/新闻聚合、互动问答/社区类内容（多数为二手/转述）

抓取建议：
- 重点用途是“定位线索”，不要把二次转载当作证据。\n- 如果页面有反爬/跳转，建议保存 HTML 快照到 `sources/` 并在证据表标注为 T3/T4。

### 雪球（Xueqiu）

常见入口：
- 用户讨论/长文、转发链路（T4 为主），偶尔有对公告/电话会的整理。

抓取建议：
- 仅作为 Rumor/情绪温度计/线索，不作为事实依据。\n- 对于“长文引用原始文件”的情况：务必跟到原始文件并引用原始文件。
- 现实情况：对自动化抓取通常存在 WAF/反爬，**不保证脚本可持续拉取**；建议把雪球定位为“人工浏览 + 线索定位”的渠道。

### 工具建议（按实际情况决定是否写脚本）

当你发现某平台经常被用来提供“可复用的证据入口”（例如稳定的公告 PDF 链接、稳定的页面结构），建议新增工具脚本并保留在：\n- `assets/tools/`（解析/抽取/快照）\n- `scripts/`（工作流编排）

默认推荐能力：
- 通用网页快照抓取（HTML/PDF 保存 + 元信息）：`assets/tools/fetch_snapshot.py`\n- 数据源登记（全局/任务级）：`assets/tools/register_source.py`

## 8) 自动生成 claims + 自动审判（强制验证）

目的：
- 用一组“必须为真”的断言强迫 thesis 可证伪；
- 通过 judge agent 的审判把逻辑漏洞和证据缺口暴露出来。

工具：
- `assets/tools/generate_claims.py`：根据主题/候选生成默认 claims 列表（可再手工微调）。
- `scripts/auto_judge.py`：一键生成 `claims.md` 与 `judge_packet.txt`（供 spawn verifier agent 使用）。

## 8.5) 新数据源沉淀（运行时发现 → 可复用资产）

目的：
- 研究过程中经常会遇到新的“权威人士采访/会议回放/行业数据库/交易所接口”等数据源。
- 为了避免每次重复摸索，把它们沉淀为 skill 的可复用资产：全局 registry + 任务级快照。

做法：
- 发现新来源后，先判断证据等级（T1..T4），并尽量下载/保存快照到任务目录 `reports/<company>/<date>/<run>/sources/`。
- 然后用工具写入全局 registry（可选同时写入任务 registry）：`assets/tools/register_source.py`。

命令示例：
- 仅写入全局 registry：\n  `python3 assets/tools/register_source.py --name \"Official conference keynote\" --url \"https://...\" --tier T2 --type \"conference video\" --date-published \"2026-05-01\" --why \"CEO gave hard capacity numbers\" --notes \"has timestamped video\"`\n+- 同时写入任务目录：\n  `python3 assets/tools/register_source.py --name \"IR webcast transcript\" --url \"https://...\" --tier T1 --type \"IR transcript\" --snapshot-path \"reports/<company>/<date>/<run>/sources/xxx.pdf\" --task-dir \"reports/<company>/<date>/<run>\"`

输出位置：
- 全局：`references/source_registry.md` + `references/source_registry.jsonl`\n- 任务：`reports/<company>/<date>/<run>/sources/source_registry_task.md`

## 9) 供应商“确认标注”（通用：针对本报告的 Anchor 公司）

当你在“组件优先候选池”里提到公司时，必须标注：
- Anchor-confirmed / Not confirmed / Rumor / Unknown

规则与证据要求：
- `assets/templates/supplier_confirmation_rules.md`

最低要求：
- 任何 “Anchor-confirmed” 都必须附带一手证据（Anchor 公司文件 / 供应商文件 / 双方 PR）与日期。
