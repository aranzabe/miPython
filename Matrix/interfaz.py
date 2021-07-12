import abc
from abc import abstractmethod

class Interfaz(abc.ABC):
    @abstractmethod
    def resumen(self):
        pass