# Description : This program uses an artificial recurrent neural network called
# Long short Term Memory LSTM
# to predict the closing stock price of a corporation using the past 60 day stock price.
#import the library
import math
import pandas_datareader as web
import numpy as np
import pandas as pd 
import io
from datetime import date, timedelta
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')
 
#List of ticker for Nifty 50 Companies.
ticker_list = ['RELIANCE.NS']##,'HDFCBANK.NS']##,'INFY.NS','HDFC.NS','TCS.NS','ICICIBANK.NS','KOTAKBANK.NS','HINDUNILVR.NS','ITC.BO','BHARTIARTL.NS','LT.NS','AXISBANK.NS','BAJFINANCE.NS','MARUTI.NS','ASIANPAINT.NS','HCLTECH.NS','SBIN.NS','NESTLEIND.NS','M&M.NS','SUNPHARMA.NS','DRREDDY.NS']
 
#Function will return the dataset with future predictions of stock prices of next 1 - year.
#1825 stands for 5 year time period.
def predict_stock_prices(company_ticker,prediction_based_on_past_days = 1825):
  """
    Explaination of function.
  """
 
  #Getting start and end date to give input to yahoo api.
  today = date.today()
  current_date = today.strftime("%m%d%Y")  
  month_old_date = (date.today()-timedelta(days=prediction_based_on_past_days)).strftime("%m%d%Y") 
  from_day = month_old_date[2:4]
  from_month = month_old_date[0:2]
  from_year = month_old_date[4:]
  to_day = current_date[2:4]
  to_month = current_date[0:2]  
  to_year = current_date[4:]
  start_date = from_year + "-" + from_month + "-" + from_day
  end_date = to_year + "-" + to_month + "-" + to_day
  
  
  #Retriving data from yahoo api.
  df = web.DataReader(company_ticker,data_source = 'yahoo',start = start_date,end = end_date)
  # df = df.set_index('Date')
  # df = df.iloc[::-1]
 
 
  # Create a new dataframe with only the close column
  data = df.filter(['Close'])
  # Convert the dataframe to a numpy array
  dataset = data.values
  #Get the number of rows to train the model on
  training_data_len = math.ceil(len(dataset) * 1)
 
  #Scale the data
  #its just a good practice to normalize or to scale the data before giving it to neural network.
  scaler = MinMaxScaler(feature_range = (0,1))
  #feature range tells us in which range the data lies.
  scaled_data = scaler.fit_transform(dataset)
 
  #Create the training data set
  #Create the scaled training data set
  train_data = scaled_data[0:training_data_len,:]
  #Split the data into x_train and y_train data sets
  x_train = []
  y_train = []
  for i in range(60,len(train_data)):
    x_train.append(train_data[i-60:i,0])
    y_train.append(train_data[i,0])
 
  #Convert the x_train and y_train to numpy arrays
  x_train, y_train = np.array(x_train) , np.array(y_train)
  #Reshape the data
  # An Lstm model expects the input  as 3-d data ,no_of_rows(no of samples) time-stamp and number of feature
  x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
  
 
  # Build the LSTM
  model = Sequential()
  model.add(LSTM(50,return_sequences = True, input_shape = (x_train.shape[1],1)))
  model.add(LSTM(50,return_sequences=False))
  model.add(Dense(25))
  model.add(Dense(1))
  
  #Compile the model 
  #optimizer is used to improve upon loss function
  #loss function used to calculate how welll the model did on training.
  model.compile(optimizer = 'adam', loss = 'mean_squared_error')
  
  #Train the model
  model.fit(x_train,y_train,batch_size = 1,epochs = 1)
  #get the quote
  apple_quote = web.DataReader(company_ticker,data_source = 'yahoo',start = start_date,end = end_date)
  #create a new dataframe
  new_df = apple_quote.filter(['Close'])
  #get the last 60 day closing price values and convert the dataframe to an array
  last_60_days = new_df[-60:].values
  #scale the data to be values b/w 0 and 1
  last_60_days_scaled = scaler.transform(last_60_days)
  #create a empty list
  X_test_ = []
  #Append teh last_60_days_scaled
  X_test_.append(last_60_days_scaled)
  X_test_ = np.array(X_test_)
  X_test__ = np.copy(X_test_)
  counter = 365
  while(counter > 0):
    X_test_ = X_test__[0][-60:]
    X_final = []
    X_final.append(X_test_)
    X_final = np.array(X_final)
    X_final = np.reshape(X_final, (X_final.shape[0],X_final.shape[1],1))
    # Get the predicted scaled price
    pred_price = model.predict(X_final)
    x_t = np.append(X_test__[0],pred_price).reshape((X_test__[0].shape[0] + pred_price.shape[0],1))
    l = []
    l.append(x_t)
    l = np.array(l)
    X_test__ = np.reshape(l,(l.shape[0],l.shape[1],1))
    counter = counter - 1
  arr = X_test__
  arr = arr.reshape(arr.shape[1],1)
  lis = []
  for i in range(0,arr.shape[0]):
    lis.append(scaler.inverse_transform(np.array(arr.item(i,0)).reshape(-1,1)).item(0,0))
  return lis

dict = {
    
}

for company in ticker_list:
  lis = predict_stock_prices(company)
  dict[company] = lis

df = pd.DataFrame(dict)
print(df.head())    
    