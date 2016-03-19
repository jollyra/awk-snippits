import client


"""
Calculate market position based off of orders
"""
def calculate_position(orders):
  stocks = 0
  cash = 0
  for order in orders:
    if fills in order:
      for fill in fills:
        price = fill['price']
        qty = fill['qty']
        if order['direction'] == 'buy':
          stocks += qty
          cash -= price * qty
        else:
          stocks -= qty
          cash += price * qty



"""
Return an updated list of orders
"""
def update(orders):
  checked_orders = []
  for order in orders:
    order_id = order['id']
    venue = order['venue']
    stock = order['symbol']
    order_status = client.order_status(order_id, venue, stock)
    checked_orders.push(order_status)
  return checked_orders
