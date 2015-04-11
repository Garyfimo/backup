import time

def MainJob():
  for i in range(1,5):
    print "Looking for a new job"
    time.sleep(2.5)
  

def Job1(nombre):
  print "Hola %s" % (nombre)
  time.sleep(4)

def Job2():
  for i in range(5,100,5):
    if i % 20 == 0:
      print "Estoy al %s porciento de subir una imagen" % (i)
      time.sleep(1.5)
  print "Imagen subida"
  
def Job3():
  for i in range(100,0,-10):
    if i % 10 == 0:
      print "Falta %s porciento para enviar el mail" % (i)
      time.sleep(1.5)
  print "Mail enviado"




lista_tareas = [MainJob,Job1,Job2,Job3]



print lista_tareas

lista_tareas[0]()