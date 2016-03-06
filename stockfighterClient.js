var https = require('https');

const apikey = '40f908637aba1d813c19119ff50aa1b20e0e925a';

module.exports = {
  placeOrder: placeOrder,
  listStocksByVenue: listStocksByVenue,
  getQuote: getQuote,
  getOrderbook: getOrderbook,
  placeOrder: placeOrder
};

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

function listStocksByVenue(venue) {
  return get(`https://api.stockfighter.io/ob/api/venues/${venue}/stocks`);
}

function getQuote(venue, stock) {
  return get(`http https://api.stockfighter.io/ob/api/venues/${venue}/stocks/${stock}/quote`);
}

function getOrderbook(venue, stock) {
  return get(`https://api.stockfighter.io/ob/api/venues/${venue}/stocks/${stock}`);
}

function hearbeat() {
  return get('https://api.stockfighter.io/ob/api/venues/TESTEX/heartbeat');
}

function placeOrder(order) {
  return new Promise(function (resolve, reject) {

    var options = {
      hostname: 'api.stockfighter.io',
      path: `/ob/api/venues/${order.venue}/stocks/${order.stock}/orders`,
      method: 'POST',
      agent: false,
      headers: {
        'Content-Type': 'application/json',
        'X-Starfighter-Authorization': apikey
      }
    };

    var req = https.request(options, (res) => {
      console.log(`STATUS: ${res.statusCode}`);
      res.setEncoding('utf8');
      var body = "";
      res.on('data', (chunk) => {
        body += chunk;
      });

      res.on('end', () => {
        resolve(body);
      });
    });

    req.on('error', (e) => {
      reject(e);
    });

    // write data to request body
    req.write(JSON.stringify(order));
    req.end();
  });
}
