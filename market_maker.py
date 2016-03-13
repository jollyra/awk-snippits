import client


account = 'PAC66537983'
venue = 'RYMMEX'
stock ='BWM'

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

shares = 0  # must be between -1000 and +1000
net_asset_value = 0  # goal is $10,000
spread = 5
qty = 1;
def market_maker():
  orders = []  # open orders
  tape = []  # filled orders E.g {price: 33, qty: 1, ts: something}
  inventory = []  # how invested am I currently

  orderbook = client.orderbook(venue, stock)
  bid_p = bootstrap_market_state('bids', orderbook)
  ask_p = bootstrap_market_state('asks', orderbook)
  spread = ask_p - bid_p

  while True:
    open_orders.append(place_bid(qty, bid_p))
    open_orders.append(place_ask(qty, ask_p))

    update_position()

def update_orders():
  for order in orders:
    order_status = client.order_status(order['id'], venue, stock)
    if len(order_status['fills']) > 0:
      tape.push(order_status['fills'])

# book = client.orderbook(venue, stock)
def bootstrap_market_state(direction, orderbook):
  total_price = 0
  total_qty = 0
  for bid in orderbook[direction][:2]:
    total_price += bid['price'] * bid['qty']
    total_qty += bid['qty']
  return total_price / total_qty

def place_bid(qty, price):
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
  if order_status['ok'] != 'true':
    print('Order invalid: %s' % order)
  else:
    return order_status

def place_ask(qty, price):
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
  if order_status['ok'] != 'true':
    print('Order invalid: %s' % order)
  else:
    return order_status
