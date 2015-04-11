from urllib2 import urlopen

def get_num_to_word(num):
    word = urlopen("http://nao-services.herokuapp.com/nums_to_words?number=%s" % (num)).read()
    return word
    
def get_word_to_num(word):
    num = urlopen("http://nao-services.herokuapp.com/words_to_nums?words=%s" % (word)).read()
    return num

def get_resultado(speech):
    if "mas" in str(speech):
        split = speech.split(" mas ")
        a = split[0].replace(" ","+")
        b = split[1].replace(" ","+")
        num1 = get_word_to_num(str(a))
        num2 = get_word_to_num(str(b))
        suma = int(num1) + int(num2)
        return get_num_to_word(suma)
    elif "menos" in str(speech):
        split = speech.split(" menos ")
        a = split[0].replace(" ","+")
        b = split[1].replace(" ","+")
        num1 = get_word_to_num(str(a))
        num2 = get_word_to_num(str(b))
        resta = int(num1) - int(num2)
        return get_num_to_word(resta)
    elif "por" in str(speech):
        split = speech.split(" por ")
        a = split[0].replace(" ","+")
        b = split[1].replace(" ","+")
        num1 = get_word_to_num(str(a))
        num2 = get_word_to_num(str(b))
        multi = int(num1) * int(num2)
        return get_num_to_word(multi)
    elif "entre" in str(speech):
        split = speech.split(" entre ")
        a = split[0].replace(" ","+")
        b = split[1].replace(" ","+")
        num1 = get_word_to_num(str(a))
        num2 = get_word_to_num(str(b))
        divi = int(num1) / int(num2)
        return get_num_to_word(divi)

print get_resultado("cuarenta y tres mas cinco")
