DELIMITER $$

CREATE PROCEDURE AjustarCantidadProducto(
    IN p_id_producto INT,          -- Identificador del producto
    IN p_cantidad_maxima INT       -- Cantidad máxima permitida
)
BEGIN
    -- Validar que la cantidad máxima sea positiva
    IF p_cantidad_maxima <= 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Error: La cantidad máxima debe ser mayor que 0.';
    END IF;

    -- Actualizar las cantidades del producto y recalcular el subtotal
    UPDATE orden_producto AS op
    JOIN producto AS p ON op.id_producto = p.id_producto
    SET op.cantidad_producto = p_cantidad_maxima,
        op.subtotal = p_cantidad_maxima * p.precio
    WHERE op.id_producto = p_id_producto AND op.cantidad_producto > p_cantidad_maxima;

    -- Mensaje informativo
    SELECT CONCAT('Cantidad del producto con id_producto = ', p_id_producto, 
                  ' ajustada a un máximo de ', p_cantidad_maxima, 
                  ' en las órdenes afectadas. Subtotales actualizados.') AS mensaje;
END$$

DELIMITER ;