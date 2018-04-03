import time
import requests
import datetime
from datetime import date
from datetime import timedelta

priceURL='https://min-api.cryptocompare.com/data/pricehistorical'

print()
print("Get the historical price of any cryptocurrencies (example: BTC, ETH, LTC...)")
print("Type the ticker of the cryptocurrency of your choice in USD")
choice = input("Type the ticker of your crypto:")
currency='USD'

date = input("Type the start date YYYY-MM-DD")
date1 = input("Type the start date YYYY-MM-DD")

#convert date to timestamp

timestamp = time.mktime(time.strptime(str(date), '%Y-%m-%d'))
timestamp1 = time.mktime(time.strptime(str(date1), '%Y-%m-%d'))

#one day is equal to 86400 in the timestamp language

step = 86400
x=timestamp

#iterating through the range (timestamp,timestamp2) in order to print historical values

numbers = range(int(timestamp),int(timestamp1)+step,step)
for count in numbers:
    x+=step
    getURL=priceURL+'?fsym='+choice+'&tsyms='+currency+'&ts='+str(x)
    r = requests.get(getURL)
    date_format = datetime.datetime.fromtimestamp(int(x-step)).strftime('%Y-%m-%d')
    print(date_format)
    print(r.json())
    