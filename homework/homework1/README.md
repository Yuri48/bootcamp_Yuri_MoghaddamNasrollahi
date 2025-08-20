# Project Title
**One‑Neighborhood Airbnb Price Estimator (Williamsburg, NYC)**

## Stage: Problem Framing & Scoping (Stage 01) — 2025-08-20

### Problem Statement
New Airbnb hosts in *Williamsburg (Brooklyn)* often don't know how to price their place for the next month. We will use a small public sample of the **Inside Airbnb** dataset to (a) describe typical nightly prices in the neighborhood and (b) build a **very simple estimator** using just a few fields—*room type, accommodates, bedrooms, and minimum nights*—to produce a **recommended price range** for a new listing.

### Stakeholder & User
- **Decision owner:** Individual host listing a property in Williamsburg.
- **Tool/operator:** You (student/analyst) running a short notebook.
- **Workflow context:** Host wants a price range to set for **next month**, updated monthly if needed.

### Useful Answer & Decision
- **Type:** Descriptive **and** Predictive (very lightweight).
- **Deliverables:** (1) A small benchmark table (median/IQR by room type & bedrooms). (2) A tiny estimator in the notebook that returns a **price recommendation range**.
- **Recommendation format:** `low = neighborhood_median - IQR/2`, `mid = neighborhood_median`, `high = neighborhood_median + IQR/2`, then adjusted by simple multipliers for accommodates/bedrooms.
- **Decision:** Set initial nightly price to the **mid** value; consider `low–high` as experimentation bounds.

### Assumptions & Constraints
- Data source: *Inside Airbnb* public CSV (NYC) filtered to Williamsburg; small sample kept locally for simplicity.
- Only a few features are used: room type, accommodates, bedrooms, minimum nights.
- Outliers (extreme prices) will be removed using simple rules (e.g., 1st–99th percentiles).
- No advanced modeling, no scraping, no APIs.
- Privacy: only public, aggregated data; no PII.

### Known Unknowns / Risks
- Listing quality (photos, amenities, reviews) not modeled → residual variation.
- Seasonality and event spikes may shift price levels month to month.
- Data freshness; we will note the snapshot date and update if needed.

**How we’ll test/monitor:** Hold out a tiny subset to check absolute error; sanity‑check against median/IQR; manually spot‑check a few listings in the neighborhood website UI (non‑automated).

### Lifecycle Mapping
- **Goal A → Stage 01 (Framing) → Deliverable:** This README + stakeholder one‑pager + repo skeleton.
- **Goal B → Stage 02 (Data) → Deliverable:** Download one NYC CSV, filter to Williamsburg, save a tiny sample + data dictionary.
- **Goal C → Stage 03 (EDA) → Deliverable:** Basic histograms/boxplots; median & IQR by (room type, bedrooms).
- **Goal D → Stage 04 (Modeling) → Deliverable:** 10‑line estimator (simple linear model or rules); function `recommend_price(...)`.
- **Goal E → Stage 05 (Evaluation) → Deliverable:** Simple hold‑out MAE; report ±IQR bands and example recommendations.
- **Goal F → Stage 06 (Communication) → Deliverable:** One‑pager with table + recommendation; notebook cell for host inputs.

### Repo Plan
```
/data/raw, /data/processed
/src
/notebooks
/docs
```
Cadence: commit per lifecycle step; push repo URL per course instructions.
