import metodos  

#Opción A)
#t = []
#metodos.iniciar(t)
#metodos.iniciar(t,4)

#Opción B)
#t = metodos.iniciar2()
t = metodos.iniciar2(5)

metodos.colocarMosca(t)
print(t)  #Comentar y descomentar esta línea para comprobar el funcionamiento.
# print(type(t))

cazada = False
intentos = 0

while(not cazada and intentos < 5):
    posicion = input("Posición en la que crees que está la mosca? ")
    intentos += 1
    qhp = metodos.manotazo(t, int(posicion))
    if (qhp==0):
        cazada = True
    if (qhp==1):
        print("Casi. La has asustado y ha revoloteado")
        metodos.revolotear(t)
        print(t)
    if (qhp==2):
        print("Ni te has acercado")

if (cazada):
    print(f"Enhorabuena, has cazado la mosca en {intentos} intentos")
else:
    print("Has perdido. Has agotado los intentos")
    print(t)