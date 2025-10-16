# Global M&A and ESG Trends Analysis

Open-data style analysis connecting **M&A transactions** with **ESG performance** across sectors (2018–2024).  
This version includes a realistic synthetic dataset with rising deal activity and a positive ESG–value relationship.

## Quickstart (view only)
- Charts: see `outputs/`  
  - `deals_per_year.png`  
  - `esg_vs_dealvalue_scatter.png`  
  - `sector_esg_vs_dealvalue.png`  
  - `esg_trend_by_sector.png`

## Reproduce (optional)
1. Install Python 3.10+
2. `pip install pandas matplotlib numpy`
3. `python analysis/analysis.py`

## Files
- `data/ma_transactions_real.csv` — transaction-level synthetic deals
- `data/esg_scores_real.csv` — sector-year ESG panel
- `analysis/analysis.py` — reproducible script
- `outputs/` — generated charts
- `Report.md` — executive summary