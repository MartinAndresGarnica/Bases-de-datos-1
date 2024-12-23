import customtkinter as ctk
from secciones.GestionProductos import GestionProductos
from secciones.GestionClientes import GestionClientes
from secciones.ProcesarOrdenes import ProcesamientoOrdenes
from secciones.BusquedaAvanzada import BusquedaAvanzada
from secciones.ReporteProductos import ReporteProductoMasVendido
from secciones.ModificarValor import ModificarValor

class Menu(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.geometry('800x800')
        ctk.set_appearance_mode("dark")
        self.title('Menu')
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill='both', expand='y')
        self.widgets()
    
    def widgets(self):
        """ Contiene la logica de los botones de la pagina principal. """

        boton_Gproductos = ctk.CTkButton(
            self.frame,
            text='Gestionar productos',
            font=('Arial', 18),
            height= 80,
            command=lambda: GestionProductos(self)
        )

        boton_Gclientes = ctk.CTkButton(
            self.frame,
            text='Gestionar clientes',
            font=('Arial', 18),
            height= 80,
            command=lambda: GestionClientes(self)
        )

        boton_Gordenes = ctk.CTkButton(
            self.frame,
            text='Procesar ordenes',
            font=('Arial', 18),
            height= 80,
            command=lambda: ProcesamientoOrdenes(self)
        )

        boton_B_avanzada = ctk.CTkButton(
            self.frame,
            text='Busqueda avanzada',
            font=('Arial', 18),
            height=80,
            command=lambda: BusquedaAvanzada(self)
        )

        boton_reportes = ctk.CTkButton(
            self.frame,
            text='Producto mas vendido',
            font=('Arial', 18),
            height=80,
            command=lambda: ReporteProductoMasVendido(self)
        )

        boton_M_valor = ctk.CTkButton(
            self.frame,
            text='Modificar valor',
            font=('Arial', 18),
            height=80,
            command=lambda: ModificarValor()
        )

        #layout
        boton_Gproductos.pack( padx=80, expand=True, fill='x')
        boton_Gclientes.pack( padx=80, expand=True, fill='x')
        boton_Gordenes.pack( padx=80, expand=True, fill='x')
        boton_B_avanzada.pack( padx= 80, expand=True, fill='x')
        boton_reportes.pack(padx= 80, expand=True, fill='x')
        boton_M_valor.pack(padx= 80, expand=True, fill='x')


if __name__ == "__main__":
    app = Menu()
    app.mainloop()