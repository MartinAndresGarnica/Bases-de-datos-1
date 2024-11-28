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
    def actualizar_cliente(id,nombre,apellido,direccion,telefono,email):
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql= "UPDATE cliente SET nombre_cliente = %s, apellido_cliente= %s, direccion = %s, telefono = %s, email = %s WHERE id_cliente=%s"
            valores=(nombre,apellido,direccion,telefono,email, id)
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
    def ordenar_por_nombre():
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM cliente 
                    ORDER BY nombre_cliente ASC"""
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
    def ordenar_por_apellido():
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM cliente 
                    ORDER BY apellido_cliente ASC"""
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
    def ordenar_por_telefono():
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM cliente 
                    ORDER BY telefono ASC"""
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
    def ordenar_por_direccion():
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM cliente 
                    ORDER BY direccion ASC"""
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
    def ordenar_por_email():
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = """SELECT * FROM cliente 
                    ORDER BY email ASC"""
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
    def cantidad_compras():
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = """SELECT cliente.id_cliente, nombre_cliente, apellido_cliente, COUNT(orden.id_cliente) AS cant_compras
                     FROM cliente
                     JOIN orden ON cliente.id_cliente = orden.id_cliente 
                     GROUP BY id_cliente
                     ORDER BY cant_compras DESC"""
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
    def dinero_gastado():
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = """SELECT cliente.id_cliente, nombre_cliente, apellido_cliente, SUM(subtotal) AS dinero_gastado
                     FROM cliente
                     JOIN orden ON cliente.id_cliente = orden.id_cliente
                     JOIN orden_producto ON orden.id_orden = orden_producto.id_orden
                     GROUP BY id_cliente
                     ORDER BY dinero_gastado DESC"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()

    
    
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
        