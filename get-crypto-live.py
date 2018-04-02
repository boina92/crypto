
import requests
priceURL='https://min-api.cryptocompare.com/data/price'


print()
print("Get the live price of any cryptocurrencies (example: BTC, ETH, LTC...)")
print("Type the ticker of the cryptocurrency of your choice in USD")
choice = input("Your choice: ")


currency="USD"
getURL=priceURL+'?fsym='+choice+'&tsyms='+currency
r = requests.get(getURL)
print(r.json())