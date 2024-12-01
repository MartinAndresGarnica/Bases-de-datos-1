import pymysql

class Conexion:
    #Funcion para conectar a la base de datos
    @staticmethod
    def conexion():
        try:
            conn = pymysql.connect(
                host="localhost",
                user="ventas",
                password="123123123",
                database="sist_ventas"
            )
            return conn
        except pymysql.MySQLError as e:
            raise ConnectionError(f"No se pudo conectar a la base de datos: {e}")