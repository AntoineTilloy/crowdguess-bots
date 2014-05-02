import httplib, urllib
import json

host = 'crowdguess2.herokuapp.com'
url = '/API/'

values = {
  'key' : '2\AIO4AM3WSAASZWTTUTJEPLJZAADVN1',
  'function' : 'get_active_markets',
  'id_market' : 2,
  'id_order': 74,
  'side' : -1,
  'volume' : 1.3,
  'price' : 24.5,
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

print 'Response: ', response.status, response.reason
print 'Data:'

print data