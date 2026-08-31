# 📚 Fundamentos de RSA y el Ataque de Wiener 

> RSA y el Ataque de Wiener explicados de forma conceptual, paso a paso y con analogías sencillas, manteniendo la precisión matemática pero haciéndolo accesible para cualquier persona que esté comenzando en criptografía.
## 💡 La Idea en 30 Segundos

- **¿Qué es RSA?** Un candado digital. Hay una **clave pública** para cerrar el candado (cifrar) y una **clave privada** para abrirlo (descifrar).

- **¿Qué es el Ataque de Wiener?** Si la clave privada es "demasiado corta" o pequeña (para ahorrar cómputo), existe un atajo matemático que permite adivinar la clave privada exacta usando solo la clave pública, **sin necesidad de romper el candado por fuerza bruta**.

## 1. ¿Cómo funciona RSA?
El sistema se apoya en una idea matemática clave: **es muy fácil multiplicar dos números primos grandes, pero casi imposible separar el resultado de vuelta en esos dos primos** (problema de factorización).
### 1.1 Preparando la Maquinaria (Claves)
1. **Elegir dos primos secretos ($p$ y $q$):** Son la base de toda la seguridad.

2. **Crear el Módulo Público ($n$):**
$$n = p \cdot q$$
	_Este número $n$ se comparte con todo el mundo.
	
3. **Calcular la Función Totiente ($\phi(n)$):**
$$\phi(n) = (p - 1)(q - 1)$$
    
    _Representa cuántos números menores que $n$ no comparten factores con él. Es un secreto que solo se conoce si sabes $p$ y $q$._
    
2. **Elegir el exponente público ($e$):** Normalmente un número pequeño y estándar (como 65537).
    
3. **Calcular el exponente privado ($d$):** Es la "inversa" matemática de $e$ módulo $\phi(n)$. Cumple la regla:      
$$e \cdot d \equiv 1 \pmod{\phi(n)} \quad \implies \quad e \cdot d - k \cdot \phi(n) = 1$$

### 1.2 El Proceso de Cifrado y Descifrado

- **Para Cifrar (Público):** Conviertes tu mensaje $m$ en texto cifrado $c$:        
$$c \equiv m^e \pmod n$$
    
- **Para Descifrar (Privado):** Recuperas el mensaje original usando tu clave secreta $d$:
$$m \equiv c^d \pmod n$$

## 2. La Vulnerabilidad: ¿Por qué falla cuando $d$ es muy pequeña?

### 2.1 La Intuición

Para que el proceso de descifrado $m = c^d \pmod n$ sea rápido, un desarrollador descuidado podría intentar elegir un número $d$ muy pequeño.

Sin embargo, en la ecuación clave:
$$e \cdot d - k \cdot \phi(n) = 1$$

Si $d$ es muy pequeño, el número $e$ se ve obligado a ser **gigantesco** (casi del mismo tamaño que el módulo $n$). Esto crea una fuga de información imprevista: **la fracción de la clave pública $\frac{e}{n}$ se vuelve una copia casi exacta de la fracción secreta $\frac{k}{d}$**.

```
    [ e / n ]  <--- Conocido por todos
       ≈ 
    [ k / d ]  <--- ¡Secreto! (Contiene la clave privada d)
```

## 3. El Ataque de Wiener al Detalle

### 3.1 El Teorema de Wiener (El Límite de Seguridad)

Michael Wiener demostró en 1990 que si los primos $p$ y $q$ tienen un tamaño similar y la clave privada $d$ cumple la siguiente condición:
$$d < \frac{1}{3} n^{1/4}$$

Entonces la fracción $\frac{k}{d}$ se encuentra **garantizada** dentro de las simplificaciones matemáticas de la fracción pública $\frac{e}{n}$

### 3.2 ¿Cómo se calcula? (El truco de las Fracciones Continuas)

Una **fracción continua** es simplemente una forma de aproximar números complejos mediante fracciones cada vez más precisas (llamadas _convergentes_).

1. **Expandir la clave pública:** Expresamos $\frac{e}{n}$ como una fracción continua:      
$$\frac{e}{n} = [a_0; a_1, a_2, a_3, \dots]$$
    
2. **Generar aproximaciones (Convergentes):** Calculamos la lista de mejores aproximaciones simplificadas:    
$$\frac{p_0}{q_0}, \quad \frac{p_1}{q_1}, \quad \frac{p_2}{q_2}, \quad \dots$$
    
3. **Probar candidatos:** Debido al Teorema de Legendre sobre aproximación diofántica, una de estas fracciones simplificadas $\frac{p_i}{q_i}$ **será exactamente la fracción $\frac{k}{d}$**.
    - El denominador $q_i$ de esa fracción es tu clave privada $d$.

## 4. Algoritmo Paso a Paso para Resolverlo

```
  [ Obtener e y n ]
         │
         ▼
  [ ¿'e' es tan grande como 'n'? ] ──► NO ──► (No aplica Wiener)
         │
        SÍ
         ▼
  [ Calcular Fracciones Continuas de e/n ]
         │
         ▼
  [ Para cada convergente (k / d): ]
         │
         ├─► Calcular candidate_phi = (e*d - 1) / k
         ├─► Resolver ecuación: x² - (n - candidate_phi + 1)x + n = 0
         │
         └─► ¿Las soluciones son números enteros (p y q)?
                   │
                  SÍ ──► ¡Clave d Encontrada! ──► Descifrar: m = c^d mod n
```

## 5. Muestra en python

```python
from Crypto.Util.number import long_to_bytes
import owiener  # pip install owiener

# 1. Datos del reto
n = 0x...  # Módulo RSA
e = 0x...  # Exponente público gigante
c = 0x...  # Texto cifrado

# 2. Ataque de Wiener (calcula d usando fracciones continuas)
d = owiener.attack(e, n)

if d:
    # 3. Descifrar el mensaje: m = c^d mod n
    m = pow(c, d, n)
    print(f"[🏁] Flag: {long_to_bytes(m).decode()}")
else:
    print("[-] El ataque falló.")
```
## 5. Resumen Visual de Reconocimiento (Cheatsheet para CTFs)

Cuando analices un reto de RSA en un CTF, usa esta tabla para detectar inmediatamente si debes usar el Ataque de Wiener:

| **Indicador**                        | **RSA Seguro**                       | **Vulnerable a Wiener (Small d)**             |
| ------------------------------------ | ------------------------------------ | --------------------------------------------- |
| **Tamaño del exponente público $e$** | Pequeño (ej. $e = 65537$)            | **Gigante** (casi de los mismos bits que $n$) |
| **Tamaño de la clave privada $d$**   | Del mismo tamaño que $n$             | **Muy pequeño** ($d < \frac{1}{3} n^{1/4}$)   |
| **Estructura del reto**              | Te dan $n$, $e$, $c$ estándar        | Te dan $n$ (ej. 2048 bits) con $e$ gigante    |
| **Técnica de resolución**            | Factorizar $n$ o buscar otros fallos | **Fracciones continuas en $\frac{e}{n}$**     |
