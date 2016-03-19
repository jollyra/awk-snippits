import client

"""
Determine market position based off of filled orders.
"""



"""
Return an updated list of orders
"""
def update(self, orders):
  checked_orders = []
  for order in orders:
    order_id = order['id']
    venue = order['venue']
    stock = order['symbol']
    order_status = client.order_status(order_id, venue, stock)
    checked_orders.push(order_status)
  return checked_orders
