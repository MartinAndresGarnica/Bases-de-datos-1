import customtkinter as ctk

class GestionProductos(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('1280x720')
        self.title('Gestion de productos')
        self.grab_set()                         #Hace que la nueva ventana tenga prioridad y no se puedan clickear las demas ventanas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.navbarFrame = ctk.CTkFrame(self)
        self.agregarProductos = ctk.CTkFrame(self)
        self.tablaProductos = ctk.CTkFrame(self)

        #layout
        self.navbarFrame.pack(side='left', fill='y')
        self.agregarProductos.pack(side='left', fill='both')
        self.tablaProductos.pack(side='left', expand=True)

        #
        self.navbar()
        self.agregar()

    def navbar(self):
        #widgets
        boton_volver = ctk.CTkButton(self.navbarFrame, text='<-', font=('Arial', 18), command=self.destroy, width=70, height=70, fg_color='gray')

        #layout
        boton_volver.pack()

    def agregar(self):
        """ Es el frame del medio que maneja la logica de agregar productos. """
        #variables

        nombre_producto = ctk.StringVar()
        precio_producto = ctk.DoubleVar(value='')
        descripcion_producto = ctk.StringVar()
        stock = ctk.IntVar(value='')
        categoria = ctk.StringVar()


        #Widgets
        label_nombre = ctk.CTkLabel(self.agregarProductos, text='Nombre del producto', font=('Arial', 20))
        label_precio = ctk.CTkLabel(self.agregarProductos, text='Precio', font=('Arial', 20))
        label_descripcion = ctk.CTkLabel(self.agregarProductos, text='Descripcion', font=('Arial', 20))
        label_stock = ctk.CTkLabel(self.agregarProductos, text='Stock', font=('Arial', 20))
        label_categoria = ctk.CTkLabel(self.agregarProductos, text='Categoria', font=('Arial', 20))

        entry_nombre = ctk.CTkEntry(self.agregarProductos, width= 200, height=40, font=('Arial', 18), textvariable=nombre_producto)
        entry_precio = ctk.CTkEntry(self.agregarProductos, width= 200, height=40, font=('Arial', 18), textvariable=precio_producto)
        entry_descripcion = ctk.CTkEntry(self.agregarProductos, width= 200, height=40, font=('Arial', 18), textvariable=descripcion_producto)
        entry_stock = ctk.CTkEntry(self.agregarProductos, width= 200, height=40, font=('Arial', 18), textvariable=stock)
        entry_categoria = ctk.CTkEntry(self.agregarProductos, width= 200, height=40, font=('Arial', 18), textvariable=categoria)

        boton_agregar = ctk.CTkButton(self.agregarProductos, text='Agregar', font=('Arial', 20), fg_color='green', width= 220, height=40, command=lambda: self.cargar(nombre_producto, precio_producto, descripcion_producto, stock, categoria, entry_nombre, entry_precio, entry_descripcion, entry_stock, entry_categoria))


        #layout del frame izquierdo
        label_nombre.pack(padx = 70, pady=(100, 0))
        entry_nombre.pack(padx = 70)

        label_precio.pack(padx = 70)
        entry_precio.pack(padx = 70)

        label_descripcion.pack(padx = 70)
        entry_descripcion.pack(padx = 70)

        label_stock.pack(padx = 70)
        entry_stock.pack(padx = 70)

        label_categoria.pack(padx = 70)
        entry_categoria.pack(padx = 70)

        boton_agregar.pack(padx= 70, pady=(20, 0))

    def cargar(self, *args):
        """ Funcion que se encarga de conectar la app con la base de datos. """
        #Validaciones
        if args[0].get() == "" or args[0].get().isspace() or args[0].get().isdigit():
            if args[0].get().isdigit():
                print('Error, el nombre no puede ser un numero.')
            else:
                print('Error, el nombre no puede estar vacio.')
        if args[1].get() < 0:
            print('El precio no puede ser menor a 0.')
        if args[2].get() == "" or args[2].get().isspace() or args[2].get().isdigit():
            if args[2].get().isdigit():
                print('Error, la descripcion no puede ser un numero.')
            else:
                print('Error, la descripcion no puede estar vacia.')
        if args[3].get() < 0:
            print('El stock no puede ser menor a 0.')
        if args[4].get() == "" or args[4].get().isspace() or args[4].get().isdigit():
            if args[4].get().isdigit():
                print('Error, la categoria no puede ser un numero.')
            else:
                print('Error, la categoria no puede estar vacia.')
        
        print(args[0].get(), args[1].get(), args[2].get(), args[3].get(), args[4].get())

        #Borrar el valor del entry
        args[5].delete(0, 'end')  #Borra el valor del entry nombre_producto desde la posicion 0 hasta el fin de la cadena de texto ingresada
        args[6].delete(0, 'end')  # precio
        args[7].delete(0, 'end')  #descripcion
        args[8].delete(0, 'end')  #stock
        args[9].delete(0, 'end')  #categoria
