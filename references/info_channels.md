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

## 1.2) Web 搜索（仅作线索导航，不作一手证据）

用途定位（默认 T4）：
- 用来**避免漏掉独立博客/行业数据库/小站点**（例如某些人形机器人供应商梳理站），以及帮助你定位“原始公告/IR/监管披露”的入口链接。
- **不能直接把搜索结果页面当证据**：要沿着链接回溯到交易所公告 PDF / 公司 IR / 监管披露等一手来源。

推荐：**You Search API（provider：ModelHub；内置 key；更省事）**：`assets/tools/you_search_api.py`

用法：
- You Search API 基础搜索（输出到 Markdown）：\n  `python3 assets/tools/you_search_api.py --query "tesla optimus suppliers" --count 10 --out leads/you_search_optimus_suppliers.md`
- You Search API 限域搜索（可选）：\n  `python3 assets/tools/you_search_api.py --query "tesla optimus suppliers" --include-domains "optimusk.blog" --out leads/you_search_site.md`

落库（推荐）：
- 对你判定“值得追踪”的站点，用 `assets/tools/register_source.py` 登记到 `references/source_registry.*`，并标注为 `T4`（线索/导航），同时写清“升级路径”（最终要引用到哪个披露/IR 原文）。

## 1.3) Serenity Twitter / X（仅作线索导航；不丢失弱信号）

用途定位（默认 T4）：
- 将 Serenity 在 Twitter/X 上发布的观点/线索作为“线索面（lead surface）”的一部分：用于捕捉 **供应链线索、关键节点猜想、潜在供应商名单、时间线与催化剂提醒**。
- 这些内容通常属于二手解读或观点，**不能直接当作一手证据**；必须回溯到：交易所披露 PDF、公司 IR/SEC、伙伴双方 PR、标准组织文件等。

必须保全的字段（避免线索在迭代中丢失）：
- Tweet 链接（可分享 URL）+ 发布时间（timestamp）+ 原文摘录（≤1–2 句）
- 它指向的“下一跳”证据入口（原文公告/IR/合同/采访/视频时间戳）
- 你对它的证据分级：默认 `Evidence grade = D`，除非 Tweet 本身就是“Anchor/供应商/标准组织”的官方账号发布且内容具备可核验性。

推荐工作流：
1) 用 `assets/tools/you_search_api.py` 做限域搜索，把 Serenity Twitter/X 的相关结果落盘保存到任务目录：
   - 示例：`python3 assets/tools/you_search_api.py --query "Serenity bottleneck Optimus supply chain" --include-domains "x.com,twitter.com" --out reports/<company>/<date>/<run>/sources/leads/you_search/serenity_x.md`
2) 在研报 Section **1.5**（交易所披露线索表）新增一行或多行：
   - `Lead (what we saw)` 写 Tweet 的核心线索
   - `Primary filing` 留空或写“待回溯”
   - `Evidence grade` 写 `D`
   - `Upgrade path` 写清楚下一步要抓哪份披露（SSE/SZSE/CNINFO/HKEX/SEC/IR/双方 PR）
3) 若 Tweet 指向了关键 PDF/IR/公告：
   - 立刻用 `assets/tools/fetch_snapshot.py` 保存原文快照到 `reports/<company>/<date>/<run>/sources/` 并登记到 source registry（T1/T2/T3 取决于原文类型）。

## 1.5) 交易所披露系统（SSE / SZSE / CNINFO / HKEX；供应链线索“必抓”）

用途定位（强烈推荐 T1/T2）：
- 供应链研究里，很多关键线索不会写在新闻稿里，而是出现在：**年度报告/临时公告/重大合同/对外投资/设立合资公司/海外园区布局**等披露文件里。
- 典型例子：公告里一句“与某公司在墨西哥园区共同出资设立合资企业”，即可把两家供应链节点**物理链接**起来（尤其适用于机器人/汽车零部件的 Tier-2 线索）。

你要抓的关键词（优先用原文 PDF grep/snippet）：
- 客户/供应商确认：`客户` / `供应商` / `Tier` / `定点` / `design-in` / `qualification`
- 合作与出海：`合资` / `共同出资` / `设立` / `协议` / `战略合作` / `Mexico` / `墨西哥` / `园区` / `工业园`
- 机器人相关：`人形机器人` / `机器人` / `减速器` / `丝杠` / `轴承` / `编码器` / `actuator`

强制工作流（避免漏线索）：
1) **先定位原文 PDF**（不引用聚合转述）：
   - 公告聚合平台可用于“导航”（默认 D）：东方财富/同花顺/雪球
   - 但最终 References 必须回溯到原文披露系统（SSE/SZSE/CNINFO/HKEX）的 PDF 链接
2) **对公告 PDF 跑线索提取**（快速扫盲，不代替全文阅读）：
   - 单文件：`python3 assets/tools/extract_pdf_snippets.py --in <file.pdf> --out <snips.md> --groups supplychain_leads,geo,capex`
   - 多链接批量：`python3 scripts/filing_lead_hunter.py --url-file urls.txt --out-dir leads/`
3) **把“线索 → 证据升级路径”写进研报**：
   - 线索来自公告原文 = 证据等级可到 A（监管披露）
   - 但“是否为某单一客户（如 Tesla）的供应商”仍需：双方文件/合同披露/明确客户名单 等进一步确认（避免把关系写死）

常见坑（必须规避）：
- 部分交易所静态域名可能有 WAF/JS 挑战，自动化脚本会下载到 HTML 而不是 PDF。
  - 识别方法：下载文件不是 `%PDF` 开头；`extract_pdf_snippets.py` 会直接报 “Input is HTML, not a PDF”。
  - 处理方法：用真实浏览器打开链接下载 PDF，再对本地 PDF 跑提取脚本。

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
