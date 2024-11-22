import tkinter as tk

class Menu:
    def __init__(self) -> None:
        self.__root = tk.Tk()
        self.__root.geometry("600x600") #Setea el tamanio de la pestania
        self.__root.title('Sistema de ventas')
        self.__frame = tk.Frame()                                                                      
        self.__frame.pack(fill= 'both', expand=True)

        self.widgets()

        #Paleta de colores #602433

    def mainloop(self):
        self.__root.mainloop()

    def widgets(self):
        """ Contiene la logica de los botones de la pagina principal. """

        gestionar_productos = tk.Button(self.__frame, text='Gestionar productos', font=('Arial', 18), bg='#d06489', fg='#f3d7e3', activebackground='#a23451', activeforeground='#f3d7e3', command=GestionProductos) #Crud productos
        gestionar_productos.pack( expand= True, fill='both')

        gestionar_clientes = tk.Button(self.__frame, text='Gestionar clientes', font=('Arial', 18), bg='#d06489', fg='#f3d7e3', activebackground='#a23451', activeforeground='#f3d7e3') #Crud clientes
        gestionar_clientes.pack( expand= True, fill='both')

        procesar_ordenes = tk.Button(self.__frame, text='Procesar ordenes', font=('Arial', 18), bg='#d06489', fg='#f3d7e3', activebackground='#a23451', activeforeground='#f3d7e3') #Mostrar ordenes pedidas por un cliente
        procesar_ordenes.pack( expand= True, fill='both')

        busqueda_avanzada = tk.Button(self.__frame, text='Busqueda avanzada', font=('Arial', 18), bg='#d06489', fg='#f3d7e3', activebackground='#a23451', activeforeground='#f3d7e3') #Recuperar productos o clientes con filtros
        busqueda_avanzada.pack( expand= True, fill='both')

        reportes = tk.Button(self.__frame, text='Reportes', font=('Arial', 18), bg='#d06489', fg='#f3d7e3', activebackground='#a23451', activeforeground='#f3d7e3') #Reporte del producto mas vendido indicando la cantidad total pedida del mismo
        reportes.pack( expand= True, fill='both')

        modificacion_valor = tk.Button(self.__frame, text='Modificar valor de producto', font=('Arial', 18), bg='#d06489', fg='#f3d7e3', activebackground='#a23451', activeforeground='#f3d7e3')
        modificacion_valor.pack(expand= True, fill='both')


class GestionProductos(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.geometry("800x600")
        self.title('Gestión de productos')
        self.widgets()
        self.grab_set()

    def widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        frameIzquierda =tk.Frame(self)
        frameDerecha = tk.Frame(self)

        frameIzquierda.grid(row=0, column=0)
        frameDerecha.grid(row=0, column=1)

        boton1 = tk.Button(frameIzquierda, text="Hola")
        boton1.pack(expand=True, fill='x')
        boton2 = tk.Button(frameDerecha, text="Chau")
        boton2.pack()



if __name__ == "__main__":
    app = Menu()
    app.mainloop()