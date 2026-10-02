import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data/raw/Age-standardized suicide rates.csv")
df["Country"]=df["Country"].str.strip(); df["Sex"]=df["Sex"].str.strip()
long=df.melt(id_vars=["Country","Sex"],var_name="Year",value_name="Rate")
long["Year"]=long["Year"].astype(int)
print(long.groupby("Year")["Rate"].agg(["mean","median","min","max"]))
both=long[long.Sex=="Both sexes"]
print(both[both.Year==2016].sort_values("Rate",ascending=False).head(15))
wide=both.pivot(index="Country",columns="Year",values="Rate").dropna()
wide["Change_2000_2016"]=wide[2016]-wide[2000]
print(wide.sort_values("Change_2000_2016").head(15))
