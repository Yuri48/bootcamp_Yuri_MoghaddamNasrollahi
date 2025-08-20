# Host One‑Pager — Williamsburg Airbnb Price Helper

**Owner:** New Airbnb Host (Williamsburg)  
**Author:** Moghaddam Nasrollahi Yuri, Student/Analyst  
**Date:** 2025-08-16

## Question
*What nightly price should I set for next month?*

## What you'll get
- A small **benchmark table** with typical prices (median & IQR) by room type and bedrooms in Williamsburg.
- A **simple estimator** that outputs a recommended **low / mid / high** price for your listing.

## How it works (simple on purpose)
- We use a tiny snapshot from the **Inside Airbnb** NYC data filtered to *Williamsburg*.
- Features used: **room type, accommodates, bedrooms, minimum nights**.
- Outliers removed with basic percentile rules; no heavy modeling or scraping.

## Recommendation rule
- Start at neighborhood **median** for your room type & bedrooms.
- Define bounds using **IQR/2** (low = median − IQR/2; high = median + IQR/2).
- Adjust mid by small multipliers for accommodates/bedrooms (documented in notebook).

## Caveats
- We do not model quality, amenities, or reviews; seasonality may shift prices.
- Refresh monthly if possible; the notebook notes the data snapshot date.

## Definition of Done
1‑pager + notebook cell `recommend_price(room_type, accommodates, bedrooms, min_nights)` that returns a price range you can use immediately.
