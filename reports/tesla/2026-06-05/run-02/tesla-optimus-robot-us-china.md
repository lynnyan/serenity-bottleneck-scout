# Serenity Thesis Pack — tesla-optimus-robot-us-china

Date: 2026-06-05
Market: US / CN
Horizon: 1-3y
Candidates: 002050.SZ (三花智控) — watchlist (Tesla supplier status: Rumor); 688017.SH (绿的谐波) — watchlist (Tesla supplier status: Rumor)

## 0) Scope & assumptions

- What’s included/excluded:
  - Included: Tesla Optimus (humanoid robot) as **demand anchor**; US + China industrial policy + supply base context; **actuation stack** as the focal *bottleneck* candidate (precision reducers → integrated electromechanical actuators).
  - Excluded: full valuation work; detailed TAM; full competitive teardown of every humanoid program.
- Key assumptions (make these falsifiable):
  - Tesla continues to treat “Bots (including Optimus)” as a product line and invests to reach “volume production” within the 1–3y horizon. [R1]
  - Tesla’s disclosed manufacturing intent (line installation / factory preparations) continues to appear in quarterly updates through FY2026. [R2] [R3]
  - Humanoid robots require high-precision joint actuation (reducers + motors + drives + sensing) and the **manufacturing/qualification of these components** is a credible bottleneck in early scale-up (vs. “AI demo”). [R4]
  - Cross-border sourcing is uncertain; any company list in this pack is **not** a confirmed Tesla supplier list unless labeled **Anchor-confirmed** under the rules.
- What would change my mind (disconfirmers):
  - Tesla deprioritizes Optimus (e.g., filings stop mentioning “Bots/Optimus”, capital plans disappear, or timelines slip beyond 2027). [R1] [R3]
  - Tesla vertically integrates the critical actuation node fast enough that external suppliers do not capture margin (e.g., explicit “in-house reducer/actuator” claims + buildout evidence).
  - Clear substitution: Tesla (or peers) shift from precision reducers to alternative joint architectures (e.g., direct-drive or different reducer tech) with comparable cost/precision at scale.

## 1) Supply-chain map (must be physical and complete)

Raw materials → substrates → devices → modules → systems → end customers

- Map (component-first, end-to-end; *actuation stack focus*):
  - Raw materials: alloy steels (gears/shafts), copper (windings), permanent magnets (motors), aluminum (housings), lubricants.
  - Substrates/processes: forging/casting, heat treatment, precision machining, grinding/honing, coating, metrology.
  - Devices (critical for joints):
    - Precision reducer elements (e.g., strain-wave / “harmonic” class parts; bearings; flex components)
    - Motor (high power density) + thermal design
    - Servo drive / power electronics + control ICs
    - Joint sensing (position/torque; encoder + force/torque sensing)
  - Modules:
    - High-precision electromechanical actuator (reducer + motor + servo driver + sensing) as an integrated “joint”
    - Wiring harness + power distribution + safety interlocks
  - Systems:
    - Humanoid robot (Optimus-class) + fleet software + training / simulation pipeline
  - End customers:
    - Tesla internal deployments first, then external enterprise/consumer (if/when commercialized)
    - China-side: broad “humanoid” industrialization push across multiple application scenarios (policy-driven). [R4]
- Where the “must-pass” gates are (chokepoints vs bottlenecks):
  - **Chokepoint (must-pass gate across ecosystems): NOT PROVEN in available sources.** Do not treat reducers/actuators as a multi-ecosystem “standard gate” today; they are generally second-sourceable with time/capex.
  - **Bottleneck (capacity/tooling + qualification friction):** precision reducer + integrated actuator manufacturing needs specialized machining/heat treatment/metrology and reliability testing; scaling yield can be slow. This pack is framed as a *bottleneck hypothesis*, not a chokepoint claim. [R4]
- Where supply is physically constrained (what to measure):
  - Specialized equipment availability (precision gear grinding, metrology, heat treatment capacity) and yield learning curves.
  - Tight tolerances + reliability testing capacity (accelerated life / safety).
  - Component supply as a named constraint in anchor communications (“component supply”, “supply chain readiness”). [R2] [R3]
- Geography/policy single points (US + China):
  - US: Tesla robotics production planning referenced at Fremont and Texas (per Q1 2026 update). [R3]
  - China: state policy explicitly calls out key component breakthroughs (incl. reducers/motors/drives) and building a “safe, reliable industrial chain and supply chain system” by 2027. [R4]
  - Cross-border: tariffs/export controls and localization incentives can accelerate dual-sourcing and shorten/lengthen qualification cycles (monitor in filings + policy updates).

