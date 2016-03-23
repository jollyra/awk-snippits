from time import sleep

import client
import position
import order
import config


def too_short(stocks):
  return stocks < -100

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

    quote = client.quote(config.venue, config.stock)
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
      orders.append(order.buy(25, ask_price - 50))
    elif too_long(stocks):
      print('too long')
      orders.append(order.sell(25, bid_price + 50))
    else:
      orders.append(order.buy(25, ask_price - 20))
      orders.append(order.sell(25, bid_price + 20))

    sleep(6) # in seconds
    print('round end\n')

# Go!
if __name__ == '__main__':
  market_maker()
