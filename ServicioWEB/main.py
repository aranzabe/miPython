import conexionOO
import json
import Persona
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

#Comenta y/o descomenta cada bloque para probar cada apartado.
#La base de datos la puedes encontrar en la carpeta del proyecto, solo tienes que importarla
#y cambiar las credenciales por las tuyas.
#https://blog.nearsoftjobs.com/crear-un-api-y-una-aplicaci%C3%B3n-web-con-flask-6a76b8bf5383
#https://content.breatheco.de/es/lesson/building-apis-with-python-flask

#pip install Flask
#pip install flask_restful

################################### Probando conexión ####################################
conex = conexionOO.Conexion('fernando','Chubaca2018','ejemplo')
# conex.cerrarConexion()


################################### Probando inserción ###################################
#Dentro del método insertar se realiza una apertura y un cerrado de la conexión.
# dni = input("DNI? ")
# nombre = input("Nombre? ")
# clave = input("Clave? ")
# tefno = input("Teléfono? ")
# resultado = conex.insertarPersona(dni, nombre, clave, tefno)
# if(resultado == -1):
#     print("Problema al insertar el registro.")
# else:
#     print("Registro insertado con éxito.")
    

################################ Probando select de todos #######################################
# Dentro del método seleccionar se realiza una apertura y un cerrado de la conexión.
# listaPersonas = conex.seleccionarTodos()
# if (len(listaPersonas) != 0):
#     for pe in listaPersonas:
#         print(pe)
#         #print("DNI: " + pe[0] + ", nombre: " + pe[1])
# else:
#     print("No se han extraído datos.")




################################# Buscando por DNI ###############################################
#Dentro del método seleccionar se realiza una apertura y un cerrado de la conexión.
# dni = input("DNI a buscar? ")
# listaPersonas = conex.buscarDNI(dni)
# if (len(listaPersonas) != 0):
#     for pe in listaPersonas:
#         print(pe)
#         print("DNI: " + pe[0] + ", nombre: " + pe[1])
# else:
#     print("No se han encontrado datos")
    
    
############################### Probando cambiar la clave de un dni ###################################
#Dentro del método cambiarClave se realiza una apertura y un cerrado de la conexión.
# dniCambiar = input("DNI a cambiar? ")
# nuevaClave = input("Nueva clave? ")
# resultado = conex.cambiarClave(dniCambiar, nuevaClave)
# if (resultado == 0):
#     print("Clave cambiada.")
# else:
#     print("No se han encontrado datos")
    

##################################### Probando borrar por dni #########################################
#Dentro del método birrarDNI se realiza una apertura y un cerrado de la conexión.
# dniBorrar = input("DNI a borrar? ")
# resultado = conex.borrarDNI(dniBorrar)
# if (resultado == 0):
#     print("Registro borrado.")
# else:
#     print("No se han borrado datos")

app = Flask(__name__)
api = Api(app)

#------------------------------------------------------------------------------
@app.route('/')
def hello():
    return 'Hola holita'

#------------------------------------------------------------------------------
#https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https
#pip install pyopenssl  --> para montarlo sobre https.
@app.route("/listado", methods=['GET']) #aquí especificamos la ruta para el endpoint.
def getPersonas(): #aquí declaramos una función que se llamará cuando se realice una request a esa url
    listaPersonas = conex.seleccionarTodos()
    print(listaPersonas)
    if (len(listaPersonas) != 0):
        resp = jsonify(listaPersonas)
        resp.status_code = 200
    else:
        respuesta = {'message': 'No se han extraido datos.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    print(resp)
    return resp

#------------------------------------------------------------------------------
@app.route("/listado/<id>", methods=['GET']) #aquí especificamos la ruta para el endpoint.
def getPersona(id): #aquí declaramos una función que se llamará cuando se realice una request a esa url
    print(id)
    listaPersonas = conex.buscarDNI(id)
    print(jsonify(listaPersonas))
    if (len(listaPersonas) != 0):
        resp = jsonify(listaPersonas)
        resp.status_code = 200
    else:
        respuesta = {'message': 'No se han extraido datos.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    print(resp)
    return resp

#------------------------------------------------------------------------------
@app.route("/registrar", methods=["POST"])
def addPersona():
    data = request.json
    print(data) #Desde Android nos llega en formato diccionario.
    print(data['DNI'])
    print(data['Nombre'])
    print(data['Tfno'])
    if (conex.insertarPersona(data['DNI'],data['Nombre'],data['Clave'],data['Tfno'])==0):
        respuesta = {'message': 'Ok.'}
        resp = jsonify(respuesta)
        resp.status_code = 200
    else:
        respuesta = {'message': 'Clave duplicada.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    
    print(resp)
    return resp 

#------------------------------------------------------------------------------    
@app.route("/borrar/<dni>", methods=["DELETE"])
def delPersona(dni):
    
    if (conex.borrarDNI(dni)>0):
        respuesta = {'message': 'Ok.'}
        resp = jsonify(respuesta)
        resp.status_code = 200
    else:
        respuesta = {'message': 'DNI' + str(dni) + ' no encontrado.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    print(respuesta)
    print(resp)
    return resp 

#------------------------------------------------------------------------------
@app.route("/modificar", methods=["PUT"])
def modPersona():
    data = request.json
    print(data) #Desde Android nos llega en formato diccionario.
    print(data['DNI'])
    print(data['Nombre'])
    print(data['Tfno'])
    if (conex.modificarPersona(data['DNI'],data['Nombre'],data['Tfno']) > 0):
        respuesta = {'message': 'Ok.'}
        resp = jsonify(respuesta)
        resp.status_code = 200
    else:
        respuesta = {'message': 'Error al modificar.'}
        resp = jsonify(respuesta)
        resp.status_code = 400
    
    print(resp)
    return resp 

# Para montarlo en http normaleras.
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host= '192.168.1.108') #Esto sería para poder usar el móvil. No arrancaría el servicio en localhost sino en esa ip.

# Esto es para montarlo en https.
# if __name__ == "__main__":
#     app.run(ssl_context='adhoc')