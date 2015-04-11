from urllib2 import urlopen
import json

request = urlopen("https://nao-services-python.herokuapp.com/categorias")
results = request.read()


results = json.loads(results)
for title in results:
	print title