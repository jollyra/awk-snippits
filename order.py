from datetime import datetime
import client
import config


def order(direction, qty, price):
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
    order_status['ts'] = datetime.now().time()
    return order_status

sell = partial(order, direction='sell')
buy = partial(order, direction='buy')
