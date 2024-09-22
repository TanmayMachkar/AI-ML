import pandas as pd
from datetime import datetime

d_parser = lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\ETH_1H.csv", parse_dates = ["Date"], date_parser = d_parser)
print(df.head())
print(df.shape)

print(df.loc[0, "Date"])
# df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %H:%M:%S") #convert to proper date-time format
print(df.loc[0, "Date"].day_name()) #print day name of that date

print(df["Date"].dt.day_name()) #get day name of all dates in column
df["DayOfWeek"] = df["Date"].dt.day_name()
print(df)

print(df["Date"].min())
print(df["Date"].max())
print(df["Date"].max() - df["Date"].min())

filt = (df["Date"] >= "2019") & (df["Date"] < "2020")
print(df.loc[filt])

filt = (df["Date"] >= pd.to_datetime("2019-01-01")) & (df["Date"] < pd.to_datetime("2020-01-01"))
print(df.loc[filt])

print(df.set_index("Date", inplace = True))
print(df.loc["2019"])

print(df.sort_index(inplace = True))
print(df["2020-01-01": "2020-02-01"]["Close"].mean()) #get dates from jan 2020 to feb 2020

print(df.loc["2020-01-01"]["High"])
print(df.loc["2020-01-01"]["High"].max())

highs = df["High"].resample("D").max()
print(highs["2020-01-01"]) #Filter by day (previously it was filtered by hours)

import matplotlib.pyplot as plt

highs.plot()
plt.show()

numeric_df = df.select_dtypes(include='number')
resampled_df = numeric_df.resample("W").mean()
print(resampled_df) #resample the date column on a weekly basis and find the mean
print(df.resample("W").agg({"Close":"mean", "High":"max", "Low":"min", "Volume":"sum"}))