from random import randrange, choice

print(randrange(10))
print(choice(["uno", "dos", "tres"]))

n = 7
if n==9:
    print('Vale 9')
else:
    print('No vale 9')

print('Fuera del bloque')

if (n==0):
    print("Cero")
elif (n>0):
    print("Mayo que cero")
else:
    print("Menor que cero")

cont = 1
while(cont <= 4):
    print(cont)
    cont = cont + 1

salir = False
while not salir:
    entrada = input("Salir?")
    if (entrada == 'S' or entrada == 's'):
        salir = True

secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
    print(elemento)

for i in range(10):  #Ir de 1 a 10.
    print("Hola ", end="") #para escribir en una linea
    #print("Hola ")
print()

cuenta = 0
for i in range(1, 6):
    if i % 2 == 0:
        cuenta = cuenta + 1
print(f"Desde 1 hasta 5 hay {cuenta} múltiplos de 2")