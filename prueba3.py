from threading import Thread
import multiprocessing
import time

data = [    ['Job1', '4'], ['Job2', '4'], ['Job3', '6'],
    ['Job4', '8'],  ['Job5', '1'], ['Job6', '3'], ['Job7', '5'], ['Job8', '7'] ]


class lista_tareas():
  def __init__(self):
    self.tareas = []
    self.len = 0
  
  def agregar_tarea(self, tarea):
    self.tareas.append(tarea)
    self.len = self.len + 1


  def realizar_tarea(self):
    self.len = self.len - 1
    return self.tareas.pop(0)()

  def is_empty(self):
    return self.tareas == []


def MainJob():
  for i in range(1,10):
    print "\t\tHaciendo otras actividades"
    time.sleep(1.5)
  

def Job1():
  print "Inicio Tarea1 - Saludo"
  time.sleep(0.5)
  print "Hola %s" % ("Lucuma")
  time.sleep(3)
  

def Job2():
  print "Inicio Tarea2 - Subir imagen"
  time.sleep(0.5)
  for i in range(5,100,5):
    if i % 20 == 0:
      print "Estoy al %s porciento de subir una imagen" % (i)
      time.sleep(1.5)
  print "Imagen subida"
  
  
def Job3():
  print "Inicio Tarea3 - Enviar mail"
  time.sleep(0.5)
  for i in range(100,0,-10):
    if i % 10 == 0:
      print "Falta %s porciento para enviar el mail" % (i)
      time.sleep(1.5)
  print "Mail enviado"
  
  
def mp_worker(tareas):
  while tareas.len > 0:
    tareas.realizar_tarea()

def mp_handler(tareas):
    Thread(target=MainJob).start()
    Thread(target=mp_worker,args=(tareas,)).start()

if __name__ == '__main__':
    lista_tareas = lista_tareas()
    lista_tareas.agregar_tarea(Job1)
    lista_tareas.agregar_tarea(Job2)
    lista_tareas.agregar_tarea(Job3)
    lista_tareas.agregar_tarea(Job1)
    lista_tareas.agregar_tarea(Job2)
    mp_handler(lista_tareas)
    