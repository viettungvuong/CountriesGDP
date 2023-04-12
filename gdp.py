import numpy as np
from scipy.stats import linregress
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.model_selection import train_test_split

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

x=np.array([int(year) for year in range(2012,2021)]).reshape(-1,1)
y=gdp.reshape(-1,1)
#plt.plot(x,y)
#plt.title("GDP Vietnam")
#plt.xlabel("Year")
#plt.ylabel("USD")
#plt.show()
# biểu đồ gdp việt nam

# chia ra thành test set và training set từ dữ liệu
# có phần lấy để train (train set), phần còn lại test set (ẻeer kiểm tra)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.75)

print(X_train)
print(y_train)
print(X_test)
print(y_test)

model = LinearRegression()

model.fit(X_train, y_train)
print('Model score '+str(model.score(X_test, y_test)))

# kết quả dự đoán từ linear regression
y_pred = model.predict(X_test)
for i in range(len(y_pred)):
    y_pred[i]=int(float(y_pred[i]))
plt.hist(y_test - y_pred)
plt.show()

for i in range(len(y_pred)):
    print(str(X_test[i])+" : "+str(y_pred[i]))
