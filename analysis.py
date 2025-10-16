
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
tx_df = pd.read_csv(BASE / "data" / "ma_transactions_real.csv")
esg_panel = pd.read_csv(BASE / "data" / "esg_scores_real.csv")

# 1) Deals per Year
count_series = tx_df.groupby("year")["deal_id"].count()
plt.figure()
count_series.plot(marker="o", title="Deals per Year (2018–2024)")
plt.xlabel("Year")
plt.ylabel("Number of Deals")
plt.tight_layout()
plt.savefig(BASE / "outputs" / "deals_per_year.png")
plt.close()

# 2) ESG vs Deal Value
x = tx_df["target_esg_score"].values
y = tx_df["deal_value_eur_m"].values
plt.figure()
plt.scatter(x, y, alpha=0.35)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xs = np.linspace(min(x), max(x), 100)
plt.plot(xs, p(xs))
plt.title("Target ESG Score vs Deal Value (€m)")
plt.xlabel("ESG Score")
plt.ylabel("Deal Value (€m)")
plt.tight_layout()
plt.savefig(BASE / "outputs" / "esg_vs_dealvalue_scatter.png")
plt.close()

# 3) Sector Avg ESG vs Avg Deal Value
sector_avg = tx_df.groupby("sector").agg(
    avg_value=("deal_value_eur_m","mean"),
    deals=("deal_id","count")
).reset_index()
sector_esg = esg_panel.groupby("sector").agg(avg_esg=("avg_esg_score","mean")).reset_index()
sec_merge = pd.merge(sector_avg, sector_esg, on="sector")

plt.figure()
sizes = (sec_merge["deals"] / sec_merge["deals"].max()) * 800 + 50
plt.scatter(sec_merge["avg_esg"], sec_merge["avg_value"], s=sizes)
for _, r in sec_merge.iterrows():
    plt.annotate(r["sector"], (r["avg_esg"], r["avg_value"]), xytext=(5,5), textcoords="offset points")
plt.title("Sector Avg ESG vs Avg Deal Value (€m)\n(Size ~ deal count)")
plt.xlabel("Avg ESG Score (2018–2024)")
plt.ylabel("Avg Deal Value (€m)")
plt.tight_layout()
plt.savefig(BASE / "outputs" / "sector_esg_vs_dealvalue.png")
plt.close()

# 4) ESG Trend by Sector
pivot = esg_panel.pivot(index="year", columns="sector", values="avg_esg_score").sort_index()
plt.figure()
pivot.plot()
plt.title("ESG Trend by Sector (2018–2024)")
plt.xlabel("Year")
plt.ylabel("Avg ESG Score")
plt.tight_layout()
plt.savefig(BASE / "outputs" / "esg_trend_by_sector.png")
plt.close()
