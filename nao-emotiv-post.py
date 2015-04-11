import requests

def mark_as_done(id):
	url_get = "https://nao-epoc.herokuapp.com/instructions/%s/mark_as_done" % id
	r = requests.post(url_get)
	print r.json()
	return r.json()

def send_instruction(instruction):
	param = {"nao_action":instruction}
	url_post = "https://nao-epoc.herokuapp.com/instructions"
	r = requests.post(url_post, param)
	print r.json()
	return r.json()


mark_as_done(340)

send_instruction("saludar")


