DROP DATABASE sist_ventas;
CREATE DATABASE sist_ventas;

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
    total decimal (10,2) NOT NULL CHECK (total >= 0),
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

-- Insercion de productos
INSERT INTO PRODUCTO (id_producto, nombre_producto, precio, descripcion, stock, categoria) VALUES
(1, 'Laptop', 1500.00, 'Laptop de alta gama', 10, 'Electrónica'),
(2, 'Auriculares', 50.00, 'Auriculares inalámbricos', 20, 'Accesorios'),
(3, 'Monitor', 300.00, 'Monitor Full HD 24 pulgadas', 15, 'Electrónica'),
(4, 'Teclado Mecánico', 80.00, 'Teclado con retroiluminación RGB', 25, 'Accesorios'),
(5, 'Mouse', 25.00, 'Mouse inalámbrico ergonómico', 30, 'Accesorios'),
(6, 'Cámara Web', 70.00, 'Cámara Full HD con micrófono', 18, 'Electrónica'),
(7, 'Disco SSD', 100.00, 'SSD 1TB', 12, 'Almacenamiento'),
(8, 'Impresora', 200.00, 'Impresora multifuncional', 8, 'Electrónica'),
(9, 'Altavoces', 120.00, 'Altavoces Bluetooth portátiles', 14, 'Audio'),
(10, 'Tablet', 400.00, 'Tablet con pantalla de 10 pulgadas', 10, 'Electrónica');

-- Insercion de clientes
INSERT INTO CLIENTE (id_cliente, nombre_cliente, apellido_cliente, telefono, direccion, email) VALUES
(1, 'Juan', 'Pérez', '1234567890', 'Calle A 123', 'juan.perez@example.com'),
(2, 'María', 'Gómez', '1234567891', 'Calle B 456', 'maria.gomez@example.com'),
(3, 'Pedro', 'Rodríguez', '1234567892', 'Calle C 789', 'pedro.rodriguez@example.com'),
(4, 'Ana', 'Martínez', '1234567893', 'Calle D 101', 'ana.martinez@example.com'),
(5, 'Luis', 'López', '1234567894', 'Calle E 202', 'luis.lopez@example.com'),
(6, 'Carmen', 'Hernández', '1234567895', 'Calle F 303', 'carmen.hernandez@example.com'),
(7, 'Jorge', 'Sánchez', '1234567896', 'Calle G 404', 'jorge.sanchez@example.com'),
(8, 'Sofía', 'Ramírez', '1234567897', 'Calle H 505', 'sofia.ramirez@example.com'),
(9, 'Carlos', 'Torres', '1234567898', 'Calle I 606', 'carlos.torres@example.com'),
(10, 'Elena', 'Ruiz', '1234567899', 'Calle J 707', 'elena.ruiz@example.com');
