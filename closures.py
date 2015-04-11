def avisar(f):
	def inner(*args, **kwargs):
		f(*args, **kwargs)
		print "Se ha ejecutado %s" % f.__name__
	return inner

def abrir_puerta():
	print "abrir_puerta"

def cerrar_puerta():
	print "cerrar_puerta"

avisar(abrir_puerta)