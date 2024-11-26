import customtkinter as ctk
import tkinter as tk
from PIL import Image
import CTkMessagebox
from repositorioClientes import DataBaseClientes

class GestionClientes(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('1280x720')
        self.title('Gestion de clientes')
        self.resizable(1920, 1080)
        self.grab_set()                         #Hace que la nueva ventana tenga prioridad y no se puedan clickear las demas ventanas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.navbarFrame = ctk.CTkFrame(self) #Este frame es el que se encuentra primero, es el que contiene el boton de volver (de izquierda a derecha)
        self.agregarClientes = ctk.CTkFrame(self, fg_color='#2b2a2a') #Este frame tiene los widgets para agregar Clientes
        self.tablaClientes = ctk.CTkFrame(self) #Este frame tiene los widgets de la tabla

        self.frame_datos = ctk.CTkScrollableFrame(self.tablaClientes)

        #Layout general
        self.navbarFrame.pack(side='left', fill='y')
        self.agregarClientes.pack(side='left', fill='both')
        self.tablaClientes.pack(side='left', expand=True, fill='both')

        #Clientes
        self.lista_clientes = DataBaseClientes.cargarClientes()

        #Encabezados
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
        """ Es el frame que maneja la logica de agregar Clientes. """
        #Variables
        nombre = ctk.StringVar()
        apellido = ctk.StringVar()
        telefono = ctk.StringVar()
        direccion = ctk.StringVar()
        mail = ctk.StringVar()


        #Widgets
        label_nombre = ctk.CTkLabel(self.agregarClientes, text='Nombre', font=('Arial', 20))
        label_apellido = ctk.CTkLabel(self.agregarClientes, text='Apellido', font=('Arial', 20))
        label_telefono = ctk.CTkLabel(self.agregarClientes, text='Telefono', font=('Arial', 20))
        label_direccion = ctk.CTkLabel(self.agregarClientes, text='Direccion', font=('Arial', 20))
        label_mail = ctk.CTkLabel(self.agregarClientes, text='Mail', font=('Arial', 20))

        entry_nombre = ctk.CTkEntry(self.agregarClientes, width= 200, height=40, font=('Arial', 18), textvariable=nombre)
        entry_apellido = ctk.CTkEntry(self.agregarClientes, width= 200, height=40, font=('Arial', 18), textvariable=apellido)
        entry_telefono = ctk.CTkEntry(self.agregarClientes, width= 200, height=40, font=('Arial', 18), textvariable=telefono)
        entry_direccion = ctk.CTkEntry(self.agregarClientes, width= 200, height=40, font=('Arial', 18), textvariable=direccion)
        entry_mail = ctk.CTkEntry(self.agregarClientes, width= 200, height=40, font=('Arial', 18), textvariable=mail)
        
        frame_botones = ctk.CTkFrame(self.agregarClientes, fg_color='#2b2a2a')
        boton_agregar = ctk.CTkButton(frame_botones, text='Agregar', font=('Arial', 20), fg_color='green', width= 180, height=40, command=lambda: self.guardarDatos(nombre, apellido, telefono, direccion, mail, entry_nombre, entry_apellido, entry_telefono, entry_direccion, entry_mail))
        boton_modificar = ctk.CTkButton(frame_botones, text='Modificar', font=('Arial', 20), fg_color='blue', width= 180, height=40, command=lambda: self.modificarDatos(nombre, apellido, telefono, direccion, mail))


        #layout del frame izquierdo
        label_nombre.pack(padx = 70, pady=(100, 0))
        entry_nombre.pack(padx = 70)

        label_apellido.pack(padx = 70)
        entry_apellido.pack(padx = 70)

        label_telefono.pack(padx = 70)
        entry_telefono.pack(padx = 70)

        label_direccion.pack(padx = 70)
        entry_direccion.pack(padx = 70)

        label_mail.pack(padx = 70)
        entry_mail.pack(padx = 70)

        frame_botones.pack()
        boton_agregar.pack(side='left', padx=(10, 10), pady=(20, 0))
        boton_modificar.pack(side='left', padx=(10, 10), pady=(20, 0))

    def tabla(self):
        """ Funcion que se encarga de mostrar la tabla de Clientes. """
        self.frame_datos.columnconfigure(0, weight=3)
        self.frame_datos.columnconfigure(1, weight=3)
        self.frame_datos.columnconfigure(2, weight=3)
        self.frame_datos.columnconfigure(3, weight=3)
        self.frame_datos.columnconfigure(4, weight=3)
        self.frame_datos.columnconfigure(5, weight=3)
        self.frame_datos.columnconfigure(6, weight=1)
        
        label_id = ctk.CTkLabel(self.frame_datos, text='ID', font=('Arial', 24))
        label_nombre = ctk.CTkLabel(self.frame_datos, text='Nombre', font=('Arial', 24))
        label_apellido = ctk.CTkLabel(self.frame_datos, text='Apellido', font=('Arial', 24))
        label_telefono = ctk.CTkLabel(self.frame_datos, text='Telefono', font=('Arial', 24))
        label_direccion = ctk.CTkLabel(self.frame_datos, text='Direccion', font=('Arial', 24))
        label_mail = ctk.CTkLabel(self.frame_datos, text='Mail', font=('Arial', 24))

        #Encabezados
        self.encabezados = [widget for widget in self.frame_datos.winfo_children() if isinstance(widget, ctk.CTkLabel)]

        #Layout
        self.frame_datos.pack(expand='true', fill='both')

        label_id.grid(row=0, column=0, pady=20, sticky='we')
        label_nombre.grid(row=0 , column=1, pady=20, sticky='we')
        label_apellido.grid(row=0, column=2, pady=20, sticky='we')
        label_telefono.grid(row=0 , column=3, pady=20, sticky='we')
        label_direccion.grid(row=0 , column=4, pady=20, sticky='we')
        label_mail.grid(row=0 , column=5, pady=20, sticky='we')

        #
        self.obtenerDatos(self.frame_datos)


    def guardarDatos(self, *args):
        """ Funcion que se encarga de conectar la app con la base de datos. """
        #Variables
        nombre = args[0]
        apellido = args[1]
        telefono = args[2]
        direccion = args[3]
        mail = args[4]

        #Validaciones
        if nombre.get() == "" or nombre.get().isspace() or nombre.get().isdigit():
            if nombre.get().isdigit():
                mensaje='Error, el nombre no puede ser un numero.'
                titulo = 'Error'
            else:
                mensaje='Error, el nombre no puede estar vacio.'
                titulo = 'Error'
        elif apellido.get() == "" or apellido.get().isspace() or apellido.get().isdigit():
            if apellido.get().isdigit():
                mensaje='Error, el apellido no puede ser un numero.'
                titulo = 'Error'
            else:
                mensaje='Error, el apellido no puede estar vacio.'
                titulo = 'Error'
        elif telefono.get() == "" or telefono.get().isspace() or telefono.get().isdigit():
            if telefono.get().isdigit():
                mensaje='Error, el telefono debe llevar el + adelante.'
                titulo = 'Error'
            else:
                mensaje='Error, el telefono no puede estar vacio.'
                titulo = 'Error'
        elif direccion.get() == "" or direccion.get().isspace() or direccion.get().isdigit():
            if direccion.get().isdigit():
                mensaje='Error, la direccion no puede ser un numero.'
                titulo = 'Error'
            else:
                mensaje='Error, la direccion no puede estar vacia.'
                titulo = 'Error'
        elif mail.get() == "" or mail.get().isspace() or mail.get().isdigit() or '@' not in mail.get():
            if mail.get().isdigit():
                mensaje='Error, la mail no puede ser un numero.'
                titulo = 'Error'
            elif '@' not in mail.get():
                mensaje='Mail invalido, debe contener un @.'
                titulo = 'Error'
            else:
                mensaje='Error, la mail no puede estar vacia.'
                titulo = 'Error'
        else:

            if DataBaseClientes.agregar_cliente(nombre, apellido, direccion, telefono, mail):
                mensaje = 'Cliente registrado correctamente.'
                titulo = 'Exito!'

                #Borrar el valor del entry
                args[5].delete(0, 'end')  #Borra el valor del entry nombre_producto desde la posicion 0 hasta el fin de la cadena de texto ingresada
                args[6].delete(0, 'end')  # apellido
                args[7].delete(0, 'end')  #telefono
                args[8].delete(0, 'end')  #direccion
                args[9].delete(0, 'end')  #mail
            
            else: 
                mensaje = 'Hubo un error al registrar el cliente.'
                titulo = 'Error'

        CTkMessagebox.CTkMessagebox(title=titulo, message=mensaje)


    def modificarDatos(self, *args):
        print('Modificar')


    def obtenerDatos(self, *args):
        """ Se encarga de la logica para mostrar los datos. """
        self.frame_datos = args[0]
        eliminar_icon = ctk.CTkImage(light_image=Image.open('bin.png'), size=(40,40))

        #Elimina los widgets (ignorando los encabezados) en caso de haber para evitar duplicado de datos
        for widget in self.frame_datos.winfo_children():
            if widget not in self.encabezados:
                widget.destroy()

        #Itera sobre cada producto(lista) dentro de lista_Clientes y a su vez el segundo for loop itera sobre cada dato del producto
        for indice_producto, producto in enumerate(self.lista_clientes):
            for indice_dato, dato in enumerate(producto):
                if (indice_producto+1) % 2 == 0:   #Esto es para que cada fila par tenga un color y cada fila impar tenga otro 
                    label = ctk.CTkLabel(args[0], text=dato, font=('Arial', 20), bg_color='#5d5d5d') 
                else:
                    label = ctk.CTkLabel(args[0], text=dato, font=('Arial', 20), bg_color='#3d3d3d')
                label.grid(row=indice_producto+1, column=indice_dato, sticky='we', ipady=15) #Acomoda cada producto en una fila nueva, use como guia el indice del producto dentro de lista_Clientes
                
            boton_eliminar = ctk.CTkButton(args[0], image=eliminar_icon, text='', command=lambda id=producto[0]: self.eliminarCliente(id, self.frame_datos), fg_color='#F34235', width=50, height=28, hover_color='#F34235')
            boton_eliminar.grid(row=indice_producto+1, column=len(producto), padx=0, pady=0)

        
    def eliminarCliente(self, *args):
        id = args[0]
        self.frame_datos = args[1]
        if DataBaseClientes.eliminar_cliente(id):
            self.lista_clientes = DataBaseClientes.cargarClientes()
            self.obtenerDatos(self.frame_datos)
        else:
            CTkMessagebox.CTkMessagebox(message='Error al eliminar el cliente.', title='Error')