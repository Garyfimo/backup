matriz = []

def fil_matriz(nro_estados, alfabeto):
	estados = range(int(nro_estados)) 
	print "Estados disponibles"
	for a in range(int(nro_estados)):
		print "q%s" % a,
	for i in range(int(nro_estados)):
		matriz.append([])
		for j in range(len(alfabeto)+1):
			if j == 0:
				matriz[i].append("%s" % str(i))
			else:
				while True:
					orden = raw_input("\nCuando %s pasar de q%s a q" % (alfabeto[j-1],i))	
					if int(orden) in estados:
						break
					else:
						print "\nq%s no es un estado, ingrese otro" % orden
				matriz[i].append("%s" % orden)
			


def show_header():
	print "------Estructuras Discretas------"

def show_menu():
	estados_finales = []
	nro_estados = raw_input("1.- Ingrese numero de estados: ")
	alfabeto = raw_input("2.- Ingrese el alfabeto con un espacios\n (Ejem: ABCDE) ")
	fil_matriz(nro_estados, alfabeto)
	while True:
		estado_inicial = raw_input("3.- Ingrese un estado inicial q")
		if len(estado_inicial) == 1:
			break
		else:
			print "Solo puede haber un estado inicial"
	nro_estados_finales = raw_input("3.- Ingrese cuantos estados finales tendra: ")
	for p in range(int(nro_estados_finales)):
		estados_finales.append(raw_input("Estado final %s -> q" % str(p+1))) 
	automata = raw_input("4.- Ingrese automata: ")
	run_automata(estado_inicial,estados_finales,automata,alfabeto)

def run_automata(e_inicial,e_finales,automata, alfabeto):
	for a in automata:
		if str(e_inicial) != "-1":
			e_inicial = matriz[int(e_inicial)][alfabeto.index(a)+1]
	if e_inicial in e_finales:
		print "Correcto"
	else:
		print "Rechazado"
	

show_header()
show_menu()