## 2) Candidate table (standard fields)

| Field | Content |
|---|---|
| Theme | Tesla Optimus (humanoid) — US + China |
| Industry layer | device → module (precision reducers / integrated electromechanical actuators) |
| Core product (bottleneck node) | **High-precision joint actuation**: reducer + high power-density motor + servo drive + sensing packaged as a repeatable module (manufacturing throughput + qualification/reliability friction). [R4] |
| Downstream must-pass customers | Humanoid robot OEMs/system integrators; *Anchor demand*: Tesla “Bots (including Optimus)” program (supplier status to Tesla is **Anchor-confirmed / Rumor / Unknown** per rules; do not treat any node as confirmed without primary evidence). [R1] |
| Candidate(s) to watch (CN) | **三花智控 (002050.SZ)** — “仿生机器人机电执行器” expansion in annual report; Tesla supplier status: **Rumor** (non-primary sources claim it; official IR record does not confirm). [R8] [R9] [R10] [R11] [R13] [R14] <br> **苏州绿的谐波 (688017.SH)** — harmonic reducers + “mechatronic actuators” (per its annual report). Tesla supplier status: **Rumor** (non-primary sources claim it; no anchor/supplier filing confirmation in this pack). [R5] [R10] [R12] [R14] |
| Alternatives / supplier count | Alternatives exist at the technology level (different reducer architectures; more in-house integration), but qualification + yield can keep the “credible supplier set” small for any frozen actuator design generation (track with customer wins and capacity additions). |
| Bottleneck evidence (lead time, price, sold-out, financing) | **Threshold check (lead time/backlog): FAIL (no primary lead-time/backlog).** Available primary text only supports “line prep” + “supply chain readiness” language, not >12m lead times. [R2 p8] [R3 p6] |
| Value capture evidence (mix, GM, ASP, backlog) | **Threshold check (assigned value-capture line item): FAIL / UNASSIGNED.** This pack does not yet tie the bottleneck to a specific disclosed pricing/backlog metric for a single public company. Treat as verification work. |
| Geography & policy | US: Tesla lines planned at Fremont/Texas (Q1 2026 update). [R3] China: policy targets 2025 milestone and 2027 supply-chain system, and explicitly calls for breakthroughs in “high torque density reducers, motors, servo drives” for actuators. [R4] |
| Catalysts (3–9m hard; 12–18m confirm) | See §5 (Catalyst clock) — deadlines anchored to Tesla quarterly disclosures and year-end “start of production before end of 2026” language. [R2] [R3] |
| Bear case | Tesla in-houses the bottleneck node; alternative joint architectures commoditize reducers; China overbuild leads to price pressure; qualification is faster than expected; or Optimus timeline slips. |
| Time window (3/6/12/24m) | 3–6m: new disclosures (Tesla Q2/Q3 2026) + China local policy follow-through. 12m: evidence of installed production line + pilot output. 24m: evidence of volume production + stable module standard. |

## 3) Scoring (100-point)

Weights:
- Demand certainty: 20
- Supply concentration: 20
- Chokepoint property: 20
- Bottleneck strength: 15
- Value capture: 15
- Catalyst distance: 10

| Item | Score | Notes |
|---|---:|---|
| Demand certainty (20) | 14 | Tesla intent + factory/line plans are explicit, but Tesla-specific deployment demand is not independently confirmed; CN peers show commercialization momentum. [R1] [R3 p6] [R6 p25] [R7 p1] |
| Supply concentration (20) | 6 | No supplier count / switching-cost proof in provided sources; treat as unknown. |
| Chokepoint property (20) | 1 | **Not proven** as a must-pass gate across ecosystems (explicitly downgraded). |
| Bottleneck strength (15) | 7 | Some “supply chain readiness” / capacity-utilization language exists, but no dated lead-time/backlog to clear the >12m threshold. [R2 p8] [R5 p23] |
| Value capture (15) | 4 | Not mapped to a specific pricing/backlog/GM metric for a single company yet (verification gap). |
| Catalyst distance (10) | 8 | Time-bounded disclosures exist (10‑Q dates + “before end of 2026”). [R2 p8] |
| **Total (100)** | **40** | Honest score: this is a verification-ready bottleneck hypothesis, not yet an evidence-cleared bottleneck thesis. |

## 4) Evidence table (claims must be falsifiable)

