#! /urs/bin/env python
from flask import Flask
from urllib2 import urlopen
import json


app = Flask(__name__)


def get_json():
	request = urlopen("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22lima%2C%20pe%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
	results = request.read().decode("utf-8")
   	results = results.encode("utf-8")
   	results = json.loads(results)

   	return results


def get_hour(hour):
	hour_list = hour.split(" ")
	hour_dic = hour_list[0].split(":")
	if "am" in hour:
		return "%s y %s de la mañana" % (get_num_to_word(hour_dic[0]), get_num_to_word(hour_dic[1]) )
	if "pm" in hour:
		return "%s y %s de la noche" % (get_num_to_word(hour_dic[0]), get_num_to_word(hour_dic[1]) )




def get_astronomy():
	results = get_json()
	hour_sunset  = results['query']['results']['channel']['astronomy']['sunset']
    hour_sunrise  = results['query']['results']['channel']['astronomy']['sunrise']
    
    return "El sol saldrá a las %s y se ocultará a las %s" % (get_hour(hour_sunset),get_hour(hour_sunrise))
def get_weather():
	results = get_json()

    low_weather = get_fahrenheit_celsius(results['query']['results']['channel']['item']['forecast'][0]['low'])
    high_weather = get_fahrenheit_celsius(results['query']['results']['channel']['item']['forecast'][0]['high'])
    return ("El clima para el dia de hoy es %s grados centigrados como minimo y %s como maximo." % (get_num_to_word(low_weather),get_num_to_word(high_weather))

def get_fahrenheit_celsius(fahrenheit):
    return self.get_num_to_word(((int(fahrenheit) - 32)*5)/9)

def get_num_to_word(num):
    word = urlopen("http://nao-services.herokuapp.com/nums_to_words?number=%s" % (num)).read()
    return word

@app.route("/")
def hello():
	hola = get_astronomy()
	return hola

if __name__ == "__main__":
	app.run(host="192.168.0.102", port=5001)
