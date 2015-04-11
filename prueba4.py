from threading import Thread, Lock
import time

def MainJob():
  for i in range(1,5):
    print "Looking for a new job\n"
    time.sleep(4)

def tarea1():
  print "Tarea1 - Saludar a LucumaLabs"
  time.sleep(2)
  print "Hola %s \n" % ("LucumaLabs")
  time.sleep(4)

def tarea2():
  print "Tarea2 - Subir una imagen"
  time.sleep(2)
  for i in range(5,100,5):
    if i % 20 == 0:
      print "Estoy al %s porciento de subir una imagen \n" % (i)
      time.sleep(1.5)
  print "Imagen subida\n"
  
def tarea3():
  print "Tarea3 - Enviar un mail"
  time.sleep(2)
  for i in range(100,0,-10):
    if i % 10 == 0:
      print "Falta %s porciento para enviar el mail \n" % (i)
      time.sleep(1.5)
  print "Mail enviado\n"

class lista_tareas():
  def __init__(self):
    self.tareas = []
    self.len = 0
  
  def agregar_tarea(self, tarea):
    self.tareas.append(tarea)
    self.len = self.len + 1


  def realizar_tarea(self):
    self.len = self.len - 1
    return self.tareas.pop(0)

    
  def is_empty(self):
    return self.tareas == []
    
tareas = lista_tareas()

tareas.agregar_tarea(tarea1)
tareas.agregar_tarea(tarea2)
tareas.agregar_tarea(tarea3)

Thread(target=MainJob).start()

print "Debo realizar %s tareas" % tareas.len

while tareas.len != 0:
  (tareas.realizar_tarea())()

print "Quedan %s tareas por realizar" % tareas.len