| Claim (must be true) | Evidence channel | Primary source link/quote | Disconfirmers | Confidence |
|---|---|---|---|---|
| Tesla positions Optimus inside a disclosed “Bots” product line in FY2025 10‑K. | Anchor filing (sectioned) | “AI robots (“Bots”) (including Optimus).” (Note 1 – Overview) [R1] | “Bots/Optimus” language removed from FY2026 filings. | Med |
| Tesla discloses specific manufacturing intent (Fremont 1M/yr line; Texas 10M/yr design) for Optimus. | Anchor quarterly update (paged) | “designed for 1 million robots a year… 10 million robots.” (p6) [R3 p6] | Later updates remove/soften the line/capacity language or contradict it. | Med |
| Tesla discloses a time-bounded production target (“before end of 2026”). | Anchor quarterly update (paged) | “start of production planned before the end of 2026.” (p8) [R2 p8] | Production start slips; “before end of 2026” removed; no evidence of line buildout. | Med |
| Independent CN primary signals show “humanoid robots” are generating revenue and deliveries (not only demos). | Peer issuer results (paged) | UBTECH: “Walker S2… started mass production and delivery officially.” (p2) [R7 p2] | Subsequent results show delivery reversal/cancellations; revenue collapses. | Med |
| CN peer financials show material humanoid revenue and unit sales (demand signal, not Tesla-specific). | Peer issuer results (paged) | UBTECH: “revenue… humanoid robot… to RMB820.6 million.” (p1) [R7 p1] | Revenue reclassified away from humanoids; margins collapse. | Med |
| Another CN peer discloses humanoid robots as core revenue mix and “rapid growth” trend. | Peer prospectus/filing (paged) | Unitree: “主营业务收入…四足机器人与人形机器人…快速增长趋势。” (p25) [R6 p25] | Updated filings show humanoid revenue is immaterial or shrinking. | Med |
| China policy explicitly prioritizes actuator components (reducers/motors/drives) as key breakthroughs for humanoids. | China primary policy (paged) | “突破高力矩密度减速器、高功率密度电机、伺服驱动器…” (p5) [R4 p5] | Policy deprioritized; substitution reduces actuator performance requirements. | Med |
| A CN actuator component supplier claims high capacity utilization + scale-up, consistent with potential bottleneck pricing power *if* demand sustains. | Supplier annual report (paged) | 绿的谐波: “产能利用率保持高位运行.” (p23) [R5 p23] | Utilization falls; pricing pressure; no sustained robotics demand. | Low→Med |
| **Lead-time bottleneck claim (>12m) is NOT evidenced today.** | Evidence-gap flag | No dated lead-time/backlog quotes tied to the actuation node are present in the provided sources. | A credible primary lead-time/backlog disclosure appears (supplier filings / OEM procurement / equipment lead times). | Low |
| **Supplier concentration (≤3) claim is NOT evidenced today.** | Evidence-gap flag | This pack does not name/confirm the top reducer/actuator suppliers for Tesla Optimus, nor switching/qualification time. | Customer concentration notes / named suppliers / teardown attribution emerges. | Low |
| **Value-capture-to-financials (4–8q) claim is NOT evidenced today.** | Evidence-gap flag | This pack does not yet map the bottleneck to a specific disclosed metric (pricing/backlog/segment GM) for one company. | A company discloses backlog/pricing/mix tied to humanoid actuator demand. | Low |

## 5) Catalyst clock

- Hard catalysts (3–9m from 2026-06-05):
  - Tesla Q2 2026 10‑Q (estimated due **2026-08-10**): look for *new* quantitative language (units, line status, capex) on Optimus factory/tooling and whether “component supply” appears as a constraint. [R2 p8] [R3 p6]
  - Tesla Q3 2026 10‑Q (estimated due **2026-11-09**): confirm whether Q2 “prep begins shortly in Q2” actually happened (construction/tool install updates). [R3 p6]
  - China policy follow-through (2026 H2): local implementation plans / standards / pilot procurement tied to the MIIT objectives (track official releases referencing the 2023 “指导意见”). [R4]
- Confirmation catalysts (12–18m from 2026-06-05):
  - **By 2026-12-31:** Tesla “start of production planned before the end of 2026” either happens or slips (binary milestone). [R2]
  - **By 2027-06-30:** evidence of sustained pilot output (e.g., repeated mentions of production rate improvement / deployment scale) and whether a stable actuator module standard has frozen (qualification moat forms).

## 6) Risks & disconfirming evidence

