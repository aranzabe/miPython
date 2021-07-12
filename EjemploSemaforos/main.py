from threading import Thread,Semaphore
 
semaforo = Semaphore(1); #Crear variable semáforo
 
#Definicion de Funciones
def region_critica(id):
    global x;
    x=x+id;
    print("El hilo "+str(id)+" valor de x="+str(x))
    x=1;
    
#Definicion de Clase Hilo
class Hilo(Thread):
    def __init__(self,id): #Constructor de la clase
         Thread.__init__(self);
         self.id=id;
 
    def run(self): #Metodo que se ejecutara con la llamada start
          semaforo.acquire();
          region_critica(self.id);
          semaforo.release();
  
#Programa Principal
hilos = [Hilo(1),Hilo(2),Hilo(3)]; #Creacion de objetos Hilos
x=1;
for h in hilos: 
     h.start(); #Ejecutar todos los hilos