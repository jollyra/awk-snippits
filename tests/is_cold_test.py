import pytest
import order
import time
from datetime import datetime


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
test_order['ts'] = order_ts

check_time = time.strptime("20 Dec 2016 17:45:15", "%d %b %Y %H:%M:%S")
check_ts = time.mktime(check_time)


def test_cold_order(monkeypatch):
  monkeypatch.setattr(time, 'time', lambda: check_ts)
  is_cold = order._is_cold(time.time(), test_order['ts'], seconds(10))
  assert is_cold == False, "is_cold returned True but the order was cold"

def test_live_order(monkeypatch):
  monkeypatch.setattr(time, 'time', lambda: check_ts)
  is_cold = order._is_cold(time.time(), test_order['ts'], seconds(1))
  assert is_cold == True, "is_cold returned False but the order wasn't cold"

def test_live_order_on_boundry(monkeypatch):
  monkeypatch.setattr(time, 'time', lambda: check_ts)
  is_cold = order._is_cold(time.time(), test_order['ts'], seconds(5))
  assert is_cold == False, "order should be cold on the boundry"

def test_live_order_off_boundry(monkeypatch):
  monkeypatch.setattr(time, 'time', lambda: check_ts)
  is_cold = order._is_cold(time.time(), test_order['ts'], seconds(4))
  assert is_cold == True, "order should be live off the boundry"

def seconds(s):
  return s
