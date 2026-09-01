# 🌐 PortSwigger Lab: [Nombre del Laboratorio]

**Categoría:** [Ej: Access Control / SQL Injection / XSS / CSRF / Authentication]  
**Dificultad:** 🟢 Apprentice / 🟡 Practitioner / 🔴 Expert  
**URL del Lab:** `https://portswigger.net/web-security/...`  
**Credenciales proporcionadas:** `usuario:contraseña` (si aplica)  

---

## 📝 Lab Description & Objective

> **Descripción:** Escribe aquí la descripción del laboratorio y el contexto de la aplicación web.  
> **Objetivo:** ¿Qué se necesita lograr para resolver el laboratorio? (Ej: acceder al panel de administración, borrar un usuario, extraer la contraseña del administrador, etc.)

---

## 🛠 Tools Used

- **Herramienta principal:** Burp Suite (Community / Professional)
- **Módulos utilizados:** (Ej: Proxy / Intercept, HTTP History, Repeater, Intruder, Decoder)
- **Extensiones / Otras:** (Ej: FoxyProxy, Hackvertor, Turbo Intruder)

---

## 🔍 Phase 1: Recon & Analysis

### 1.1 Exploración Inicial
- Comportamiento de la aplicación al navegar normalmente.
- Endpoints identificados en el sitemap y HTTP history.

### 1.2 Detección de la Vulnerabilidad
- Parámetros, cookies o headers sospechosos identificados.
- Comportamiento al manipular valores en Burp Suite.

---

## 🚀 Phase 2: Exploitation & Resolution

### 2.1 Paso a paso de explotación

1. **Intercepción / Envío al Repeater:**
   - Detalle de la petición HTTP original interceptada.
2. **Manipulación del Payload:**
   - Modificación realizada (parámetro, cookie, header o método HTTP).
3. **Ejecución y Verificación:**
   - Respuesta obtenida del servidor (código de estado, contenido).

```http
GET /ejemplo HTTP/1.1
Host: target.web-security-academy.net
Cookie: session=xyz; parametro=valor_modificado
```

---

## 🏁 Resolution Proof & Status

- **Resultado:** ✅ Solved
- **Acción final completada:** (Ej: Usuario `carlos` eliminado, sesión de admin obtenida).

---

## 🛡️ Mitigation & Remediation

- ¿Cómo se previene esta vulnerabilidad en el backend?
- Buenas prácticas de desarrollo seguro (Secure Coding).

---

## 💡 Key Takeaways & Lessons Learned

- **Concepto clave:** 
- **Tips para Burp Suite:** 
