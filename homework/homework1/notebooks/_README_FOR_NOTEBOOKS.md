# Notebook: 01_framing — Williamsburg Airbnb Price Estimator

**Purpose:** Give a new host a simple, defensible nightly price range for next month.  
**Data:** Inside Airbnb NYC CSV filtered to Williamsburg; tiny local sample.  
**Outputs:** benchmark table (median/IQR) and `recommend_price(...)` helper with low/mid/high.

**Method (very simple):**
- Clean basic fields; drop outliers (1st–99th pct).  
- Group by (room_type, bedrooms) → median & IQR.  
- Optional: fit a minimal linear model as a cross‑check; use rules for the recommendation.
