import persona

p = persona.Persona("Inma", 41)
print(p)
print(persona.Persona.curso)
print(p.curso)
print(p.edad)
print(p.nombre)
if (p.esMayorEdad()):
    print("Es mayor de edad.")
else:
    print("No lo es.")