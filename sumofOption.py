import time
import requests

def sum_of_option():
	base_url = 'http://esignal.co.kr/get/get_jupo.php'
	query_string = {'_': str(int(time.time()))+'000'}
	fin = requests.get(base_url, params=query_string)
	now_list = fin.json()[-1]
	sum_value = now_list[1]
	data = 'Sum of Option: {}'.format(sum_value)
	return data
