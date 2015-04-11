matriz = []
automatas = []


def read_file():
	file_datos = open('matriz.txt','r')
	l = file_datos.readline().rstrip('\n').split(" ")
	nro_estados = l[0]
	alfabeto = l[1]
	for i in range(int(nro_estados)):
		matriz.append(file_datos.readline().rstrip('\n').split(" "))
	e_inicial =  file_datos.readline().rstrip('\n')
	if len(e_inicial) > 1 or len(e_inicial) == 0:
		print "Error con el estado inicial, debe ser uno"
	e_final = file_datos.readline().rstrip('\n')
	for j in range(int(file_datos.readline().rstrip('\n'))):
		automatas.append(file_datos.readline().rstrip('\n'))
	file_datos.close()
	run_automata(automatas,e_inicial,e_final,alfabeto)

def run_automata(automatas,e_inicial,e_final,alfabeto):
	for a in automatas:
		for e in a:
			if str(e_inicial) != "-1":
				e_inicial = matriz[int(e_inicial)][int(alfabeto.index(e))]
		if e_inicial in e_final:
			print "Automata %s es correcto" % a
		else:
			print "Automata %s es rechazado" % a

read_file()

