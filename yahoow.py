from urllib2 import urlopen
import json

request = urlopen("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22lima%2C%20pe%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
results = request.read().decode("utf-8")
results = results.encode("utf-8")

results = json.loads(results)

def get_fahrenheit_celsius(fahrenheit):
	return ((int(fahrenheit) - 32)*5)/9

weather = get_fahrenheit_celsius(results['query']['results']['channel']['item']['forecast'][0]['low'])



print weather