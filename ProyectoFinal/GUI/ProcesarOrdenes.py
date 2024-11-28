import customtkinter as ctk
from tkinter import ttk
from PIL import Image
import CTkMessagebox
from repositorioOrdenes import DatabaseOrdenes

class ProcesamientoOrdenes(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('1280x720')
        self.title('Procesamiento de ordenes')
        self.resizable(0, 0)
        self.grab_set()                         #Hace que la nueva ventana tenga prioridad y no se puedan clickear las demas ventanas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        #Frames
        self.navbarFrame = ctk.CTkFrame(self) #Este frame es el que se encuentra primero, es el que contiene el boton de volver (de izquierda a derecha)
        self.agregarOrdenes = ctk.CTkFrame(self, fg_color='#2b2a2a') #Este frame tiene los widgets para agregar Ordenes
        self.tablaOrdenes = ctk.CTkFrame(self) #Este frame tiene los widgets de la tabla

        #Layout general
        self.navbarFrame.pack(side='left', fill='y')
        self.agregarOrdenes.pack(side='left', fill='both')
        self.tablaOrdenes.pack(side='left', expand=True, fill='both')


        #Encabezados
        self.encabezados = []

        #Menu
        Menu = ctk.CTkOptionMenu(self.agregarOrdenes, values=['Orden', 'Cliente'], command=self.entrys)
        Menu.pack(pady=(40, 0))

        #Llamar a las funciones
        self.navbar()
        self.entrys()
        self.tabla()

    def navbar(self):
        #widgets
        boton_volver = ctk.CTkButton(self.navbarFrame, text='<-', font=('Arial', 18), command=self.destroy, width=30, height=30, fg_color='#2b2a2a')

        #layout
        boton_volver.pack()


    def entrys(self, *args):
        """ Es el frame que maneja la logica de agregar Ordenes. """
        #Variables
        id_orden = ctk.IntVar(value='')

        for widget in self.agregarOrdenes.winfo_children():
            if not isinstance(widget, ctk.CTkOptionMenu):
                widget.destroy()

        #Widgets
        label_id = ctk.CTkLabel(self.agregarOrdenes, text='ID', font=('Arial', 20))

        entry_id =  ctk.CTkEntry(self.agregarOrdenes, width=100, height=40, font=('Arial', 18), textvariable=id_orden)
        
        frame_botones = ctk.CTkFrame(self.agregarOrdenes, fg_color='#2b2a2a')
        if 'Cliente' in args:
            boton_filtrar = ctk.CTkButton(frame_botones, text='Filtrar', font=('Arial', 20), fg_color='blue', width= 140, height=40, command=lambda: self.tabla(id_orden, 'FiltrarCliente'))
            boton_eliminar = ctk.CTkButton(frame_botones, text='Eliminar', font=('Arial', 20), fg_color='blue', width= 140, height=40, command=lambda: self.eliminarOrden(id_orden))
        else:
            boton_filtrar = ctk.CTkButton(frame_botones, text='Filtrar', font=('Arial', 20), fg_color='blue', width= 140, height=40, command=lambda: self.tabla(id_orden, 'Filtrar'))
            boton_eliminar = ctk.CTkButton(frame_botones, text='Eliminar', font=('Arial', 20), fg_color='blue', width= 140, height=40, command=lambda: self.eliminarOrden(id_orden))
    
        boton_mostrarTodas = ctk.CTkButton(self.agregarOrdenes, text='Mostrar todas', font=('Arial', 20), fg_color='green', width= 180, height=40, command= self.tabla)

        #layout del frame izquierdo
        boton_mostrarTodas.pack(pady= 40)

        label_id.pack(padx = 70, pady=(30, 0))
        entry_id.pack(padx = 70, pady=5)


        frame_botones.pack()
        boton_filtrar.pack(side='left', padx = 10, pady = 10)
        boton_eliminar.pack(side='left', padx = 10,pady = 10)

    def ajustar_columnas(self, event):
        """Ajustar dinámicamente las columnas al tamaño del Treeview."""
        tabla = event.widget  # Treeview que activó el evento
        ancho_total = tabla.winfo_width()  # Ancho total disponible
        numero_columnas = len(tabla["columns"])  # Número de columnas
        ancho_columna = ancho_total // numero_columnas  # Ancho promedio por columna

        for columna in tabla["columns"]:
            tabla.column(columna, width=ancho_columna, anchor='c')


    def tabla(self, *args):
        if 'Filtrar' in args:
            id = args[0].get()
            self.lista_Ordenes = DatabaseOrdenes.mostrar_orden_ID(id)
        elif 'FiltrarCliente' in args:
            id = args[0].get()
            self.lista_Ordenes = DatabaseOrdenes.mostrar_orden_cliente(id)
        else: 
            self.lista_Ordenes = DatabaseOrdenes.cargarOrdenes()

        for widget in self.tablaOrdenes.winfo_children():
                widget.destroy()

        #Crea un estilo para los encabezados
        estiloEncabezados = ttk.Style()
        estiloEncabezados.theme_use("default")  # Cambia el estilo base
        estiloEncabezados.configure("Treeview.Heading", background="#2b2a2a", foreground="white", fieldbackground="#2a2d2e", font=('Arial', 18))
        
        #Crea un estilo para la tabla
        estiloTabla = ttk.Style()
        estiloTabla.theme_use("default")  # Cambia el estilo base
        estiloTabla.configure("Treeview", background="#2b2a2a", foreground="white", fieldbackground="#2a2d2e", rowheight=40, font=('Arial', 12))

        #Crea la tabla
        tabla = ttk.Treeview(self.tablaOrdenes, columns=("ID_orden", "ID_cliente", "ID_producto", "Cantidad_producto", "Fecha", "Total"), show="headings")
        tabla.heading("ID_orden", text='ID orden')
        tabla.heading("ID_cliente", text='ID cliente')
        tabla.heading("ID_producto", text='ID producto')
        tabla.heading("Cantidad_producto", text='Cantidad')
        tabla.heading("Fecha", text='Fecha')
        tabla.heading("Total", text='Total')

        #Configura las columnas para ajustarse dinamicamente
        tabla.bind("<Configure>", self.ajustar_columnas)
        

        #Inserta los datos en la tabla y les pone un tag para poder agregarle el color segun sea par o impar
        for indice, orden in enumerate(self.lista_Ordenes):
            if indice % 2 == 0:
                tabla.insert("", "end", values=orden, tags='Par')
            else:
                tabla.insert("", "end", values=orden, tags='Impar')

        #Asignamos colores segun su tag
        tabla.tag_configure('Par', background='#5d5d5d')
        tabla.tag_configure('Impar', background='#3d3d3d')

        #Layout
        tabla.pack(expand=True, fill='both')


    def eliminarOrden(self, *args):
        id = args[0].get()
        if DatabaseOrdenes.eliminar_orden(id):
            self.tabla()
            CTkMessagebox.CTkMessagebox(message='Orden eliminada correctamente', title='Error')
        else:
            CTkMessagebox.CTkMessagebox(message='Error al eliminar la orden.', title='Error')