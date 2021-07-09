import tablero  

t = tablero.Tablero()

t.colocarMosca()
print(t)  #Comentar y descomentar esta línea para comprobar el funcionamiento.

cazada = False
intentos = 0

while(not cazada and intentos < 5):
    posicion = input("Posición en la que crees que está la mosca? ")
    intentos += 1
    qhp = t.manotazo(int(posicion))
    if (qhp==0):
        cazada = True
    if (qhp==1):
        print("Casi. La has asustado y ha revoloteado")
        t.revolotear()
        print(t)
    if (qhp==2):
        print("Ni te has acercado")

if (cazada):
    print(f"Enhorabuena, has cazado la mosca en {intentos} intentos")
else:
    print("Has perdido. Has agotado los intentos")
    print(t) #Llama al método __str__ (toString de Java)