import pymysql
from pymysql.err import Error

class DatabaseOrdenes:

    #Funcion para conectar a la base de datos
    @staticmethod
    def conexion():
        try:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="martin145",
                database="sist_ventas"
            )
            return conn
        except pymysql.MySQLError as e:
            raise ConnectionError(f"No se pudo conectar a la base de datos: {e}")

    #Funcion para cargar todas las ordenes
    @staticmethod
    def cargarOrdenes() -> tuple:
        try:
            conn = DatabaseOrdenes.conexion()
            cursor = conn.cursor()
            sql= """SELECT orden.id_orden, id_cliente, fecha, SUM(subtotal)
                    FROM orden
                    JOIN orden_producto ON orden_producto.id_orden = orden.id_orden
                    GROUP BY orden.id_orden;"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Hubo un error al obtener las ordenes: {err}')
            return None
        finally:
            cursor.close()
            conn.close()

        
    @staticmethod    
    # Funcion para mostrar Ordenes por id "READ"
    def mostrar_orden_ID(id) -> tuple:
        try:
            conn = DatabaseOrdenes.conexion()
            cursor = conn.cursor()
            sql = """SELECT orden.id_orden, id_cliente, fecha, SUM(subtotal)
                    FROM orden
                    JOIN orden_producto ON orden_producto.id_orden = orden.id_orden
                    WHERE orden.id_orden = %s
                    GROUP BY orden.id_orden;"""
            cursor.execute(sql, id)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consutla: {err}')
            return None
        finally:
            cursor.close()
            conn.close()


    #Funcion para mostrar las ordenes de un cliente dado
    @staticmethod
    def mostrar_orden_cliente(id) -> tuple:
        try:
            conn = DatabaseOrdenes.conexion()
            cursor = conn.cursor()
            sql = """SELECT orden.id_orden, id_cliente, fecha, SUM(subtotal)
                    FROM orden
                    JOIN orden_producto ON orden_producto.id_orden = orden.id_orden
                    WHERE id_cliente = %s
                    GROUP BY orden.id_orden;"""
            cursor.execute(sql, id)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consutla: {err}')
            return []
        finally:
            cursor.close()
            conn.close()
    
    
    # Funcion para eliminar un orden "DElETE"
    @staticmethod
    def eliminar_orden(id) -> bool:
        conn = DatabaseOrdenes.conexion()
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM orden WHERE id_orden = %s"
            cursor.execute(sql, id)
            conn.commit()
            return True
        except Error as err:
            print(f'Hubo un error al eliminar el cliente: {err}')
            return False
        finally:
            cursor.close()
            conn.close()

    #Funcion para obtener el detalle de las ordenes (nombre y cantidad de productos)
    @staticmethod
    def detalles_orden(id) -> tuple:
        try:
            conn = DatabaseOrdenes.conexion()
            cursor = conn.cursor()
            sql = """SELECT nombre_producto, cantidad_producto
                    FROM orden_producto
                    JOIN producto ON orden_producto.id_producto = producto.id_producto
                    WHERE id_orden = %s;"""
            cursor.execute(sql, id)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consutla: {err}')
            return None
        finally:
            cursor.close()
            conn.close()
        