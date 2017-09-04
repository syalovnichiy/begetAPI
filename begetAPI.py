import requests
import urllib
import json



class BegetAPIRequest(object):
	
	"""
	accesssory class for BegetAPI
	this class use for catch the method of called partition
	and make request
	"""


	def __init__(self, api, partition):

		"""
		init by called in BegetAPI partition and user's instance
		"""

		self.partition = partition
		self.api_instans = api


	def begetRequest(self, method, **args):
		
		"""
		this method create url and make request
		return beget API errors or return boty of response
		"""

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
			urllib.quote(json.dumps(args))
		)

		response = json.loads(requests.post(request).content)
		if response['status'] == 'error':
			print response['error_code'], ':', response['error_text']cp
		elif response['answer']['status'] == 'error':
			answer = response['answer']['errors'][0]
			print answer['error_code'],' : ', answer['error_text']
		else:
			return response['answer']


	def __getattr__(self, method):
		return lambda **args: self.begetRequest(method, **args)



class BegetAPI:
	
	"""
	The main class 
	create beget's user instance
	use for call beget api methond for current user's account
	"""


	def __init__(self, login, password):

		"""
		init user by login and password
		"""

		self.login = login
		self.password = password	


	def __getattr__(self, atribute):

		"""
		catch called partition of begetAPI
		"""

		return BegetAPIRequest(self, atribute)