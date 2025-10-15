import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
ma = pd.read_csv(BASE / "data" / "ma_transactions_sample.csv")
esg = pd.read_csv(BASE / "data" / "esg_scores_sample.csv")

# Deals per year
deals_per_year = ma.groupby("year")["deal_id"].count()
plt.figure()
deals_per_year.plot(kind="bar", title="Deals per Year")
plt.ylabel("Number of Deals")
plt.tight_layout()
plt.savefig(BASE / "outputs" / "deals_per_year.png")
plt.close()

# ESG vs Deal Value
plt.figure()
plt.scatter(ma["esg_score_target"], ma["deal_value_usd_m"])
plt.title("ESG Score (Target) vs Deal Value (USD m)")
plt.xlabel("ESG Score (Target)")
plt.ylabel("Deal Value (USD m)")
plt.tight_layout()
plt.savefig(BASE / "outputs" / "esg_vs_dealvalue_scatter.png")
plt.close()

# Sector averages
avg_deal = ma.groupby("sector")["deal_value_usd_m"].mean().reset_index()
avg_esg = esg.groupby("sector")["avg_esg_score"].mean().reset_index()
merged = pd.merge(avg_deal, avg_esg, on="sector", how="inner")

plt.figure()
plt.scatter(merged["avg_esg_score"], merged["deal_value_usd_m"])
for _, r in merged.iterrows():
    plt.annotate(r["sector"], (r["avg_esg_score"], r["deal_value_usd_m"]), xytext=(5,5), textcoords="offset points")
plt.title("Sector Avg ESG vs Avg Deal Value")
plt.xlabel("Avg ESG Score")
plt.ylabel("Avg Deal Value (USD m)")
plt.tight_layout()
plt.savefig(BASE / "outputs" / "sector_esg_vs_dealvalue.png")
plt.close()

print("Done. Charts in outputs/.")