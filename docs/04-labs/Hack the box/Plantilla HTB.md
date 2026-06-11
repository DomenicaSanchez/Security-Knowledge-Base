# 🖥️ HTB: [Nombre de la Máquina]

**Dificultad:**  🟢 Fácil / 🟡 Media / 🔴 Difícil
**OS:** [🐧 Linux / 🪟 Windows
**IP:** `10.10.XX.XX`

---

## 📝 Executive Summary

> Escribe aquí un párrafo breve que resuma la experiencia general. ¿Fue una máquina de Active Directory? ¿Hubo mucho pivoting? ¿Fue puramente explotación web?

---

## 🛠 Tools Used

- **Enumeración:** (Ej: Nmap, GoBuster, Enum4linux)
- **Acceso:** (Ej: Burp Suite, Metasploit, Reverse Shells)
- **Escalada:** (Ej: LinPeas, WinPeas, BloodHound)

---

## 🔍 Phase 1: Enumeration

### 1.1 Network Scanning

```
# Pega aquí el comando exacto de Nmap que usaste
```

- **Puertos Abiertos:** (Lista de puertos y servicios detectados)
- **Notas de servicios:** (Versiones detectadas, banners interesantes, etc.)

### 1.2Web Reconnaissance

- **Directorios hallados:** (Resultados de Fuzzing)
- **Subdominios:** (Si tuviste que hacer Virtual Hosting)
- **Tecnologías:** (Wappalyzer, CMS detectado, lenguajes)

---

## 🚀 Phase 2: Exploitation (User Flag)

### 2.1 Vulnerability Discovery

Explica cómo encontraste el punto de entrada.
> **Hallazgo:** Se encontró una versión vulnerable de `[Software]` en el puerto 80.
- **Vector de entrada:** (Explica cómo pasaste del escaneo a la sospecha de una vulnerabilidad)
- **CVE o CWE:** (Si aplica, indica el código de la vulnerabilidad)

### 2.2 Gaining Access

1. **Preparación:** (Modificaciones al exploit, configuración de listeners en Netcat)
2. **Ejecución:** (Comando ejecutado para obtener acceso)
3. **Intrusión:** (Pega aquí la salida de la shell inicial)

**🚩 User Flag:** `[PEGA_AQUÍ_EL_HASH]`

---

## ⚡ Phase 3: Privilege Escalation (Root Flag)

### 3.1 Local Enumeration

- **Usuario actual:** (Nombre de usuario y grupos: `id` o `whoami /all`)
- **Vectores encontrados:** (Menciona si encontraste archivos SUID, permisos de Sudo, tareas Cron, o credenciales en archivos de config)

### 3.2 Path to Root

1. **Procedimiento:** (Pasos seguidos para escalar privilegios)
2. **Explotación:** (Comandos usados para convertirte en root/system)

**🚩 Root Flag:** `[PEGA_AQUÍ_EL_HASH]`

---

## 📖 Notas Post-Explotación

- **Credenciales extraídas:** (Tabla de usuarios y contraseñas encontrados)
- **Archivos interesantes:** (Rutas de archivos de configuración o bases de datos)

---

## 💡Lessons Learned & Tips

- **¿Qué aprendí?:** (Técnica nueva, herramienta nueva o concepto teórico)
- **¿Qué me retrasó?:** (Errores cometidos o "rabbit holes" donde caíste)