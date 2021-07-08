def mmultiplesArgs(a, *otros):
    """Esta función admite argumentos variables en otros; será una tupla que podemos recorrer."""
    print(a)
    for elemento in otros:
        print(elemento, end=" ")
    print()

def mmultiplesArgs2(a, **otros):
    """Esta función admite argumentos variables en otros; será un diccionario que podemos recorrer."""
    print(a)
    for elemento in otros:
        print(elemento, end=" ")
    print()


def f(a, b):
    a = a + 3
    b.append(23)
    print("Dentro de la función: " + str(a) + str(b))
#Como vemos la variable x no conserva los cambios una vez salimos de
#la función porque los enteros son inmutables en Python. Sin embargo
#la variable y si los conserva, porque las listas son mutables.
    #print(x) #Curiosidad, la variable del main sí es reconocido aquí.
    #x = x + 1 #Pero si intentamos operarla da un error.
    #variables libres: las que pertenecen a ámbitos superiores pero son accesibles en la subrutina


x = 22
y = [22]
f(x,y)
print("Después de llamar a la función: " + str(x) + str(y))

mmultiplesArgs(x,1,2,3,4)
mmultiplesArgs2(x,uno=1, dos=2, tres=3)

########################################################################################

def calcula_media(x, y):
    resultado = (x + y) / 2
    return resultado

a = 4
b = 5
media = calcula_media(a, b)
print(f"La media de {a} y {b} es: {media}")
print()

def calcula_media(*args):
    total = 0
    for i in args:
        total += i
    resultado = total / len(args)
    return resultado

a, b, c = 4, 5, 12
media = calcula_media(a, b, c)
print(f"La media de {a}, {b} y {c} es: {media}")
print()



#Permite devolver más de un valor en el return!!!
def calcula_media_desviacion(*args):
    total = 0
    for i in args:
        total += i
    media = total / len(args)
    total = 0
    for i in args:
        total += (i - media) ** 2
    desviacion = (total / len(args)) ** 0.5
    return media, desviacion

a, b, c, d = 3, 5, 10, 12
media, desviacion_tipica = calcula_media_desviacion(a, b, c, d)
print(f"Datos: {a} {b} {c} {d}")
print(f"Media: {media}")
print(f"Desviación típica: {desviacion_tipica}")

