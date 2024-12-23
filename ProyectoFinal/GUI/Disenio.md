# <p style="text-align:center;">Trabajo practico integrado: Sistema de ventas</p>

# Participantes:
- Martin Andres Garnica
- Thomas Emanuel Sejas
- Franco Devaux

&nbsp;

# Explicación de diseño

![Menú principal](./static/Diagrama.jpg)

## Entidades y Atributos

### El diseño cuenta con las siguientes entidades:
- **`Cliente`**
- **`Orden`**
- **`Orden_producto`**
- **`Producto`**

> Decidimos agregar `Orden_producto` para permitir al cliente comprar varios productos dentro de una misma orden.

### Atributos

#### **`Producto`**
- `id_producto` (Clave primaria)
- `nombre_producto`
- `descripcion`
- `stock`
- `categoria`

#### **`Cliente`**
- `id_cliente` (Clave primaria)
- `nombre_cliente`
- `apellido_cliente`
- `telefono`
- `direccion`
- `email`

#### **`Orden`**
- `id_orden` (Clave primaria)
- `id_cliente` (Clave foránea referenciando a `Cliente`)
- `fecha`

#### **`Orden_producto`**
- `id_producto` (Clave foránea referenciando a `Producto`)
- `id_orden` (Clave foránea referenciando a `Orden`)
- `cantidad_producto`
- `subtotal`
- (Clave primaria compuesta por `id_producto` y `id_orden`)

---

## Relaciones

- **`Clientes` < `Orden`**
  - Un cliente puede tener muchas órdenes y una orden pertenece a un único cliente.

- **`Orden` <> `Producto`**
  - Una orden puede incluir muchos productos y un producto puede estar en muchas órdenes, esta relacion se consigue mediante la tabla `Orden_Producto`.


## Primera forma normal (1NF):

- **PRODUCTO**:   
Cada producto tiene su identificador unico `id_producto`.   
 `nombre_producto`, `precio`, `descripcion`, `stock` y `categoria` contienen valores atómicos.

- **CLIENTE**:  
 Cada cliente tiene un identificador único `id_cliente`, y `nombre_cliente`, `apellido_cliente`, `telefono`, `direccion` y `email` contienen valores atómicos.

- **ORDEN**:    
La tabla de órdenes contiene un identificador único `id_orden`, una referencia a un cliente con `id_cliente`, y la columna `fecha` tiene un valor atómico (la `fecha`)

- **ORDEN_PRODUCTO**:   
Esta tabla es una tabla de relación entre las tablas ORDEN y PRODUCTO. Cada fila contiene un `id_orden`, un `id_producto`, la `cantidad_producto` y el `subtotal`, todos con valores atómicos.

## Segunda forma normal (2NF):

- **Cumple con la primera forma normal**

- **PRODUCTO**:     
La clave primaria `id_producto` determina de manera unica las demas columnas (`id_producto`, `precio`, `descripcion`, `stock`, `categoria`). No hay dependencias parciales

- **CLIENTE**:  
 La clave primaria `id_cliente` determina de manera única las columnas `nombre_cliente`, `apellido_cliente`, `telefono`, `direccion` y `email`. No hay dependencias parciales.

- **ORDEN**:  
La clave primaria `id_orden` determina de manera única el `id_cliente` y la `fecha`. No hay dependencias parciales.

- **ORDEN_PRODUCTO**:   
 La clave primaria compuesta `id_orden` e `id_producto` determina de manera única `cantidad_producto` y `subtotal`. Todos los atributos dependen completamente de la clave primaria compuesta


## Tercera forma normal (3NF):

- **Cumple con la segunda forma normal**

- **PRODUCTO**:     
La tabla `PRODUCTO` tiene solo atributos relacionados directamente con el `id_producto`. No hay dependencias transitivas.

- **CLIENTE**:  
 En la tabla `CLIENTE`, el `id_cliente` determina directamente los atributos relacionados con el cliente. No hay dependencias transitivas.

- **ORDEN**:    
La tabla `ORDEN` tiene el `id_orden` como clave primaria y depende del `id_cliente` para la relacion. Ademas, la `fecha` depende directamente del `id_orden`. No hay dependencias transitivas

