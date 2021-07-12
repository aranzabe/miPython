import threading

class MiHilo(threading.Thread):
    def run(self):
        contador = 1
        while contador <= 10:
            print('ejecutando', 
                  threading.current_thread().getName(), 
                  contador)
            contador+=1

for numero in range(10):
    hilo = MiHilo()
    hilo.start()