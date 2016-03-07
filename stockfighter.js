var client = require('./stockfighterClient');
var _ = require('lodash');

function timeout(duration) {
  return new Promise((resolve, reject) => {
    setTimeout(resolve, duration);
  });
}

var test = {
  accounts: 'EXB123456',
  venue: 'TESTEX',
  stock: 'FOOBAR'
};

var live = {
  account: 'WAM74680374',
  venue: 'QYYJEX',
  stock: 'PTIM'
};

var filled = 0;
var openOrders = [];
var done = false;

function doSomeWork() {
  return new Promise(function (resolve, reject) {
    console.log('hello');
    i--;
    resolve();
  });
}

function pWhile(condition, promiseWork) {
  return new Promise(function (resolve, reject) {
    if (!condition()) {
      resolve();
    } else {
      promiseWork().then(function () {
        resolve(pWhile(condition, promiseWork));
      });
    }
  });
}

var i = 10;
var isNotZero = function () {
  return i >= 0;
}
pWhile(isNotZero, doSomeWork);

// while (! done) {
//   client.getQuote(live.venue, live.stock).then(function (quote) {
//     return {
//       'account': live.account,
//       'venue': live.venue,
//       'stock': live.stock,
//       'qty': 1,
//       'price': quote.bid,
//       'direction': 'buy',
//       'orderType': 'limit'
//     };
//   }).then(function (order) {
//     return client.placeOrder(order);
//   }).then(function (confirmation) {
//       return openOrders.push(confirmation);
//   }).then(function () {
//     return openOrders = _.map(openOrders, function (order) {
//       if (order && order.open === false) {
//         filled += order.totalFilled;
//       } else if(order && order.open === true) {
//         return order;
//       }
//     });
//   }).then(function () {
//     console.log(`filled ${filled} orders`);
//     timeout(1000);
//     if (filled >= 100000) {
//       done = true;
//     }
//   }).catch(err => {
//     throw new Error(`Something went pear-shaped: ${err}`);
//   });
// }
