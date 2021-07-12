import animal, random

class Perro(animal.Animal):

    def __init__(self, nombre,raza,peso,color,lealtad):
        super().__init__(nombre,raza,peso,color) 
        self._lealtad = lealtad

    def __str__(self):
        return "Perro {Nombre: " + self._nombre + ", Raza: " + self._raza + ", Peso: " + str(self._peso) + ", Color: " + self._color + ", Lealtad: " + str(self._lealtad) + "}"
    
    def hacerRuido(self):
        return "Perro: " + self._nombre + " haciendo: GUAU"
    
    def hacerCaso(self):
        alea = random.randint(0, 100)
        caso = " ni caso"
        if (alea <= self._lealtad):
            caso = " haciendo caso"
        return "Perro: " + self._nombre + " " + caso

    def sacarPaseo(self):
        return "Perro: " + self._nombre + " saliendo de paseo."

    def comer(self):
        return "Perro: " + self._nombre + " comiendo"