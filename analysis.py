from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE/'data.csv', parse_dates=['date']).dropna(subset=['co2_ppm']).sort_values('date')
assert df.co2_ppm.between(250, 500).all()
df['year'] = df.date.dt.year
annual = df.groupby('year', as_index=False).co2_ppm.mean()
annual['change_ppm'] = annual.co2_ppm.diff()
annual.to_csv(BASE/'annual_summary.csv', index=False)
trend = np.polyfit(annual.year, annual.co2_ppm, 1)
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(annual.year, annual.co2_ppm, label='Annual mean')
ax.plot(annual.year, np.polyval(trend, annual.year), '--', label='Linear descriptive trend')
ax.set(title='Mauna Loa atmospheric CO₂', xlabel='Year', ylabel='CO₂ (ppm)')
ax.legend(); fig.tight_layout(); fig.savefig(BASE/'co2_trend.png', dpi=180)
print(f"Annual records: {len(annual)}; descriptive trend: {trend[0]:.3f} ppm/year")
