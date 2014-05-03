from ExchangeLib import *

API_key='4@8CV21YK2TDQ6NS7XSH9U3O0M9KZPAV'

market=Market(API_key,2,3)

max_inventory=50
elem_pos=5
okToBuy=True
okToSell=True

while True:
	market.updateAll()
	if market.bestBidPrice()>market.myBestBidPrice() and market.spreadWithMe()>0.5 and okToBuy:
		result=market.buy(elem_pos,market.bestBidPrice()+0.5)
		if result['response']=='request succeeded':
			print "buy order sent"
		time.sleep(market.lag)
	market.updateAll()
	if market.bestAskPrice()<market.myBestAskPrice() and market.spreadWithMe()>0.5 and okToSell:
		result=market.sell(elem_pos,market.bestAskPrice()-0.5)
		if result['response']=='request succeeded':
			print "sell order sent"
		time.sleep(market.lag)
	market.updateAll()


	if market.inventory()>max_inventory:
		okToBuy=False
	else:
		okToBuy=True

	if market.inventory()<-max_inventory:
		okToSell=False
	else:
		okToSell=True

	market.cancelAllNotAtBest()
	market.cancelAllTooGood()

