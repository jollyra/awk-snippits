import client


account = 'PAC66537983'
venue = 'RYMMEX'
stock ='BWM'

filled = 0
openOrders = []
count = 0

"""
Policy
If there's an ask buy the best ask
If there's a bid beat the best bid by 1
If the book is empty lowball
"""
while count < 100000:
  orderbook = client.orderbook(venue, stock)
  price = 0
  if orderbook['asks']:
    bestAsk = orderbook['asks'][0]
    price = bestAsk['price']
    qty = bestAsk['qty']

  elif orderbook['bids'][0]:
    bestBid = orderbook['bids'][0]
    price = bestBid['price'] + 1
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
  client.placeOrder(order)
  count += 1