- Substitution:
  - Alternative joint architectures (direct drive, different reducer types, different actuator packaging) reduce the “must-pass” nature of harmonic reducers.
  - Software/controls improvements reduce the need for ultra-precision in hardware (lower-cost acceptable).
- Policy/geography:
  - Dual-sourcing and localization incentives can compress supplier power; conversely, cross-border friction can force slower qualification.
  - China policy sets direction but does not guarantee profitable outcomes (risk of overbuild and price competition).
- Cycle/valuation/liquidity (general research note):
  - Cyclical capex behavior in industrial automation can whipsaw orders; do not assume linear growth from policy or demos.
- Execution/quality:
  - Actuator reliability and safety certification cycles can delay volume ramp; yield learning curves can erode margins even if revenue grows.

## 7) Judge verdict (after spawning verifier agent)

- Verdict (Round 2): **REVISE** (not yet evidence-cleared as a chokepoint/bottleneck thesis).
- Verdict file: /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/judge/round_2/judge_verdict.md
- Required revisions (to reach APPROVE under this skill’s thresholds):
  - Prove (or change) the **must-pass gate** claim with primary evidence (standards/qualification/certification gate *across ecosystems*), or switch the node to one that is a true gate and re-map the supply chain accordingly.
  - Add **dated lead-time/backlog** evidence tied to the specific node (reducers/actuators or critical equipment), not generic robotics narratives.
  - Show **supplier concentration ≤3** *or* document qualification/switching time as a moat, with concrete sources.
  - Map **value capture** to an observable public KPI for at least one listed company within 4–8 quarters (segment GM/mix/backlog/ASP/utilization/pricing) and define pass/fail thresholds.
- Top disconfirmers to monitor (high priority):
  - Tesla slips “production before end of 2026” (watch Q2/Q3 2026 disclosures and whether the milestone is reaffirmed or softened). [R2 p8] [R3 p6]
  - Rapid multi-source / commoditization in China (watch utilization + ASP/margin language in supplier reports). [R5]
  - Actuation architecture shift (direct drive / alternate reducers reduce harmonic relevance).

## References

- [R1] Tesla 2025 10‑K HTML snippet file (extracted): /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/filing_snippets_tsla_10k.md
- [R2] Tesla Q4 2025 Update (PDF): /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/TSLA-Q4-2025-Update.pdf
- [R3] Tesla Q1 2026 Update (PDF): /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/TSLA-Q1-2026-Update.pdf
- [R4] 《人形机器人创新发展指导意见》 (工信部科〔2023〕193号, 2023‑10‑20; PDF): https://www.ncsti.gov.cn/kjdt/tzgg/202311/P020231103479626066804.pdf
- [R5] 绿的谐波 2025 年年度报告 (PDF): /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/688017_2025_annual_report_2026-04-23.pdf
- [R6] 宇树科技（Unitree）上交所披露文件 (PDF, 2026‑03‑20): /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/Unitree_SSE_2026-03-20.pdf
- [R7] UBTECH FY2025 results (HKEX, PDF, 2026‑03‑31): /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/UBTECH_HKEX_2026-03-31_FY2025_results.pdf
- [R8] 三花智控 2025 年年度报告全文 (CNINFO, PDF, 2026‑03‑24): /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/sanhua_002050_annual_2025_2026-03-24_cninfo.pdf
- [R9] 三花智控 2026‑05‑26 投资者关系活动记录表（编号：2026‑004，CNINFO PDF）: /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/sanhua_002050_investor_activity_2026-05-26_cninfo_1225332276.pdf
- [R10] 36Kr (EU) article claiming Tesla placed a $685m actuator order with Sanhua; mentions “harmonic reducers (e.g., Green Harmonic)” (2025‑10‑15): https://eu.36kr.com/en/p/3510288514980998 (snapshot: /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/rumor_36kr_sanhua_685m_order.html)
- [R11] Eastmoney Caifuhao post claiming Sanhua is Optimus “core supplier” (2025年12月12日): https://caifuhao.eastmoney.com/news/20251212090942688077930 (snapshot: /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/rumor_caifuhao_sanhua_core_supplier_2025-12-12.html)
- [R12] Eastmoney Caifuhao post claiming Green Harmonic entered Optimus supply chain (2025年12月25日): https://caifuhao.eastmoney.com/news/20251225133947133551540 (snapshot: /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/rumor_caifuhao_greenharmonic_tesla.html)
- [R13] Jiemian article discussing “50亿订单” rumor and noting the company does not confirm robot business details (2026年2月28日): https://www.jiemian.com/article/13508755.html (snapshot: /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/rumor_jiemian_sanhua_50b_rumor.html)
- [R14] Rumor dossier (compiled, non-primary): /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/rumor_dossier.md
- [R15] Tesla patent (primary) — “ACTUATOR AND ACTUATOR DESIGN METHODOLOGY” (WO2024072984A1): https://patents.google.com/patent/WO2024072984A1/en (PDF snapshot: /Users/bytedance/Documents/选股skill/serenity-bottleneck-scout/reports/tesla/2026-06-05/run-02/sources/web/tesla_patent_WO2024072984A1_actuator_design.pdf)
- [R16] Tesla patent (primary) — “Systems and methods for a robot knee joint assembly” (WO2024073135A1 / EP4594165A1): https://patents.google.com/patent/WO2024073135A1/en

