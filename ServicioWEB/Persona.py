import json

class PersonaEncoder(json.JSONEncoder):
 
    def default(self, obj):
        return obj.__dict__
    
    
class Persona(object):
    def __init__(self, dni, nombre, clave, tfno) -> None :
        self.DNI =dni
        self.Nombre = nombre
        self.Clave = clave
        self.Tfno = tfno
    
    # def toJSON(self):
    #     #return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    #     return json.dump(self)
    #     #return json.dumps(self, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
    
    def __str__(self) :
        return json.dumps(self)

#http://daniel.blogmatico.com/convertir-un-objeto-python-a-un-objeto-json/