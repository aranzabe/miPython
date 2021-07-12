class HelloWorld:
    
    saludo = 'Hola mundo'
    def __init__(self):
        self.saludo = 'No hay saludo'
    
    @staticmethod
    def saludoStaticmethod(self):
        return self.saludo
    @classmethod
    def saludoClassmethod(self):
        return self.saludo

        
print(HelloWorld.saludoStaticmethod(HelloWorld))
print(HelloWorld.saludoClassmethod())

#Si te fijas en el código, ya no necesito realizar una instancia de la clase para llamar a los métodos. Pero una diferencia es 
#que el @staticmethod necesita recibir en el método, el nombre de la clase ya que de lo contrario arrojará error, por otro lado 
#el @classmethod hace lo mismo que el anterior, solo que este decorados ya le dice a Python que los métodos que este decorados
#con este, automáticamente deben recibir el nombre de la clase.