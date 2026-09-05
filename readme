# Reducing Loan Defaults & Fraud Losses Through Risk-Based Underwriting

`SQL` `Python` `Power BI` · [Interactive Dashboard](#dashboard-preview) · [Full Recommendation Log](business_recommendations.md)

---

## Overview

This project analyzes a consumer lending institution's loan portfolio to understand where credit risk and fraud actually concentrate. Like most lenders, the business generates the majority of its revenue through lending, but carries the dual challenge of managing loan defaults and detecting fraudulent activity, both of which directly affect profitability. Its priorities include tightening underwriting where risk is highest, strengthening fraud detection, and doing both without adding unnecessary friction for lower-risk borrowers — which requires knowing exactly where risk concentrates, rather than relying on portfolio-wide averages that can hide which specific segments, loan types, and transaction patterns are actually driving losses.

To support underwriting policy, fraud-control, and portfolio-monitoring decisions, application, credit, and transaction data was analyzed across three key areas, mirroring the structure of the underlying Power BI dashboard:

- **Credit Risk Analysis** — assessed whether loan approval decisions actually align with borrowers' real default risk across income, profession, and credit tier.
- **Fraud Detection** — identified where fraud concentrates across loan purpose, loan size, transaction channel, and customer tier.
- **Customer Overview** — examined default risk across regional and demographic customer segments.

*(Entity relationship diagram and full technical methodology: see [`powerbi/README.md`](powerbi/README.md).)*

---

## Executive Summary

The portfolio carries **$293M in approved loans** across 30,000 applications and 10,000 customers, with an **8% overall default rate** and **$22M in realized defaults** to date.

- The portfolio's riskiest identifiable segment — **$70K–$99K income, top risk band** — defaults at **75%** (~9.4x the 8% baseline) and is simultaneously **approved at 73.12%**, the highest approval rate of any segment measured, and above the portfolio's own 54% average. The approval process is not screening out its highest-risk applicants — it's favoring them.
- **Engineers with "excellent" credit scores default at 6%**, 3–6x the 1–2% rate of other excellent-credit borrowers. Credit score alone is hiding this group's real risk.
- **Basic-tier customers carry a 0.24 loan-to-income ratio** — nearly double Advance customers (0.13) and more than 3x Premium customers (0.07) — and account for 5,185 of the portfolio's high-risk customers, more than Advance and Premium combined.
- Fraud is concentrated, not spread evenly: it clusters in **Debt Consolidation and Car Loan applications**, in **medium-sized loans ($10K–$50K) with 600–800 credit scores still awaiting a decision**, and fraud *application* volume spiked from **6 to 104 in a single month** (May→June 2023) — a pattern worth an automated alert, not just a quarterly review.
- Regional risk doesn't track with regional volume: **Penticton and White Rock** are low-volume branches carrying the highest severity risk, while **Vancouver and Surrey** — the two fastest-growing regions (21 and 11 new customers last month) — carry the highest fraud *volume* and need controls that scale with growth rather than against it.

---

## Summary of Insights

Each finding follows the same structure: **what we found → the benchmark it's measured against → why it matters → who at the company would act on it.** Findings are grouped under the same three areas as the dashboard. Full detail and underlying dashboard logic: [`business_recommendations.md`](business_recommendations.md).

### Credit Risk Analysis

**Finding 1 — The approval process is favoring its riskiest segment, not screening it out.**
Borrowers earning **$70K–$99K** in the **top risk band (51–100%)** default at **75%** — ~9.4x the 8% baseline — and that exact segment has the **highest approval rate in the portfolio, at 73.12%**, above the 54% overall average. This is the single most consequential finding in the analysis: a segment defaulting at nearly 10x the average is being approved *more* often than average, not less. **Affects:** Underwriting / Credit Policy. → **[R1](#recommendations)**

**Finding 2 — Credit score alone misreads risk for Engineers.**
Engineers with *excellent* credit scores default at **~6%**, versus **~1–2%** for other excellent-credit borrowers — a 3–6x gap hidden behind a score that's supposed to be the strongest signal available. **Affects:** Underwriting / Risk Model team. → **[R2](#recommendations)**

**Finding 3 — Basic-tier customers are carrying more debt relative to income than any other class.**
Basic-class customers average a **0.24 loan-to-income ratio** — ~1.8x Advance (0.13) and ~3.4x Premium (0.07) — and hold **5,185 high-risk customers**, more than Advance (2,968) and Premium (1,847) combined. Customer class is currently a segmentation label, not a lending constraint, despite this real leverage gap. **Affects:** Credit Policy. → **[R3](#recommendations)**

**Finding 4 — High income does not reliably predict low risk.**
Doctors (100K+) and Software Developers (100K+ and 70–99K) show the highest default rates among high earners; Engineers in the 40–69K band run a **9.09% average risk score**, modestly above the 8% baseline, with a notably higher loan-to-income ratio (~0.28). Income-tiered approval logic — the simplest, most common underwriting shortcut — misprices all three groups. **Affects:** Underwriting / Credit Policy. → **[R4](#recommendations)**

### Fraud Detection

**Finding 5 — Fraud concentrates in the single largest loan category.**
Debt Consolidation is both the **#1 approved loan purpose** (5,000 of 16,000 approved loans, ~31%) and, alongside Car Loans, the purpose **most frequently linked to fraud**. Your highest-volume category is also your highest fraud-risk category. **Affects:** Fraud / Compliance Ops. → **[R5](#recommendations)**

**Finding 6 — Fraud has a specific address: medium loans, mid-range credit, still pending.**
Fraud concentrates most in the **$10K–$50K** range, among applicants with **600–800 credit scores**, on applications still marked **active / not yet approved** — the last checkpoint before a decision. This isn't the low-credit-score profile most fraud rules are tuned to catch. **Affects:** Fraud Ops. → **[R6](#recommendations)**

**Finding 7 — Fraud channel differs by customer tier.**
Prime customers' fraud concentrates in **ATM transactions**; Subprime and Near-prime customers' fraud concentrates in **Transfer transactions**. A single uniform fraud rule set is necessarily too loose for some tiers and too strict for others. **Affects:** Fraud / Risk Ops. → **[R7](#recommendations)**

**Finding 9 — Fraud volume spiked sharply in a single month.**
Fraud loan applications jumped from **6 to 104** between May and June 2023; fraud transactions separately jumped from **7 to 103** between May and June 2024 — both roughly **15–17x** month-over-month increases, far outside normal variation. A gradual trend can wait for a quarterly review; a 15x spike cannot. **Affects:** Fraud Ops / Risk Monitoring. → **[R9](#recommendations)**

### Customer Overview

**Finding 8 — Regional risk doesn't track with regional volume.**
**Penticton** (top default region) and **White Rock** (top fraud region) are comparatively low-volume branches carrying the highest *severity* of risk. **Vancouver and Surrey** carry the highest fraud *volume* and are also the fastest-growing regions (21 and 11 new customers in the last 30 days). **Campbell River**, by contrast, has the portfolio's highest average credit score and a clean fraud/default profile — worth studying as an internal benchmark. **Affects:** Regional Risk Ops. → **[R8](#recommendations)**

**Finding 10 — Default risk concentrates in three identifiable applicant profiles.**
The highest default rates cluster among **widowed customers on work permits** and **customers under 25 with poor credit scores**. Important caveat: marital status and immigration/visa status are protected or heavily restricted factors under fair-lending regulation in most jurisdictions. **This should not be read as "decline these groups."** The actionable version is to identify the *permissible* underlying drivers correlated with these labels — income stability, credit history length, employment tenure — and build policy around those instead. **Affects:** Credit Policy, with Compliance/Legal. → **[R10](#recommendations)**

---

## Recommendations

*Ten findings, ten corresponding actions. Every row below traces back to a specific finding, benchmark, and business rationale above — this section is the point of the project, not an appendix to it.*

| # | Priority | Action | Owner | Expected Impact | Metric to Track |
|---|---|---|---|---|---|
| **R1** | **P0** | Cap or add mandatory manual review for auto-approvals in the **$70K–$99K income + top risk band** segment — do not let this segment's approval rate exceed the portfolio average until its default rate normalizes. | Underwriting / Credit Policy | Directly targets the segment defaulting at 75% (9.4x baseline) while currently being approved above the portfolio average (73.12% vs 54%) — the clearest source of avoidable loss identified in this analysis. | Segment default rate (target: <2x baseline), segment approval rate (target: at or below the 54% portfolio average) |
| **R2** | **P0** | Require income/DTI verification for **Engineer** applicants specifically, rather than relying on credit score alone. | Underwriting / Risk Model team | Closes a 3–6x default-rate gap (6% vs. 1–2%) hidden behind an "excellent" credit score. | Default rate: Engineers vs. all excellent-credit-score borrowers |
| **R3** | **P1** | Introduce a loan-to-income cap for **Basic-tier** approvals, and prioritize Advance/Premium applicants where portfolio capacity is limited. | Credit Policy | Basic-tier LTI (0.24) is ~1.8x Advance and ~3.4x Premium; Basic also holds more high-risk customers than the other two tiers combined. | Basic-tier average LTI, Basic-tier risk score trend |
| **R4** | **P1** | Rebuild the approval scorecard around **profession × income** cross-segments instead of income-only tiers, starting with Doctors, Software Developers, and Engineers (40–69K). | Risk Analytics / Model team | Removes the income-only approval shortcut currently misreading at least three known profession/income combinations. | Default rate by profession × income segment (quarterly refresh) |
| **R5** | **P0** | Add secondary verification (supporting documentation or identity re-check) for **Debt Consolidation** and **Car Loan** applications specifically. | Fraud / Compliance Ops | Targets the loan purpose that is simultaneously the largest share of approved volume (~31%) and the top fraud-linked purpose. | Fraud flag rate by loan purpose |
| **R6** | **P0** | Strengthen **Pending-stage** review specifically for **$10K–$50K** loans from applicants with **600–800 credit scores**. | Fraud Ops | Targets the exact combination where fraud concentrates most, at the last checkpoint before disbursement. | Fraud catch rate at Pending stage, for this specific segment |
| **R7** | **P1** | Replace the uniform fraud rule set with **tier-specific rules by channel**: ATM-focused for Prime, Transfer-focused for Subprime, both for Near-prime. | Fraud / Risk Ops | Tightens coverage where it's currently too loose (Transfer fraud in Subprime/Near-prime) without adding false positives where it's already working (ATM in Prime). | Catch rate and false-positive rate, by tier × channel |
| **R8** | **P0 (Penticton, White Rock)** / **P2 (Vancouver, Surrey)** | Deploy early-detection triggers in Penticton and White Rock first; scale (not restrict) controls in Vancouver/Surrey in proportion to their growth. Use Campbell River's profile as the internal benchmark for "healthy." | Regional Risk Ops | Matches control intensity to actual severity rather than volume, protecting two small high-severity branches without slowing two branches the business is actively growing. | Branch-level default/fraud rate vs. the Campbell River benchmark |
| **R9** | **P0** | Build an automated month-over-month spike alert on fraud application and transaction counts, rather than relying on quarterly review. | Fraud Ops / Risk Monitoring | Would have flagged the 15–17x spikes seen in 2023 and 2024 in real time instead of after the fact. | Month-over-month % change in fraud applications and transactions, with an alert threshold (e.g., >3x) |
| **R10** | **P1** | Rebuild the "highest-risk applicant" policy around **permissible underlying drivers** (income stability, credit history length, employment tenure) rather than the demographic labels they currently correlate with. Route through Compliance/Legal before implementation. | Credit Policy + Compliance/Legal | Preserves the risk signal while keeping the policy fair-lending compliant. | Default rate by the *replacement* permissible-driver segments, post-compliance review |

**Total risk exposure addressed:** $22M in realized defaults plus $23M in flagged-fraud loan value equals **~$45M in identified risk exposure — roughly 15% of the $293M approved loan book**. R1, R5, R6, and R9 alone target the segments and moments responsible for the clearest, most immediately actionable share of that exposure.

---

## Appendix

### Dataset & Methodology

The analysis runs on a relational loan portfolio dataset — **30,000 applications, 10,000 customers, 233,000 transactions** — spanning the full lending lifecycle across 9 linked tables (`applications`, `customers`, `credit_bureau`, `credit_history`, `transactions`, `fraud_indicators`, `past_loans`, `risk_labels`, `branches`), joined on `CustomerID` and `ApplicationID`.

- **SQL** — data cleaning, validation, referential integrity checks, and derived segmentation fields (income buckets, credit score ranges, risk bands) across all 9 tables.
- **Python (Pandas, NumPy, Matplotlib)** — exploratory analysis of loan, income, and credit-score distributions; outlier detection; fraud-account aggregation that informed the segmentation used above.
- **Power BI (DAX)** — the 4-page interactive dashboard (Executive Summary, Credit Risk Analysis, Fraud Detection, Customer Overview) every finding above is drawn from.

Full technical documentation, the entity relationship diagram, and DAX measure definitions: see [`powerbi/README.md`](powerbi/README.md).

### Dashboard Preview

![Executive Summary](powerbi/screenshots/Executive_Summary.png)

### Assumptions & Caveats

- Application, transaction, and credit data are treated as complete and accurate for the analysis window, with no material missing or duplicate records.
- Risk bands, tiers, and fraud flags reflect the labeling already present in the source data; this analysis segments and prioritizes against that labeling rather than re-deriving fraud/default definitions from scratch.
- "Customer default rate" (8%) and "loan default rate" (7.46%) are reported at different grains (per-customer vs. per-loan) and are both cited above — they are not the same measure and shouldn't be used interchangeably.
- Recommendation R10 explicitly requires a fair-lending compliance review before any policy change — see the caveat under Finding 10.
- The exact default rate for the Doctors/Software Developer high-income cross-segment (Finding 4) has not yet been pulled from the dashboard as a precise figure — recommended before external sharing.

---

**Sara Samiei** — Data Analyst | [LinkedIn](https://linkedin.com/in/sara-samiei) | [GitHub](https://github.com/SamieiSara)
