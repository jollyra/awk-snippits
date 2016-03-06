var client = require('./stockfighterClient');


var test = {
  accounts: 'EXB123456',
  venue: 'TESTEX',
  stock: 'FOOBAR'
};

var live = {
  account: 'HAP83466447',
  venue: 'BMHKEX',
  stock: 'EZQE'
};

var order = {
  'account': test.account,
  'venue': test.venue,
  'stock': test.stock,
  'qty': 1000,
  'price': 5000,
  'direction': 'buy',
  'orderType': 'limit'
}

var i = 0;
while (i < 1) {
  setTimeout(function() {
    client.placeOrder(order).then(function (res) {
      console.log(res);
    }).catch(err => {
      throw `Something went pear-shaped: ${err}`;
    });
  }, 500);
  i++;
}
