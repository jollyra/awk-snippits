import pytest
import json
import position
import test_data


def load_from_json(fn):
  with open(fn, encoding='utf-8') as f:
    data = json.load(f)
    return data

def test_calculate_position_single():
  orders = test_data.orders
  stocks, cash = position.calculate_position(orders[:1])
  assert stocks == 30
  assert cash == -30000

def test_calculate_position_multiple():
  orders = test_data.orders
  stocks, cash = position.calculate_position(orders[:2])
  assert stocks == 30 + 50
  assert cash == -30000 - 50 * 1020

def test_calculate_position_no_fills():
  orders = test_data.orders_no_fills
  stocks, cash = position.calculate_position(orders[:2])
  assert stocks == 0
  assert cash == 0

