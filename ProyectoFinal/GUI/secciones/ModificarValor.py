import customtkinter as ctk
import CTkMessagebox
from repositorios.repositorioProductos import DataBaseProductos


class ModificarValor(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('400x300')
        self.title('Modificar Cantidad Máxima')
        self.resizable(0, 0)
        self.grab_set()

        self.producto_id = ctk.IntVar()
        self.cantidad_maxima = ctk.IntVar()

        label_titulo = ctk.CTkLabel(self, text="Modificar Órdenes", font=('Arial', 18))
        label_producto_id = ctk.CTkLabel(self, text="ID del Producto:", font=('Arial', 14))
        entry_producto_id = ctk.CTkEntry(self, textvariable=self.producto_id)

        label_cantidad_maxima = ctk.CTkLabel(self, text="Cantidad Máxima:", font=('Arial', 14))
        entry_cantidad_maxima = ctk.CTkEntry(self, textvariable=self.cantidad_maxima)

        boton_modificar = ctk.CTkButton(
            self, 
            text="Aplicar Cambios", 
            command=self.aplicar_cambios
        )

        label_titulo.pack(pady=20)
        label_producto_id.pack(pady=5)
        entry_producto_id.pack(pady=5)
        label_cantidad_maxima.pack(pady=5)
        entry_cantidad_maxima.pack(pady=5)
        boton_modificar.pack(pady=20)

    def aplicar_cambios(self):
        # Obtener valores
        producto_id = self.producto_id.get()
        cantidad_maxima = self.cantidad_maxima.get()

        if producto_id <= 0 or cantidad_maxima <= 0:
            CTkMessagebox.CTkMessagebox(title="Error", message="Ingrese valores válidos.")
            return

        # Verificar si el producto existe
        if not DataBaseProductos.verificar_producto_existe(producto_id):
            CTkMessagebox.CTkMessagebox(
                title="Error", 
                message=f"El producto con ID {producto_id} no existe en la base de datos."
            )
            return

        # Llamar a la función del repositorio para ajustar las cantidades
        filas_afectadas = DataBaseProductos.ajustar_cantidades(producto_id, cantidad_maxima)

        if filas_afectadas > 0:
            CTkMessagebox.CTkMessagebox(
                title="Operación Exitosa", 
                message=f"Se ajustaron {filas_afectadas} órdenes."
            )
        else:
            CTkMessagebox.CTkMessagebox(
                title="Sin Cambios", 
                message="No se encontraron órdenes para modificar."
            )

        self.destroy()

