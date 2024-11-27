import mysql.connector
import pymysql
from pymysql.err import Error

class DataBaseProductos:

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
    def cargarProductos() -> list:
        conn = DataBaseProductos.conexion()
        cursor = conn.cursor()
        sql= "SELECT * FROM producto;"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados

    @staticmethod
    # Funcion para agregar un nuevo Cliente  "CREATE"
    def agregar_producto(nombre, precio, descripcion, stock, categoria):
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = "INSERT INTO producto (nombre_producto, precio, descripcion, stock, categoria) VALUES (%s,%s,%s,%s,%s)"
            valores = (nombre, precio, descripcion, stock, categoria)
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
    def mostrar_producto_por_id(id):
        conn = DataBaseProductos.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM producto WHERE id={id}"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
            

    @staticmethod
    # Funcion para actualizar datos de un cliente "UPDATE"
    def actualizar_producto(id ,nombre_producto,precio,descripcion,stock,categoria):
        conn = DataBaseProductos.conexion()
        cursor = conn.cursor()
        sql= "UPDATE FROM producto WHERE id={id}"
        valores=(nombre_producto,precio,descripcion,stock,categoria)
        cursor.execute(sql,valores)
        conn.commit()
        cursor.close()
        conn.close()
        print("Producto modificado con exito")
    
    @staticmethod
    # Funcion para eliminar un cliente "DElETE"
    def eliminar_producto(id):
        conn = DataBaseProductos.conexion()
        try:
            cursor = conn.cursor()
            sql = f"DELETE FROM producto WHERE id_producto = {id}"
            cursor.execute(sql)
            conn.commit() 
            return True
        except Error as err:
            print(f'Hubo un error al eliminar el producto: {err}')
            return False
        finally:
            cursor.close()
            conn.close()