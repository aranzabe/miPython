import abc
from abc import abstractmethod

class Animal(abc.ABC):
#class Animal():
    def __init__(self,nombre,raza,peso,color):
        self._nombre = nombre;
        self._raza = raza;
        self._peso = peso;
        self._color = color;

    def __str__(self):
        return "Animal {Nombre: " + self._nombre + ", Raza: " + self._raza + ", Peso: " + str(self._peso) + ", Color: " + self._color + "}"

    def getNombre(self):
        return self._nombre
    
    def getRaza(self):
        return self._raza
    
    def getPeso(self):
        return self._peso
    
    def getColor(self):
        return self._color

    def setPeso(self, peso):
        self._peso = peso
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def vacunar(self):
        return "Animal: " + self._nombre + " vacunado"
    
    @abstractmethod
    def comer(self):
        #return "Animal: " + self._nombre + " comiendo"
        pass
    
    def dormir(self):
        return "Animal: " + self._nombre + " durmiendo"

    @abstractmethod
    def hacerRuido(self):
        #return "Animal: " + self._nombre + " haciendo ruido genérico"
        pass
    
    def hacerCaso(self):
        return "Animal: " + self._nombre + " haciendo caso genérico"