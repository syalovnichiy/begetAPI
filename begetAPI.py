import requests
import urllib
import json



class BegetAPIMethod(object):
	"""docstring for BegetAPIMethod"""
	def __init__(self, api, partition):
		self.partition = partition
		self.api_instans = api

	def begetRequest(self, method, **args):
		#request = 'https://api.beget.com/api/{}/{}?login={}&passwd={}&output_format=json&input_format=json&input_data={}'.format(method.split('_')[0], method.split('_')[1], self.login, self.password, urllib.quote(json.dumps(args)))
		request = (
			'https://api.beget.com/api'
			'/{}/{}?login={}&passwd={}&'
			'output_format=json&'
			'input_format=json&input_data={}'
		).format(
			self.partition,
			method,
			self.api_instans.login,
			self.api_instans.password, 
			json.dumps(args)
		)

		#response = json.loads(requests.get(request).content)
		#if response['status'] == 'error':
		#	raise Exception('{} : {}'.format(response['error_code'], response['error_text']))
		#else:
		#	print response['answer']
		return request


	def __getattr__(self, method):
		return lambda **args: self.begetRequest(method, **args)

class BegetAPI:

	def __init__(self, login, password):
		self.login = login
		self.password = password	


	def __getattr__(self, atribute):
		return BegetAPIMethod(self, atribute)

a = BegetAPI('test','test')
a.razdel.method(a=1, b=2)