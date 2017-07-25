import requests
import json


def begetRequest(section, method, login, password):
	return 'https://api.beget.com/api/' + section + '/' + method + '?login=' + login + '&passwd=' + password + '&output_format=json'

class BegetAPI:

	def __init__(self, login, password):
		request = begetRequest('user', 'getAccountInfo', login, password)
		print request
		response = requests.get(request)
		#print response.content
		user = json.loads(response.content)	
		if user['status'] == 'error':
			raise Exception(user['error_text'])
		else:
			self.login = login
			self.password = password


	def getAccountInfo(self):
		response = requests.get(begetRequest('user', 'getAccountInfo', self.login, self.password))
		return json.loads(response.content)


	def toggleSsh(self, status, **kwargs):
		request = requests.get(begetRequest('user', 'getAccountInfo', self.login, self.password) + '&status=' + status)
		if 'ftplogin' in kwargs.keys():
			response = requests.get(request + '&ftplogin=' + kwargs['ftplogin'])
		else:
			response = requests.get(request)

		return json.loads(response.content)



