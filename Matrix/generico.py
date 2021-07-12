import persona, interfaz

class Generico(persona.Persona, interfaz.Interfaz):
    def __init__(self, nombre, localizacion, edad, porcMorir):
        super().__init__(nombre, localizacion, edad)
        self._porcMorir = porcMorir
        
    def __str__(self):
        return  "Genérica {Nombre: " + self._nombre + ", Edad: " + str(self._edad) + ", " + str(self._localizacion) + ", Porcentaje morir: " + str(self._porcMorir) + "}"
    
    def setPorcentaje(self, porMorir):
        self._porcMorir = porMorir
    
    def getPorcentaje(self):
        return self._porcMorir
    
    #Obligada a implementarse por incluir la interfaz en la herencia.
    def resumen(self):
        return "G{" + self._nombre + ", " + str(self._porcMorir) + "}"
    