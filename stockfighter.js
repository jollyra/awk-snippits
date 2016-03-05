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

function heartbeat() {
  return get('https://api.stockfighter.io/ob/api/venues/TESTEX/heartbeat');
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

get(api.getOrderbook('TESTEX', 'FOOBAR')).then(function (res) {
  console.log(res);
});
