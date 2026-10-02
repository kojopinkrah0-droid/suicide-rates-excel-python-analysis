# Excel Analysis Guide
1. Import the CSV with **Data → From Text/CSV** and convert it to a Table named `tblSuicide`.
2. In Power Query select `Country` and `Sex`, then **Unpivot Other Columns** to create Year and Rate.
3. Create KPI cards for number of countries, 2016 average, 2000 average and sex-specific averages.
4. PivotTables: Year/average rate; Country/2016 rate; Year × Sex/average rate; Country/2000 vs 2016 change.
5. Charts: yearly line, 2016 top-15 bar, sex comparison line, largest-change bar.
6. Add conditional formatting and slicers for Year, Sex and Country.
