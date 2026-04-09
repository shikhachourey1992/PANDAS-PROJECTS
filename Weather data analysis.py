#mini data project
#Weather data analysis

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("weather.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.info())
# print(df.isnull().sum())
# avrage_temp=df.groupby("City")["Temperature"].mean()
# print(avrage_temp)
# avrge_rainfall=df.groupby("City")["Rainfall"].mean()
# print(avrge_rainfall)
# print(df.max())
# print(df.min())
# Rain_fall=df[df["Rainfall"] > 5]
# print(Rain_fall)
# print(df.groupby("City")["Humidity"].max())
# plt.plot(df["Date"],df["Temperature"])
# plt.xlabel("Date")
# plt.ylabel("Temperature(°C)")
# plt.title("Temperature Trands")
# plt.show()
# plt.bar(df["City"],df["Rainfall"])
# plt.xlabel("City")
# plt.ylabel("Rainfall")
# plt.title("Rainfall Trands")
# plt.show()
# Challenge 1
# Find the windiest day.
# Challenge 2
# Filter days where:
# Temperature > 25°C
# Humidity < 70%
# Challenge 3
# Sort cities by average rainfall.
filtered_days = df[(df['Temperature'] > 25) & (df['Humidity'] < 70)]
print(filtered_days)
print(df.groupby("City")["WindSpeed"].max())
avrage_Rainfall=df.groupby("City")["Rainfall"].mean()
sort_city=avrage_Rainfall.sort_values(ascending=False)
print(sort_city)



