---
name: serenity-bottleneck-scout
description: Serenity-style chokepoint/bottleneck stock research workflow. Build a supply-chain map, validate via IR/filings, partner PR, conferences, lead times, geography/policy, standards/PDKs, and price/volume. Includes reverse-debate verification by spawning a judge agent. General research only; not personalized financial advice.
metadata:
  short-description: Bottleneck investing research + debate verification
---

# Serenity Bottleneck Scout

This skill turns the “bottleneck / chokepoint investing” method into a repeatable workflow:
- Anchor **high-certainty demand**
- Draw the **full supply chain map**
- Separate **chokepoint** (must-pass interface) vs **bottleneck** (tight supply + price/lead-time control)
- Validate with multiple public evidence channels
- Force a **reverse debate** (judge agent) before treating the thesis as investable

## Safety rules

- Output is **general research**. Do not provide personalized buy/sell instructions, allocations, or suitability.
- Prefer primary sources where possible (filings, IR decks, earnings calls, official PR, standards bodies).
- Clearly label: assumptions, estimates, and what would falsify the thesis.

## Inputs (ask if missing)

- Theme: e.g. “optical interconnect / ELS / InP substrates”
- Market: US / CN / Global
- Candidate set: tickers or company names (can start with 3–10)
- Horizon: 0–6m / 1–3y / 3–5y

## Output (deliverables)

1) Supply-chain map (raw materials → substrates → devices → modules → systems → end customers) + key geography/policy exposures  
2) Candidate table (standard fields)  
3) Scoring (100-point) + explanation  
4) Catalyst clock (3–9m hard catalysts; 12–18m confirmation catalysts)  
5) Bear case / disconfirmers + position discipline (general, not personalized)  
6) **Judge verdict** (APPROVE / REVISE / REJECT) from a spawned verifier agent

Use templates from `assets/templates/`.

## Report language & terminology (required)

- Default output is **Chinese**.
- Key technical terms must appear in **English** (keep them consistent across the report), and include a short **Glossary** that explains them in Chinese.
  - Examples: `chokepoint`, `bottleneck`, `lead time`, `qualification`, `integrated actuator`, `backlog`, `capex`.

## PDF output (required)

For every final report, also produce a PDF next to the Markdown source:
- Markdown: `report.md`
- PDF: `report.pdf`

Renderer:
- `python3 scripts/render_report_pdf.py --in /path/to/report.md --out /path/to/report.pdf`

Notes:
- The first run may download the `md-to-pdf` renderer via `npx` (network required).
- Keep the Markdown as the source of truth; PDF is a rendered artifact.

## Core definitions

- **Chokepoint**: a “must-pass” interface/platform/standard entry point (the Strait analogy).
- **Bottleneck**: supply is tight and hard to expand, giving control over lead time / delivery / pricing.
- Best candidates are **both**.

## 7-step workflow (with thresholds)

Use the exact steps below (adapted from the provided Serenity report):

1) **Anchor high-certainty demand**
   - Evidence: Tier-1 earnings/capex, management commentary, industry conferences
   - Threshold: ≥2 independent primary signals confirming 12–24m expansion
2) **Draw the full supply chain map**
   - Must include: physical steps + key vendors + critical equipment + geography/policy points
   - Threshold: identify nodes where downstream “cannot route around”; best if ≤3 credible suppliers
3) **Determine chokepoint**
   - Evidence: standards/MSA/PDK, platform access, design-in / qualification, partner ecosystem
   - Threshold: connects to ≥2 Tier-1 downstream players OR sits at a standards/platform gate
4) **Determine bottleneck**
   - Evidence: lead times, sold-out language, shortages, capacity reservations, prepayments, price increases, expansion financing
   - Threshold: lead time >12 months = watch; >18 months = strong signal; add points if financing/capacity grabs appear
5) **Verify value capture**
   - Evidence: revenue mix, gross margin, ASP, backlog/order quality, BOM criticality
   - Threshold: plausible mix/profit step-up over next 4–8 quarters; capacity expansion >50% is a plus
6) **Set catalyst clock**
   - Evidence: earnings, conference dates, partner PR, plant ramp, policy dates
   - Threshold: ≥1 hard catalyst in 3–9 months AND ≥1 confirmation catalyst in 12–18 months
7) **Reverse-proof + discipline**
   - Evidence: substitution paths, geopolitics/export controls, customer switching, valuation/illiquidity
   - Rule: score <60 watch; 60–79 track/partial exposure; ≥80 only qualifies as “high conviction” (still non-personalized)

## Evidence channels (how to collect)

Open and follow:
- `references/info_channels.md` (what to pull from each channel, why it matters, and how to automate)
  - Includes an “authority statements” channel (founder/CEO/CTO) and a “new source registry” mechanism.

