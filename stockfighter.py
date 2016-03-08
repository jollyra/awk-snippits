import requests


def heartbeat(venue):
  r = requests.get('https://api.stockfighter.io/ob/api/venues/%s/heartbeat' % venue)
  print('%s is online' % r.json()['venue'])

def stocks(venue):
  r = requests.get('https://api.stockfighter.io/ob/api/venues/%s/stocks' % venue)
  stocks = r.json()
  print(stocks['ok'])
  return stocks

def orderbook(venue, symbol):
  r = requests.get('https://api.stockfighter.io/ob/api/venues/%s/stocks/%s' % (venue, symbol))
  orderbook = r.json()
  print(orderbook['ok'])

print(stocks('TESTEX'))
