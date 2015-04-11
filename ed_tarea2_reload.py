def make_word(matrix, l_contador,p):
    pos_true = get_pos_true(matrix, l_contador)
    sumar = 0
    for q in pos_true:
        sumar += 1
    palabra = ""
    for i in range(l_contador):
        if matrix[i][1]:
            if matrix[i][3]:
                por = (int(matrix[i][2]) + 1)
                palabra = palabra + (matrix[i][0] * por)
            else:
                palabra = palabra + matrix[i][0] * (matrix[i][2])
        else:
            palabra = palabra + matrix[i][0]
    return palabra

def change_state(matrix,l_contador, pos_true):
    pos = -1
    sumar = 0
    for q in pos_true:
        sumar += 1
    for s in range(l_contador):
        if matrix[s][3]:
            pos = s
    if pos == -1:
        matrix[pos_true[0]][3] = True
        #matrix[pos_true[0]][2] += 1
    else:
        if pos == (l_contador-1):
            matrix[pos][3] = False
            matrix[pos_true[0]][3] = True
         #   matrix[pos_true[0]][2] += 1

        else:
            if matrix[pos][1]:
                pos_index = pos_true.index(pos)
                matrix[pos][3] = False
                if pos_index == (len(pos_true)-1):
                    matrix[pos_true[0]][3] = True
          #          matrix[pos_true[0]][2] += 1
                    for l in range(sumar):
                        matrix[pos_true[l]][2] += 1
                    
                else:
                    matrix[pos_true[pos_index+1]][3] = True
           #         matrix[pos_true[pos_index+1]][2] += 1
    return matrix

def fil_matrix(regex):
    matrix = []
    s_contador = 0
    l_contador = 0
    while s_contador < len(regex):
        if regex[s_contador] != '*':
            matrix.append([])
            matrix[l_contador].append(regex[s_contador])
            if s_contador != (len(regex)-1):
                if regex[s_contador+1] == '*':
                    matrix[l_contador].append(True)
                else:
                    matrix[l_contador].append(False)
            else:
                matrix[l_contador].append(False)
            matrix[l_contador].append(0)
            matrix[l_contador].append(False)
            l_contador += 1
        s_contador += 1
    return matrix

def get_pos_true(matrix ,l_contador):
    pos_true = []
    for s in range(l_contador):
        if matrix[s][1]:
            pos_true.append(s)
    return pos_true

def get_num_symbols(regex):
    contador = 0
    for s in regex:
        if not s == '*':
            contador += 1
    return contador

def get_words():
    regex = "a*bc*"
    cant_palabras = 10
    matrix = fil_matrix(regex)
    palabras = []
    if "*" in regex:
        l_contador = get_num_symbols(regex)
        pos_true = get_pos_true(matrix ,l_contador)
        for p in range(cant_palabras):
            palabra = ""
            a = matrix
            #print a
            if p > 0:
                change_state(matrix,l_contador, pos_true)
            palabra = make_word(matrix, l_contador, p)
            if not palabra in palabras:
                palabras.append(palabra)
    else:
        palabras.append(regex)
    print matrix, palabras

get_words()