import persona

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