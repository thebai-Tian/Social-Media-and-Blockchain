from binance.client import Client
import time


client = Client(api_key="0IXsONY8LqXSUeVydhJLRoBdNWvm4msMzATLrcmYMJ5nmbn3wXW71YJ1F3ky3nSw", api_secret="*")


start_timestamp = 1702666221  
end_timestamp = 1703022954    


current_time = int(time.time())
if start_timestamp <= current_time <= end_timestamp:
    ticker = client.get_symbol_ticker(symbol="DOGEUSDT")
    price = ticker["price"]
    print(f"Timestamp: {current_time}, Price: {price}")
else:
    print("Current time is outside the specified timestamp range.")
