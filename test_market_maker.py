import pytest
import json
import position

def load_from_json(fn):
  with open(fn, encoding='utf-8') as f:
    data = json.load(f)
    return data

def test_position():
    assert 4 == 4
