CREATE TABLE Empleados (
		Id INT PRIMARY KEY AUTO_INCREMENT,
		Nombre VARCHAR(100) NOT NULL,
		Departamento VARCHAR(50) NOT NULL,
		Salario DECIMAL(10,2) NOT NULL
);
CREATE TABLE Ventas (
		VentaId INT PRIMARY KEY AUTO_INCREMENT,
		EmpleadoId INT,
		Monto DECIMAL(10,2) NOT NULL,
		FechaVenta DATE NOT NULL,
        FOREIGN KEY (EmpleadoId) REFERENCES Empleados(Id)
);
CREATE TABLE Bonificaciones(
		BonificacionID INT PRIMARY KEY AUTO_INCREMENT,
		EmpleadoID INT NOT NULL,
		MontoBonificacion DECIMAL(10, 2) NOT NULL,
		FechaBonificacion DATE NOT NULL,
		CONSTRAINT fk_empleado FOREIGN KEY (EmpleadoID)
		REFERENCES Empleados(Id)
);