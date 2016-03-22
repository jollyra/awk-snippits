import client
import position
from time import sleep
from datetime import datetime

account = 'BM54105917'
venue = 'YRPHEX'
stock ='CIIC'


def sell(qty, price):
  order = {
    'account': account,
    'venue': venue,
    'stock': stock,
    'qty': qty,
    'price': int(price),
    'direction': 'sell',
    'orderType': 'limit'
  }
  print('sell: qty %s price %s' % (qty, price))
  order_status = client.place_order(order)
  if order_status['ok'] != True:
    print('Order invalid: %s' % order)
    print('Server response: %s' % order_status)
  else:
    return order_status

def buy(qty, price):
  order = {
    'account': account,
    'venue': venue,
    'stock': stock,
    'qty': qty,
    'price': int(price),
    'direction': 'buy',
    'orderType': 'limit'
  }
  print('buy: qty %s price %s' % (qty, price))
  order_status = client.place_order(order)
  if order_status['ok'] != True:
    print('Order invalid: %s' % order)
    print('Server response: %s' % order_status)
  else:
    order_status['ts'] = datetime.now().time()
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
    orders = position.update(orders)  # check the status of orders
    stocks, cash = position.calculate_position(orders)  # determine market position
    print('stocks %s' % stocks)
    print('cash %s' % position.cash_to_str(cash))
    print('# of orders %s' % len(orders))

    quote = client.quote(venue, stock)
    if 'ask' in quote:
      ask_price = quote['ask']
    else:
      ask_price = 100
    if 'bid' in quote:
      bid_price = quote['bid']
    else:
      bid_price = 100

    if too_short(stocks):
      print('too short')
      orders.append(buy(25, ask_price - 50))
    elif too_long(stocks):
      print('too long')
      orders.append(sell(25, bid_price + 50))
    else:
      orders.append(buy(25, ask_price - 20))
      orders.append(sell(25, bid_price + 20))

    sleep(6) # in seconds
    print('round end\n')

# Go!
if __name__ == '__main__':
  market_maker()
