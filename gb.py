import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
days = 300
dates = pd.date_range(start='2020-01-01', periods=days)

price = np.cumsum(np.random.randn(days)) + 100
sentiment = np.random.uniform(-1, 1, days)
valuation = np.random.uniform(0.5, 2.0, days)
macro = np.random.choice([0, 1], size=days, p=[0.95, 0.05])  # rare macro shifts

mu_price = pd.Series(price).rolling(window=50, min_periods=1).mean()
a1, a2, a3 = 10, 20, 50
gb_score = price - mu_price - a1 * sentiment - a2 * valuation + a3 * macro
gb_index = np.argmin(gb_score)
gb_date = dates[gb_index]

print(f"Generational Bottom Estimated at: {gb_date.date()}")
print(f"Score at Bottom: {gb_score[gb_index]:.2f}")

plt.figure(figsize=(12, 6))
plt.plot(dates, gb_score, label='GB Score', color='steelblue')
plt.axvline(gb_date, color='red', linestyle='--', label='Estimated GB')
plt.title('Generational Bottom Score Over Time')
plt.xlabel('Date')
plt.ylabel('GB Score')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