## Appendix: component-first universe (with supplier confirmation flag)

> This is not a confirmed supplier list. For each company you mention, you must label whether it is **Anchor-confirmed**.
> Allowed labels: **Anchor-confirmed / Not confirmed / Rumor / Unknown** and include an evidence note (URL or filing reference).
>
> Anchor company (the demand anchor for this report): Tesla (Optimus / “Bots” program) [R1]

| Node | Company | Market | Anchor supplier status | Evidence note | Why it matters |
|---|---|---|---|---|---|
| Downstream humanoid OEM (peer demand signal) | UBTECH | CN/HK | Not confirmed | Reports humanoid revenue growth and “mass production and delivery” (FY2025 results p1–p2). [R7 p1] [R7 p2] | Independent primary demand/commercialization signal (not Tesla-specific). |
| Downstream humanoid OEM (peer demand signal) | Unitree | CN | Not confirmed | Discloses humanoid robots as part of main revenue and “rapid growth” trend (p25). [R6 p25] | Independent primary demand/commercialization signal (not Tesla-specific). |
| Integrated actuators / mechatronics (candidate) | 三花智控 (002050.SZ) | CN | Rumor | Non-primary sources claim Tesla Optimus actuator/joint supply relationship, but no primary confirmation in filings/IR: see [R10] [R11] and compiled notes [R14]. Official 2026‑05‑26 IR record does not mention Tesla/Optimus/joints. [R9] | If humanoids scale, actuator assembly (integration + validation) could be an early capacity/quality bottleneck; anchor tie remains unverified. |
| Precision reducers (strain-wave class) | 绿的谐波 (688017.SH) | CN | Rumor | Non-primary sources claim Green Harmonic is in Optimus supply chain; see [R10] [R12] and compiled notes [R14]. Company annual report does not name Tesla/Optimus. [R5] | Potential capacity lever if humanoid/robotics joint demand scales, but Tesla tie is unverified. |
| Precision reducers (global incumbent examples) | Harmonic Drive Systems / Nabtesco | Non‑US/CN | Unknown | Not evaluated here for Tesla tie (no primary evidence) | Sets competitive benchmark; potential alternative supply base. |
| Integrated actuators (reducer+motor+drive) | 绿的谐波 (mechatronic actuators) | CN | Unknown | Described as “机电一体化产品” in annual report; no Tesla confirmation [R5] | Module packaging can become the qualification bottleneck. |
| Motors (high power density) | (examples) Nidec / domestic CN motor suppliers | Mixed | Unknown | No primary Tesla tie provided | Motor supply affects torque density and thermal limits. |
| Servo drives / power electronics | (examples) TI / Infineon / CN domestic drive vendors | Mixed | Unknown | No primary Tesla tie provided | Drives and control ICs can become constraints at volume. |
| Sensors (vision/force/encoders) | (examples) CN sensor startups / global metrology firms | Mixed | Unknown | MIIT calls for “专用传感器” key tech; no Tesla tie [R4] | Sensing quality affects manipulation and safety; qualification heavy. |

## Change log

- Reframed the node from “chokepoint” to **bottleneck-only** and explicitly marked chokepoint status as **NOT PROVEN** (per Judge).
- Added auditable **verbatim excerpts with page numbers** for Tesla’s 1M/10M line intent (Q1 2026 p6) and “before end of 2026” production target (Q4 2025 p8). [R2 p8] [R3 p6]
- Added **independent CN primary demand signals** (UBTECH FY2025 results + Unitree disclosure) with page-numbered excerpts. [R6 p25] [R7 p1] [R7 p2]
- Downgraded/flagged unsupported claims as explicit **FAIL / evidence gaps** for lead time (>12m), supplier concentration (≤3), and value capture (4–8q).
