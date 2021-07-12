class HelloWorld:
    
    saludo = 'Hola mundo'
    def __init__(self):
        self.saludo = 'No hay saludo'
    
    def saludoStaticmethod(self):
        return self.saludo
    def saludoClassmethod(self):
        return self.saludo
        
instancia = HelloWorld() # Realizamos una instancia para poder llamar a los métodos
print(instancia.saludoStaticmethod())
print(instancia.saludoClassmethod())

#Al ejecutar este código se nos imprimirá dos veces la cadena de texto “No hay saludo”, esto es porque ambos retornan lo mismo. 
#Pero, si te fijas la clase contiene una variable estática llamada saludo que contiene un “Hola mundo” y es aquí donde entran 
#los métodos estáticos: ver main2.py