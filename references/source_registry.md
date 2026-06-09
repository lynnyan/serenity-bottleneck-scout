# Source Registry (living index)

This file is a **living index of evidence channels and specific sources** discovered while running the skill.

Rules:
- Prefer **primary** sources; label credibility tier.
- When a new source is discovered during a run, add it here **and** (optionally) to the task folder under `reports/<company>/<date>/<run>/sources/`.
- Keep entries short; store full snapshots under the task’s `sources/` folder.

## Credibility tiers

- **T1 Primary**: filings, official IR decks, official press releases, standards bodies, official conference proceedings, patents.
- **T2 High-quality secondary**: reputable mainstream outlets with original reporting and clear provenance.
- **T3 Secondary / market**: trade press, interviews without transcript, analyst notes, event recaps (use with caution).
- **T4 Rumor / social**: reposts, anonymous claims, unverified “channel checks”.

## Entries (append-only)

<!-- New entries appended by tools/scripts. -->

### CNINFO IR activity records (SZSE)
- Tier: `T1`
- Type: `exchange IR platform`
- URL: https://irm.cninfo.com.cn
- Found-at (UTC): 2026-06-06T09:35:57+00:00
- Why: Primary channel for investor activity records and official attachments
- Notes: Often provides PDF attachments; prefer saving snapshots into task sources/
### Eastmoney (portal)
- Tier: `T3`
- Type: `finance portal`
- URL: https://www.eastmoney.com
- Found-at (UTC): 2026-06-06T09:54:14+00:00
- Why: Secondary channel for market narrative; often links to official filings
- Notes: Treat as non-primary; prefer following through to CNINFO/SSE/SZSE/HKEX PDFs
### Eastmoney notices hub
- Tier: `T3`
- Type: `notices aggregator`
- URL: https://data.eastmoney.com/notices
- Found-at (UTC): 2026-06-06T09:54:14+00:00
- Why: Often contains links to official notice PDFs
- Notes: Use to discover official PDF URLs; snapshot only for reproducibility
### Eastmoney Caifuhao
- Tier: `T4`
- Type: `UGC / influencer posts`
- URL: https://caifuhao.eastmoney.com
- Found-at (UTC): 2026-06-06T09:54:14+00:00
- Why: Rumor and narrative discovery
- Notes: Do not treat as confirmation; must upgrade via primary documents
### 10jqka (Tonghuashun)
- Tier: `T3`
- Type: `finance portal`
- URL: https://www.10jqka.com.cn
- Found-at (UTC): 2026-06-06T09:54:15+00:00
- Why: Secondary channel for news/aggregation; can surface leads
- Notes: Often anti-scrape; treat as non-primary
### Xueqiu
- Tier: `T4`
- Type: `community / UGC`
- URL: https://xueqiu.com
- Found-at (UTC): 2026-06-06T09:54:15+00:00
- Why: Rumor, sentiment, link discovery
- Notes: Do not treat as confirmation; follow through to original sources
### Tesla Q1 2026 Update (IR PDF)
- Tier: `T1`
- Type: `IR update deck`
- URL: https://assets-ir.tesla.com/tesla-contents/IR/TSLA-Q1-2026-Update.pdf
- Published: 2026-04-??
- Found-at (UTC): 2026-06-06T12:43:55+00:00
- Snapshot: `reports/tesla/2026-06-06/run-01/sources/web/TSLA-Q1-2026-Update.pdf`
- Why: Contains disclosed robot manufacturing line intent (1M/10M robots/year)
### Tesla Q4 2025 Update (IR PDF)
- Tier: `T1`
- Type: `IR update deck`
- URL: https://assets-ir.tesla.com/tesla-contents/IR/TSLA-Q4-2025-Update.pdf
- Published: 2026-01-??
- Found-at (UTC): 2026-06-06T12:43:55+00:00
- Snapshot: `reports/tesla/2026-06-06/run-01/sources/web/TSLA-Q4-2025-Update.pdf`
- Why: Contains Optimus production timeline language
### Tesla 2025 10-K (IR PDF)
- Tier: `T1`
- Type: `SEC filing (10-K PDF mirror)`
- URL: https://ir.tesla.com/_flysystem/s3/sec/000162828026003952/tsla-20251231-gen.pdf
- Published: 2026-01-29
- Found-at (UTC): 2026-06-06T12:43:55+00:00
- Snapshot: `reports/tesla/2026-06-06/run-01/sources/web/tsla-20251231-gen.pdf`
- Why: Primary disclosure that Tesla develops/commercializes AI robots (Bots)
### MIIT humanoid robot guidance (PDF)
- Tier: `T1`
- Type: `policy document`
- URL: https://www.ncsti.gov.cn/kjdt/tzgg/202311/P020231103479626066804.pdf
- Published: 2023-10-20
- Found-at (UTC): 2026-06-06T12:43:55+00:00
- Snapshot: `reports/tesla/2026-06-06/run-01/sources/web/MIIT_humanoid_guidance_2023-10-20.pdf`
- Why: China policy baseline for humanoid robot industrial chain
### Tesla patent WO2024072984A1 (Actuator design)
- Tier: `T1`
- Type: `patent`
- URL: https://patents.google.com/patent/WO2024072984A1/en
- Published: 2024
- Found-at (UTC): 2026-06-06T12:43:55+00:00
- Snapshot: `reports/tesla/2026-06-06/run-01/sources/web/tesla_patent_WO2024072984A1.pdf`
- Why: Primary technical evidence about actuator and actuator design methodology
### Tuopu Group 601689 2025 Annual Report
- Tier: `T1`
- Type: `annual report (CNINFO)`
- URL: https://static.cninfo.com.cn/finalpage/2026-03-24/1225026446.PDF
- Published: 2026-03-24
- Found-at (UTC): 2026-06-09T07:19:17+00:00
- Snapshot: `reports/tesla/2026-06-09/run-02/sources/filings/cn/tuopu_601689_2025_annual_report.pdf`
- Why: Primary disclosure for robot actuator business and overseas footprint
### Sanhua 002050 2025 Annual Report
- Tier: `T1`
- Type: `annual report (PDF)`
- URL: https://notice.10jqka.com.cn/api/pdf/cb562f0b53fd48c9_1774270293/%E4%B8%89%E8%8A%B1%E6%99%BA%E6%8E%A7%EF%BC%9A2025%E5%B9%B4%E5%B9%B4%E5%BA%A6%E6%8A%A5%E5%91%8A.pdf
- Published: 2026-03
- Found-at (UTC): 2026-06-09T07:19:29+00:00
- Snapshot: `reports/tesla/2026-06-09/run-02/sources/filings/cn/sanhua_002050_2025_annual_report.pdf`
- Why: Primary disclosure for bionic robot electromechanical actuators expansion
- Notes: If available, prefer swapping URL to CNINFO/SZSE canonical.
### Wuzhou Xinchun 603667 2024 Annual Report
- Tier: `T1`
- Type: `annual report (CNINFO)`
- URL: https://static.cninfo.com.cn/finalpage/2025-04-29/1223385949.PDF
- Published: 2025-04-29
- Found-at (UTC): 2026-06-09T07:19:40+00:00
- Snapshot: `reports/tesla/2026-06-09/run-02/sources/filings/cn/wuzhouxinchun_603667_2024_annual_report.pdf`
- Why: Primary disclosure on planetary roller screw strategy for embodied/intelligent robots
### Lvd Harmonic 688017 2025 Annual Report
- Tier: `T1`
- Type: `annual report (PDF)`
- URL: https://stockmc.xueqiu.com/202604/688017_20260423_EU45.pdf
- Published: 2026-04-23
- Found-at (UTC): 2026-06-09T07:19:52+00:00
- Snapshot: `reports/tesla/2026-06-09/run-02/sources/filings/cn/leaderdrive_like_688017_2025_annual_report.pdf`
- Why: Primary disclosure on harmonic drive business and robotics-related subsidiaries
- Notes: Prefer CNINFO/SSE canonical if later located.
### Serenity (@aleabitoreddit) Twitter/X lead sweep (Optimus)
- Tier: `T4`
- Type: `social lead sweep`
- URL: reports/tesla/2026-06-09/run-02/sources/leads/you_search/serenity_x_optimus.md
- Published: 2026-06-09
- Found-at (UTC): 2026-06-09T07:20:05+00:00
- Why: Preserve weak-signal leads; must be upgraded to filings/IR/PR
