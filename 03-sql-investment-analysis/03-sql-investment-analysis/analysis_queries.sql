-- Historical firm investment panel, amounts are in the original dataset units.
-- 1: Firm averages
SELECT firm, ROUND(AVG(invest),2) AS mean_investment, COUNT(*) AS years FROM investment GROUP BY firm ORDER BY mean_investment DESC;

-- 2: Year-over-year investment growth, with window function
WITH growth AS (SELECT firm, year, invest, LAG(invest) OVER (PARTITION BY firm ORDER BY year) AS previous FROM investment)
SELECT firm, year, ROUND(100.0*(invest-previous)/NULLIF(previous,0),2) AS yoy_pct FROM growth WHERE previous IS NOT NULL ORDER BY firm,year;

-- 3: Investment-to-market-value ratio by year
SELECT year, ROUND(SUM(invest)/NULLIF(SUM(value),0),4) AS invest_to_value FROM investment GROUP BY year ORDER BY year;
