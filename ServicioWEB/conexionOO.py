import pymysql
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
            # print("Ocurrió un error al conectar: ", e)
            return -1

    def seleccionarTodos(self):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT DNI, Nombre, Clave, Tfno FROM personas")

                # Con fetchall traemos todas las filas
                pers = cursor.fetchall()
                lisPersonas = []
                # Recorrer e imprimir
                for pe in pers:
                    lisPersonas += [pe]
                    
                self.cerrarConexion()
                return pers
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return []
        
    def buscarDNI(self, dni):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT * FROM personas WHERE DNI = %s", (dni))

                # Con fetchall traemos todas las filas
                pers = cursor.fetchall()
                lisPersonas = []
                # Recorrer e imprimir
                for pe in pers:
                    lisPersonas += [pe]
                self.cerrarConexion()
                return lisPersonas
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
        
        
    def borrarDNI(self, dniBorrar):
        try:
            self.conectar()
            with self._conexion.cursor() as cursor:
                consulta = "DELETE FROM personas WHERE DNI = %s;"
                cursor.execute(consulta, (dniBorrar))

                # No olvidemos hacer commit cuando hacemos un cambio a la BD
                self._conexion.commit()
                self.cerrarConexion()
                return 0
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return -1
