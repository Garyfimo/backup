import requests

def get_answer(id):
	url_response = "http://nao-assistant.herokuapp.com/call_requests/%s/check_response" % (id)
	r = requests.get(url_response)
	#print r.json()
	res = r.json()
	print res['status'], res['response']

get_answer(5)