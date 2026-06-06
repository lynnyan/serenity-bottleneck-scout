# serenity-bottleneck-scout

Serenity 风格的 “chokepoint / bottleneck” 研报工作流 skill：从主题出发画供应链地图、抽取财报关键段落、生成 claims、并通过 **Reporter ⇄ Verifier Judge 多轮 debate** 强制做证据审判；最终输出同时保留 **Markdown + PDF**。

> 研报语言约束（强制）：研报正文以中文呈现；关键技术术语以英文呈现，并提供 Glossary（术语表，中文解释）。

## 你会得到什么

- 可重复的 7-step 研究流程（需求锚定 → 供应链地图 → chokepoint/bottleneck 判定 → 价值捕获 → 催化剂 → 反证 → 审判）
- 自动化产物：claims 列表、judge packet、财报关键段落抽取（risk/backlog/capex/geo）、PDF 渲染
- 供应商关系标注：`Anchor-confirmed / Not confirmed / Rumor / Unknown`（严格证据分级）
- 运行中发现的新数据源可沉淀：全局 source registry + 任务级快照

## 目录结构（核心）

- `SKILL.md` / `SKILL.zh-CN.md`：skill 使用说明（中英文需保持一致）
- `assets/templates/`：研报模板、judge/reporter prompt、供应商确认规则、PDF CSS
- `assets/tools/`：可复用的抓取/抽取/登记工具脚本
- `scripts/`：工作流编排脚本（生成研报骨架、debate bundle、judge bundle、PDF 渲染等）
- `references/`：信息渠道说明、source registry、数据源可用性 smoke targets
- `reports/<company>/<YYYY-MM-DD>/<run>/`：每次任务的所有中间产物 + 最终产物（强制）

## 快速开始（典型一次任务）

1) 创建任务骨架 + Round 1 Reporter 包（会落到 `reports/<company>/<date>/<run>/debate/round_1/`）：

```bash
python3 scripts/debate_bundle.py \
  --company "AnchorCo" --theme "..." --market "US / CN" --horizon "1-3y" \
  --create-report --date "YYYY-MM-DD" --run "run_01"
```

2) Round 1：让 Reporter 按 `debate/round_1/reporter_packet_round1.txt` 改写研报（在同一路径就地编辑），并保存回复到：
- `debate/round_1/reporter_response.md`

3) Round 1：准备 judge bundle 并让 Judge 审判（输出 `judge_packet.txt`，把 Judge 回复保存为 `judge_verdict.md`）：

```bash
python3 scripts/auto_judge.py \
  --report /path/to/report.md --theme "..." --horizon "1-3y" --round 1
```

4) 若 verdict=REVISE：生成 Round 2 Reporter 修订包并继续循环直到 APPROVE/REJECT：

```bash
python3 scripts/revision_bundle.py \
  --report /path/to/report.md \
  --judge-verdict /path/to/judge/round_1/judge_verdict.md \
  --next-round 2
```

5) APPROVE 后（强制）：在同目录渲染 PDF：

```bash
python3 scripts/render_report_pdf.py --in /path/to/report.md --out /path/to/report.pdf
```

## 数据源沉淀（运行中发现新来源）

- 全局 registry：`references/source_registry.md` + `references/source_registry.jsonl`
- 任务级（可选）：`reports/<company>/<date>/<run>/sources/source_registry_task.md`

登记命令：

```bash
python3 assets/tools/register_source.py \
  --name "..." --url "..." --tier T1|T2|T3|T4 --type "..." \
  --snapshot-path "reports/<company>/<date>/<run>/sources/xxx.pdf" \
  --task-dir "reports/<company>/<date>/<run>"
```

## 常用工具脚本（选用）

- SEC filings：`assets/tools/sec_edgar.py`（需要 `SEC_USER_AGENT`）
- Filing snippets（risk/backlog/capex/geo）：`assets/tools/extract_filing_snippets.py`
- PDF snippets（risk/backlog/capex/geo）：`assets/tools/extract_pdf_snippets.py`
- 网页/公告快照（HTML/PDF + meta）：`assets/tools/fetch_snapshot.py`
- 数据源登记：`assets/tools/register_source.py`

## 数据源可用性测试（持续性保障）

- 目标清单：`references/source_smoke_targets.json`
- 运行冒烟测试（会输出 `OK / BLOCKED / FAIL`；雪球常见 `BLOCKED` 属于现实约束）：

```bash
python3 scripts/source_smoke_test.py
```

- pytest（默认跳过网络；需要时显式开启）：

```bash
SERENITY_RUN_NET_TESTS=1 pytest -q tests/test_source_smoke_targets.py
```

## 环境变量

- `SEC_USER_AGENT`：SEC EDGAR 抓取所需（示例：`"YourName (contact: email@domain.com)"`）
- `SERENITY_RUN_NET_TESTS=1`：开启网络集成测试（默认关闭）

## 重要约束（避免误用）

- 供应商确认必须遵循 `assets/templates/supplier_confirmation_rules.md`：
  - `Anchor-confirmed` 必须有一手点名（Tesla/供应商/双方联合公告）
  - `Rumor` 只能表示“多源二手说法存在”，且必须写清升级路径
- 东方财富/同花顺/雪球等平台默认作为 T3/T4 线索来源：**不能直接作为一手证据**，必须尽量追溯到公告/财报/IR 原文或 PDF。
