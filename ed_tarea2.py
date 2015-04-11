regex = "a*bc*"
cant_palabras = 9
palabras = []

def fil_matrix(s_repetidos):
	s_contador = 0
	l_contador = 0
	while s_contador < len(regex):
		if regex[s_contador] != '*':
			s_repetidos.append([])
			s_repetidos[l_contador].append(regex[s_contador])
			if s_contador != (len(regex)-1):
				if regex[s_contador+1] == '*':
					s_repetidos[l_contador].append(True)
				else:
					s_repetidos[l_contador].append(False)	
			else:
				s_repetidos[l_contador].append(False)
			s_repetidos[l_contador].append(0)
			s_repetidos[l_contador].append(False)
			l_contador += 1
		s_contador += 1
	return l_contador

def get_pos_true(s_repetidos ,l_contador):
	pos_true = []
	for s in range(l_contador):
		if s_repetidos[s][1]:
			pos_true.append(s)
	return pos_true

def change_state(s_repetidos,l_contador, pos_true):
	pos = -1
	for s in range(l_contador):
		if s_repetidos[s][3]:
			pos = s
	if pos == -1:
		s_repetidos[pos_true[0]][3] = True
		s_repetidos[pos_true[0]][2] += 1
	else:
		if pos == (l_contador-1):
			s_repetidos[pos][3] = False
			s_repetidos[pos_true[0]][3] = True
			s_repetidos[pos_true[0]][2] += 1

		else:
			if s_repetidos[pos][1]:
				pos_index = pos_true.index(pos)
				s_repetidos[pos][3] = False
				if pos_index == (len(pos_true)-1):
					s_repetidos[pos_true[0]][3] = True
					s_repetidos[pos_true[0]][2] += 1
				else:
					s_repetidos[pos_true[pos_index+1]][3] = True
					s_repetidos[pos_true[pos_index+1]][2] += 1
	return s_repetidos

def get_words():
	s_repetidos = []
	if "*" in regex:
		l_contador = fil_matrix(s_repetidos)
		pos_true = get_pos_true(s_repetidos ,l_contador)
		for p in range(cant_palabras):
			palabra = ""
			a = s_repetidos
			print a
			if p > 0:
				change_state(a,l_contador, pos_true)
			""" make_word """
			for i in range(l_contador):
				if s_repetidos[i][1]:
					palabra = palabra + (s_repetidos[i][0] * s_repetidos[i][2])
				else:
					palabra = palabra + s_repetidos[i][0]
			if not palabra in palabras:
				palabras.append(palabra)
	else:
		palabras.append(regex)
	print s_repetidos

get_words()

print "\n"
print palabras
	