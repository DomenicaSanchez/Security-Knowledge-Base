# 🕵️ Categoría: Cryptography / Diffie-Hellman  & XOR

---

## 📘 Descripción

El reto presenta unos parámetros de un intercambio de claves Diffie-Hellman junto con un texto cifrado en hexadecimal.

El objetivo es recuperar la bandera utilizando los valores proporcionados en el archivo `message.txt`.

El error principal del reto es que el secreto privado del cliente, `b`, fue entregado directamente. Esto permite calcular el secreto compartido sin necesidad de romper el problema matemático de Diffie-Hellman.


---

## 🛠 Herramientas utilizadas

- Python 3
- `pow()` de Python para realizar exponenciación modular
- CyberChef (opcional) para realizar el XOR
- Terminal

---

## ⚙️ Metodología

### 1. Reconocimiento inicial

Primero se revisó el contenido de `message.txt`:

```bash
cat message.txt
```

El archivo contiene los siguientes valores:

- `g = 2`: generador utilizado por Diffie-Hellman.
- `p`: número primo utilizado como módulo.
- `A`: clave pública del servidor.
- `b`: secreto privado del cliente.
- `enc`: mensaje cifrado en hexadecimal.

La parte importante es que **`b` aparece directamente en el archivo**.
![[01_DH-b.png]]

En un intercambio Diffie-Hellman normal, `b` debería mantenerse secreto. Sin embargo, al conocer `A`, `b` y `p`, podemos calcular directamente:

![[02_DH-python.png]]

```text
shared = A^b mod p
```

---

### 2. Cálculo del secreto compartido

Se utilizó Python para calcular el secreto compartido:

```python
shared = pow(A, b, p)
```

Después, el código original del reto indica que solamente se utiliza el último byte del secreto:

```python
key = shared % 256
```

El resultado obtenido fue:

```text
key = 226
```

En hexadecimal:

```text
e2
```

Por lo tanto, `e2` es la clave utilizada para el XOR.
![[04_DH-shared.png]]

---

### 3. Descifrado del mensaje

El reto cifra la bandera mediante:

```python
enc = bytes([x ^ (shared % 256) for x in flag])
```

Esto significa que cada byte de la bandera fue combinado mediante XOR con la clave `e2`.

Como XOR es reversible:

```text
cifrado XOR clave = texto original
```

Se toma el valor de `enc`:

```text
928b818da1b6a499868abd91d18190d196bdd1d08781d0d4d5db9f
```

y se aplica XOR utilizando la clave:

```text
e2
```

![[04-DH-Solution.png]]

---

## 🧠 ¿Cuál fue el error del reto?

El intercambio Diffie-Hellman está diseñado para que las partes puedan obtener un secreto compartido sin revelar sus secretos privados.

Normalmente tendríamos:

```text
Servidor:
a = secreto privado
A = g^a mod p

Cliente:
b = secreto privado
B = g^b mod p
```

y ambos calculan:

```text
shared = g^(ab) mod p
```

En este reto, sin embargo, se proporcionó:

```text
A
b
p
```

Por lo que podemos calcular directamente:

```text
shared = A^b mod p
```

No fue necesario romper Diffie-Hellman ni calcular el secreto `a`.

---

## 🏁 Flag

```text
picoCTF{dh_s3cr3t_32ec2679}
```

**Reto resuelto por:** [Doménica Sánchez](https://github.com/DomenicaSanchez)
