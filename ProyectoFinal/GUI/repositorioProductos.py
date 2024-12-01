import pymysql
from pymysql.err import Error

class DataBaseProductos:

    #Funcion para establecer la conexion con la base de datos
    @staticmethod
    def conexion():
        try:
            conn = pymysql.connect(
                host="localhost",
                user="martin",
                password="123456789",
                database="sist_ventas"
            )
            return conn
        except pymysql.MySQLError as e:
            raise ConnectionError(f"No se pudo conectar a la base de datos: {e}")

    #Funcion para cargar todos los productos
    @staticmethod
    def cargarProductos() -> tuple:
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
    # Funcion para agregar un nuevo producto  "CREATE"
    def agregar_producto(nombre, precio, descripcion, stock, categoria) -> bool: 
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
    # Funcion para mostrar producto por id "READ"
    def mostrar_producto_por_id(id) -> tuple:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = "SELECT * FROM producto WHERE id=%s"
            cursor.execute(sql, id)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error en la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()
            
    # Funcion para actualizar datos de un producto "UPDATE"
    @staticmethod
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
    
    #Funcion para ordenar por nombre
    @staticmethod
    def ordenar_por_nombre() -> tuple:
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
        
    #Funcion para ordenar por precio
    @staticmethod
    def ordenar_por_precio() -> tuple:
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

    #Funcion para ordenar por descripcion
    @staticmethod
    def ordenar_por_descripcion() -> tuple:
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

    #Funcion para ordenar por stock
    @staticmethod
    def ordenar_por_stock() -> tuple:
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
    
    #Funcion para ordenar por categoria la lista
    @staticmethod
    def ordenar_por_categoria() -> tuple:
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

    #Funcion para obtener la cantidad de ventas que tuvo cada producto
    @staticmethod
    def cant_ventas() -> tuple:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT producto.id_producto, nombre_producto, precio, categoria, COALESCE(SUM(cantidad_producto), 0) AS cant_ventas
                     FROM producto
                     LEFT JOIN orden_producto ON producto.id_producto = orden_producto.id_producto 
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

    #Funcion para ordenar la lista segun la plata generada por cada producto entre todas las ordenes
    @staticmethod
    def mas_ganancias() -> tuple:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT producto.id_producto, nombre_producto, precio, categoria, COALESCE(SUM(cantidad_producto), 0) AS cant_ventas, COALESCE(SUM(subtotal), 0) AS total
                     FROM producto
                     LEFT JOIN orden_producto ON producto.id_producto = orden_producto.id_producto 
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
    
    #Funcion para obtener los 5 productos mas caros
    @staticmethod
    def cinco_mas_caros() -> tuple:
        try:
            conn = DataBaseProductos.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM producto 
                    ORDER BY precio DESC
                    LIMIT 5"""
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
    # Funcion para eliminar un producto "DElETE"
    def eliminar_producto(id) -> bool:
        conn = DataBaseProductos.conexion()
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM producto WHERE id_producto = %s"
            cursor.execute(sql, id)
            conn.commit() 
            return True
        except Error as err:
            print(f'Hubo un error al eliminar el producto: {err}')
            return False
        finally:
            cursor.close()
            conn.close()

    #Obtener el producto mas vendido
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

        
        
    @staticmethod
    def ajustar_cantidades(producto_id: int, cantidad_maxima: int) -> int:
        conn = DataBaseProductos.conexion()
        cursor = conn.cursor()
        try:
            # Actualizar las órdenes que excedan la cantidad máxima
            sql = """
                call AjustarCantidadProducto(%s,%s)
            """
            cursor.execute(sql, (producto_id, cantidad_maxima))
            conn.commit()

            # Retornar el número de filas afectadas
            return cursor.rowcount
        except pymysql.MySQLError as e:
            print(f"Error al ajustar cantidades: {e}")
            return 0
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def verificar_producto_existe(producto_id: int) -> bool:
        """
        Verifica si un producto con el ID dado existe en la base de datos.
        parametro --> producto_id: ID del producto a verificar.
        return: True si el producto existe, False en caso contrario.
        """
        conn = DataBaseProductos.conexion()
        cursor = conn.cursor()
        try:
            sql = "SELECT COUNT(*) FROM producto WHERE id_producto = %s"
            cursor.execute(sql, (producto_id,))
            resultado = cursor.fetchone()
            return resultado[0] > 0
        except pymysql.MySQLError as e:
            print(f"Error al verificar producto: {e}")
            return False
        finally:
            cursor.close()
            conn.close()