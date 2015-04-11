import requests


url_post = "http://nao-assistant.herokuapp.com/call_requests"

def get_request_id(to, visitor):
	params = {'to':to, 'from':visitor}
	r = requests.post(url_post, params=params)
	print r.json()
	return r.json()



get_request_id("Gary Figuerola","Leslie Almendra")