- **ORDEN_PRDUCTO**:    
 En la tabla `ORDEN_PRODUCTO`, las columnas cantidad y subtotal dependen de la combinacion de `id_orden` y `id_producto`. No hay dependencias transitivas

&nbsp;

# Organización del proyecto
## Modulos utilizados
- Pymysql
- Tkinter
- CustomTkinter
- CTKmessagebox
- Pillow

## Distribución de archivos:

### Carpeta repositorios:
- Contiene los archivos que se encargan de las consultas específicas de cada sección.

### Carpeta secciones:
- Contiene las distintas partes del proyecto separadas en sus respectivos archivos. Además, utilizamos clases como forma de organizar el código para tener un orden y un mejor manejo de las funciones.

### Carpeta static:
- Guarda las imágenes necesarias para el proyecto.

### Carpeta SQL:
- Contiene los códigos para crear la base de datos, poblarla y generar órdenes aleatorias (dependiendo del stock) entre productos y clientes.

### Menu.py:
- Es el archivo principal que se encarga de conectar todas las secciones del proyecto.


&nbsp;

# Pequeña guía de la app

## Dependencias

En el proyecto está incluido un archivo llamado `requirements.txt`, el cual se puede usar junto con el comando `pip install -r requirements.txt` para instalar todas las dependencias necesarias para el correcto funcionamiento de la app.


## Conexión

- Para conectarse a la base de datos, primero debes entrar en la carpeta de repositorios y luego abrir el archivo `Conexion_BD.py`.

- ![Conexión](./static/conexion.jpg)

- Una vez dentro del archivo, deberás cambiar los datos de `host`, `user`, `password` y `database` por los de tu base de datos.

- ![Conexión datos](./static/conexion2.jpg)


## Iniciar la app

- La aplicación consiste en un menú principal con elementos para gestionar un sistema de ventas. 
- Para iniciar (ya habiendo instalado y configurado todo) hay que correr el archivo `Menu.py`.

- ![Menú principal](./static/Menu.jpg)

---

## Gestión de productos y gestión de clientes cumplen la función de CRUD.

- La pantalla principal del CRUD muestra una lista con los datos cargados (en caso de existir) y permite agregar o eliminar. Cuenta con un menú desplegable que permite cambiar entre la función de agregar y modificar (usando la ID del cliente/producto).

- ![Gestión de productos](./static/Gestion_productos.jpg)  

- ![Gestión de clientes](./static/Gestion_cliente.jpg)  

- ![Gestión de clientes (modificar)](./static/Gestion_clienteMOD.jpg)

---

## Procesar órdenes

- Permite ver las órdenes y al hacerles clic abre una ventana con los detalles.  
- Además, permite filtrarlas o eliminarlas según la ID de la orden o la del cliente.

- ![Procesar órdenes](./static/Procesar_ordenes.jpg)  

- ![Detalle de una orden](./static/Procesar_ordenDetalle.jpg)  

- ![Filtrar por ID de orden](./static/Procesar_ordenID.jpg)

---

## Búsqueda avanzada

- Permite mostrar productos y clientes, aplicando filtros preestablecidos.  
- Si la lista no tiene filtros aplicados, se puede ordenar la tabla según sus columnas haciendo clic sobre las mismas.

- ![Búsqueda avanzada](./static/Busqueda_avanzada.jpg)  

- ![Búsqueda avanzada con filtros Producto](./static/Busqueda_avanzadaFiltros.jpg)  

- ![Búsqueda avanzada con filtros Cliente](./static/Busqueda_avanzadaFiltros2.jpg)

---

## Producto más vendido

- No necesita explicación, simplemente abre una ventana mostrando el nombre y la cantidad de ventas del producto más vendido.

- ![Producto más vendido](./static/Reporte_producto.jpg)

---

## Ajustar Cantidad Máxima

- Limita la cantidad maxima que se puede comprar del producto ingresado por ID.  
- Si existen órdenes que exceden el límite (por ejemplo, 3 auriculares y se limitó a 2), modifica la orden con el valor máximo permitido ingresado y ajusta el precio a dicha cantidad.

- ![Ajustar valor](./static/Cantidad_maxima.jpg)