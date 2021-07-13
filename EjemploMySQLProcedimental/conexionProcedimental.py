import pymysql

def conectar(usuario, clave, bd):
    """Devuelve la variable conexion o -1 si la conexión no ha sido correcta."""
    try:
        conexion = pymysql.connect(host='localhost',
                                user=usuario,
                                password=clave,
                                db=bd)
        #print("Conexión correcta")
        return conexion
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    # print("Ocurrió un error al conectar: ", e)
        return -1

def cerrarConexion(conexion):
    conexion.close()
     
def insertarPersona(conexion, dni, nombre, clave, tfno):
    """Insertar una persona en la tabla Personas."""
    try:
        cursor =  conexion.cursor()
        consulta = "INSERT INTO personas(DNI, Nombre, Clave, Tfno) VALUES (%s, %s, %s, %s)"
        cursor.execute(consulta, (dni, nombre, clave, tfno))
        conexion.commit()
        return 0
    except (pymysql.err.IntegrityError) as e:
        # print("Ocurrió un error al conectar: ", e)
        return -1

def seleccionarTodos(conexion):
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM personas")

            # Con fetchall traemos todas las filas
            pers = cursor.fetchall()
            lisPersonas = []
            # Recorrer e imprimir
            for pe in pers:
                lisPersonas += [pe]
            return lisPersonas
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        return []
    
def buscarDNI(conexion, dni):
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM personas WHERE DNI = %s", (dni))

            # Con fetchall traemos todas las filas
            pers = cursor.fetchall()
            lisPersonas = []
            # Recorrer e imprimir
            for pe in pers:
                lisPersonas += [pe]
            return lisPersonas
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        return []
    
def cambiarClave(conexion, dniEditar, nueva):
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE personas SET clave = %s WHERE dni = %s;"
            cursor.execute(consulta, (nueva, dniEditar))

        # No olvidemos hacer commit cuando hacemos un cambio a la BD
        conexion.commit()
        return 0
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        return -1
    
    
def borrarDNI(conexion, dniBorrar):
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM personas WHERE DNI = %s;"
            cursor.execute(consulta, (dniBorrar))

            # No olvidemos hacer commit cuando hacemos un cambio a la BD
            conexion.commit()
            return 0
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        return -1