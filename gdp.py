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
    years.append(int(float((vietnam[i].to_numpy())[0])))

gdp=np.array(years)
print(len(gdp))
print(gdp)

y=np.array([int(year) for year in range(2012,2021)])
x=gdp
plt.plot(x,y)
plt.show()
# biểu đồ gdp việt nam