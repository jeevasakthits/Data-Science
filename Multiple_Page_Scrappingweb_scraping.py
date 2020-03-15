import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

import requests
import urllib.request
import time 
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import lxml
import re
import pandas as pd

txt="500570"
r=pd.read_html("https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx?scripcode="+str(txt)+"&flag=sp&Submit=G")
print(r[5])
data1=pd.DataFrame(r[5])
data1=data1.drop([0,1],axis=0)
data1=data1.rename(columns={0: "Date", 1: "Open Price", 2: "High Price",3: "Low Price", 4: "Close Price",5: "WAP",6: "No.of Shares", 7: "No. of Trades", 8: "Total Turnover (Rs.)",9: "Deliverable Quantity", 10: "% Deli. Qty to Traded Qty", 11: "Spread High-Low", 12: "Spread Close-Open"}, errors="raise")
print(data1.head())

df=pd.read_csv("F:/jeeva/Salary_prediction_web_app/files/"+txt+".csv")
date=df["Date"]
print(df.head())
for i in range(len(date)):
    s=date[i]
    s=re.split("-",s)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    rep=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    indx=months.index(str(s[1]))
    s[1]=str(rep[months.index(str(s[1]))])
    s1='/'.join(map(str, s))
    date[i]=s1
df["Date"]=date
row={"Date":data1["Date"][0],"Open Price":data1["Open Price"][0],"High Price":data1["High Price"][0],"Low Price":data1["Low Price"][0],"Close Price":data1["Close Price"][0],"WAP":data1["WAP"][0],"No.of Shares":data1["No.of Shares"][0], "No. of Trades":data1["No. of Trades"][0], "Total Turnover (Rs.)":data1["Total Turnover (Rs.)"][0],"Deliverable Quantity":data1["Deliverable Quantity"][0], "% Deli. Qty to Traded Qty":data1["% Deli. Qty to Traded Qty"][0],  "Spread High-Low":data1["Spread High-Low"][0], "Spread Close-Open":data1["Spread Close-Open"][0]}
final_df = df.append(row, ignore_index=True)
print(len(final_df))
print(final_df.head())
print(final_df.tail())
        





































"""
def SelectedParamToCSV(rawData):
date=[]
price1=[]
price2=[]
price3=[]
price4=[]
price5=[]
price6=[]
for i in range(len(rawData)):
  l1=data["stock"][i].split(",")
date.append(l1[0])
  price1.append(float(l1[1]))
  price2.append(float(l1[2]))
  price3.append(float(l1[3]))
  price4.append(float(l1[4]))
  price5.append(int(l1[5]))
  price6.append(float(l1[6]))
dFrame=pd.DataFrame()
dFrame["Date"]=date
dFrame["Open"]=price1
dFrame["High"]=price2
dFrame["Low"]=price3
dFrame["Close"]=price4
dFrame["Volume"]=price5
dFrame["Profit"]=price6
dFrame.to_csv("Toclk_EURUSD.csv")
return dFrame

def SplitData(data, limit):
train = data.iloc[0:10000, 1:2].values
test=data.iloc[10000:,1:2].values
return train, test


data=pd.read_csv("/content/EURUSDH1.csv",encoding = "cp1252")
#data.columns
#len(data)
#data.head()
#data["stock"][0]

df3 = SelectParamToCSV(data)

#df3.head()
#len(df3)

training_set, test_set = SplitData(data, 10000)


from matplotlib import pyplot
df3.plot()
pyplot.show()
price=pd.DataFrame()
price['Date']=df3['Date']
price['High Price']=df3['High']

price.plot()
pyplot.show()
diet = price[['High Price']]
diet.rolling(12).mean().plot()
plt.xlabel('Year', fontsize=20);

price.plot(style='k.')
pyplot.show()

price.hist()
pyplot.show()

price.plot(kind='kde')
pyplot.show()

training_set, test_set = SplitData(df3, 10000)

training_set
test_set

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)
training_set_scaled= training_set

X_train = []
y_train = []
for i in range(200, 10000):
    X_train.append(training_set_scaled[i-200:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

regressor = Sequential()

# Adding the first LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50,activation='relu', return_sequences = True, input_shape = (X_train.shape[1], 1)))
regressor.add(Dropout(0.2))

# Adding a second LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50,activation='relu', return_sequences = True))
regressor.add(Dropout(0.2))

# Adding a third LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50,activation='relu', return_sequences = True))
#regressor.add(Dropout(0.2))

# Adding a fourth LSTM layer and some Dropout regularisation
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

# Adding the output layer
regressor.add(Dense(units = 1))

# Compiling the RNN
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
regressor.fit(X_train, y_train, epochs = 25, batch_size = 32)


model.save("games.h5")

path= "./jeeva.pkl"
with open(path, 'wb') as f:
        pickle.dump(regressor, f)
        print("Done Pickiling")
        #print("Pickled clf at {}".format(path))

with High("jeeva.pkl", 'rb') as f:
            regressor = pickle.load(f)

data.columns

len(data)

data.columns

data_total = df3['Open']
inputs = data_total[11946 -1946- 200:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

X_test = []
for i in range(200, len(inputs)):
    X_test.append(inputs[i-200:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

print(len(test_set),len(predicted_stock_price))

plt.plot(test_set, color = 'red', label = 'Real Company Prices')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted company Price')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()


from sklearn import metrics
#MAE
print(metrics.mean_absolute_error(test_set,predicted_stock_price))
#MSE
print(metrics.mean_squared_error(test_set,predicted_stock_price))
#RMSE Value
print(np.sqrt(((predicted_stock_price - test_set) ** 2).mean()))

print(min(test_set),max(test_set))
rmse=np.sqrt(((predicted_stock_price - test_set) ** 2).mean())
acc=(rmse-2)/(505749-2)
#Accuracy
print(1-acc)

l=predicted_stock_price.tolist()
import itertools
l=list(itertools.chain(*l))

df=pd.DataFrame()
df["Predicted_Price"]=l
df.to_csv("prediction_of_stock_High_Price_for_500212.csv")

for i in range(1,len(predicted_stock_price)):
  traders=predicted_traders[i]
  prices=predicted_stock_price[i]
  if predicted_traders[i-1]>traders and prices>predicted_stock_price[i-1]:
    print("I Recommend you to choose this stock because this stock is having lesser traders and this stock price will go up may be it will help you get profit")
  else:
    print("I will not Recommend you ")"""
