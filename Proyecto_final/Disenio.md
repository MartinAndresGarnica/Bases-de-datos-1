# Explicacion de diseño

## Primera forma normal (1NF):

- PRODUCTO: Cada producto tiene su identificador unico id_producto, y nombre_producto, precio, descripcion, stock y categoria contienen valores atómicos.

- CLIENTE: Cada cliente tiene un identificador único id_cliente, y nombre_cliente, apellido_cliente, telefono, direccion y email contienen valores atómicos.

- ORDEN: La tabla de órdenes contiene un identificador único id_orden, una referencia a un cliente con id_cliente, y la columna fecha tiene un valor atómico (la fecha)

- ORDEN_PRODUCTO: Esta tabla es una tabla de relación entre las tablas ORDEN y PRODUCTO. Cada fila contiene un id_orden, un id_producto, la cantidad_producto y el subtotal, todos con valores atómicos.

## Segunda forma normal (2NF):

- Cumple con la primera forma normal

- PRODUCTO: La clave primaria id_producto determina de manera unica las demas columnas (id_producto, precio, descripcion, stock, categoria). No hay dependencias parciales

- CLIENTE: La clave primaria id_cliente determina de manera única las columnas nombre_cliente, apellido_cliente, telefono, direccion y email. No hay dependencias parciales.

- ORDEN: La clave primaria id_orden determina de manera única el id_cliente y la fecha. No hay dependencias parciales.

- ORDEN_PRODUCTO: La clave primaria compuesta id_orden e id_producto determina de manera única cantidad_producto y subtotal. Todos los atributos dependen completamente de la clave primaria compuesta


## Tercera forma normal (3NF):

- Cumple con la segunda forma normal

- PRODUCTO: La tabla PRODUCTO tiene solo atributos relacionados directamente con el id_producto. No hay dependencias transitivas.

- CLIENTE: En la tabla CLIENTE, el id_cliente determina directamente los atributos relacionados con el cliente. No hay dependencias transitivas.

- ORDEN: La tabla ORDEN tiene el id_orden como clave primaria y depende del id_cliente para la relacion. Ademas, la fecha depende directamente del id_orden. No hay dependencias transitivas

- ORDEN_PRDUCTO: En la tabla ORDEN_PRODUCTO, las columnas cantidad y subtotal dependen de la combinacion de id_orden y id_producto. No hay dependencias transitivas