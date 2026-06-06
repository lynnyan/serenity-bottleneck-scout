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
