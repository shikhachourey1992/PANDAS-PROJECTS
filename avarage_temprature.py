# Display the dataset.
#
# Find average temperature of each city.
#
# Find total rainfall city-wise.
#
# Which city has highest humidity?
#
# Filter days where rainfall is more than 10 mm.
#
# Find hottest day overall.

import pandas as pd
import matplotlib.pyplot as plt
# df=pd.read_csv("data1.csv")
# print(df)
# print(df.groupby("City")["Temperature"].mean())
# print(df.groupby("City")["Rainfall"].sum())
# print(df.groupby("City")["Humidity"].max())
# print(df["Humidity"].max())
# filter_days=df[df["Rainfall"]>10]
# print(filter_days)
# hot_days=df["Temperature"].max()
# print(hot_days)

# Show all data.
# Find average temperature season-wise.
#  Which season has maximum rainfall?
#  Which city receives most rainfall in monsoon?
#  Sort seasons by rainfall.

df=pd.read_csv("data2.csv")
print(df)
print(df.groupby("Season")["AvgTemp"].mean())
print(df.groupby("Season")["AvgRainfall"].max())
print(df["AvgRainfall"].max())
print(df.sort_values(by="AvgRainfall", ascending=True))
