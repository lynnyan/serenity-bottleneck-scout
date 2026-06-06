---
name: serenity-bottleneck-scout-zh
description: （中文审阅版）Serenity 风格的 chokepoint / bottleneck 选股研究流程：画供应链地图，并用 IR/财报、伙伴 PR、行业会议、lead time、地理与政策、标准/PDK、股价成交量等多渠道验证；强制通过 spawn 的审判 agent 做反向论证。仅供一般研究，不构成个性化投资建议。
metadata:
  short-description: （中文）瓶颈研究 + 审判验证
---

# Serenity Bottleneck Scout（中文审阅版）

这个 skill 把“瓶颈 / chokepoint 投资法”改写为可重复执行的研究流程：
- 锚定**高确定性需求**
- 画出**完整供应链图**
- 区分 **chokepoint**（必经接口）与 **bottleneck**（供给紧 + 交付/价格/lead time 控制权）
- 用多类公开信息渠道交叉验证
- 在把研报视为“可用”之前，强制进行一次**反向辩论/审判**（spawn judge agent）

## 安全与边界

- 输出为**一般性研究**：不提供个性化买卖指令、仓位比例、适配性判断。
- 尽量优先一手资料：财报/年报/公告、IR 材料、电话会、官方 PR、标准组织文件等。
- 需明确标注：假设、估算、以及“什么证据会推翻 thesis”。

## 输入（缺失则先问）

- 主题：例如 “optical interconnect / ELS / InP substrates”
- 市场：US / CN / Global
- 候选集合：ticker 或公司名（可先从 3–10 个开始）
- 周期：0–6m / 1–3y / 3–5y

## 输出（交付物）

1) 供应链地图（原料 → 衬底 → 器件 → 模块 → 系统 → 终端客户）+ 地理/政策暴露  
2) 候选标准字段表（统一模板）  
3) 100 分制打分 + 解释  
4) 催化剂时钟（3–9 个月硬催化；12–18 个月确认催化）  
5) Bear case / 反证线索 + 纪律（一般性，不个性化）  
6) **审判结论**（APPROVE / REVISE / REJECT）：由 spawn 出来的 verifier/judge agent 给出  

模板位于：`assets/templates/`。

## 报告语言与术语（强制）

- 默认输出为**中文研报**。
- 关键技术术语必须以**英文**呈现（全篇统一用词），并在报告中提供一个 **Glossary（术语表）** 用中文解释。
  - 示例：`chokepoint`, `bottleneck`, `lead time`, `qualification`, `integrated actuator`, `backlog`, `capex`。

## PDF 输出（强制）

每份最终研报必须同时保留 Markdown 与 PDF 两种版本（同目录）：
- Markdown：`report.md`
- PDF：`report.pdf`

渲染命令：
- `python3 scripts/render_report_pdf.py --in /path/to/report.md --out /path/to/report.pdf`

说明：
- 首次运行可能通过 `npx` 下载 `md-to-pdf` 渲染器（需要网络）。
- Markdown 为“事实源”；PDF 仅为渲染产物。

## 核心定义

- **Chokepoint（必经口）**：必须经过的接口/平台/标准入口（“海峡”比喻）。
- **Bottleneck（供给瓶颈）**：供给紧且难扩，导致交期/交付/价格具有控制权。
- 最理想标的是二者**同时成立**。

## 7 步流程（含阈值）

严格按下面步骤执行（来自你提供的 Serenity report 的可执行化抽象）：

1) **锚定高确定性需求**
   - 证据：Tier-1 财报/资本开支、管理层表述、行业会议
   - 阈值：≥2 个独立的一手信号同时确认未来 12–24 个月扩张
2) **画完整供应链图**
   - 必须包含：物理步骤 + 关键供应商 + 关键设备 + 地理/政策点
   - 阈值：找到“下游无法绕过”的节点；最好 ≤3 家可信供应商
