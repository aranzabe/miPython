import conexionProcedimental

#Comenta y/o descomenta cada bloque para probar cada apartado.
#La base de datos la puedes encontrar en la carpeta del proyecto, solo tienes que importarla
#y cambiar las credenciales por las tuyas.


################################### Probando conexión ####################################
#conex = conexionProcedimental.conectar('fernando','Chubaca2018','ejemplo')
#conexionProcedimental.cerrarConexion(conex)


################################### Probando inserción ###################################
# if (conex != -1):
#     print("Conexión realizada.")
#     dni = input("DNI? ")
#     nombre = input("Nombre? ")
#     clave = input("Clave? ")
#     tefno = input("Teléfono? ")
#     #resultado = conexionProcedimental.insertarPersona(conex, 'C5','Inma','Akira','1234')
#     resultado = conexionProcedimental.insertarPersona(conex, dni, nombre, clave, tefno)
#     if(resultado == -1):
#         print("Problema al insertar el registro.")
#     else:
#         print("Registro insertado con éxito.")
#     conexionProcedimental.cerrarConexion(conex)
#     print("Conexión cerrada")
# else:
#     print("Error en la conexión, revise las credenciales.")
    

################################ Probando select de todos #######################################
conex = conexionProcedimental.conectar('fernando','Chubaca2018','ejemplo')
if (conex != -1):
    print("Conexión realizada.")
    listaPersonas = conexionProcedimental.seleccionarTodos(conex)
    if (len(listaPersonas) != 0):
        for pe in listaPersonas:
            print(pe)
            #print("DNI: " + pe[0] + ", nombre: " + pe[1])
    else:
        print("No se han extraído datos.")
    conexionProcedimental.cerrarConexion(conex)
    print("Conexión cerrada.")
else:
    print("Error en la conexión, revise las credenciales.")


################################# Buscando por DNI ###############################################
# dni = input("DNI a buscar? ")
# conex = conexionProcedimental.conectar('fernando','Chubaca2018','ejemplo')
# if (conex != -1):
#     print("Conexión realizada.")
#     listaPersonas = conexionProcedimental.buscarDNI(conex, dni)
#     if (len(listaPersonas) != 0):
#         for pe in listaPersonas:
#             print(pe)
#             print("DNI: " + pe[0] + ", nombre: " + pe[1])
#     else:
#         print("No se han encontrado datos")
#     conexionProcedimental.cerrarConexion(conex)
#     print("Conexión cerrada.")
# else:
#     print("Error en la conexión, revise las credenciales.")
    
    
############################### Probando cambiar la clave de un dni ###################################
# dniCambiar = input("DNI a cambiar? ")
# nuevaClave = input("Nueva clave? ")
# conex = conexionProcedimental.conectar('fernando','Chubaca2018','ejemplo')
# if (conex != -1):
#     print("Conexión realizada.")
#     resultado = conexionProcedimental.cambiarClave(conex, dniCambiar, nuevaClave)
#     if (resultado == 0):
#         print("Clave cambiada.")
#     else:
#         print("No se han encontrado datos")
#     conexionProcedimental.cerrarConexion(conex)
#     print("Conexión cerrada.")
# else:
#     print("Error en la conexión, revise las credenciales.")
    

############################### Probando borrar por dni ###################################
# dniBorrar = input("DNI a borrar? ")
# conex = conexionProcedimental.conectar('fernando','Chubaca2018','ejemplo')
# if (conex != -1):
#     print("Conexión realizada.")
#     resultado = conexionProcedimental.borrarDNI(conex, dniBorrar)
#     if (resultado == 0):
#         print("Registro borrado.")
#     else:
#         print("No se han borrado datos")
#     conexionProcedimental.cerrarConexion(conex)
#     print("Conexión cerrada.")
# else:
#     print("Error en la conexión, revise las credenciales.")