import client
from time import sleep


account = 'MYC23658935'
venue = 'KDEX'
stock ='FPCM'

def check_orders():
  position = 0
  res = client.status_for_all_orders(venue, account, stock)
  orders = res['orders']
  for order in orders:
    if order['direction'] == 'buy':
      position += order['qty']
    elif order['direction'] == 'sell':
      position -= order['qty']
    else:
      print('Invalid direction:\n %s' % order)
  return position

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
  position = 0  # must be between -1000 and +1000

  while True:
    print('round start')
    print('position %s' % position)
    quote = client.quote(venue, stock)
    if position > 0:
      if 'ask' in quote:
        price = quote['ask']
        price -= 5  # buy lower
        place_ask(10, price)
    else:
      if 'bid' in quote:
        price = quote['bid']
        price += 5  # sell higher
        place_bid(10, price)
    sleep(5) # in seconds
    position = check_orders()
    print('round end')


# Go!
if __name__ == '__main__':
  market_maker()
