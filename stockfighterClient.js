var https = require('https');

const apikey = '40f908637aba1d813c19119ff50aa1b20e0e925a';
const baseurl = 'api.stockfighter.io';

module.exports = {
  placeOrder: placeOrder,
  listStocksByVenue: listStocksByVenue,
  getQuote: getQuote,
  getOrderbook: getOrderbook,
  placeOrder: placeOrder,
  orderStatus: orderStatus
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
  return get(`${baseurl}/ob/api/venues/${venue}/stocks`);
}

function getQuote(venue, stock) {
  return get(`${baseurl}/ob/api/venues/${venue}/stocks/${stock}/quote`);
}

function getOrderbook(venue, stock) {
  return get(`${baseurl}/ob/api/venues/${venue}/stocks/${stock}`);
}

function hearbeat() {
  return get('${baseurl}/ob/api/venues/TESTEX/heartbeat');
}

function orderStatus(id, venue, stock) {
  return get(`${baseurl}/ob/api/venues/${venue}/stocks/${stock}/orders/${id}`);
}

function placeOrder(order) {
  return new Promise(function (resolve, reject) {

    var options = {
      hostname: baseurl,
      path: `/ob/api/venues/${order.venue}/stocks/${order.stock}/orders`,
      method: 'POST',
      agent: false,
      headers: {
        'Content-Type': 'application/json',
        'X-Starfighter-Authorization': apikey
      }
    };

    var req = https.request(options, (res) => {
      // console.log(`STATUS: ${res.statusCode}`);
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
