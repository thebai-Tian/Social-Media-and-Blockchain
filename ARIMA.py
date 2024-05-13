import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
 
# Load the CSV file
csv_path = 'C:\\Users\\86151\\Desktop\\extracted_tweet_data.csv'
data = pd.read_csv(csv_path)
 
# Convert 'CreatedAt' to datetime if it's not already
data['CreatedAt'] = pd.to_datetime(data['CreatedAt'])
 
# Sort the data by date
data.sort_values('CreatedAt', inplace=True)
 
# Using 95% of data for training and the rest for testing
train_size = int(len(data) * 0.90)
train, test = data.iloc[:train_size], data.iloc[train_size:]
 
# The 'price' column is what we want to predict
train_price = train['price']
test_price = test['price']
 
# Fit the ARIMA model (p,d,q) parameters need to be optimized for your specific case
# Here, we'll just use (1,1,1) as a placeholder
model = ARIMA(train_price, order=(2, 2, 2))
model_fit = model.fit()
 
# Forecast
forecast = model_fit.forecast(steps=len(test_price))
 
# Calculate the mean squared error
error = mean_squared_error(test_price, forecast)
 
# Output the error to see how well our model performed
print(f"The Mean Squared Error of the forecast is: {error}")
 
# If you want to see the forecasted values you can print the forecast
print(forecast)
