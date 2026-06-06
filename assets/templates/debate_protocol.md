# Multi-round debate workflow (Reporter ⇄ Verifier Judge)

Use this workflow to force iterative improvement of a thesis pack.

Roles:
- **Reporter**: produces and revises the thesis pack.
- **Verifier Judge**: hostile reviewer; demands evidence, falsifiability, and clear chokepoint vs bottleneck separation.

Goal:
- Run multiple rounds until the Judge returns **APPROVE**, or you stop at a defined max round.

Recommended max rounds: 3–5.

## Round 0: Setup

- Create the report skeleton using `scripts/new_serenity_report.py`.
- Generate default claims using `assets/tools/generate_claims.py`.
- Ensure the report includes the “component-first universe” appendix with **anchor supplier status** labels.

## Round 1..N (loop)

### Reporter (draft/revise)

Reporter must:
- Update the thesis pack to address the last Judge verdict.
- Keep changes evidence-first (add citations/quotes/links, not just narrative).
- Maintain a short list of “must-be-true” claims and make them testable.
- Apply supplier confirmation rules from `assets/templates/supplier_confirmation_rules.md`.

### Verifier Judge (review)

Use `assets/templates/judge_prompt.md`. Attach:
- thesis pack text (or file path)
- claims list
- (optional) filing snippets from `assets/tools/extract_filing_snippets.py`

Judge must output:
- Verdict: **APPROVE / REVISE / REJECT**
- Required changes (concrete, evidence-channel-specific)

## Convergence rule (when to stop)

- **APPROVE**: stop, publish report.
- **REJECT**: stop; thesis lacks evidence or is structurally non-falsifiable.
- **REVISE**: loop another round, but only if you can name the missing evidence and a concrete plan to obtain it.
