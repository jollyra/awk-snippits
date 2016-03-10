import client


account = 'PAC66537983'
venue = 'RYMMEX'
stock ='BWM'

shares = 0  # must be between -1000 and +1000
net_asset_value = 0  # goal is $10,000

def market_maker():
  while net_asset_value < 100000:
    orderbook = client.orderbook(venue, stock)
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
