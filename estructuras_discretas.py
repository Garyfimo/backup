import re

regs = {
	"1" : "^(0?|-?[1-9]+)$",
	"2" : "^-?[0-9]+.[1-9]+$",
	"3" : "^[A-Z]+|[a-z]+|[A-Z]+$",
}

def show_header():
	print "------Estructuras Discretas------"
	print "------Elija una opcion------"

def show_menu():
	print "1.- Procesar numero entero:"
	print "2.- Procesar numero real: "
	print "2.- Procesar cadena de texto: "
	opcion = raw_input("Ingrese opcion: ")
	print "Correcto" if action_menu(opcion) else "Incorrecto"

def action_menu(opcion):
	dato = raw_input("Ingrese dato: ")
	matcher = re.compile(regs[opcion])
	return matcher.match(dato) is not None
		

show_header()
show_menu()