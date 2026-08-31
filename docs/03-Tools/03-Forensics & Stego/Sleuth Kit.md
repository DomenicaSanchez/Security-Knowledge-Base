#tool/the-sleuth-kit

---

## 🕵️ Información

**¿Qué es The Sleuth Kit?**

**The Sleuth Kit (TSK)** es una colección de herramientas de código abierto orientadas al análisis forense digital de discos, imágenes de disco y sistemas de archivos.

TSK proporciona diferentes herramientas de línea de comandos que permiten examinar una imagen forense sin necesidad de modificar directamente la evidencia original.

Entre las tareas que permite realizar se encuentran:

- Identificar la estructura de particiones de una imagen de disco.
    
- Identificar el tipo y características de un sistema de archivos.
    
- Enumerar archivos y directorios.
    
- Analizar metadatos e inodos.
    
- Recuperar archivos mediante sus identificadores de inodo.
    
- Identificar archivos eliminados.
    
- Analizar estructuras internas de sistemas de archivos.
    
- Construir líneas de tiempo de actividad de archivos.
    
- Examinar imágenes de discos utilizadas como evidencia digital.
    

Algunas de las herramientas más utilizadas de The Sleuth Kit son:

|Herramienta|Función|
|---|---|
|`mmls`|Analizar la tabla de particiones de una imagen|
|`fsstat`|Mostrar información del sistema de archivos|
|`fls`|Listar archivos y directorios|
|`icat`|Extraer contenido asociado a un inodo|
|`istat`|Mostrar información detallada de un inodo|
|`ifind`|Encontrar el inodo asociado a un archivo o estructura|
|`ffind`|Encontrar el nombre asociado a un inodo|
|`blkls`|Extraer bloques de datos|
|`blkstat`|Mostrar información sobre un bloque|
|`ils`|Listar información de inodos|
|`mactime`|Generar una línea de tiempo a partir de metadatos|

---

## 🧠 ¿Por qué es útil en CTFs?

The Sleuth Kit es especialmente útil en retos de **Forensics**, donde normalmente se proporciona una imagen de disco, una partición o un sistema de archivos y se debe encontrar información oculta, eliminada o modificada.

Entre sus usos más comunes en CTFs se encuentran:

- Analizar imágenes `.img`, `.dd` y otros formatos forenses.
    
- Identificar particiones y sus offsets.
    
- Determinar qué sistema de archivos utiliza una partición.
    
- Explorar directorios sin montar la imagen.
    
- Recuperar archivos eliminados.
    
- Obtener información de inodos.
    
- Extraer archivos directamente desde una imagen.
    
- Analizar timestamps de archivos.
    
- Investigar artefactos de sistemas Linux y Windows.
    
- Recuperar información que ya no es visible desde la estructura normal de directorios.
    

Una ventaja importante es que muchas de estas operaciones pueden realizarse directamente sobre la imagen utilizando un **offset de partición**, evitando modificar el contenido original.

---

## ⚡ Instalación

### Instalar mediante el gestor de paquetes

En Kali Linux y distribuciones basadas en Debian:

```bash
sudo apt install sleuthkit
```

### Verificar la instalación

Se puede comprobar que las herramientas están disponibles mediante:

```bash
mmls -h
```

o:

```bash
fls -h
```

También se puede comprobar la versión instalada:

```bash
mmls -V
```

---

## ⚡ Quick Cheat Sheet

### 💽 `mmls` — Analizar particiones

`mmls` permite identificar la estructura de particiones dentro de una imagen de disco.

Uso básico:

```bash
mmls <imagen>
```

Ejemplo:

```bash
mmls disk.img
```

La salida permite identificar:

- Sector inicial de cada partición.
    
- Sector final.
    
- Tamaño de la partición.
    
- Tipo de partición.
    
- Espacio no asignado.
    

Un dato especialmente importante es **Start**, ya que posteriormente puede utilizarse como offset en otras herramientas de TSK.

---

### 🔍 `fsstat` — Información del sistema de archivos

`fsstat` muestra información detallada sobre el sistema de archivos.

Uso:

```bash
fsstat -o <offset> <imagen>
```

#### `-o`

La opción:

```text
-o
```

significa **offset**.

Indica a TSK en qué sector comienza el sistema de archivos que queremos analizar.

Por ejemplo:

```bash
fsstat -o 2048 disk.img
```

significa:

> Analizar el sistema de archivos que comienza en el sector `2048` de `disk.img`.

El offset normalmente se obtiene previamente mediante:

```bash
mmls disk.img
```

