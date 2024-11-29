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
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql= "SELECT * FROM producto;"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error en la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()

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
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = "SELECT * FROM producto WHERE id={id}"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error en la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()
            

    @staticmethod
    # Funcion para actualizar datos de un cliente "UPDATE"
    def actualizar_producto(id ,nombre_producto,precio,descripcion,stock,categoria) -> bool:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql= "UPDATE producto SET nombre_producto = %s, precio= %s, descripcion = %s, stock = %s, categoria = %s WHERE id_producto=%s"
            valores=(nombre_producto,precio,descripcion,stock,categoria, id)
            cursor.execute(sql,valores)
            conn.commit()
            return True
        except Error as err:
            print(f'Ocurrio un error: {err}')
            return False
        finally: 
            cursor.close()
            conn.close()
    
    @staticmethod
    def ordenar_por_nombre() -> list:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM producto
                    ORDER BY nombre_producto ASC"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()
        
    @staticmethod
    def ordenar_por_precio() -> list:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM producto 
                    ORDER BY precio ASC"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def ordenar_por_descripcion() -> list:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM producto 
                    ORDER BY descripcion ASC"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def ordenar_por_stock() -> list:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM producto 
                    ORDER BY stock ASC"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def ordenar_por_categoria() -> list:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM producto
                    ORDER BY categoria ASC"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def mas_vendido() -> list:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT producto.id_producto, nombre_producto, precio, categoria, SUM(cantidad_producto) AS cant_ventas
                     FROM producto
                     JOIN orden_producto ON producto.id_producto = orden_producto.id_producto 
                     GROUP BY producto.id_producto
                     ORDER BY cant_ventas DESC"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def mas_ganancias() -> list:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT producto.id_producto, nombre_producto, precio, categoria, SUM(cantidad_producto) AS cant_ventas, SUM(subtotal) AS total
                     FROM producto
                     JOIN orden_producto ON producto.id_producto = orden_producto.id_producto 
                     GROUP BY producto.id_producto
                     ORDER BY total DESC"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()
    
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

    @staticmethod
    def producto_mas_vendido():
        conn = DataBaseProductos.conexion()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            sql = "SELECT p.nombre_producto, SUM(d.cantidad_producto) as total_vendido FROM producto p JOIN orden_producto d ON p.id_producto = d.id_producto GROUP BY p.id_producto ORDER BY total_vendido DESC LIMIT 1"
            cursor.execute(sql)
            producto = cursor.fetchone()
            return producto
        except pymysql.MySQLError as e:
            print(f"Error al buscar el producto más vendido: {e}")
            return None
        finally:
            cursor.close()
            conn.close()