# -*- coding: utf-8 -*- 
from __future__ import (absolute_import, division, print_function, unicode_literals)
from bothub_client.bot import BaseBot
from bothub_client.messages import Message
from .kospi200 import tradePrice
from .sumofOption import sum_of_option

class Bot(BaseBot):
	def handle_message(self, event, context):
		message = event.get('content')
		menu = self.get_project_data().get('keyboard').split(',')

		if message == '/start':
			msg = Message(event).set_text('키보드를 설정합니다.')
			for item in menu:
				msg.add_keyboard_button(item)
			self.send_message(msg)
		elif message == '/price':
			data = 'Kospi200 : {}'.format(tradeprice())
			msg = Message(event).set_text(data)
			self.send_message(msg)
		elif message == '/sum':
			data = sum_of_option()
			msg = Message(event).set_text(data)
			self.send_message(msg)


		elif message in menu:
			self.auto_response(event, message)
		elif message == '/max':
			data = self.get_project_data()
			data['aaa'] = '111'
			self.set_project_data(data)
			self.send_message('set data in project')
		elif message == '/ask':
			message = Message(event).set_text('현재 계신 위치를 알려주세요').add_location_request('위치 전송하기')
			self.send_message(message)
		elif message == '/postback':
			message = Message(event).set_text('가장 가까운 상영관들입니다.\n')
			data = '/schedule {} {}'.format('1234', 'cinema')
			message.add_postback_button('cinema', data)
			self.send_message(message)
		elif message.startswith('/schedule'):
			_, theater_id, theater_name = message.split(maxsplit=2)
			message = Message(event).set_text(theater_name)
			self.send_message(message)
		else:
			self.send_message('아직 준비중입니다.')
	def auto_response(self, event, message):
		answer = self.get_project_data().get(message)
		msg = Message(event).set_text(answer.get('answer'))
		if answer.get('link'):
			msg.add_url_button(answer.get('title'), answer.get('link'))
		self.send_message(msg)
