# Tableau: US macroeconomic resilience dashboard

**Source:** [statsmodels US macrodata](https://www.statsmodels.org/stable/datasets/generated/macrodata.html), quarterly US economic observations 1959–2009. This is not a modern live-data feed.

## Build in Tableau Public / Desktop
1. Connect to `dashboard_data.csv`.
2. Create `Quarter date` with `MAKEDATE(INT([year]), 1 + (INT([quarter])-1)*3, 1)`.
3. Create four worksheets: **Real GDP trend** (line by quarter date), **Unemployment trend** (line), **Inflation vs interest rates** (two-series line with clear units), **GDP vs investment** (scatter).
4. Add a year-range filter and a quarter-date tooltip.
5. Arrange the four worksheets into a 2×2 dashboard and title it *US Macroeconomic Conditions, 1959–2009*.

**Deliverable:** `dashboard_data.csv` and `dashboard_preview.png` (static verified reference). A native `.twbx` requires Tableau and is not generated here.
