
#Author : JEEVA T
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

data=pd.read_csv("/content/prices.csv")

data.columns

data_1=data.sort_values(['date'])#.groupby('symbol')

data_1

data_1.head()

print(len(data))
print(data.head())

price=[]
for i in range(len(data_1)):
  if 
  price.a
  training_set = data.iloc[len(data)-4000:len(data)-1000, 2:3].values
test_set=data.iloc[len(data)-1000:,2:3].values

from matplotlib import pyplot
data.plot()
pyplot.show()

price=pd.DataFrame()
price['date']=data['date']
price['open']=data['open']

price.plot()
pyplot.show()

diet = price[['open']]
diet.rolling(12).mean().plot()
plt.xlabel('Year', fontsize=20);

price.plot(style='k.')
pyplot.show()

price.hist()
pyplot.show()

price.plot(kind='kde')
pyplot.show()

price=[]
for i in range(len(data_1)):
  if data_1['symbol'][i]=='INTC':
    price.append(data_1['open'][i])
len(price)
training_set = data.iloc[:len(price)-200, 2:3].values
test_set=data.iloc[len(data)-200:,2:3].values

training_set

test_set

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

X_train = []
y_train = []
for i in range(200, len(price)-200):
    X_train.append(training_set_scaled[i-200:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

X_train.shape

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
#Long Training use 53 epoch because after that the loss is having lesser difference
regressor.fit(X_train, y_train, epochs = 100, batch_size = 100)

path= "./model.pkl"
with open(path, 'wb') as f:
        pickle.dump(regressor, f)
        print("Done Pickiling")
        #print("Pickled clf at {}".format(path))

with open("model.pkl", 'rb') as f:
            regressor = pickle.load(f)

data.columns

type(data['open'])

data_total = pd.core.series.Series(price)
inputs = data_total[len(price)-250:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

inputs.shape

X_test = []
for i in range(200, len(inputs)):
    X_test.append(inputs[i-200:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

plt.plot(test_set, color = 'red', label = 'Real Company Prices')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted company Price')
plt.title('Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()


#I created Dynamic Stock Market Price Prediction Web App using Flask https://www.linkedin.com/feed/update/urn:li:activity:6676910874441211904/     Demo Video
# Next stage I planned to predict stock prices using RNN+Sentiment_Analysis will give better result
