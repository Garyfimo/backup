from urllib2 import urlopen
import json
import unicodedata

def get_json():
	request = urlopen("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22lima%2C%20pe%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
	results = request.read().decode("utf-8")
   	results = results.encode("utf-8")
   	results = json.loads(results)

   	return results

def get_num_to_word(num):
    word = urlopen("http://nao-services.herokuapp.com/nums_to_words?number=%s" % (num)).read()
    return word

def get_hour(hour):
	hour_list = hour.split(" ")
	hour_dic = hour_list[0].split(":")
	if "am" in hour:
		return ("%s y %s de la manana" % (get_num_to_word(hour_dic[0]), get_num_to_word(hour_dic[1]) )).encode("ascii", "ignore")
	if "pm" in hour:
		return ("%s y %s de la noche" % (get_num_to_word(hour_dic[0]), get_num_to_word(hour_dic[1]) )).encode("ascii", "ignore")


def get_astronomy():
	results = get_json()
	hour_sunset  = results['query']['results']['channel']['astronomy']['sunset']
	hour_sunrise  = results['query']['results']['channel']['astronomy']['sunrise']
	return "El sol saldra a las %s y se ocultara a las %s" % (get_hour(hour_sunrise),get_hour(hour_sunset))

get_astronomy()
