n = 12
print("El valor de n es " + str(n))
n2 = 5
sol = n / n2
print(sol)

t = (12,'a',3.6)  #La tupla es fija, una vez definida no se puede cambiar.
print("Contenido de la tupla:",str(t))
print(t[0])


l = [1,4,"hola",True] #Equivalente al LinkedList.
print("Contenido de la lista:",str(l))
print(l[-1]) #Desplazamiento desde la derecha
l.append('añadido') #Añade un elemento
l.extend("al final") #Añade al final un elemento, pero lo hace letra a letra
print("Contenido de la lista:",str(l))
l.remove('hola') #Borra el elemento indicado por contenido
print("Contenido de la lista:",str(l))
del(l[0]) #Borra el elemento 0
print("Contenido de la lista:",str(l))
l.pop(1)  #Similar al anterior, borra el elemento 1
print("Contenido de la lista:",str(l))


d = {'Uno' : 'Primer elemento',
     'Dos' : 'Segundo elemento'} #Tabla hash. Equivalente a un vector asociativo PHP.
print(d['Uno'])
d['Tres'] = 'Añadimos el tercero' #Para añadir
print("Contenido del diccionario:",str(d))
del(d['Dos']) #Borramos el elemento 2.
print("Contenido del diccionario:",str(d))