from time import sleep

import client
import position
import order
import config


def market_maker():
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
    orders.append(order.buy(25, ask_price - 20))
    orders.append(order.sell(25, bid_price + 20))
    orders.cancel_cold_orders(orders, 10);
    sleep(6) # in seconds
    print('round end\n')

def bootstrap():
  quote = client.quote(config.venue, config.stock)
  if 'ask' in quote:
    ask_price = quote['ask']
  else:
    ask_price = 100
  if 'bid' in quote:
    bid_price = quote['bid']
  else:
    bid_price = 100

# Go!
if __name__ == '__main__':
  market_maker()
