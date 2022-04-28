

from numpy import double
import requests
  
def start() :
    # array of cryptocurrencies
    symbols = ["BTC", "ETH", "BNB", "CHZ", "SOL", "XRP", "ADA", "DOT", "DOGE", "TRX"]
    data = {
        "Tokens": []
    }
    for i in symbols:
    
        # api request
        key = f"https://api.binance.com/api/v3/ticker/price?symbol={i}EUR"
        token_data = requests.get(key)  
        token_data = token_data.json()

        # add € 
        token_data["price"] = f"€ {(double(token_data['price']))}"

        # remove the EUR
        token_data["symbol"] = token_data["symbol"][0:(len(token_data["symbol"])-3)]

        data["Tokens"].append(token_data)
        
    return (data)