3) **判定 chokepoint**
   - 证据：标准/MSA/PDK、平台接入、design-in/qualification、伙伴生态
   - 阈值：连接 ≥2 个 Tier-1 下游生态，或处在标准/平台入口
4) **判定 bottleneck**
   - 证据：lead time、sold out、短缺、capacity reservation、预付款、涨价、扩产融资
   - 阈值：lead time >12 个月 = 可关注；>18 个月 = 强信号；若出现融资/抢产能等再加分
5) **验证价值捕获**
   - 证据：收入结构、毛利率、ASP、backlog/订单质量、BOM 关键性
   - 阈值：未来 4–8 个季度存在结构性抬升空间；产能扩张 >50% 加分
6) **安排催化剂时钟**
   - 证据：财报、会议日程、伙伴 PR、工厂投产/爬坡、政策日期
   - 阈值：3–9 个月内 ≥1 个硬催化 + 12–18 个月内 ≥1 个确认催化
7) **反证与纪律**
   - 证据：替代路径、地缘/出口、客户切换、估值/流动性
   - 规则：<60 仅观察；60–79 跟踪/部分暴露；≥80 才算“高确信度候选”（仍不个性化）

## 信息渠道（如何收集）

打开并按其指引执行：
- `references/info_channels.md`（每个渠道要抓的字段、为什么重要、以及如何用脚本半自动化）
  - 已包含“权威人士公开表述（创始人/CEO/CTO）”渠道，以及“新数据源沉淀”机制。

可用脚本（按需）：
- SEC 财报下载：`assets/tools/sec_edgar.py`
- 财报关键段落抽取（risk/backlog/capex/geo）：`assets/tools/extract_filing_snippets.py`
- PDF 关键段落抽取（risk/backlog/capex/geo）：`assets/tools/extract_pdf_snippets.py`
- 股价/成交量 OHLCV：`assets/tools/price_ohlcv.py`
- RSS/PR 抓取：`assets/tools/rss_watch.py`
- 网页/公告快照抓取（HTML/PDF + 元信息）：`assets/tools/fetch_snapshot.py`
- 数据源 registry（把运行中发现的新来源沉淀下来）：`assets/tools/register_source.py`
- 自动生成 claims：`assets/tools/generate_claims.py`
- 研报骨架生成：`scripts/new_serenity_report.py`
- 一键准备审判材料：`scripts/auto_judge.py`
- 多轮辩论打包（Reporter packet + claims）：`scripts/debate_bundle.py`
- 外部数据源可用性冒烟测试（可选网络集成测试）：`scripts/source_smoke_test.py`（目标：`references/source_smoke_targets.json`）
- PDF 渲染（Markdown → PDF）：`scripts/render_report_pdf.py`

## 反向辩论 / 审判验证（spawn judge agent）

完成 thesis pack 后，必须 spawn 一个 verifier/judge agent 进行审判。

本 skill 将该步骤视为**强制**：在拿到审判之前，不把研报视为“ready”。

### Judge prompt

使用 `assets/templates/judge_prompt.md` 作为 verifier agent 的消息模板。需要提供：
- 研报全文（或文件路径）
- claims 列表（5–10 条“必须为真”的断言）
- 证据表（你整理的 evidence table）

可选辅助：
- `assets/tools/build_judge_packet.py`：把研报 + claims 拼成一份可直接发送的 judge packet。
- `scripts/auto_judge.py`：一键生成 `claims.md` 与 `judge_packet.txt`。

### 什么叫“通过”

Judge 必须返回：
- Verdict：APPROVE / REVISE / REJECT
- 最薄弱的 5 条关键断言 + 需要补的证据（明确对应渠道）
- 3 个最强反证与监控方法
- “chokepoint vs bottleneck 混淆”检查
- 催化剂时钟合理性检查（是否足够具体、是否被模糊叙事冒充）
- 供应商确认审计：任何标注为 “Anchor-confirmed” 的公司若无一手证据必须被指出。

## 供应商确认（锚定公司/Anchor）

