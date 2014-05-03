import httplib, urllib
import json
import time

def SendRequest(API_key,function,id_market=1,id_order=1,side=1,volume=0,price=0):
  host = 'crowdguess2.herokuapp.com'
  url = '/API/'
  values = {
      'key' : API_key,
      'function' : function,
      'id_market' : id_market,
      'id_order': id_order,
      'side' : side,
      'volume' : volume,
      'price' : price,
  }
  headers = {
      'User-Agent': 'python',
      'Content-Type': 'application/x-www-form-urlencoded',
  }
  values = urllib.urlencode(values)
  conn = httplib.HTTPConnection(host)
  conn.request("POST", url, values, headers)
  response = conn.getresponse()
  data = response.read()
  data= json.loads(data)
  return data

def SendOrder(API_key,id_market,side,volume,price):
  return SendRequest(API_key,'send_order',id_market,'',side,volume,price)

def CancelOrder(API_key,id_market,id_order):
  return SendRequest(API_key,'cancel_order',id_market,id_order)

def GetBalance(API_key):
  return SendRequest(API_key,'get_balance')

def GetLimits(API_key,id_market):
  return SendRequest(API_key,'get_my_limits',id_market)

def GetOrderBook(API_key,id_market):
  return SendRequest(API_key,'get_limits',id_market)

def GetTrades(API_key,id_market):
  return SendRequest(API_key,'get_my_trades',id_market)


class Market:
  def __init__(self,API_key,market_id,lag):
    self.API_key=API_key
    self.id=market_id
    self.lag=lag
    self.updateAll()

  def inventory(self):
    inventory=0
    for trade in self.trades:
      inventory+=trade['side']*trade['volume']
    return inventory

  def updateNakedOB(self):
    nob=[]
    for order in self.ob:
      orderId=order['id_order']
      add=True
      for limit in self.limits:
        if limit['id_order']==orderId:
          add=False
          break
      if add:
        nob.append(order)
    self.nob=nob

  def updateOB(self):
    obRequest=GetOrderBook(self.API_key,self.id)
    if obRequest['response']=='request succeeded':
      self.ob=obRequest['limits']
    else:
      print "initialization failure, could not get order book"
    time.sleep(self.lag)
  def updateTrades(self):
    tradeRequest=GetTrades(self.API_key,self.id)
    if tradeRequest['response']=='request succeeded':
      self.trades=tradeRequest['trades']
    else:
      print "initialization failure, could not get trades"
    time.sleep(self.lag)
  def updateLimits(self):
    limitRequest=GetLimits(self.API_key,self.id)
    if limitRequest['response']=='request succeeded':
      self.limits=limitRequest['limits']
    else:
      print "initialization failure, could not get your limits"
    time.sleep(self.lag)
  def updateAll(self):
    self.updateOB()
    self.updateLimits()
    self.updateNakedOB()
    self.updateTrades()

  def bestBidPrice(self):
    bids=[]
    for order in self.nob:
      if order['side']==1:
        bids.append(order['price'])
    return max(bids)
  def bestAskPrice(self):
    asks=[]
    for order in self.nob:
      if order['side']==-1:
        asks.append(order['price'])
    return min(asks)
  def myBestBidPrice(self):
    bids=[]
    for order in self.limits:
      if order['side']==1:
        bids.append(order['price'])
    if bids!=[]:
      maxbids=max(bids)
    else:
      maxbids=0.0
    return maxbids
  def myBestAskPrice(self):
    asks=[]
    for order in self.limits:
      if order['side']==-1:
        asks.append(order['price'])
    if asks!=[]:
      minasks=min(asks)
    else:
      minasks=100.0
    return minasks
  def spread(self):
    return self.bestAskPrice()-self.bestBidPrice()
  def spreadWithMe(self):
    return min([self.bestAskPrice(),self.myBestAskPrice()])-max([self.myBestBidPrice(),self.bestBidPrice()])
  def buy(self,volume,price):
    return SendOrder(self.API_key,self.id,1,volume,price)  
  def sell(self,volume,price):
    return SendOrder(self.API_key,self.id,-1,volume,price)
  def cancelAllNotAtBest(self):
    for limit in self.limits:
      if limit['price']<self.bestBidPrice() and limit['side']==1:
        CancelOrder(self.API_key,self.id,limit['id_order'])
        time.sleep(self.lag)
      if limit['price']>self.bestAskPrice() and limit['side']==-1:
        CancelOrder(self.API_key,self.id,limit['id_order'])
        time.sleep(self.lag)
  def cancelAllTooGood(self):
    for limit in self.limits:
      if limit['price']>self.bestBidPrice()+0.5 and limit['side']==1:
        CancelOrder(self.API_key,self.id,limit['id_order'])
        time.sleep(self.lag)
      if limit['price']<self.bestAskPrice()-0.5 and limit['side']==-1:
        CancelOrder(self.API_key,self.id,limit['id_order'])
        time.sleep(self.lag)





