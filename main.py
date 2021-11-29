import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chart_studio.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
import chart_studio.tools as ctls
#from prophet import Prophet
import logging
from scipy import stats
import statsmodels.api as sm
import seaborn as sns
import glob
import os


#sns.set()
#pd.set_option('display.max_rows', None)

# Не заработает, если неправильно указать путь к csv-файлам
PZ_dayahead_price = pd.read_csv("C:\\Users\Asus\Desktop\RU_Electricity_Market_PZ_dayahead_price_volume.csv")
UES_dayahead_price = pd.read_csv("C:\\Users\Asus\Desktop\RU_Electricity_Market_UES_dayahead_price.csv")
UES_intraday_price = pd.read_csv("C:\\Users\Asus\Desktop\RU_Electricity_Market_UES_intraday_price.csv")

#print(PZ_dayahead_price.head())
#print(UES_dayahead_price.head())
#print(UES_intraday_price.head())

# def data_details(data):
#     head = data.head()
#     info = data.info()
#     describe = data.describe()
#     any_null = data.isnull().any()
#
#     return (print(head),
#             print(info),
#             print(describe),
#             print(any_null))

#data_details(PZ_dayahead_price)
#data_details(UES_dayahead_price)
#data_details(UES_intraday_price)


# count = 0
# count1 = 0
# count2 = 0
# for row, i in UES_intraday_price.iterrows():
#     if i[1] == 0:
#         count += 1
#     if i[2] == 0:
#         count1 += 1
#     if i[3] == 0:
#         count2 += 1
# print (f"There are {count} - 0 values in UES_Northwest")
# print (f"There are {count1} - 0 values in UES_Siberia")
# print (f"There are {count2} - 0 values in UES_Center")
#
# for row, i in UES_intraday_price.iterrows():
#     if i[1] == 0:
#         print (i)

#

# def replace_vals(data):
#     data.reset_index(drop=True, inplace=True)
#     data["timestep"] = pd.to_datetime(data["timestep"])
#     data.drop("timestep", axis=1)
#     data.set_index("timestep", drop=True, inplace=True)
#
#     # 2. replace all values between 0 & 50 with Nan
#
#     for item in data:
#         data[item] = data[item].mask(data[item] < 50, np.nan)
#
#     # 3. replace all NaN values by mean
#
#     data = data.fillna(data.mean(), inplace=True)
#     # data.drop("timestep", axis = 1)"""
#     return data
#
# print(UES_intraday_price)
# replace_vals(UES_intraday_price)
# UES_intraday_price.head()
# print(UES_intraday_price)

# replace_vals(PZ_dayahead_price)
# PZ_dayahead_price.head()
# print(PZ_dayahead_price)
#
# replace_vals(UES_dayahead_price)
# UES_dayahead_price.head()
# print(UES_dayahead_price)

# всё, что до этого в основном считает нулевые значения и заменяет слишком маленькие  на средние, туту пробелма может быть в том, что
# файлы могут не открыться

# графики для PZ_dayahead_price

PZ_dayahead_price.head()

plt.figure(figsize = (29,15))

ax1 = plt.subplot(4, 1, 1)
PZ_dayahead_price['consumption_eur'].plot()
ax1.set_ylabel("consumption_eur")

ax2 = plt.subplot(4, 1, 2)
PZ_dayahead_price['consumption_sib'].plot()
ax2.set_ylabel("consumption_sib")

ax3 = plt.subplot(4, 1, 3)
PZ_dayahead_price['price_eur'].plot()
ax3.set_ylabel("price_eur")

ax4 = plt.subplot(4, 1, 4)
PZ_dayahead_price['price_sib'].plot()
ax4.set_ylabel("price_sib")

plt.show()

#графики для UES_dayahead_price

UES_dayahead_price.head()


plt.figure(figsize = (29,15))

ax1 = plt.subplot(6, 1, 1)
UES_dayahead_price['UES_Northwest'].plot()
ax1.set_ylabel("UES_Northwest")

ax2 = plt.subplot(6, 1, 2)
UES_dayahead_price['UES_Siberia'].plot()
ax2.set_ylabel("UES_Siberia")

ax3 = plt.subplot(6, 1, 3)
UES_dayahead_price['UES_Middle_Volga'].plot()
ax3.set_ylabel("UES_Middle_Volga")

ax4 = plt.subplot(6, 1, 4)
UES_dayahead_price['UES_Urals'].plot()
ax4.set_ylabel("UES_Urals")

ax5 = plt.subplot(6, 1, 5)
UES_dayahead_price['UES_Center'].plot()
ax5.set_ylabel("UES_Center")

ax6 = plt.subplot(6, 1, 6)
UES_dayahead_price['UES_South'].plot()
ax4.set_ylabel("UES_South")

plt.show()

#графики для UES_intraday_price

UES_intraday_price.head()

plt.figure(figsize = (29,15))

ax1 = plt.subplot(3, 1, 1)
UES_intraday_price['UES_Northwest'].plot()
ax1.set_ylabel("UES_Northwest")

ax2 = plt.subplot(3, 1, 2)
UES_intraday_price['UES_Siberia'].plot()
ax2.set_ylabel("UES_Siberia")

ax3 = plt.subplot(3, 1, 3)
UES_intraday_price['UES_Center'].plot()
ax3.set_ylabel("UES_Center")

plt.show()
