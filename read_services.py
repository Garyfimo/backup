from urllib2 import urlopen
import json
import unicodedata

request = urlopen("https://nao-services-python.herokuapp.com/news/futbol")
results = request.read()

def elimina_tildes(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
 
def elimina_comillas(s):
	return s.replace('"','')

results = json.loads(results)
for title in results:
	print elimina_comillas(elimina_tildes(title))