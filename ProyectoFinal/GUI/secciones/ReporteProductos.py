import customtkinter as ctk
from repositorios.repositorioProductos import DataBaseProductos

class ReporteProductoMasVendido(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('400x300')  # Tamaño de la ventana emergente
        self.title('Reporte Producto Más Vendido')
        self.resizable(0, 0)
        self.grab_set()

        # Cargar los datos del producto más vendido
        producto = DataBaseProductos.producto_mas_vendido()
        if producto:
            nombre_producto = producto[0]
            cantidad_vendida = producto[1]
        else:
            nombre_producto = "No se pudo obtener el producto"
            cantidad_vendida = "0"

        # Etiquetas para mostrar los resultados
        label_titulo = ctk.CTkLabel(self, text="Producto Más Vendido", font=('Arial', 18))
        label_producto = ctk.CTkLabel(self, text=f"Producto: {nombre_producto}", font=('Arial', 16))
        label_cantidad = ctk.CTkLabel(self, text=f"Cantidad Vendida: {cantidad_vendida}", font=('Arial', 16))

        # Layout
        label_titulo.pack(pady=20)
        label_producto.pack(pady=10)
        label_cantidad.pack(pady=10)

        # Botón para cerrar la ventana
        boton_cerrar = ctk.CTkButton(self, text='Cerrar', command=self.destroy)
        boton_cerrar.pack(pady=20)
