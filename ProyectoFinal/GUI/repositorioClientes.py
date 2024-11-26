import mysql.connector
import pymysql
from pymysql.err import Error

class DataBaseClientes:

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

    @staticmethod
    def cargarClientes() -> list:
        conn = DataBaseClientes.conexion()
        cursor = conn.cursor()
        sql= "SELECT * FROM cliente;"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados

    @staticmethod
    # Funcion para agregar un nuevo Cliente  "CREATE"
    def agregar_cliente(nombre,apellido,direccion,telefono,email):
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = "INSERT INTO cliente (nombre_cliente,apellido_cliente,direccion,telefono,email) VALUES (%s,%s,%s,%s,%s)"
            valores = (nombre,apellido,direccion,telefono,email)
            cursor.execute(sql,valores)
            conn.commit()
            return True
        except Error as err:
            print(f'Hubo un error al agregar el cliente: {err}')
            return False
        finally:
            cursor.close()
            conn.close()
        
    @staticmethod    
    # Funcion para mostrar clientes por id "READ"
    def mostrar_cliente_por_id(id):
        conn = DataBaseClientes.conexion()
        cursor = conn.cursor()
        sql = f"SELECT * FROM cliente WHERE id={id}"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
            

    @staticmethod
    # Funcion para actualizar datos de un cliente "UPDATE"
    def actualizar_cliente(self, id,nombre,apellido,direccion,telefono,email):
        conn = DataBaseClientes.conexion()
        cursor = conn.cursor()
        sql= f"UPDATE FROM cliente WHERE id={id}"
        valores=(nombre,apellido,direccion,telefono,email)
        cursor.execute(sql,valores)
        conn.commit()
        cursor.close()
        conn.close()
        print("Cliente modificado con exito")
    
    
    # Funcion para eliminar un cliente "DElETE"
    @staticmethod
    def eliminar_cliente(id):
        conn = DataBaseClientes.conexion()
        try:
            cursor = conn.cursor()
            sql = f"DELETE FROM cliente WHERE id_cliente={id}"
            cursor.execute(sql)
            conn.commit()
            return True
        except Error as err:
            print(f'Hubo un error al eliminar el cliente: {err}')
            return False
        finally:
            cursor.close()
            conn.close()
        