import animal
import perro, gato

#Este bloque que hay comentado a continuación solo será posible si la clase Animal no es abstracta.
#La hemos vuelto abstracta al poner: class Animal(abc.ABC): en la declaración y métodos abstractos en el cuerpo.
# a = animal.Animal("Fliqui", "Siamés" , 4, "Marrón")
# print(a)
# print(a.getNombre())
# a.setNombre("Akira")
# a.setPeso(9)
# print(a)
# print(a.hacerRuido())
# oa = a
# print(oa)
# oa.setNombre("Otro Akira")
# print("Valor de a modificado a través de oa: " + str(a))


#Si no implementamos todos los métodos abstractos nos daría el siguiente error:
#TypeError: Can't instantiate abstract class Perro with abstract method comer
p = perro.Perro("Tara","Pastor",19,"Negro",90)
print(p)
print(p.hacerCaso())
print(p.hacerRuido())
print(p.sacarPaseo())


#Si no implementamos todos los métodos abstractos nos daría el siguiente error:
#TypeError: Can't instantiate abstract class Gato with abstract method comer
g = gato.Gato("Akira","Siamés",7,"Marrón",10)
print(g)
print(g.hacerCaso())
print(g.hacerRuido())
print(g.toserBolaPelo())

#zoo = [a,g,p]
zoo = []
#zoo.append(a)
#zoo += [a]
#zoo.append(g)
zoo += [g]
#zoo.append(p)
zoo += [p]

print(zoo)
for elemento in zoo:
    print(elemento.hacerCaso())
    #A diferencia de Java no tenemos que castear la variable para acceder a los métodos específicos.
    if (isinstance(elemento,gato.Gato)):
        print(elemento.toserBolaPelo())
    if (isinstance(elemento,perro.Perro)):
        print(elemento.sacarPaseo())
    print(elemento.comer())
