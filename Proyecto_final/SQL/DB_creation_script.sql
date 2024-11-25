DROP DATABASE IF exists sist_ventas;
Create DATABASE sist_ventas;
USE sist_ventas;

CREATE TABLE PRODUCTO (
	id_producto int primary key,
    nombre_producto varchar(255) NOT NULL,
    precio decimal (10,2) NOT NULL CHECK(precio>0),
    descripcion varchar(255),
    stock int NOT NULL CHECK(stock>0),
    categoria varchar(255) NOT NULL
);

CREATE TABLE CLIENTE (
	id_cliente int primary key,
    nombre_cliente varchar(255) NOT NULL,
    apellido_cliente varchar(255) NOT NULL,
    telefono varchar(20) NOT NULL UNIQUE ,
    direccion varchar(255),
    email varchar(255) NOT NULL UNIQUE
);

CREATE TABLE ORDEN (
	id_orden int primary key,
    id_cliente int NOT NULL,
    fecha datetime NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente)
		ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE ORDEN_PRODUCTO (
	id_orden_producto int primary key,
    id_producto int NOT NULL,
    id_orden int NOT NULL,
    cantidad_producto int NOT NULL CHECK (cantidad_producto > 0),
    subtotal decimal NOT NULL CHECK (subtotal >= 0),
    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto)
		ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_orden) REFERENCES ORDEN(id_orden)
		ON DELETE CASCADE ON UPDATE CASCADE
);