La salida de `fsstat` puede proporcionar información como:

- Tipo de filesystem.
    
- Tamaño de bloques.
    
- Tamaño de inodos.
    
- Rango de inodos.
    
- Directorio raíz.
    
- Información de grupos de bloques.
    
- Características del filesystem.
    
- Información temporal.
    

---

### 📂 `fls` — Listar archivos y directorios

`fls` permite listar archivos y directorios dentro de un sistema de archivos.

Uso básico:

```bash
fls -o <offset> <imagen>
```

Ejemplo:

```bash
fls -o 2048 disk.img
```

#### `-o`

Como en `fsstat`, indica el **sector de inicio del filesystem**:

```bash
-o <offset>
```

#### `-r`

La opción:

```text
-r
```

significa **recursivo**.

Permite recorrer los subdirectorios y mostrar su contenido.

Sin `-r`:

```bash
fls -o 2048 disk.img
```

se muestra únicamente el contenido del directorio analizado.

Con `-r`:

```bash
fls -o 2048 -r disk.img
```

se recorren también sus subdirectorios.

Esto resulta especialmente útil para localizar rápidamente archivos o directorios de interés.

Por ejemplo:

```bash
fls -o 2048 -r disk.img | grep -i flag
```

permite buscar entradas cuyo nombre contenga `flag`.

---

### 📁 Analizar un directorio específico mediante su inodo

`fls` también puede recibir un número de inodo:

```bash
fls -o <offset> <imagen> <inodo>
```

Por ejemplo:

```bash
fls -o 2048 disk.img 64770
```

Esto indica que se quiere listar el contenido correspondiente al inodo `64770`.

Los inodos pueden obtenerse mediante `fls`, `ils` u otras herramientas de TSK.

Combinándolo con `-r`:

```bash
fls -o 2048 -r disk.img 64770
```

se analiza recursivamente el directorio asociado al inodo.

---

### 📤 `icat` — Extraer contenido de un inodo

`icat` permite recuperar el contenido asociado a un inodo.

Uso:

```bash
icat -o <offset> <imagen> <inodo>
```

Ejemplo:

```bash
icat -o 2048 disk.img 12345
```

Esto extrae el contenido del inodo `12345`.

También podemos guardar el resultado en un archivo:

```bash
icat -o 2048 disk.img 12345 > recovered.bin
```

De esta manera, el contenido recuperado queda almacenado en:

```text
recovered.bin
```

#### `-o`

Indica nuevamente el offset donde comienza el filesystem.

```text
-o <offset>
```

#### ¿Por qué `icat` es importante en Forensics?

Porque permite recuperar contenido directamente desde la imagen utilizando el **inodo**, incluso cuando el archivo no es fácilmente accesible mediante una ruta convencional.

Esto resulta especialmente útil para:

- Archivos eliminados.
    
- Archivos ocultos.
    
- Artefactos forenses.
    
- Archivos cuyo nombre ha sido perdido.
    
- Recuperación de objetos almacenados dentro de estructuras específicas.
    

---

### 🧬 `istat` — Analizar un inodo

`istat` proporciona información detallada sobre un inodo.

Uso:

```bash
istat -o <offset> <imagen> <inodo>
```

Ejemplo:

```bash
istat -o 2048 disk.img 12345
```

Puede proporcionar información relacionada con:

- Tipo de archivo.
    
- Permisos.
    
- UID/GID.
    
- Tamaño.
    
- Timestamps.
    
- Bloques asociados.
    
- Información de metadatos.
    

Es especialmente útil cuando primero encontramos un inodo interesante mediante `fls`.

---

### 🔎 `ils` — Listar inodos

`ils` permite obtener información sobre los inodos del filesystem.

Uso:

```bash
ils -o <offset> <imagen>
```

Por ejemplo:

```bash
ils -o 2048 disk.img
```

Puede ser útil para investigar:

- Inodos asignados.
    
- Inodos eliminados.
    
- Estado de los inodos.
    
- Información temporal asociada.
    

---

### 🧭 `ifind` — Encontrar un inodo

`ifind` permite localizar el inodo asociado a determinados datos o estructuras.

Uso general:

```bash
ifind -o <offset> <imagen>
```

Dependiendo del modo utilizado, puede ayudar a relacionar bloques, archivos e inodos.

Es especialmente útil cuando durante una investigación se encuentra un bloque de datos interesante y se necesita determinar qué archivo estaba asociado con él.

---

### 🏷️ `ffind` — Encontrar el nombre de un archivo

`ffind` permite determinar qué archivo está asociado con un determinado inodo.

Uso:

