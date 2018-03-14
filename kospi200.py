import json
from urllib.request import urlopen

def tradeprice():
	base_url = 'http://stock.kakao.com/api/securities/KOREA-D2011029.json'
	fin = urlopen(base_url).read().decode('utf-8')
	j_data = json.loads(fin)
	tradePrice = j_data.get('recentSecurity').get('tradePrice')
	signedChangePrice = j_data.get('recentSecurity').get('signedChangePrice')
	data = '{} {}'.format(tradePrice,signedChangePrice)
	return data
