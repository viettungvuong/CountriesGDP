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

vietnam = df.loc[df['Country Code'] == 'VNM']
for i in year_cols:
    years.append(vietnam[i].to_numpy())
print(len(years))
print(years)
