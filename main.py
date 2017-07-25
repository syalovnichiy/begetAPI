import requests
import json

class User:

	def __init__(self, login, password):
		request = 'https://api.beget.com/api/user/getAccountInfo?login=' + login + '&passwd=' + password
		response = requests.get(request)
		user = json.loads(response.content)	
		if user['status'] == 'error':
			raise Exception(user['error_text'])
		else:
			self.login = login
			self.password = password


			

