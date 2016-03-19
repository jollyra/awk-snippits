import client
import position
from time import sleep

account = 'TMB99612289'
venue = 'GTIEX'
stock ='SYO'


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
  print('bid: qty %s price %s' % (qty, price))
  order_status = client.place_order(order)
  if order_status['ok'] != True:
    print('Order invalid: %s' % order)
    print('Server response: %s' % order_status)
  else:
    return order_status

def place_ask(qty, price):
  order = {
    'account': account,
    'venue': venue,
    'stock': stock,
    'qty': qty,
    'price': price,
    'direction': 'sell',
    'orderType': 'limit'
  }
  print('ask: qty %s price %s' % (qty, price))
  order_status = client.place_order(order)
  if order_status['ok'] != True:
    print('Order invalid: %s' % order)
    print('Server response: %s' % order_status)
  else:
    return order_status

def too_short(stocks):
  return stocks < 100

def too_long(stocks):
  return stocks > 100


""" Algorithm
get a quote for the stock
buy or sell depending on position
wait a bit
check orders for fills and update state

Problem:
I'm only tracking position, but I need to track cash as well
"""

def market_maker():
  # bootstrap
  stocks = 0  # must be between -1000 and +1000
  cash = 0    # goal is $10,000
  orders = []

  while True:
    print('round start')
    orders = position.update(orders)
    stocks, cash = position.calculate_position(orders)
    print('stocks %s' % stocks)
    print('cash %s' % position.cash_to_str(cash))
    print('# of orders %s' % len(orders))
    quote = client.quote(venue, stock)
    if too_short(stocks):
      if 'ask' in quote:
        price = quote['ask']
        price -= 5  # buy lower
        orders.append(place_ask(100, price))
    elif too_long(stocks):
      if 'bid' in quote:
        price = quote['bid']
        price += 5  # sell higher
        orders.append(place_bid(100, price))
    else:
      return

    sleep(5) # in seconds
    print('round end\n')

# Go!
if __name__ == '__main__':
  market_maker()