If you need scripts:
- SEC filings helper: `assets/tools/sec_edgar.py`
- Filing snippet extractor (risk/backlog/capex/geo): `assets/tools/extract_filing_snippets.py`
- PDF snippet extractor (risk/backlog/capex/geo): `assets/tools/extract_pdf_snippets.py`
- Price/volume helper: `assets/tools/price_ohlcv.py`
- RSS/PR helper: `assets/tools/rss_watch.py`
- Snapshot fetcher (HTML/PDF snapshot + meta): `assets/tools/fetch_snapshot.py`
- Source registry helper (persist newly discovered data sources): `assets/tools/register_source.py`
- Claims generator: `assets/tools/generate_claims.py`
- Report generator: `scripts/new_serenity_report.py`
- Auto-judge bundle prep: `scripts/auto_judge.py`
- Debate bundle (reporter packet + claims): `scripts/debate_bundle.py`
- External source availability smoke test (opt-in network): `scripts/source_smoke_test.py` (targets: `references/source_smoke_targets.json`)
- PDF renderer (Markdown → PDF): `scripts/render_report_pdf.py`

## Reverse debate / verification (spawn a judge agent)

After drafting a thesis pack, spawn a verifier agent to judge it harshly.

This step is **mandatory** in this skill: always run the judge before presenting the research as “ready”.

### Judge prompt

Use `assets/templates/judge_prompt.md` as the message to the verifier agent. Provide:
- the report text (or file path)
- the claims list (top 5–10 “must be true” statements)
- the evidence table you built

Optional helper:
- `assets/tools/build_judge_packet.py` to assemble a single “judge packet” message from your report + claims.
- `scripts/auto_judge.py` to generate both `claims.md` and `judge_packet.txt` in one run.

### What “passing” looks like

The judge must return:
- Verdict: APPROVE / REVISE / REJECT
- Top 5 weakest claims and what evidence would fix them
- 3 strongest disconfirmers and how to monitor them
- “Chokepoint vs bottleneck confusion” check
- Catalyst timing sanity check (is the clock real or hand-wavy?)
- Supplier confirmation audit: flag any “Anchor-confirmed” label without primary evidence.

## Supplier confirmation (anchor company)

When you list a “component-first universe”, label each company:
- Anchor-confirmed / Not confirmed / Rumor / Unknown

Rules live in:
- `assets/templates/supplier_confirmation_rules.md`

## New data sources (discovery → persistence)

During a run, if you discover a new useful data source (official IR hub, conference archive, database, standards portal, founder interview channel):
- Save a reproducible snapshot into the task folder when possible: `reports/<company>/<YYYY-MM-DD>/<run>/sources/`
- Register it into the global index:
  - `python3 assets/tools/register_source.py --name "..." --url "..." --tier T1|T2|T3|T4 --type "..." --date-published "..." --snapshot-path "..." --task-dir "reports/<company>/<YYYY-MM-DD>/<run>"`

Registry locations:
- Global: `references/source_registry.md` and `references/source_registry.jsonl`
- Per-task (optional): `reports/<company>/<YYYY-MM-DD>/<run>/sources/source_registry_task.md`

## Default report workflow (local files)

1) Start a multi-round workflow (Reporter ⇄ Verifier Judge):
   - `python3 scripts/debate_bundle.py --company "AnchorCo" --theme "..." --market "US / CN" --horizon "1-3y" --create-report --date "YYYY-MM-DD" --run "run_01"`
   - This creates a `reporter_packet_round1.txt` and `claims.md` in a debate run folder.
2) Spawn a **Reporter** agent (Round 1):
   - Send it the contents of `debate/round_1/reporter_packet_round1.txt` (created by `scripts/debate_bundle.py`).
   - Reporter edits the thesis pack file in place and fills evidence/catalysts.
   - Save the reporter’s response text under `debate/round_1/reporter_response.md` (so the full debate transcript is preserved).
3) Spawn a **Verifier Judge** agent (Round 1, required):
   - `python3 scripts/auto_judge.py --report /path/to/report.md --theme "..." --horizon "1-3y" --round 1`
   - Send `judge/round_1/judge_packet.txt` to the Judge agent.
   - Save the Judge output into `judge/round_1/judge_verdict.md`.
4) Multi-round debate loop (required, until convergence):
   - If verdict is **APPROVE**: stop; report is publishable.
   - If verdict is **REJECT**: stop; report is not supportable with current evidence.
   - If verdict is **REVISE**:
     - Create Reporter revision packet for next round:
       - `python3 scripts/revision_bundle.py --report /path/to/report.md --judge-verdict judge/round_1/judge_verdict.md --next-round 2`
     - Spawn **Reporter** agent with `debate/round_2/reporter_packet.txt` and have it revise the report.
     - Save the reporter’s response text under `debate/round_2/reporter_response.md`.
     - Re-run Judge for the new round:
       - `python3 scripts/auto_judge.py --report /path/to/report.md --theme "..." --horizon "1-3y" --round 2 --extra-file judge/round_1/judge_verdict.md`
     - Save verdict into `judge/round_2/judge_verdict.md`, then repeat (Round 3, Round 4...) until APPROVE/REJECT or you hit your max rounds (recommend 3–5).
5) After APPROVE (required): render PDF next to the Markdown:
   - `python3 scripts/render_report_pdf.py --in /path/to/report.md --out /path/to/report.pdf`

## Output folder convention (company/date)

All artifacts for a task live under:
- `reports/<company>/<YYYY-MM-DD>/`

If you run multiple tasks on the same company/date, add a run subfolder:
- `reports/<company>/<YYYY-MM-DD>/<run>/`

Inside that folder:
- report(s): `*.md` (default: Chinese report) and `*.pdf` (rendered)
- debate artifacts: `debate/round_*/`
- judge artifacts: `judge/round_*/`
