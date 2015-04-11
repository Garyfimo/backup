from num2word_ES import to_card

frase = raw_input("ingresa frase: ")
array = str(frase).split()

if array[1].lower() == 'mas':
    resultado = int(array[0]) + int(array[2])
elif array[1].lower() == 'menos':
	    resultado = int(array[0]) - int(array[2])
elif array[1].lower() == 'por':
        resultado = int(array[0]) * int(array[2])
elif array[1].lower() == 'entre':
        resultado = int(array[0]) / int(array[2])
else:
        resultado = "Comando %s no encontrado." % (array[1])

print to_card(resultado)
print to_card(4)