
-- Insercion de productos
INSERT INTO PRODUCTO (nombre_producto, precio, descripcion, stock, categoria) VALUES
('Laptop', 1500.00, 'Laptop de alta gama', 10, 'Electrónica'),
('Auriculares', 50.00, 'Auriculares inalámbricos', 20, 'Accesorios'),
('Monitor', 300.00, 'Monitor Full HD 24 pulgadas', 15, 'Electrónica'),
('Teclado Mecánico', 80.00, 'Teclado con retroiluminación RGB', 25, 'Accesorios'),
('Mouse', 25.00, 'Mouse inalámbrico ergonómico', 30, 'Accesorios'),
('Cámara Web', 70.00, 'Cámara Full HD con micrófono', 18, 'Electrónica'),
('Disco SSD', 100.00, 'SSD 1TB', 12, 'Almacenamiento'),
('Impresora', 200.00, 'Impresora multifuncional', 8, 'Electrónica'),
('Altavoces', 120.00, 'Altavoces Bluetooth portátiles', 14, 'Audio'),
('Tablet', 400.00, 'Tablet con pantalla de 10 pulgadas', 10, 'Electrónica');

-- Insercion de clientes
INSERT INTO CLIENTE (nombre_cliente, apellido_cliente, telefono, direccion, email) VALUES
('Juan', 'Pérez', '1234567890', 'Calle A 123', 'juan.perez@example.com'),
('María', 'Gómez', '1234567891', 'Calle B 456', 'maria.gomez@example.com'),
('Pedro', 'Rodríguez', '1234567892', 'Calle C 789', 'pedro.rodriguez@example.com'),
('Ana', 'Martínez', '1234567893', 'Calle D 101', 'ana.martinez@example.com'),
('Luis', 'López', '1234567894', 'Calle E 202', 'luis.lopez@example.com'),
('Carmen', 'Hernández', '1234567895', 'Calle F 303', 'carmen.hernandez@example.com'),
('Jorge', 'Sánchez', '1234567896', 'Calle G 404', 'jorge.sanchez@example.com'),
('Sofía', 'Ramírez', '1234567897', 'Calle H 505', 'sofia.ramirez@example.com'),
('Carlos', 'Torres', '1234567898', 'Calle I 606', 'carlos.torres@example.com'),
('Elena', 'Ruiz', '1234567899', 'Calle J 707', 'elena.ruiz@example.com');

DELIMITER $$

CREATE PROCEDURE InsertarOrdenes()
BEGIN
    DECLARE cliente INT DEFAULT 1;
    DECLARE orden INT DEFAULT 1;
    DECLARE contador INT;

    WHILE cliente <= 10 DO
        SET contador = 1;
        WHILE contador <= 10 DO
            INSERT INTO ORDEN (id_cliente, fecha)
            VALUES (cliente, DATE_ADD('2024-11-01 10:00:00', INTERVAL contador DAY));
            SET contador = contador + 1;
        END WHILE;
        SET cliente = cliente + 1;
    END WHILE;
END$$

DELIMITER ;


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
                -- Comprobar si ya existe este producto en esta orden
                IF NOT EXISTS (SELECT 1 FROM ORDEN_PRODUCTO WHERE id_orden = orden AND id_producto = producto) THEN
                    -- Insertar en ORDEN_PRODUCTO
                    INSERT INTO ORDEN_PRODUCTO (id_producto, id_orden, cantidad_producto, subtotal)
                    VALUES (producto, orden, cantidad, cantidad * precios);
                END IF;
            END IF;

            SET num_productos = num_productos - 1;  -- Reducir el número de productos restantes
        END WHILE;

        SET orden = orden + 1;  -- Incrementar el índice de órdenes
    END WHILE;

    SELECT 'Procedimiento completado exitosamente' AS mensaje;
END$$

DELIMITER ;

CALL InsertarOrdenes();
CALL InsertarOrdenProductos()