当你在“组件优先候选池”里列公司时，必须标注：
- Anchor-confirmed / Not confirmed / Rumor（传闻）/ Unknown

规则文件：
- `assets/templates/supplier_confirmation_rules.md`

## 新数据源沉淀（发现 → 复用）

每次任务运行过程中如果发现新的有效数据源（例如：公司 IR 入口、会议资料库、行业数据库、标准组织入口、创始人/高管采访频道）：
- 能下载就先把快照保存到任务目录：`reports/<company>/<YYYY-MM-DD>/<run>/sources/`
- 再把来源登记到全局 registry（可选同时写入任务 registry）：
  - `python3 assets/tools/register_source.py --name "..." --url "..." --tier T1|T2|T3|T4 --type "..." --date-published "..." --snapshot-path "..." --task-dir "reports/<company>/<YYYY-MM-DD>/<run>"`

登记位置：
- 全局：`references/source_registry.md` 与 `references/source_registry.jsonl`
- 任务（可选）：`reports/<company>/<YYYY-MM-DD>/<run>/sources/source_registry_task.md`

## 默认本地工作流

1) 启动多轮工作流（Reporter ⇄ Verifier Judge）：
   - `python3 scripts/debate_bundle.py --company "AnchorCo" --theme "..." --market "US / CN" --horizon "1-3y" --create-report --date "YYYY-MM-DD" --run "run_01"`
   - 生成一份 `reporter_packet_round1.txt` 和 `claims.md`（位于 debate run 文件夹）。
2) spawn 一个 **Reporter**（第 1 轮）：
   - 把 `debate/round_1/reporter_packet_round1.txt` 的内容发给 Reporter（由 `scripts/debate_bundle.py` 生成）。
   - Reporter 在研报文件中补齐证据/地图/催化剂。
   - 将 Reporter 的回复文本保存到 `debate/round_1/reporter_response.md`（保留完整的辩论记录）。
3) spawn 一个 **Verifier Judge**（第 1 轮，必做）：
   - `python3 scripts/auto_judge.py --report /path/to/report.md --theme "..." --horizon "1-3y" --round 1`
   - 把 `judge/round_1/judge_packet.txt` 发给 Judge。
   - 将 Judge 输出保存为 `judge/round_1/judge_verdict.md`。
4) 多轮 debate（必做，直到收敛）：
   - 若 verdict = **APPROVE**：停止，研报可发布。
   - 若 verdict = **REJECT**：停止，说明在当前证据条件下 thesis 不成立或不可证伪。
   - 若 verdict = **REVISE**：
     - 生成下一轮 Reporter 修订包：
       - `python3 scripts/revision_bundle.py --report /path/to/report.md --judge-verdict judge/round_1/judge_verdict.md --next-round 2`
     - 用 `debate/round_2/reporter_packet.txt` spawn Reporter 进行改稿。
     - 将 Reporter 的回复文本保存到 `debate/round_2/reporter_response.md`。
     - 进入下一轮审判：
       - `python3 scripts/auto_judge.py --report /path/to/report.md --theme "..." --horizon "1-3y" --round 2 --extra-file judge/round_1/judge_verdict.md`
     - 将 verdict 保存为 `judge/round_2/judge_verdict.md`，然后继续（第 3 轮、第 4 轮…），直到 APPROVE/REJECT 或达到最大轮数（建议 3–5）。
5) APPROVE 后（必做）：在 Markdown 同目录渲染 PDF：
   - `python3 scripts/render_report_pdf.py --in /path/to/report.md --out /path/to/report.pdf`

## 输出目录规范（公司/日期）

每次任务的所有中间产物与最终产物统一放在：
- `reports/<company>/<YYYY-MM-DD>/`

若同一公司/日期下需要区分多次任务，增加 run 子目录：
- `reports/<company>/<YYYY-MM-DD>/<run>/`

目录内：
- 研报：`*.md`（默认中文）与 `*.pdf`（渲染产物）
- debate 中间产物：`debate/round_*/`
- judge 中间产物：`judge/round_*/`
