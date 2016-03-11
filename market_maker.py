import client


account = 'PAC66537983'
venue = 'RYMMEX'
stock ='BWM'

shares = 0  # must be between -1000 and +1000
net_asset_value = 0  # goal is $10,000
open_orders = []  # keep track of my position in the market
spread = 10
"""
Algorithm:
  init baseline
  place asks at price p
  if p is not filled:
    place ask at price p + 1
  else if p is filled:
    place ask at p - 1
    place bid at p - spread
  update baseline

Now in plain ambiguous English:
  buy some stock as cheap as we can
  try selling if for as much as possible
  reduce price until we can sell
  repeat
"""
def market_maker():
  while True:
    price = 0
    if orderbook['asks']:
      best_ask = orderbook['asks'][0]
      price = best_ask['price']
      qty = best_ask['qty']

    elif orderbook['bids'][0]:
      best_bid = orderbook['bids'][0]
      price = best_bid['price'] + 1
      qty = 10

    else:
      price = 1

    count += 1


# book = client.orderbook(venue, stock)
def bootstrap_market_state(direction, orderbook):
  total_price = 0
  total_qty = 0
  for bid in orderbook[direction][:2]:
    total_price += bid['price'] * bid['qty']
    total_qty += bid['qty']
  return total_price / total_qty

def bid(qty, price):
  order = {
    'account': account,
    'venue': venue,
    'stock': stock,
    'qty': qty,
    'price': price,
    'direction': 'buy',
    'orderType': 'limit'
  }
  order_status = client.place_order(order)
  if order_status['ok'] == 'true':
    open_orders.append()
  else:
    print('Order invalid: %s' % order)

def ask(qty, price):
  order = {
    'account': account,
    'venue': venue,
    'stock': stock,
    'qty': qty,
    'price': price,
    'direction': 'ask',
    'orderType': 'limit'
  }
  order_status = client.place_order(order)
  if order_status['ok'] == 'true':
    open_orders.append()
  else:
    print('Order invalid: %s' % order)