```bash
ffind -o <offset> <imagen> <inodo>
```

Ejemplo:

```bash
ffind -o 2048 disk.img 12345
```

Puede ser útil para relacionar un identificador interno del filesystem con su nombre o ubicación.

---

### 🧱 `blkls` — Extraer bloques

`blkls` permite extraer datos de bloques del sistema de archivos.

Uso básico:

```bash
blkls -o <offset> <imagen>
```

Es una herramienta especialmente útil en análisis de espacio no asignado y recuperación de información que no aparece como archivos normales.

Puede utilizarse como parte de procesos de recuperación de archivos eliminados o análisis de datos residuales.

---

### 🧱 `blkstat` — Información de un bloque

`blkstat` muestra información sobre un bloque específico.

Uso:

```bash
blkstat -o <offset> <imagen> <bloque>
```

Ejemplo:

```bash
blkstat -o 2048 disk.img 123456
```

Permite investigar las características y el estado de un bloque concreto.

---

### 🕒 `mactime` — Timeline forense

`mactime` se utiliza para construir líneas de tiempo a partir de información temporal de archivos.

Normalmente se combina con otras herramientas de TSK, como `fls`.

Un flujo común es:

```bash
fls -r -m / -o <offset> disk.img > bodyfile.txt
```

y posteriormente:

```bash
mactime -b bodyfile.txt
```

Esto permite organizar cronológicamente eventos relacionados con:

- Modificación (`mtime`).
    
- Acceso (`atime`).
    
- Cambio de metadatos (`ctime`).
    
- Creación, cuando el filesystem proporciona dicho dato.
    

Las líneas de tiempo son especialmente útiles para reconstruir la secuencia de eventos de un incidente o encontrar archivos modificados durante un período determinado.

---

## 🧩 Opciones importantes

Las opciones pueden variar según la herramienta, pero algunas de las más habituales en TSK son:

|Opción|Significado|Uso|
|---|---|---|
|`-o`|Offset|Indica dónde comienza la partición/filesystem|
|`-r`|Recursive|Recorre directorios recursivamente|
|`-a`|Allocated|Trabaja con elementos asignados|
|`-d`|Deleted|Trabaja con elementos eliminados|
|`-m`|MAC/Boddyfile|Formato utilizado para generar timelines|
|`-f`|File system type|Especifica manualmente el tipo de filesystem|
|`-i`|Image type|Especifica el tipo de imagen|
|`-h`|Help|Muestra la ayuda de la herramienta|

> Las opciones disponibles dependen de la herramienta específica. Antes de utilizar una opción, es recomendable consultar su documentación con `-h`.

---

## 🔬 Flujo de trabajo recomendado

Un flujo general para analizar una imagen de disco con The Sleuth Kit puede ser:

```bash
# 1. Identificar particiones
mmls disk.img

# 2. Identificar el filesystem
fsstat -o <offset> disk.img

# 3. Listar el contenido
fls -o <offset> disk.img

# 4. Buscar recursivamente
fls -o <offset> -r disk.img

# 5. Buscar archivos de interés
fls -o <offset> -r disk.img | grep -i <keyword>

# 6. Analizar un inodo
istat -o <offset> disk.img <inode>

# 7. Recuperar el contenido
icat -o <offset> disk.img <inode>

# 8. Guardar el contenido recuperado
icat -o <offset> disk.img <inode> > recovered_file
```

La lógica general es:

```text
Imagen de disco
      │
      ▼
    mmls
      │
      ▼
Identificar particiones
      │
      ▼
   fsstat
      │
      ▼
Identificar filesystem
      │
      ▼
    fls
      │
      ▼
Explorar archivos/directorios
      │
      ▼
    istat
      │
      ▼
Analizar metadatos
      │
      ▼
    icat
      │
      ▼
Recuperar contenido
```

---

## 🛡️ Buenas prácticas en análisis forense

Cuando se trabaja con una imagen forense es recomendable:

- Trabajar siempre sobre una copia cuando sea posible.
    
- Evitar modificar la imagen original.
    
- Registrar los comandos utilizados.
    
- Registrar los offsets de las particiones.
    
- Registrar los inodos relevantes.
    
- Mantener una estructura organizada para los archivos recuperados.
    
- Calcular hashes de archivos recuperados cuando sea necesario.
    
- Documentar cada paso de la investigación.
    

Una de las principales ventajas de utilizar herramientas como The Sleuth Kit es que permiten realizar gran parte del análisis **directamente sobre la imagen**, reduciendo la necesidad de modificar o montar la evidencia original.

---