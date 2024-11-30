import customtkinter as ctk
from tkinter import ttk
from repositorios.repositorioClientes import DataBaseClientes
from repositorios.repositorioProductos import DataBaseProductos

class BusquedaAvanzada(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('1280x720')
        self.title('Busqueda avanzada')
        self.resizable(1920, 1080)
        self.grab_set()                         #Hace que la nueva ventana tenga prioridad y no se puedan clickear las demas ventanas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        #Frames
        self.navbarFrame = ctk.CTkFrame(self) #Este frame es el que se encuentra primero, es el que contiene el boton de volver (de izquierda a derecha)
        self.frame_filtros = ctk.CTkFrame(self, fg_color='#2b2a2a') #Este frame tiene los widgets para agregar Ordenes
        self.tablas = ctk.CTkFrame(self) #Este frame tiene los widgets de la tabla

        #Layout general
        self.navbarFrame.pack(side='left', fill='y')
        self.frame_filtros.pack(side='left', fill='both')
        self.tablas.pack(side='left', expand=True, fill='both')


        #Encabezados
        self.encabezados = []

        #Menu
        Menu = ctk.CTkOptionMenu(self.frame_filtros, values=['Producto', 'Clientes'], command= self.tabla)
        Menu.pack(pady=(40, 0))

        #Llamar a las funciones
        self.navbar()
        self.filtros()
        self.tabla()

    def navbar(self):
        #widgets
        boton_volver = ctk.CTkButton(self.navbarFrame, text='<-', font=('Arial', 18), command=self.destroy, width=30, height=30, fg_color='#2b2a2a')

        #layout
        boton_volver.pack()


    def filtros(self, *args):
        """ Es el frame que maneja la logica de agregar Ordenes. """

        for widget in self.frame_filtros.winfo_children():
            if not isinstance(widget, ctk.CTkOptionMenu):
                widget.destroy()

        frame_botones = ctk.CTkFrame(self.frame_filtros)
        frame_botones.pack()


        if 'Clientes' in args:
            boton_tablaPrincipal = ctk.CTkButton(frame_botones, text='Quitar filtro', font=('Arial', 18), width=180, height=40, command=lambda: self.tabla('Clientes'))
            boton_masCompras = ctk.CTkButton(frame_botones, text='Cantidad de compras', font=('Arial', 18), width=180, height=40, command=lambda: self.tabla('Clientes', 'CantCompras'))
            boton_dineroGastado = ctk.CTkButton(frame_botones, text='Dinero gastado', font=('Arial', 18), width=180, height=40, command=lambda: self.tabla('Clientes', 'DineroGastado'))
            boton_menor_diez = ctk.CTkButton(frame_botones, text='Menos de 10 compras', font=('Arial', 18), width=180, height=40, command=lambda: self.tabla('Clientes', 'CantCompras', 'menor_10'))


            boton_tablaPrincipal.pack(padx = 15, pady = 30)
            boton_masCompras.pack(padx = 15, pady= 10)
            boton_dineroGastado.pack(padx = 15 , pady = 10)
            boton_menor_diez.pack(padx= 15, pady = 10)
        else:

            boton_tablaPrincipal = ctk.CTkButton(frame_botones, text='Quitar filtro', font=('Arial', 18), width=180, height=40, command= self.tabla)
            boton_masVendido = ctk.CTkButton(frame_botones, text='Productos mas vendidos', font=('Arial', 18), width=180, height=40, command=lambda: self.tabla('MasVendido'))
            boton_masGanancia = ctk.CTkButton(frame_botones, text='Mayor recaudacion', font=('Arial', 18), width=180, height=40, command=lambda: self.tabla('MasGanancia'))
            boton_cinco_mas_caros = ctk.CTkButton(frame_botones, text='5 mas caros', font=('Arial', 18), width=180, height=40, command=lambda: self.tabla('cinco_mas_caros'))
            

            boton_tablaPrincipal.pack(padx = 15, pady = 30)
            boton_masVendido.pack(padx = 15, pady= 10)
            boton_masGanancia.pack(padx = 15 , pady = 10)
            boton_cinco_mas_caros.pack(padx = 15, pady= 10)


    def ajustar_columnas(self, event):
        """Ajustar dinámicamente las columnas al tamaño del Treeview."""
        tabla = event.widget  # Treeview que activó el evento
        ancho_total = tabla.winfo_width()  # Ancho total disponible
        numero_columnas = len(tabla["columns"])  # Número de columnas
        ancho_columna = ancho_total // numero_columnas  # Ancho promedio por columna

        for columna in tabla["columns"]:
            tabla.column(columna, width=ancho_columna, anchor='c')


    def tabla(self, *args):
        
        for widget in self.tablas.winfo_children():
            widget.destroy()

        #Crea un estilo para los encabezados
        estiloEncabezados = ttk.Style()
        estiloEncabezados.theme_use("default")  # Cambia el estilo base
        estiloEncabezados.configure("Treeview.Heading", background="#2b2a2a", foreground="white", fieldbackground="#2a2d2e", font=('Arial', 18))
        
        #Crea un estilo para la tabla
        estiloTabla = ttk.Style()
        estiloTabla.theme_use("default")  # Cambia el estilo base
        estiloTabla.configure("Treeview", background="#2b2a2a", foreground="white", fieldbackground="#2a2d2e", rowheight=40, font=('Arial', 12))


        if 'Clientes' in args:
            self.filtros('Clientes')
            if 'ID_cliente' in args:
                self.lista = DataBaseClientes.cargarClientes()
            elif 'Nombre' in args:
                self.lista = DataBaseClientes.ordenar_por_nombre()
            elif 'Apellido' in args:
                self.lista = DataBaseClientes.ordenar_por_apellido()
            elif 'Telefono' in args:
                self.lista = DataBaseClientes.ordenar_por_telefono()
            elif 'Direccion' in args:
                self.lista = DataBaseClientes.ordenar_por_direccion()
            elif 'Mail' in args:
                self.lista = DataBaseClientes.ordenar_por_email()
            else:
                self.lista = DataBaseClientes.cargarClientes()

            if 'CantCompras' in args:
                if 'menor_10' in args:
                    self.lista = DataBaseClientes.clientes_menos_diez()
                else:
                    self.lista = DataBaseClientes.cantidad_compras()
                #Crea la tabla
                tabla = ttk.Treeview(self.tablas, columns=("ID_cliente", "Nombre", "Apellido", "Compras"), show="headings")

                tabla.heading("ID_cliente", text='ID cliente')
                tabla.heading("Nombre", text='Nombre')
                tabla.heading("Apellido", text='Apellido')
                tabla.heading("Compras", text='Compras realizadas')

                #Configura las columnas para ajustarse dinamicamente
                tabla.bind("<Configure>", self.ajustar_columnas)
                

                #Inserta los datos en la tabla y les pone un tag para poder agregarle el color segun sea par o impar
                for indice, orden in enumerate(self.lista):
                    if indice % 2 == 0:
                        tabla.insert("", "end", values=orden, tags='Par')
                    else:
                        tabla.insert("", "end", values=orden, tags='Impar')
            
            elif 'DineroGastado' in args:

                self.lista = DataBaseClientes.dinero_gastado()
                list(self.lista)
                print(self.lista)
                #Crea la tabla
                tabla = ttk.Treeview(self.tablas, columns=("ID_cliente", "Nombre", "Apellido", "Dinero"), show="headings")

                tabla.heading("ID_cliente", text='ID cliente')
                tabla.heading("Nombre", text='Nombre')
                tabla.heading("Apellido", text='Apellido')
                tabla.heading("Dinero", text='Monto total gastado')

                #Configura las columnas para ajustarse dinamicamente
                tabla.bind("<Configure>", self.ajustar_columnas)
                

                #Inserta los datos en la tabla y les pone un tag para poder agregarle el color segun sea par o impar
                for indice, orden in enumerate(self.lista):
                    if indice % 2 == 0:
                        tabla.insert("", "end", values=orden, tags='Par')
                    else:
                        tabla.insert("", "end", values=orden, tags='Impar')

            else:
                #Crea la tabla
                tabla = ttk.Treeview(self.tablas, columns=("ID_cliente", "Nombre", "Apellido", "Telefono", "Direccion", "Mail"), show="headings")

                tabla.heading("ID_cliente", text='ID cliente', command=lambda: self.tabla('Clientes', 'ID_cliente'))
                tabla.heading("Nombre", text='Nombre', command=lambda: self.tabla('Clientes', 'Nombre'))
                tabla.heading("Apellido", text='Apellido',command=lambda: self.tabla('Clientes', 'Apellido'))
                tabla.heading("Telefono", text='Telefono', command=lambda: self.tabla('Clientes', 'Telefono'))
                tabla.heading("Direccion", text='Direccion', command=lambda: self.tabla('Clientes', 'Direccion'))
                tabla.heading("Mail", text='Mail', command=lambda: self.tabla('Clientes', 'Mail'))

                #Configura las columnas para ajustarse dinamicamente
                tabla.bind("<Configure>", self.ajustar_columnas)
                

                #Inserta los datos en la tabla y les pone un tag para poder agregarle el color segun sea par o impar
                for indice, orden in enumerate(self.lista):
                    if indice % 2 == 0:
                        tabla.insert("", "end", values=orden, tags='Par')
                    else:
                        tabla.insert("", "end", values=orden, tags='Impar')
        else:
            self.filtros()
            if 'Nombre' in args:
                self.lista = DataBaseProductos.ordenar_por_nombre()
            elif 'Precio' in args:
                self.lista = DataBaseProductos.ordenar_por_precio()
            elif 'Descripcion' in args:
                self.lista = DataBaseProductos.ordenar_por_descripcion()
            elif 'Stock' in args:
                self.lista = DataBaseProductos.ordenar_por_stock()
            elif 'Categoria' in args:
                self.lista = DataBaseProductos.ordenar_por_categoria()
            else:
                self.lista = DataBaseProductos.cargarProductos()
            
            
            if 'MasVendido' in args:
                self.lista = DataBaseProductos.cant_ventas()
                tabla = ttk.Treeview(self.tablas, columns=("ID_producto", "Nombre", "Precio", "Categoria", "Cantidad_vendida"), show="headings")
                tabla.heading("ID_producto", text='ID')
                tabla.heading("Nombre", text='Nombre')
                tabla.heading("Precio", text='Precio')
                tabla.heading("Categoria", text='Categoria')
                tabla.heading("Cantidad_vendida", text='Cantidad vendida')

                #Configura las columnas para ajustarse dinamicamente
                tabla.bind("<Configure>", self.ajustar_columnas)
                tabla.column("ID_producto", width=60, anchor='c')
                

                #Inserta los datos en la tabla y les pone un tag para poder agregarle el color segun sea par o impar
                for indice, orden in enumerate(self.lista):
                    if indice % 2 == 0:
                        tabla.insert("", "end", values=orden, tags='Par')
                    else:
                        tabla.insert("", "end", values=orden, tags='Impar')
            
            elif 'MasGanancia' in args:
                self.lista = DataBaseProductos.mas_ganancias()
                tabla = ttk.Treeview(self.tablas, columns=("ID_producto", "Nombre", "Precio", "Categoria", "Cantidad_vendida", "Total"), show="headings")
                tabla.heading("ID_producto", text='ID')
                tabla.heading("Nombre", text='Nombre')
                tabla.heading("Precio", text='Precio')
                tabla.heading("Categoria", text='Categoria')
                tabla.heading("Cantidad_vendida", text='Vendidos')
                tabla.heading("Total", text='Total')

                #Configura las columnas para ajustarse dinamicamente
                tabla.bind("<Configure>", self.ajustar_columnas)
                tabla.column("ID_producto", width=60, anchor='c')
                

                #Inserta los datos en la tabla y les pone un tag para poder agregarle el color segun sea par o impar
                for indice, orden in enumerate(self.lista):
                    if indice % 2 == 0:
                        tabla.insert("", "end", values=orden, tags='Par')
                    else:
                        tabla.insert("", "end", values=orden, tags='Impar')

            else:
                if 'cinco_mas_caros' in args:
                    self.lista = DataBaseProductos.cinco_mas_caros()

                tabla = ttk.Treeview(self.tablas, columns=("ID_producto", "Nombre", "Precio", "Descripcion","Stock", "Categoria"), show="headings")
                tabla.heading("ID_producto", text='ID', command= self.tabla)
                tabla.heading("Nombre", text='Nombre', command=lambda: self.tabla('Nombre'))
                tabla.heading("Precio", text='Precio', command=lambda: self.tabla('Precio'))
                tabla.heading("Descripcion", text='Descripcion', command=lambda: self.tabla('Descripcion'))
                tabla.heading("Stock", text='Stock', command=lambda: self.tabla('Stock'))
                tabla.heading("Categoria", text='Categoria', command=lambda: self.tabla('Categoria'))

                #Configura las columnas para ajustarse dinamicamente
                tabla.bind("<Configure>", self.ajustar_columnas)
                tabla.column("ID_producto", width=60, anchor='c')
                

                #Inserta los datos en la tabla y les pone un tag para poder agregarle el color segun sea par o impar
                for indice, orden in enumerate(self.lista):
                    if indice % 2 == 0:
                        tabla.insert("", "end", values=orden, tags='Par')
                    else:
                        tabla.insert("", "end", values=orden, tags='Impar')

        #Asignamos colores segun su tag
        tabla.tag_configure('Par', background='#5d5d5d')
        tabla.tag_configure('Impar', background='#3d3d3d')

        #Layout
        tabla.pack(expand=True, fill='both')