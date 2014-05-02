Syntax : see API example.

values = {
  'key' : '2\AIO4AM3WSAASZWTTUTJEPLJZAADVN1', // The API key that you have generated on the website (go to your dashboard and click on 'generate')
  'function' : 'get_trades',                  // Name of the function that you wish to call
  'id_market' : 2,							  // Input arguments if needed
}

1. 'get_active_markets'

	args : None

	returns : 
	- list of events sorted by creation date with 
		- 'id_event' : ID of the event,
		- 'event' : title of the event,
		- 'end' : date when trading closes (Unix timestamp),
		- 'markets' : array of markets containing for each market in the event :
			- 'id_market' : ID of the market
			- 'outcome' : title of the market
	- 'response' : success/error message
	
2. 'get_my_trades' / 'get_trades' (one's trades / all trades)

	args : 
	- 'id_market' : ID of the market on which you want to get your trades 
	
	returns : 
	- a list of trades ordered by timestamp with
		- 'id' : ID of trade 
		- 'side' : side of the trade  (1 : buy, -1 : sell)
		- 'price' : price at which the trade occurred 
		- 'volume' : volume of the trade in number of contracts (1 contract = 1 mBTC) 
		- 'timestamp' : timestamp at which the trade occurred  (Unix timestamp)
		- 'PNL' : PNL of the trade  (0 if the market is not settled)
	- 'response' : success/error message

3. 	'get_my_limits' / 'get_limits' (one's limit orders / all limit orders)

	args : 
	- 'id_market' : ID of the market on which you want to get your placed orders 
	
	returns : 
	- a list of orders ordered by timestamp with
		- 'id' : ID of order 
		- 'side' : side of the limit (1 : buy, -1 : sell)
		- 'price' : price at which the order is placed 
		- 'volume' : volume of the order in number of contracts (1 contract = 1 mBTC) 
		- 'timestamp' : timestamp at which the order was placed (Unix timestamp)
	- 'response' : success/error message

4. 'get_balance'

	args : None
	
	returns : 
	- 'available' : available balance in mBTC
	- 'response' : success/error message

5. 'send_order'

	args : 
	- 'id_market' : ID of the market on which you want to send your order
	- 'side' : side of your order (1 : buy, -1 : sell)
	- 'price' : price at which you want to place you order (multiple of 0.5, in (0, 100) )
	- 'volume' : number of contracts (1 contract = 1 mBTC)
	
	returns :
	- 'response' : success/error message
	
6. 'cancel_order'

	args : 
	- 'id_market' : ID of the market on which you want to send your order
	- 'id_order' : ID of the order you want to cancel
	
	returns :
	- 'response' : success/error message
	