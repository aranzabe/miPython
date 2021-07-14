class Persona2:
    """Esta clase define los atributos de la misma como privados (protegidos más bien) para encapsular y no tocar directamente los atributos fuera"""
    curso = "DAW2" #Esto equivale a una variable static de Java
    def __init__(self, nombre, edad):
        self._nombre = nombre #Poniendo el guion bajo convertimos el atributo en privado (equivalente a protected en Java).
        self.__edad = edad     #Si ponemos doble guion lo convertimos en privado por lo que si alguna clase hereda de esta no lo podrá tocar directamente.
    
    def __str__(self): #Equivalente al toString
        return f"Persona: nombre = {self._nombre}, edad = {self.__edad}"

    def esMayorEdad(self):
        loes = False
        if (self.edad >= 18):
            loes = True
        return loes

    #Ahora nos harán falta los get/set. A todos los métodos hay que pasarle una referencia a la instancia del objeto (self equivale a this)
    def getEdad(self):
        return self.__edad
    
    def setEdad(self, eda):
        self.__edad = eda
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nom):
        self._nombre = nom
    