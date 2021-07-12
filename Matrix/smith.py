import persona, interfaz

class Smith(persona.Persona, interfaz.Interfaz):
    def __init__(self, localizacion, edad, porcInfeccion):
        super().__init__("Smith", localizacion, edad)
        self._porcInfeccion = porcInfeccion
        
    def __str__(self):
        return "Smith: {Infección: " + str(self._porcInfeccion) + ", " + str(self._localizacion) 
    
    def setPorcentaje(self, porInf):
        self._porcInfeccion = porInf
    
    def getPorcentaje(self):
        return self._porcInfeccion
    
    #Obligada a implementarse por incluir la interfaz en la herencia.
    def resumen(self):
        return "S{" + str(self._porcInfeccion) + "}"

