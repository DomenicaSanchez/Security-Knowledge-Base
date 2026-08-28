# 🕵️ Category: Cryptography / RSA

## 📘 Description

El reto **Small trouble** presenta una implementación de RSA con una grave falla de diseño: la clave privada $d$ es demasiado pequeña (solo 256 bits para un módulo $n$ gigante de 2096 bits). Aunque no podemos romper $n$ mediante fuerza bruta, esta flaqueza permite aplicar el **Ataque de Wiener**, un método que usa fracciones continuas para deducir $d$ directamente desde la clave pública $e$ y descifrar el mensaje $c$.

## 🛠 Tools Used

- **Python 3**
- **Librería `owiener`** (para automatizar el cálculo de fracciones continuas)
- **PyCryptodome** (`Crypto.Util.number` para conversión de bytes)

## ⚙️ Methodology

### 1. Reconocimiento Inicial

Al revisar el código fuente o las variables proporcionadas ($n$, $e$, $c$), destacan dos anomalías clave:
![[01_WA-message.png]]

![[02_WA-cod.png]]

- **Módulo $n$:** 2096 bits (tamaño seguro estándar).
- **Exponente público $e$:** Es un número monstruoso de ~600 dígitos decimales (casi del mismo tamaño que $n$).
- **Generación de $d$:** Se utilizó `d = getPrime(256)`, creando una clave privada de solo 256 bits.

### 2. Identificación de la Vulnerabilidad

Un $e$ tan grande ocurre únicamente cuando $d$ se genera muy pequeño. Para confirmar si es vulnerable al **Ataque de Wiener**, validamos la condición de seguridad:

$$d < \frac{1}{3} n^{1/4}$$

- Para nuestro $n$ de 2096 bits, $n^{1/4} \approx 2^{524}$ bits.
- Como nuestra $d$ es de solo 256 bits, cumple ampliamente la regla ($2^{256} < \frac{1}{3} \cdot 2^{524}$). La vulnerabilidad queda confirmada.
### 3. Explotación y Resolución

El ataque aprovecha que la fracción pública $\frac{e}{n}$ es una aproximación casi exacta de la fracción secreta $\frac{k}{d}$:

1. **Fracciones Continuas:** Se expande $\frac{e}{n}$ en fracciones continuas para obtener aproximaciones simplificadas (convergentes).
2. **Búsqueda de $d$:** El denominador de una de estas aproximaciones es nuestra clave privada $d$.
3. **Descifrado:** Con $d$ recuperada, se despeja el mensaje original mediante exponenciación modular:
$$m = c^d \pmod n$$

**Script de guía para la Explotación:**
```python
from Crypto.Util.number import long_to_bytes
import owiener

# 1. Recuperar d usando el ataque de Wiener
d = owiener.attack(e, n)

# 2. Descifrar el mensaje cifrado c
if d:
    m = pow(c, d, n)
    print(long_to_bytes(m).decode())
```

## 🏁 Flag

`flag{w13n3r5_4774ck_r3c0v3r5_sm4ll_d_34sy}`

---
**Reto resuelto por:** [Doménica Sánchez](https://github.com/DomenicaSanchez)