class Persona:
    curso = "DAW2"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f"Persona: nombre = {self.nombre}, edad = {self.edad}"

    def esMayorEdad(self):
        loes = False
        if (self.edad >= 18):
            loes = True
        return loes
    