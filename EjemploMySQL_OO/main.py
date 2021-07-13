import conexionOO

#Comenta y/o descomenta cada bloque para probar cada apartado.
#La base de datos la puedes encontrar en la carpeta del proyecto, solo tienes que importarla
#y cambiar las credenciales por las tuyas.


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
listaPersonas = conex.seleccionarTodos()
if (len(listaPersonas) != 0):
    for pe in listaPersonas:
        print(pe)
        #print("DNI: " + pe[0] + ", nombre: " + pe[1])
else:
    print("No se han extraído datos.")




################################# Buscando por DNI ###############################################
#Dentro del método seleccionar se realiza una apertura y un cerrado de la conexión.
dni = input("DNI a buscar? ")
listaPersonas = conex.buscarDNI(dni)
if (len(listaPersonas) != 0):
    for pe in listaPersonas:
        print(pe)
        print("DNI: " + pe[0] + ", nombre: " + pe[1])
else:
    print("No se han encontrado datos")
    
    
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