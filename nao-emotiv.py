from urllib2 import urlopen
import json

def get_instruction():
        url = "https://nao-epoc.herokuapp.com/instructions/last"
        results = json.loads(urlopen(url).read())
        if not results["done"]:
            return results["action"]
        else:
            return "no tengo nada que decir"

print get_instruction()