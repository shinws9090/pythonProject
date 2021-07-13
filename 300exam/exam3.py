import time

import requests




url = "https://api.upbit.com/v1/market/all"

querystring = {"isDetails": "false"}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

url = "https://api.upbit.com/v1/ticker"

querystring = {"markets":"KRW-med"}

headers = {"Accept": "application/json"}
while True:
    response = requests.request("GET", url, headers=headers, params=querystring)

    open_price = response.json()[0]['trade_price']
    print("메디블록 : {}원".format(open_price))
    time.sleep(0.5)

