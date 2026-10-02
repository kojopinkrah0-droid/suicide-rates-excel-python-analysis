# Age-Standardized Suicide Rates — Excel + Python Portfolio

Public-health analytics project using **Excel and Python** to explore age-standardized suicide rates by country and sex for 2000, 2010, 2015 and 2016.

## Dataset
- 549 records
- 183 country/sex combinations
- 4 years
- 0 missing values
- Age-standardized rate per 100,000 population

## Key Findings
The dataset shows substantial variation between countries and sex categories. The 2000–2016 comparison identifies countries with the largest increases and decreases in the reported rate. The average annual pattern and sex-specific pattern are visualized in the portfolio.

These are **descriptive observations** and do not establish causes.

## Visualizations
![Average rate](images/average_rate_by_year.png)
![Top 15](images/top15_2016.png)
![By sex](images/rate_by_sex.png)
![Largest changes](images/largest_changes.png)

## Excel
`excel/Excel_Analysis_Guide.md` provides Power Query, PivotTable, KPI, chart, conditional-formatting and slicer instructions. Excel-ready summary CSVs are included.

## Python
`python/analysis.py` reproduces the core transformation and analysis using pandas.

## Structure
```text
suicide-rates-excel-python-portfolio/
├── data/raw/
├── data/processed/
├── python/
├── excel/
├── images/
├── results/
├── docs/
└── README.md
```

## Skills
**Excel · Power Query · PivotTables · Python · pandas · matplotlib · Data Cleaning · EDA · Trend Analysis · Public Health Analytics · Data Visualization · GitHub**

## Interpretation
Age-standardization supports population-level comparison, but this dataset alone cannot establish causes or individual-level risk.
