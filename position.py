import client
from functools import partial

"""
Calculate market position based off of orders
"""
def calculate_position(orders):
  stocks = 0
  cash = 0
  for order in orders:
    if 'fills' in order:
      for fill in order['fills']:
        price = fill['price']
        qty = fill['qty']
        if order['direction'] == 'buy':
          stocks += qty
          cash -= price * qty
        else:
          stocks -= qty
          cash += price * qty
  return stocks, cash

"""
Calculate NAV based off of a single symbol
"""
def calculate_NAV(venue, symbol, stocks, cash):
  quote = client.quote(venue, symbol)
  best_bid = quote['bid']
  return cash + stocks * best_bid

"""
Return an updated list of orders
"""
def update(orders):
  checked_orders = []
  for order in orders:
    order_id = order['id']
    venue = order['venue']
    stock = order['symbol']
    order_status = client.order_status(order_id, venue, stock)
    checked_orders.append(order_status)
  return checked_orders

def cash_to_str(cash):
  cash = cash / 100
  return '$%s' % cash

def ask_value(orders):
  total_price_of_asks = 0
  num_of_asks = 0
  asks = get_last_n_asks(5, orders)
  for ask in asks:
    if 'fills' in ask:
      for fill in ask['fills']:
        price = fill['price']
        qty = fill['qty']
        total_price_of_asks += price * qty
        num_of_asks += qty
  value = None
  if num_of_asks != 0:
    value = total_price_of_asks / num_of_asks
  return value

def bid_value(orders):
  total_price_of_bids = 0
  num_of_bids = 0
  bids = get_last_n_bids(5, orders)
  for bid in bids:
    if 'fills' in bid:
      for fill in bid['fills']:
        price = fill['price']
        qty = fill['qty']
        total_price_of_bids += price * qty
        num_of_bids += qty
  value = None
  if num_of_bids != 0:
    value = total_price_of_bids / num_of_bids
  return value

def get_last_n_orders(n, orders, direction):
  return list(filter(lambda o: o['direction'] == direction, orders))[-n:]

get_last_n_bids = partial(get_last_n_orders, direction='buy')
get_last_n_asks = partial(get_last_n_orders, direction='sell')
