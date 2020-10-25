# Description : This program uses an artificial recurrent neural network called
# Long short Term Memory LSTM
# to predict the closing stock price of a corporation using the past 60 day stock price.

#import the library
import math
import pandas_datareader as web
import numpy as np
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')

# Get the number of rows and 
df = web.DataReader('AAPL',data_source = 'yahoo',start = '2012-01-01',end = '2019-12-17')
print(df)

# Get the number of rows and columns in the data set
print(df.shape