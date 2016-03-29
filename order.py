from functools import partial
from time import time
from datetime import datetime
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
    order_status['ts'] = time.time()
    return order_status

sell = partial(order, direction='sell')
buy = partial(order, direction='buy')

def cancel_cold_orders(orders, cutoff_seconds):
  now_ts = time()
  [_cancel(order) for order in orders if _is_cold(now_ts, order['ts'], cutoff_seconds)]

def _is_cold(now_ts, order_ts, cutoff_seconds):
  return now_ts - order_ts > cutoff_seconds

def _cancel(order):
  client.cancel_order(order['id'], order['venue'], order['symbol'])
