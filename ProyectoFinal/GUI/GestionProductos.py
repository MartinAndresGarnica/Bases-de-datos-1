import customtkinter as ctk
from PIL import Image
import CTkMessagebox
from repositorioProductos import DataBaseProductos

class GestionProductos(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('1280x720')
        self.title('Gestion de productos')
        self.resizable(0,0)
        self.grab_set()                         #Hace que la nueva ventana tenga prioridad y no se puedan clickear las demas ventanas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.navbarFrame = ctk.CTkFrame(self) #Este frame es el que se encuentra primero, es el que contiene el boton de volver (de izquierda a derecha)
        self.agregarProductos = ctk.CTkFrame(self, fg_color='#2b2a2a') #Este frame tiene los widgets para agregar productos
        self.tablaProductos = ctk.CTkFrame(self) #Este frame tiene los widgets de la tabla

        #Layout
        self.navbarFrame.pack(side='left', fill='y')
        self.agregarProductos.pack(side='left', fill='both')
        self.tablaProductos.pack(side='left', expand=True, fill='both')

        #Productos
        self.lista_productos = DataBaseProductos.cargarProductos()

        #Encabezados tabla
        self.encabezados = []

        #Llamar a las funciones
        self.navbar()
        self.agregar()
        self.tabla()

    def navbar(self):
        #widgets
        boton_volver = ctk.CTkButton(self.navbarFrame, text='<-', font=('Arial', 18), command=self.destroy, width=30, height=30, fg_color='#2b2a2a')

        #layout
        boton_volver.pack()


    def agregar(self):
        """ Es el frame que maneja la logica de agregar productos. """
        #Variables
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
        
        frame_botones = ctk.CTkFrame(self.agregarProductos, fg_color='#2b2a2a')
        boton_agregar = ctk.CTkButton(frame_botones, text='Agregar', font=('Arial', 20), fg_color='green', width= 180, height=40, command=lambda: self.guardarDatos(nombre_producto, precio_producto, descripcion_producto, stock, categoria, entry_nombre, entry_precio, entry_descripcion, entry_stock, entry_categoria))
        boton_modificar = ctk.CTkButton(frame_botones, text='Modificar', font=('Arial', 20), fg_color='blue', width= 180, height=40, command=lambda: self.modificarDatos(nombre_producto, precio_producto, descripcion_producto, stock, categoria))


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

        frame_botones.pack()
        boton_agregar.pack(side='left', padx=(10, 10), pady=(20, 0))
        boton_modificar.pack(side='left', padx=(10, 10), pady=(20, 0))

    def tabla(self):
        """ Funcion que se encarga de mostrar la tabla de productos. """
        frame_datos = ctk.CTkScrollableFrame(self.tablaProductos)
        frame_datos.columnconfigure(0, weight=3)
        frame_datos.columnconfigure(1, weight=3)
        frame_datos.columnconfigure(2, weight=3)
        frame_datos.columnconfigure(3, weight=3)
        frame_datos.columnconfigure(4, weight=3)
        frame_datos.columnconfigure(5, weight=3)
        frame_datos.columnconfigure(6, weight=1)
        
        label_id = ctk.CTkLabel(frame_datos, text='ID', font=('Arial', 24))
        label_nombre = ctk.CTkLabel(frame_datos, text='Nombre', font=('Arial', 24))
        label_precio = ctk.CTkLabel(frame_datos, text='Precio', font=('Arial', 24))
        label_descripcion = ctk.CTkLabel(frame_datos, text='Descripcion', font=('Arial', 24))
        label_stock = ctk.CTkLabel(frame_datos, text='Stock', font=('Arial', 24))
        label_categoria = ctk.CTkLabel(frame_datos, text='Categoria', font=('Arial', 24))

        #Encabezados
        self.encabezados = [widget for widget in frame_datos.winfo_children() if isinstance(widget, ctk.CTkLabel)]

        #Layout
        frame_datos.pack(expand='true', fill='both')

        label_id.grid(row=0 , column=0, pady=20, sticky='we')
        label_nombre.grid(row=0 , column=1, pady=20, sticky='we')
        label_precio.grid(row=0, column=2, pady=20, sticky='we')
        label_descripcion.grid(row=0 , column=3, pady=20, sticky='we')
        label_stock.grid(row=0 , column=4, pady=20, sticky='we')
        label_categoria.grid(row=0 , column=5, pady=20, sticky='we')

        #
        self.obtenerDatos(frame_datos)


    def guardarDatos(self, *args):
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


    def modificarDatos(self, *args):
        print('Modificar')


    def obtenerDatos(self, *args):
        """ Se encarga de la logica para mostrar los datos. """
        frame_datos = args[0]
        eliminar_icon = ctk.CTkImage(light_image=Image.open('bin.png'), size=(40,40))

        #Elimina los widgets (ignorando los encabezados) en caso de haber para evitar duplicado de datos
        for widget in frame_datos.winfo_children():
            if widget not in self.encabezados:
                widget.destroy()

        #Itera sobre cada producto(lista) dentro de lista_productos y a su vez el segundo for loop itera sobre cada dato del producto
        for indice_producto, producto in enumerate(self.lista_productos):
            for indice_dato, dato in enumerate(producto):
                if (indice_producto+1) % 2 == 0:   #Esto es para que cada fila par tenga un color y cada fila impar tenga otro 
                    label = ctk.CTkLabel(frame_datos, text=dato, font=('Arial', 20), bg_color='#5d5d5d') 
                else:
                    label = ctk.CTkLabel(frame_datos, text=dato, font=('Arial', 20), bg_color='#3d3d3d')
                label.grid(row=indice_producto+1, column=indice_dato, sticky='we', ipady=15) #Acomoda cada producto en una fila nueva, use como guia el indice del producto dentro de lista_productos
                
            boton_eliminar = ctk.CTkButton(frame_datos, image=eliminar_icon, text='', command=lambda id=producto[0]: self.eliminarProducto(id, frame_datos), fg_color='#F34235', width=50, height=28, hover_color='#82211a')
            boton_eliminar.grid(row=indice_producto+1, column=len(producto), padx=0, pady=0)

        
    def eliminarProducto(self, *args):
        id = args[0]
        frame_datos = args[1]
        if DataBaseProductos.eliminar_producto(id):
            self.lista_productos = DataBaseProductos.cargarProductos()
            self.obtenerDatos(frame_datos)
        else:
            CTkMessagebox.CTkMessagebox(message='Error al eliminar el producto.', title='Error')

    

        

