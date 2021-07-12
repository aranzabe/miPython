import animal, random

class Gato(animal.Animal):

    def __init__(self, nombre,raza,peso,color,lealtad):
        super().__init__(nombre,raza,peso,color) 
        self._lealtad = lealtad

    def __str__(self):
        return "Gato {Nombre: " + self._nombre + ", Raza: " + self._raza + ", Peso: " + str(self._peso) + ", Color: " + self._color + ", Lealtad: " + str(self._lealtad) + "}"
    
    def hacerRuido(self):
        return "Gato: " + self._nombre + " haciendo: MIAU"
    
    def hacerCaso(self):
        alea = random.randint(0, 100)
        caso = " ni caso"
        if (alea <= self._lealtad):
            caso = " haciendo caso"
        return "Gato: " + self._nombre + " " + caso

    def toserBolaPelo(self):
        return "Gato: " + self._nombre + " tosiendo bola de pelo"

    def comer(self):
        return "Gato: " + self._nombre + " comiendo"