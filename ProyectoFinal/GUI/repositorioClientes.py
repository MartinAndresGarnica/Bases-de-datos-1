import pymysql
from pymysql.err import Error

class DataBaseClientes:

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

    #Funcion para cargar los clientes
    @staticmethod
    def cargarClientes() -> tuple:
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql= "SELECT * FROM cliente;"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Error en la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()

    # Funcion para agregar un nuevo Cliente  "CREATE"
    @staticmethod
    def agregar_cliente(nombre,apellido,direccion,telefono,email) -> bool:
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
    
    # Funcion para mostrar clientes por id "READ"
    @staticmethod    
    def mostrar_cliente_por_id(id) -> tuple:
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = f"SELECT * FROM cliente WHERE id={id}"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Error en la consulta {err}')
            return []
        finally:
            cursor.close()
            conn.close()
            
    # Funcion para actualizar datos de un cliente "UPDATE"
    @staticmethod
    def actualizar_cliente(id,nombre,apellido,direccion,telefono,email) -> bool:
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

    #Funcion para ordenar la lista por nombre
    @staticmethod
    def ordenar_por_nombre() -> tuple:
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
    
    #Funcion para ordenar la lista por apellido
    @staticmethod
    def ordenar_por_apellido() -> tuple:
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

    #Funcion para ordenar la tabla por telefono
    @staticmethod
    def ordenar_por_telefono() -> tuple:
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

    #Funcion para ordenar la tabla por direccion (Alfabeticamente)
    @staticmethod
    def ordenar_por_direccion() -> tuple:
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
    
    #Funcion para ordenar la tabla por email (Alfabeticamente)
    @staticmethod
    def ordenar_por_email() -> tuple:
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

    #Funcion para obtener la cantidad de compras que realizo cada cliente
    @staticmethod
    def cantidad_compras() -> tuple:
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = """SELECT cliente.id_cliente, nombre_cliente, apellido_cliente, COUNT(orden.id_cliente) AS cant_compras
                     FROM cliente
                     LEFT JOIN orden ON cliente.id_cliente = orden.id_cliente 
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

    #Funcion para obtener la suma total de lo que gasto cada cliente
    @staticmethod
    def dinero_gastado() -> tuple:
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            #La funcion COALESCE te devuelve el primer valor no nulo, por ende si ponemos COALESCE(SUM(SUBTOTAL), 0) cuando el cliente no tenga compras y subtotal sea null va a devolver 0.
            sql = """SELECT cliente.id_cliente, nombre_cliente, apellido_cliente, COALESCE(SUM(subtotal), 0) AS dinero_gastado  
                     FROM cliente
                     LEFT JOIN orden ON cliente.id_cliente = orden.id_cliente
                     LEFT JOIN orden_producto ON orden.id_orden = orden_producto.id_orden
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
    def eliminar_cliente(id) -> bool:
        conn = DataBaseClientes.conexion()
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM cliente WHERE id_cliente=%s"
            cursor.execute(sql, id)
            conn.commit()
            return True
        except Error as err:
            print(f'Hubo un error al eliminar el cliente: {err}')
            return False
        finally:
            cursor.close()
            conn.close()

    #Funcion para obtener los clientes que hicieron menos de 10 compras
    @staticmethod
    def clientes_menos_diez() -> tuple:
        try:
            conn = DataBaseClientes.conexion()
            cursor = conn.cursor()
            sql = """SELECT cliente.id_cliente, nombre_cliente, apellido_cliente, COUNT(orden.id_cliente) AS cant_compras
                     FROM cliente
                     LEFT JOIN orden ON cliente.id_cliente = orden.id_cliente 
                     GROUP BY id_cliente
                     HAVING cant_compras < 10
                     ORDER BY cant_compras DESC;"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f'Ocurrio un error con la consulta: {err}')
            return []
        finally:
            cursor.close()
            conn.close()
