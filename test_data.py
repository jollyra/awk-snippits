orders = [{
  "ok": "true",
  "symbol": "FOOBAR",
  "venue": "TESTEX",
  "direction": "buy",
  "originalQty": 200,
  "qty": 100,
  "price": 1050,
  "orderType": "limit",
  "id": 1,
  "account": "EXB123456",
  "ts": "2016-03-16T06:02:07.755758288Z",
  "fills": [{
    "price": 1000,
    "qty": 10,
    "ts": "2015-07-05T22:16:18+00:00"
    },{
    "price": 1000,
    "qty": 10,
    "ts": "2015-07-05T22:16:18+00:00"
    },{
    "price": 1000,
    "qty": 10,
    "ts": "2015-07-05T22:16:18+00:00"
    }
  ],
  "totalFilled": 30,
  "open": "true"
},{
  "ok": "true",
  "symbol": "FOOBAR",
  "venue": "TESTEX",
  "direction": "buy",
  "originalQty": 100,
  "qty": 100,
  "price": 1020,
  "orderType": "limit",
  "id": 2,
  "account": "EXB123456",
  "ts": "2016-03-16T06:02:07.755758288Z",
  "fills": [{
    "price": 1020,
    "qty": 50,
    "ts": "2015-07-05T22:16:18+00:00"
    }],
  "totalFilled": 50,
  "open": "true"
},{
  "ok": "true",
  "symbol": "FOOBAR",
  "venue": "TESTEX",
  "direction": "buy",
  "originalQty": 100,
  "qty": 100,
  "price": 1030,
  "orderType": "limit",
  "id": 3,
  "account": "EXB123456",
  "ts": "2016-03-16T06:02:07.755758288Z",
  "fills": [{
    "price": 1000,
    "qty": 20,
    "ts": "2015-07-05T22:16:18+00:00"
    }],
  "totalFilled": 20,
  "open": "true"
},{
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
  "fills": [{
    "price": 1050,
    "qty": 50,
    "ts": "2015-07-05T22:16:18+00:00"
    }],
  "totalFilled": 50,
  "open": "true"
}]

orders_no_fills = [{
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
}]
