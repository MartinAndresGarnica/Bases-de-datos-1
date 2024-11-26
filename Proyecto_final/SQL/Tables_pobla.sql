
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

DELIMITER $$

CREATE PROCEDURE InsertarOrdenes()
BEGIN
    DECLARE cliente INT DEFAULT 1;
    DECLARE orden INT DEFAULT 1;
    DECLARE contador INT;

    WHILE cliente <= 10 DO
        SET contador = 1;
        WHILE contador <= 10 DO
            INSERT INTO ORDEN (id_orden, id_cliente, fecha)
            VALUES (orden, cliente, DATE_ADD('2024-11-01 10:00:00', INTERVAL contador DAY));
            SET orden = orden + 1;
            SET contador = contador + 1;
        END WHILE;
        SET cliente = cliente + 1;
    END WHILE;
END$$

DELIMITER ;

call InsertarOrdenes()

DELIMITER $$

CREATE PROCEDURE InsertarOrdenProductos()
BEGIN
    DECLARE orden INT DEFAULT 1;
    DECLARE producto INT;
    DECLARE cantidad INT;
    DECLARE precios DECIMAL(10,2);
    DECLARE num_productos INT;
    DECLARE max_orden INT;
    DECLARE max_producto INT;
    DECLARE id_orden_producto INT DEFAULT 1;

    -- Obtener el número máximo de órdenes y productos
    SELECT MAX(id_orden) INTO max_orden FROM ORDEN;
    SELECT MAX(id_producto) INTO max_producto FROM PRODUCTO;

    -- Validar que existan datos en ambas tablas
    IF max_orden IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: La tabla ORDEN está vacía.';
    END IF;

    IF max_producto IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: La tabla PRODUCTO está vacía.';
    END IF;

    -- Recorrer las órdenes
    WHILE orden <= max_orden DO
        -- Generar un número aleatorio de productos entre 1 y 10 para esta orden
        SET num_productos = FLOOR(1 + (RAND() * 10));  -- Número de productos aleatorios (1 a 10)
        
        -- Seleccionar productos aleatorios para esta orden
        WHILE num_productos > 0 DO
            SET producto = FLOOR(1 + (RAND() * max_producto)); -- Producto aleatorio

            SET cantidad = FLOOR(1 + (RAND() * 5)); -- Cantidad aleatoria entre 1 y 5

            -- Obtener el precio del producto seleccionado
            SELECT precio INTO precios FROM PRODUCTO WHERE id_producto = producto;

            -- Validar que el precio no sea NULL
            IF precios IS NOT NULL THEN
                -- Insertar en ORDEN_PRODUCTO
                INSERT INTO ORDEN_PRODUCTO (id_orden_producto, id_producto, id_orden, cantidad_producto, subtotal)
                VALUES (id_orden_producto, producto, orden, cantidad, cantidad * precios);

                SET id_orden_producto = id_orden_producto + 1; -- Incrementar id_orden_producto
            END IF;

            SET num_productos = num_productos - 1;  -- Reducir el número de productos restantes
        END WHILE;

        SET orden = orden + 1;  -- Incrementar el índice de órdenes
    END WHILE;

    SELECT 'Procedimiento completado exitosamente' AS mensaje;
END$$

DELIMITER ;
CALL InsertarOrdenProductos()