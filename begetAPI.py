import requests
import urllib
import json


class BegetAPIMethod(object):
	"""docstring for BegetAPIMethod"""
	def __getattr__(self, method):

		print method


class BegetAPI:

	def __init__(self, login, password):
		self.login = login
		self.password = password


	def begetRequest(self, method, **args):
#		request = 'https://api.beget.com/api/{}/{}?login={}&passwd={}&output_format=json&input_format=json&input_data={}'.format(method.split('_')[0], method.split('_')[1], self.login, self.password, urllib.quote(json.dumps(args)))
		#request = 'https://api.beget.com/api/{}?login={}&passwd={}&output_format=json&input_format=json&input_data={}'.format(method, self.login, self.password, json.dumps(args))

		#response = json.loads(requests.get(request).content)
		#if response['status'] == 'error':
		#	raise Exception('{} : {}'.format(response['error_code'], response['error_text']))
		#else:
		#	print response['answer']
		print request	

	def __getattr__(self, partition):
		print attribute

		self.partition = BegetAPIMethod()
		return self.attribute
		#print **args
		#return lambda **args: self.begetRequest(method, **args)
