from urllib2 import urlopen

def get_number(numero):
	request = urlopen("http://nao-services.herokuapp.com/nums_to_words?number=%s" % (numero)).read()
	return request
    
print "El resultado es %s" % (get_number("56"))