import client


account = 'PAC66537983'
venue = 'RYMMEX'
stock ='BWM'

shares = 0  # must be between -1000 and +1000
net_asset_value = 0  # goal is $10,000
orders = []

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

    order = {
      'account': account,
      'venue': venue,
      'stock': stock,
      'qty': qty,
      'price': price,
      'direction': 'buy',
      'orderType': 'limit'
    }
    client.place_order(order)
    count += 1

def bootstrap_market_state(direction):
  book = client.orderbook(venue, stock)
  total_price = 0
  total_qty = 0
  for bid in book[direction][:2]:
    total_price += bid['price'] * bid['qty']
    total_qty += bid['qty']
  return total_price / total_qty

