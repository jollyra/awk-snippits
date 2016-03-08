import requests
import json


apikey = '40f908637aba1d813c19119ff50aa1b20e0e925a'

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
  return orderbook

def quote(venue, symbol):
  r = requests.get('https://api.stockfighter.io/ob/api/venues/%s/stocks/%s/quote' % (venue, symbol))
  quote = r.json()
  print(quote['ok'])
  return quote

def placeOrder(order):
  url = 'https://api.stockfighter.io/ob/api/venues/%s/stocks/%s/orders' % (order['venue'], order['stock'])
  headers = {
      'Content-Type': 'application/json',
      'X-Starfighter-Authorization': apikey
  }
  r = requests.post(url, headers=headers, data=order)
  confirmation = r.json()
  print(confirmation['ok'])
  return confirmation

sampleOrder = {
  'account': 'MST92145671',
  'venue': 'LOBHEX',
  'stock': 'LPEI',
  'qty': 100,
  'direction': 'buy',
  'orderType': 'market'
}

placeOrder(sampleOrder)