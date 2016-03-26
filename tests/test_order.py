import pytest
import order
import time


test_order = {
  "ok": "true",
  "symbol": "FOOBAR",
  "venue": "TESTEX",
  "direction": "buy",
  "originalQty": 100,
  "qty": 100,
  "price": 1000,
  "orderType": "limit",
  "id": 4,
  "account": "EXB123456",
  "ts": "2016-03-16T06:02:07.755758288Z",
  "fills": [],
  "totalFilled": 0,
  "open": "true"
}

order_time = time.strptime("20 Dec 2016 17:45:10", "%d %b %Y %H:%M:%S")
order_ts = time.mktime(order_time)

check_time = time.strptime("20 Dec 2016 17:45:15", "%d %b %Y %H:%M:%S")
check_ts = time.mktime(check_time)

test_order['ts'] = order_ts

def test_is_cold():
  assert order._is_cold(test_order, seconds(10)) == False

def seconds(s):
  return s
