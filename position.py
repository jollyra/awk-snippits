import client

"""
Determine market position based off of filled orders.
"""
def position(orders):
  statuses = []
  for order in orders:
    order_id = order['id']
    venue = order['venue']
    stock = order['symbol']
    order_status = client.order_status(order_id, venue, stock)
    statuses.push(order_status)

