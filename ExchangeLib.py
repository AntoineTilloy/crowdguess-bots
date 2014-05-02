import httplib, urllib
import json


def SendRequest(function,id_market,id_order,side,volume,price):

	values = {
  		'key' : '2\AIO4AM3WSAASZWTTUTJEPLJZAADVN1',
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

	conn = httplib.HTTPConnection(host)
	conn.request("POST", url, values, headers)
	response = conn.getresponse()

	data = response.read()
	data= json.loads(data)
	return data


