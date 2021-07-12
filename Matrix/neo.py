import persona, random, interfaz

class Neo(persona.Persona, interfaz.Interfaz):
    def __init__(self, localizacion, edad, meLoCreo):
        super().__init__("Neo", localizacion, edad)
        self._meLoCreo = meLoCreo
        
    def __str__(self):
        return "Neo: {Me lo creo: " + str(self._meLoCreo) + ", " + str(self._localizacion) 
    
    #Realmente esta función no es necesaria aquí pero es por tener un ejemplo de función privada.
    def _decide(self):
        alea = random.randint(1, 2)
        if (alea == 1):
            self._meLoCreo = True
        else:
            self._meLoCreo = False
    
    def getMeLoCreo(self):
        self._decide()
        return self._meLoCreo
    
    #Obligada a implementarse por incluir la interfaz en la herencia.
    def resumen(self):
        return "N{" + str(self._meLoCreo) + "}"