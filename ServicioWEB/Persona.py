import json

class Persona:
    def __init__(self, dni, nombre) -> None:
        self.nombre = nombre
        self.dni =dni
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
