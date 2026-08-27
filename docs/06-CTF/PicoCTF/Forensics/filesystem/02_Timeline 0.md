# 🕵️ Categoría: Forense / Metadatos / Imagen de disco

---

## 📘 Descripción

El reto proporciona una imagen de disco comprimida en formato `.img.gz`. El objetivo es analizar el sistema de archivos y construir una **línea temporal MAC utilizando Sleuth Kit** para identificar timestamps sospechosos.

El reto proporciona dos pistas:

1. **Create a Sleuthkit MAC timeline!**
    
2. **Sloppy timestomping can yield strange (very old) timestamps.**
    

La segunda pista indica que debemos buscar archivos cuyos timestamps hayan sido modificados artificialmente y presenten fechas extremadamente antiguas.

---

## 🛠 Herramientas utilizadas

- `file`
    
- `fdisk`
    
- `mmls`
    
- `fls`
    
- `mactime`
    
- `grep`
    
- `istat`
    
- `icat`
    
- `base64`
    

---

## ⚙️ Metodología

### 1. Reconocimiento inicial

Descomprimimos el archivo el archivo `.img.gz` 
![[descomprimir.png]]

Después de descomprimir el archivo `.img.gz`, se obtuvo la imagen:

```text
partition4.img
```

Primero se identificó el tipo de sistema de archivos:

```bash
file partition4.img
```

El resultado confirmó que se trataba de un sistema de archivos **EXT4**:
![[tipo_sitema_archivos.png]]

Posteriormente se comprobó la estructura de particiones:

```bash
fdisk -l partition4.img
```

![[estructura_particiones.png]]
---

### 2. Creación de la línea temporal MAC

La primera pista indicaba:

> **Create a Sleuthkit MAC timeline!**

Por ello, se utilizó `fls` para generar el archivo de cuerpo con la información de los archivos:

```bash
fls -r -m / partition4.img > partition.txt
```

![[cuerpo_sistema_archivos.png]]


Posteriormente se utilizó `mactime` para generar la línea temporal:

```bash
mactime -b partition.txt > timeline.txt
```

![[mactime.png]]

Aunque `mactime` mostró advertencias relacionadas con separadores de paquetes de Perl obsoletos, el archivo `timeline.txt` se generó correctamente.

---

### 3. Búsqueda de timestamps sospechosos

La segunda pista indicaba:

> **Sloppy timestomping can yield strange (very old) timestamps.**

Por lo tanto, se buscaron fechas inusualmente antiguas dentro de la línea temporal:

```bash
grep -E '\b(18|19)[0-9]{2}\b' timeline.txt
```

Entre los resultados apareció el siguiente registro:
![[inspeccion_timeline.png]]

El archivo sospechoso identificado fue:

```text
/bin/bcab
```

con el inode:

```text
4945
```

La fecha de **1 de enero de 1985** resultó especialmente sospechosa debido a la pista sobre timestomping.

---

### 4. Análisis del inode sospechoso

Para analizar con mayor detalle el inode `4945`, se utilizó:

```bash
istat partition4.img 4945
```

La información obtenida indicó:
![[inode_4945.png]]

```

Lo más importante fueron los timestamps:

```text
Accessed:       1985-01-01 12:00:00.150000000 (EST)
File Modified:  1985-01-01 12:00:00.150000000 (EST)
Inode Modified: 1985-01-01 12:00:00.150000000 (EST)
File Created:   1985-01-01 12:00:00.150000000 (EST)
```

Los cuatro timestamps tenían exactamente la misma fecha y hora.

Esto confirmó que `/bin/bcab` era el artefacto relevante señalado por la pista del reto y que presentaba un timestamp anormalmente antiguo.

---

### 5. Extracción del contenido

Para obtener el contenido real del archivo asociado al inode `4945`, se utilizó `icat` , luego hicimos un cat del archivo resultante

```bash
icat partition4.img 4945 > p4945.txt
```

![[revisar_inode.png]]

Se obtuvo:

```text
NzFtMzExbjNfMHU3MTEzcl9oM3JfNDNhMmU3YWYK
```

El contenido tenía el formato característico de una cadena codificada en **Base64**.

---

### 6. Decodificación

Se utilizó `base64` para decodificar la cadena:

![[decodificar_b64.png]]

El resultado fue:

```text
71m311n3_0u7113r_h3r_43a2e7af
```

---

## 🏁 Flag

```text
71m311n3_0u7113r_h3Jr_43a2e7af
```