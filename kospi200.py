import json
from urllib.request import urlopen

def tradePrice():
	base_url = 'http://stock.kakao.com/api/securities/KOREA-D2011029.json'
	fin = urlopen(base_url).read().decode('utf-8')
	return json.loads(fin).get('recentSecurity').get('tradePrice')
