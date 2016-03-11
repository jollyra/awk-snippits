import json

def load(fn):
  with open(fn, encoding='utf-8') as f:
    data = json.load(f)
    return data
