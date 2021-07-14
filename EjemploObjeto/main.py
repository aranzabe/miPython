import persona, persona2

#Esta primera forma es estilo "Duck typing". Se definen los atributos para cada instancia y se pueden tocar directamente.
p = persona.Persona("Pepe", 30)
print(p)
print(persona.Persona.curso)
print(p.curso)
print(p.edad)
print(p.nombre)
if (p.esMayorEdad()):
    print("Es mayor de edad.")
else:
    print("No lo es.")

#Un estilo de orientación a objetos más formal, encapsulando los atributos y utilizando los métodos para acceder a esos atributos.
p2 = persona2.Persona2("Maria", 20)
print(p2)
p2.setEdad(36)
p2.setNombre("Rigoberta")
print(p2.getEdad())
print(p2.getNombre())