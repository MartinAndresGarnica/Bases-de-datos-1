DELIMITER $$
-- Creamos el procedimiento para calcular los beneficios
CREATE PROCEDURE CalcularBonificaciones()
BEGIN
	-- Variables 
	DECLARE EmpleadoIDV INT;
	DECLARE MontoTotalv DECIMAL(10, 2);
	DECLARE Bonificacion DECIMAL(10, 2);
	DECLARE MesAnterior DATE;
	DECLARE Umbral DECIMAL(10, 2);
	DECLARE done INT DEFAULT FALSE;
    
    -- Creamos el cursor
    DECLARE cursor_bonificaciones CURSOR FOR 
	SELECT EmpleadoId, SUM(Monto) AS MontoTotal
	FROM Empleados 
	JOIN Ventas ON Empleados.Id = Ventas.EmpleadoId
	WHERE Ventas.FechaVenta >= DATE_SUB(CURDATE(),INTERVAL 1 month) -- En esta parte se puede poner una fecha estatica para hacer la prueba de los datos por ejemplo WHERE Ventas.FechaVenta >= '20240928' (Suponiendo que la fecha actual es 28/10/2024)
    GROUP BY EmpleadoId;
	
    -- Handler para determinar si no hay mas elementos 
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- Le asigno valores a las variables
	SET Umbral = 2200;
	SET Bonificacion = 0;
	
    -- Abrimos el cursor
	OPEN cursor_bonificaciones;
		
        -- Tomamos los datos del cursor y los almacenamos en la variables correspondientes (Este comando lo volvemos a repetir dentro del bucle de abajo para que tome los datos del siguiente empleado)
		FETCH cursor_bonificaciones INTO EmpleadoIDV, MontoTotalv;
		
        -- Iniciamos el bucle para que aplique la condicion a cada empleado
		WHILE NOT done DO
			IF MontoTotalv >= Umbral THEN
				BEGIN
					-- Seteamos la bonificacion adicional
					SET Bonificacion = MontoTotalv * 0.10; -- Seteamos la bonificacion adicional
					SET MontoTotalv = MontoTotalv + Bonificacion; -- Le sumamos la bonificacion al sueldo
					INSERT INTO Bonificaciones (EmpleadoID, MontoBonificacion, FechaBonificacion) 
					VALUES (EmpleadoIDV, Bonificacion, CURDATE()); -- Le insertamos los datos en la tabla de bonificaciones
					UPDATE Empleados SET Salario = MontoTotalv WHERE Id = EmpleadoIDV; -- Actualizamos el salario del empleado que recibe la bonificacion
				END;
			END IF;
            
            -- Aca repetimos el comando 
            FETCH cursor_bonificaciones INTO EmpleadoIDV, MontoTotalv;
		END WHILE;
			
	CLOSE cursor_bonificaciones;

END$$
DELIMITER ;