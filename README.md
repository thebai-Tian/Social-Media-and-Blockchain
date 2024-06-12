# Using AI together with blockchain technology

This repository contains part of the experimental code and part of the data for the master's thesis ‘Using AI together with blockchain technology’ at the Budapest University of Economics and Technology.

## Function

- extracted_tweet_data.csv is the final version of the data obtained via api and processed by natural language processing and third party tools. It contains data of 20,000 processed tweets, including their sentiment, value, and price at the time of publishing, etc.
- The report.zip is the json file of the tweets processed by tweet binder.
- ARIMA.py is the code to train the arima model, the corresponding training file is extracted_tweet_data.csv.
- lstm.py is the code to train lstm model, the corresponding training file is extracted_tweet_data.csv.
- tweets.py is the code to get tweets, to run it you need to buy the tweet api and change to your own tweet api on the api.
- binance.py is the code to get the price of dogcoin at the corresponding time, replace it with your own binanceAPI when using it
- lstm.ipynb for the lstm model training process, which provides some visual images for reference.

## P.S.
If you want to check out specific projects, please visit our thesis website https://diplomaterv.vik.bme.hu/en/ to search for specific things I've researched. If you are interested in my project or have any specific questions about the code, please contact me at tian.zebai@edu.bme.hu.
