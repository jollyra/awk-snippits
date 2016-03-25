from functools import partial
from time import time
import client
import config


def order(qty, price, direction):
  order = {
    'account': config.account,
    'venue': config.venue,
    'stock': config.stock,
    'qty': qty,
    'price': int(price),
    'direction': direction,
    'orderType': 'limit'
  }
  print('%s: qty %s price %s' % (direction, qty, price))
  order_status = client.place_order(order)
  if order_status['ok'] != True:
    print('Order invalid: %s' % order)
    print('Server response: %s' % order_status)
  else:
    order_status['ts'] = int(time.time())
    return order_status

sell = partial(order, direction='sell')
buy = partial(order, direction='buy')

# cancel(filter(is_cold, orders))
# def cancel_cold_orders(orders, seconds_elapsed):
#   for order in orders:
#     if time.time() - order['ts'] > seconds_elapsed:
#       client.cancel_order(order['id'], order['venue'], order['symbol'])

def is_cold(order, cutoff_seconds):
  return time() - int(order['ts']) > cutoff_seconds
