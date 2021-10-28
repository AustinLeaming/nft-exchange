import requests
import apikey

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey.API_KEY,
}

params = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']

for x in coins:
    print(x['symbol'], x['quote']['USD']['price'])