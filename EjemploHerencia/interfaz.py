import abc
from abc import abstractmethod

#Si queremos usar una interfaz para que la clase animal no sea abstracta y pueda instanciarse, usamos la siguiente clase:

class Interfaz(abc.ABC):
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def hacerRuido(self):
        pass

#Ahora las definiciones de perros y gatos serían: class Gato(animal.Animal, interfaz.Interfaz)
