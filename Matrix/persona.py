class Localizacion:
    def __init__(self,longitud, latitud, ciudad):
        self._longitud = longitud
        self._latitud = latitud
        self._ciudad = ciudad
    
    def __str__(self):
        return "Localizacion {Ciudad: " + self._ciudad + ", (" + str(self._longitud) + ", " + str(self._latitud) + ")}"
        
#------------------------ Clase Persona --------------------------
class Persona:
    
    #Varianle estática de clase
    cantidadPersona = 0
    
    def __init__(self, nombre, localizacion, edad):
        self._nombre = nombre
        self._localizacion = localizacion
        self._edad = edad
        Persona.cantidadPersona += 1
        
    def __str__(self):
        return "Persona {Nombre: " + self._nombre + ", Edad: " + str(self._edad) + ", " + str(self._localizacion) + "}"
    
    @classmethod
    def cuantasPersonasDefinidas(cls):
        return Persona.cantidadPersona
    
    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getLocalizacion(self):
        return self._localizacion
    
    def setEdad(self, edad):
        self._edad = edad
        
    
    
    