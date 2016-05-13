Test api with httpie: http POST https://api.stockfighter.io/ob/api/venues/TESTEX/stocks/FOOBAR/orders 'X-Starfighter-Authorization:40f908637aba1d813c19119ff50aa1b20e0e925a' < sample/order.json

TODO:
funtions that need to be built
- get market position (in stocks)
- track cash position
- get total number of open bids
- get total number of open asks
- git a range of good prices to act on

features
- log algorithm actions to a file for later analysis
- create more comprehensive test orders
