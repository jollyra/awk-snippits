var https = require('https');

function heartbeat() {
  https.get('https://api.stockfighter.io/ob/api/venues/TESTEX/heartbeat', function (res) {

    res.on('data', function (d) {
      process.stdout.write(d);
    });

  }).on('error', function (e) {
    console.error(e);
  });
}

function listStocksByEx(venue) {
  https.get(`https://api.stockfighter.io/ob/api/venues/${venue}/stocks`, function (res) {

    res.on('data', function (d) {
      process.stdout.write(d);
    });

  }).on('error', function (e) {
    console.error(e);
  });
}

function getOrderbook(venue, stock, callback) {
  https.get(`https://api.stockfighter.io/ob/api/venues/${venue}/stocks/${stock}`, function (res) {
    var body = "";

    res.on('data', function (d) {
      body += d;
    });

    res.on('end', function () {
      callback(null, body);
    });

  }).on('error', function (e) {
    callback(e, null);
  });
}

getOrderbook('TESTEX', 'FOOBAR', function (err, data) {
  if (err) {
    throw 'The world is burning!' + err;
  }
  var bids = data.bids;
  console.log(data);
});
