import requests
from time import sleep


url_post = "http://nao-assistant.herokuapp.com/call_requests"

def get_request_id(to, visitor):
	params = {'to':to, 'from':visitor}
	r = requests.post(url_post, params=params)
	print r.json()
	return r.json()

def get_answer(id):
	url_response = "http://nao-assistant.herokuapp.com/call_requests/%s/check_response" % (id)
	r = requests.get(url_response)
	print r.json()
	return r.json()
	#print res['status'], res['response']


texto = ""
id = get_request_id("Gary Figuerola","Leslie Almendra")
for n in range(0,5):
	res = get_answer(id)
	if res['status']:
		texto = res['response']
		break
	else:
		sleep(5)
		texto = "NADA"

print texto
