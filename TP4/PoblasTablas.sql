INSERT INTO Empleados (Nombre, Departamento, Salario) VALUES 
		('Juan Pérez', 'Ventas', 50000.00),
		('María García', 'Marketing', 55000.00),
		('Carlos Sánchez', 'Ventas', 52000.00),
		('Ana López', 'IT', 60000.00),
		('Lucía Fernández', 'Ventas', 48000.00),
		('David Martínez', 'IT', 65000.00),
		('Laura Gómez', 'Marketing', 58000.00),
		('Fernando Torres', 'Ventas', 49000.00),
		('Gabriela Ruiz', 'IT', 72000.00),
		('Sofía Ortega', 'Marketing', 57000.00),
		('Pedro Jiménez', 'Ventas', 51000.00),
		('Claudia Morales', 'Ventas', 53000.00),
		('Andrés Romero', 'IT', 60000.00),
		('Valeria Soto', 'Marketing', 55000.00),
		('Javier Cruz', 'Ventas', 52000.00),
		('Cristina Díaz', 'IT', 64000.00),
		('Diego Ríos', 'Marketing', 59000.00),
		('Esteban Cordero', 'Ventas', 45000.00),
		('Patricia Salazar', 'IT', 67000.00),
		('Ricardo Medina', 'Ventas', 48000.00),
		('Vanessa Aguirre', 'Marketing', 56000.00);
        
INSERT INTO Ventas (EmpleadoId, Monto, FechaVenta) VALUES 
		(1, 1500.00, '2024-10-01'),  -- Juan Pérez
		(1, 2300.00, '2024-10-15'),  -- Juan Pérez
		(2, 1200.00, '2024-10-07'),  -- María García
		(3, 2500.00, '2024-09-10'),  -- Carlos Sánchez (fuera del mes)
		(4, 1750.00, '2024-10-05'),  -- Ana López
		(5, 1100.00, '2024-09-03'),  -- Lucía Fernández (fuera del mes)
		(6, 3000.00, '2024-10-12'),  -- David Martínez
		(7, 1400.00, '2024-10-14'),  -- Laura Gómez
		(8, 1800.00, '2024-10-11'),  -- Fernando Torres
		(9, 2000.00, '2024-09-09'),  -- Gabriela Ruiz (fuera del mes)
		(10, 2200.00, '2024-10-16'),  -- Sofía Ortega
		(11, 1600.00, '2024-10-20'),  -- Pedro Jiménez
		(12, 2400.00, '2024-09-25'),  -- Claudia Morales (fuera del mes)
		(13, 1900.00, '2024-10-21'),  -- Andrés Romero
		(14, 1700.00, '2024-10-22'),  -- Valeria Soto
		(15, 1300.00, '2024-09-23'),  -- Javier Cruz (fuera del mes)
		(16, 1500.00, '2024-10-24'),  -- Cristina Díaz
		(17, 2100.00, '2024-10-26'),  -- Esteban Cordero
		(18, 2400.00, '2024-09-27'),  -- Patricia Salazar (fuera del mes)
		(19, 2500.00, '2024-10-28'),  -- Ricardo Medina
		(20, 2300.00, '2024-09-29');  -- Vanessa Aguirre