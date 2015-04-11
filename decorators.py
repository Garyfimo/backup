def avisar(f):
	def inner(*args, **kwargs):
		f(*args, **kwargs)
		print "Se ha ejecutado %s" % f.__name__
	return inner

def autenticado(f):
	def inner(*args, **kwargs):
		if AUTHENTICATED:
			f(*args, **kwargs)
		else:
			raise Exception
	return inner


@autenticado 
@avisar
def abrir_puerta():
	print "abrir_puerta"

@autenticado
@avisar
def cerrar_puerta():
	print "cerrar_puerta"


#abrir_puerta()
#cerrar_puerta()

#abrir_puerta = avisar(abrir_puerta)
cerrar_puerta()