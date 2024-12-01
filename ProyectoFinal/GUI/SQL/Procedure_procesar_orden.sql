-- Procedimiento para agregar una orden si tiene stock suficiente
DELIMITER $$

CREATE PROCEDURE ProcesarOrden(cliente_id INT, producto_id INT, cantidad INT) 
BEGIN
	
	DECLARE stock_actual INT;
    DECLARE orden_id INT;

    
	START TRANSACTION;
    IF EXISTS (SELECT id_cliente FROM CLIENTE WHERE id_cliente = cliente_id) AND EXISTS (SELECT id_producto FROM PRODUCTO WHERE id_producto = producto_id) then
    
		SELECT stock INTO stock_actual FROM PRODUCTO WHERE id_producto = producto_id;
		
		IF stock_actual >= cantidad THEN
		
			INSERT INTO ORDEN (id_cliente, fecha) VALUES (cliente_id, NOW());
			SET orden_id = LAST_INSERT_ID();
			
			INSERT INTO ORDEN_PRODUCTO (id_producto, id_orden, cantidad_producto, subtotal)
			VALUES (producto_id, orden_id, cantidad, cantidad*(SELECT precio FROM PRODUCTO WHERE id_producto = producto_id));
			
			UPDATE PRODUCTO
			SET stock = stock - cantidad
			WHERE id_producto = producto_id;
			
			COMMIT;
			
		ELSE
		
			ROLLBACK;
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: Stock insuficiente para generar la orden';
			
		END IF;    
	ELSE
		ROLLBACK;
        SIGNAL sqlstate '45000' SET MESSAGE_TEXT = 'ERROR: El cliente o producto no existe';
    END IF;
END$$

DELIMITER ;
