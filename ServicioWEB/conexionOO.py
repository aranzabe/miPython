import pymysql
import json
import Persona
from Persona import Persona, PersonaEncoder
#La librería se instala con el comando: pip install pymysql
class Conexion:
    
    def __init__(self, usuario, passw, bd):
        self._usuario = usuario
        self._passw = passw
        self._bd = bd
        try:
            #Abrimos y cerramos la bd para dos cosas: comprobar que los datos de conexión son correctos y
            #dar el tipo adecuado a la variable self._conexion.
            self._conexion = pymysql.connect(host='localhost',
                                    user=self._usuario,
                                    password=self._passw,
                                    db=self._bd)
            self._conexion.close()
            print("Datos de conexión correctos.")
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error con los datos de conexión: ", e)
        
         
    def conectar(self):
        """Devuelve la variable conexion o -1 si la conexión no ha sido correcta."""
        try:
            self._conexion = pymysql.connect(host='localhost',
                                    user=self._usuario,
                                    password=self._passw,
                                    db=self._bd)
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return -1

    def cerrarConexion(self):
        self._conexion.close()
        
        
    def insertarPersona(self, dni, nombre, clave, tfno):
        """Insertar una persona en la tabla Personas."""
        try:
            self.conectar()
            cursor =  self._conexion.cursor()
            consulta = "INSERT INTO personas(DNI, Nombre, Clave, Tfno) VALUES (%s, %s, %s, %s)"
            cursor.execute(consulta, (dni, nombre, clave, tfno))
            self._conexion.commit()
            self.cerrarConexion()
            return 0
        except (pymysql.err.IntegrityError) as e:
            # print("Ocurrió un error al insertar: clave duplicada.", e)
            return -1


    #https://stackoverflow.com/questions/3286525/return-sql-table-as-json-in-python
    def seleccionarTodos(self):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT DNI, Nombre, Clave, Tfno FROM personas")
                r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
                #print(r)
                self.cerrarConexion()
                return r
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return []


    #https://www.programcreek.com/python/example/104689/sklearn.datasets.fetch_20newsgroups
    #https://stackoverflow.com/questions/11280382/object-is-not-json-serializable
    def buscarDNI(self, dni):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT DNI, Nombre, Clave, Tfno FROM personas WHERE DNI = %s", (dni))
                
                r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
                # print(r)
                # print("----")
                print(r)
                # objJson = r[0]
                # # Con fetchall traemos todas las filas
                # pers = cursor.fetchall()
                # # Recorrer e imprimir
                # for row in pers:
                #     p = Persona(row[0],row[1],row[2],row[3])
                # objJson = json.dumps(p, cls=PersonaEncoder, indent=4)
                # #print(objJson)
                
                self.cerrarConexion()
                
                
                if (r):
                    return r[0]
                else:
                    return []
                
                
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return []
        
        
        
    def cambiarClave(self, dniEditar, nueva):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                consulta = "UPDATE personas SET clave = %s WHERE dni = %s;"
                cursor.execute(consulta, (nueva, dniEditar))

            # No olvidemos hacer commit cuando hacemos un cambio a la BD
            self._conexion.commit()
            self.cerrarConexion()
            return 0
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return -1
        
        
    #https://pynative.com/python-mysql-delete-data/
    def borrarDNI(self, dniBorrar):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                consulta = "DELETE FROM personas WHERE DNI = %s;"
                cursor.execute(consulta, (dniBorrar))

                # No olvidemos hacer commit cuando hacemos un cambio a la BD
                self._conexion.commit()
                self.cerrarConexion()
                return cursor.rowcount #Registros afectados en el borrado.
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return -1
        
    #https://pynative.com/python-mysql-update-data/
    def modificarPersona(self, dni, nombre, tfno):
        """Insertar una persona en la tabla Personas."""
        try:
            self.conectar()
            cursor =  self._conexion.cursor()
            consulta = "UPDATE personas SET DNI = %s, Nombre = %s, Tfno = %s  WHERE dni = %s;"
            cursor.execute(consulta, (dni, nombre, tfno, dni))
            self._conexion.commit()
            self.cerrarConexion()
            return cursor.rowcount
        except (pymysql.err.IntegrityError) as e:
            # print("Ocurrió un error al insertar: clave duplicada.", e)
            return -1

