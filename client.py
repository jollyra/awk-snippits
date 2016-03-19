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
  return orderbook

def quote(venue, symbol):
  r = requests.get('https://api.stockfighter.io/ob/api/venues/%s/stocks/%s/quote' % (venue, symbol))
  return r.json()

def order_status(orderId, venue, symbol):
  url = 'https://api.stockfighter.io/ob/api/venues/%s/stocks/%s/orders/%s' % (venue, symbol, orderId)
  headers = {
      'X-Starfighter-Authorization': apikey
  }
  r = requests.get(url, headers=headers)
  return r.json()

def status_for_all_orders(venue, account, symbol):
  url = 'https://api.stockfighter.io/ob/api/venues/%s/accounts/%s/stocks/%s/orders' % (venue, account, symbol)
  headers = {
      'Content-Type': 'application/json',
      'X-Starfighter-Authorization': apikey
  }
  r = requests.get(url, headers=headers)
  return r.json()

def cancel_order(orderId, venue, symbol):
  r = requests.delete('https://api.stockfighter.io/ob/api/venues/%s/stocks/%s/orders/%s' % (venue, symbol, orderId))
  return r.json()

def place_order(order):
  """ Accepts an Order named tuple and returns an Order """
  url = 'https://api.stockfighter.io/ob/api/venues/%s/stocks/%s/orders' % (order['venue'], order['stock'])
  headers = {
      'Content-Type': 'application/json',
      'X-Starfighter-Authorization': apikey
  }
  r = requests.post(url, headers=headers, data=json.dumps(order))
  confirmation = r.json()
  return confirmation


if __name__ == '__main__':
  heartbeat('TESTEX')
