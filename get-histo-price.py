import time
import requests
from datetime import date
from datetime import timedelta

priceURL='https://min-api.cryptocompare.com/data/pricehistorical'

print()
print("Get the historical price of any cryptocurrencies (example: BTC, ETH, LTC...)")
print("Type the ticker of the cryptocurrency of your choice in USD")
choice = input("Type the ticker of your crypto:")
currency='USD'

date = input("Type the start date YYYY-MM-DD")
before = input("Type the start date YYYY-MM-DD")
timestamp = time.mktime(time.strptime(str(date), '%Y-%m-%d'))
timestamp1 = time.mktime(time.strptime(str(before), '%Y-%m-%d'))
step = 86400
x=timestamp

getURL=priceURL+'?fsym='+choice+'&tsyms='+currency+'&ts='+str(round(timestamp,0))
r = requests.get(getURL)
print(r.json())

numbers = range(int(timestamp),int(timestamp1),step)
for count in numbers:
    x+=step
    getURL=priceURL+'?fsym='+choice+'&tsyms='+currency+'&ts='+str(x)
    r = requests.get(getURL)
    print(r.json())