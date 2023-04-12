import numpy as np
from scipy.stats import linregress
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal

pd.options.display.max_rows = 9999

# read data from csv file
df = pd.read_csv('gdp.csv',index_col='Country Name')

years=[]

year_cols = [str(yr) for yr in range(2012, 2021)] # lấy tất cả các năm
for i in year_cols:
    years.append(df[i].to_numpy())

print(years[0][0])
print(type(years[0][0]))



for i in range(len(years)):
    years[i][years[i] == '..'] = 0
    for j in range(len(years[i])):
        years[i][j]=Decimal(float(years[i][j]))

