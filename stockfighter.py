import requests


def heartbeat(venue):
  r = requests.get('https://api.stockfighter.io/ob/api/venues/%s/heartbeat' % venue)
  print('%s is online' % r.json()['venue'])

heartbeat('TESTEX')

