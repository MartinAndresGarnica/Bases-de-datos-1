# Ejercicio: Torneo

**Esquema de BD:**

`TORNEO< cod_torneo, nombre_torneo, cod_corredor, cod_bicicleta, marca_bicicleta, nyap_corredor, sponsor, DNI_presidente_sponsor, DNI_medico >`

Decidimos agregar `<id_corredor, id_bicicleta, id_sponsor>` para cumplir con las restricciones planteadas.

## Punto 1

con las restricciones: 
* a. El código del torneo es único y no se repite para diferentes torneos. Pero los nombres de
torneo pueden repetirse entre diferentes torneos (por ejemplo, el “Tour de Francia” se
desarrolla todos los años y siempre lleva el mismo nombre).
* b. Un corredor corre varios torneos. Tiene un código único por torneo, pero en diferentes
torneos tiene diferentes códigos.
* c. Cada corredor tiene varias bicicletas asignadas para un torneo.
* d. Los cod_bicicleta pueden cambiar en diferentes torneos, pero dentro de un torneo son
únicos.
* e. Cada bicicleta tiene una sola marca.
* f. Cada corredor tiene varios sponsors en un torneo, y un sponsor puede representar a
varios corredores.
* g. Cada sponsor tiene un único presidente y un único médico

### Resolucion dependencias funcionales

> cod_torneo -> nombre_torneo: El codigo del torneo es unico pero el nombre se puede repetir por lo que el nombre_torneo depende funcionalmente del codigo del torneo.

> id_corredor -> nombre, apellido: El corredor tiene una id unica global la cual contiene su nombre y apellido por lo que nombre y apellido dependen funcionalmente de id_corredor.

> cod_torneo, id_corredor -> cod_corredor: El codigo del corredor es unico por torneo pero puede cambiar o repetirse en otros torneos por lo que cod_corredor depende funcionalmente de cod_torneo y id_corredor.

> id_bicicleta -> marca_bicicleta: Una bicicleta tiene una unica marca por lo que la misma depende funcionalmente de id_bicicleta.

> id_bicicleta, cod_torneo -> cod_bicicleta: Una bicicleta puede ser usada por distintos corredores en distintos torneos y su codigo es unico en un torneo pero puede cambiar o repetirse en otro torneo.

> id_sponsor -> nombre, DNI_presidente_sponsor, DNI_medico: Un sponsor tiene un unico nombre, un unico presidente y un unico medico por lo que estos atributos dependen funcionalmente de id_sponsor.


## Punto 2 Determinar las claves candidatas

Las claves candidatas son: 

> cod_torneo ya que permite identificar de manera unica cada torneo.

> id_corredor ya que permite identificar de manera unica al corredor permitiendo generarle un codigo diferente o igual para distintos torneos (combinando cod_corredor, id_corredor)

> id_bicicleta ya que permite identificar de manera unica a cada bicicleta y su marca permitiendo asignarle un codigo distinto o igual en diferentes torneos (combinando cod_torneo, id_bicicleta)

> id_sponsor ya que permite identificar de manera unica a cada sponsor permitiendo asi que un sponsor patrocine a muchos corredores en distintos torneos.

Con estas 4 llaves candidatas (`cod_torneo`, `id_sponsor`, `id_bicicleta`, `id_corredor`) podemos identificar de manera unica cada registro cumpliendo con las restricciones propuestas.

Las relaciones que formamos a traves de las claves mencionadas anteriormente son: 

1. Tabla Torneo_Corredores:
    - Clave primaria compuesta: `cod_torneo`, `id_corredor`
    - Define una unica entrada de un corredor para cada torneo, para que el corredor tenga un unico codigo en cada torneo

2. Tabla Torneo_Bicicletas:
    - Clave primaria compuesta: `id_bicicleta`, `cod_torneo`
    - Garantiza que cada bicicleta tenga una unica entrada para cada torneo, sin repetir combinaciones de `id_bicicleta` y `cod_torneo`, 
      haciendo que `cod_bicicleta` pueda repetirse en diferentes torneos, pero es unico dentro de un torneo

3. Tabla Corredor_Bicicleta:
    - Clave primaria compuesta: `id_bicicleta`, `cod_torneo`, `id_corredor`
    - Cada combinacion de `id_bicicleta`, `cod_torneo` y `id_corredor` es unica, permitiendo que cada corredor tenga varias bicicletas en un torneo

4. Tabla Corredor_Sponsor:
    - Clave primaria compuesta: `cod_torneo`, `id_corredor`, `id_sponsor`
    - Cada combinacion es unica y permite que un corredor tenga varios patrocinadores en un torneo y que un patrocinador tenga varios corredores



## Punto 3 

Para cumplir con la 3NF se realizaron los siguientes pasos:
* 1NF
    - Todas las columnas ahora son atomicas.
    - Las filas son unicas ya que se identifican con una clave primaria.

* 2NF
    - Cumple con la 1NF
    - Todos los atributos no clave dependen de una clave primaria por ejemplo `nombre_torneo` depende de `cod_torneo`.

* 3NF 
    - Cumple con la 1NF y la 2NF
    - Ningun atributo no clave depende de otro atributo no clave (Se eliminaron las dependencias transitivas)

### El diagrama quedaria de la siguiente forma:    

1.  Tabla Torneo:
    - `cod_torneo` (Clave primaria)
    - `nombre_torneo`

2. Tabla Corredor:
   - `id_corredor` (Clave primaria)
   - `nombre`
   - `apellido`

3. Tabla Bicicleta:
   - `id_bicicleta` (Clave primaria)
   - `marca`

4. Tabla Sponsor:
   - `id_sponsor` (Clave primaria)
   - `nombre`
   - `DNI_presidente_sponsor`
   - `DNI_medico`

5. Tabla Torneo_Corredores:
   - `cod_torneo` (Clave foranea que referencia a `torneo`)
   - `id_corredor` (Clave foranea que referencia a `corredor`)
   - `cod_corredor`
   - Clave primaria compuesta (`cod_torneo`, `id_corredor`)

6. Tabla Torneo_Bicicletas:
   - `id_bicicleta` (Clave foranea que referencia a `bicicleta`)
   - `cod_torneo` (Clave foranea que referencia a `torneo`)
   - `cod_bicicleta`
   - Clave primaria compuesta (`id_bicicleta`, `cod_torneo`)

7. Tabla Corredor_Bicicleta:
   - `id_bicicleta` (Clave foranea que referencia a `bicicleta`)
   - `cod_torneo` (Clave foranea que referencia a `torneo`)
   - `id_corredor` (Clave foranea que referencia a `corredor`)
   - Clave primaria compuesta (`id_bicicleta`, `cod_torneo`, `id_corredor`)

8.  Tabla Corredor_Sponsor:
    - `cod_torneo` (Clave foranea que referencia a `torneo`)
    - `id_corredor` (Clave foranea que referencia a `corredor`)
    - `id_sponsor` (Clave foranea que referencia a `sponsor`)
    - Clave primaria compuesta (`cod_torneo`, `id_corredor`, `id_sponsor`)



