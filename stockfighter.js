var https = require('https');

function get(url) {
  return new Promise(function (resolve, reject) {
    https.get(url, function (res) {
      var body = "";

      res.on('data', function (d) {
        body += d;
      });

      res.on('end', function () {
        resolve(body);
      });

    }).on('error', function (e) {
      reject(e);
    });
  });
}

function placeOrder(order) {

  var options = {
    hostname: 'api.stockfighter.io',
    path: `/ob/api/venues/${order.venue}/stocks/${order.stock}/orders`,
    method: 'POST',
    agent: false,
    headers: {
      'Content-Type': 'application/json',
      'X-Starfighter-Authorization': '40f908637aba1d813c19119ff50aa1b20e0e925a'
    }
  };

  var req = https.request(options, (res) => {
    console.log(`STATUS: ${res.statusCode}`);
    console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
    res.setEncoding('utf8');
    res.on('data', (chunk) => {
      console.log(`BODY: ${chunk}`);
    });
    res.on('end', () => {
      console.log('No more data in response.')
    })
  });

  req.on('error', (e) => {
    console.log(`problem with request: ${e.message}`);
  });

  // write data to request body
  req.write(JSON.stringify(order));
  req.end();
}

var api = {
  hearbeat: function () {
    'https://api.stockfighter.io/ob/api/venues/TESTEX/heartbeat'
  },
  listStocksByVenue: function (venue) {
    return `https://api.stockfighter.io/ob/api/venues/${venue}/stocks`;
  },
  getQuote: function (venue, stock) {
    return `http https://api.stockfighter.io/ob/api/venues/${venue}/stocks/${stock}/quote`;
  },
  getOrderbook: function (venue, stock) {
    return `https://api.stockfighter.io/ob/api/venues/${venue}/stocks/${stock}`;
  }
}

// get(api.getOrderbook('TESTEX', 'FOOBAR')).then(function (res) {
//   console.log(res);
// });

var order = {
  'account': 'EXB123456',
  'venue': 'TESTEX',
  'stock': 'FOOBAR',
  'qty': 100,
  'direction': 'buy',
  'orderType': 'limit'
}

// placeOrder('TESTEX', 'FOOBAR', order).then(function (res) {
//   console.log(res);
// });
placeOrder(order);
