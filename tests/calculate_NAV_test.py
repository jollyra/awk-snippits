import pytest
from position import calculate_NAV


def test_with_both_stock_and_cash():
  total_stocks = 10
  total_cash = 250
  quoted_bid_price = 3000
  NAV = calculate_NAV(total_stocks, total_cash, quoted_bid_price)
  assert NAV == 550

def test_with_float_bid_value():
  total_stocks = 10
  total_cash = 250
  quoted_bid_price = 3250
  NAV = calculate_NAV(total_stocks, total_cash, quoted_bid_price)
  assert NAV == 575

def test_with_no_assets():
  total_stocks = 0
  total_cash = 0
  quoted_bid_price = 3000
  NAV = calculate_NAV(total_stocks, total_cash, quoted_bid_price)
  assert NAV == 0

def test_with_no_cash():
  total_stocks = 10
  total_cash = 0
  quoted_bid_price = 3000
  NAV = calculate_NAV(total_stocks, total_cash, quoted_bid_price)
  assert NAV == 300

def test_with_no_stocks():
  total_stocks = 0
  total_cash = 100
  quoted_bid_price = 3000
  NAV = calculate_NAV(total_stocks, total_cash, quoted_bid_price)
  assert NAV == 100
