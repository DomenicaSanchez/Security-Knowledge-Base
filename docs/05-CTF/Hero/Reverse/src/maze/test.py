#!/usr/bin/env python3
from pwn import *

# Configuración del servidor del reto
HOST = "reverse.heroctf.fr"
PORT = 7001

# Ruta a tu archivo de solución en C
VALID_PASS_FILE = "src/valid_pass.c"

def main():
    # Conectar al servicio remoto
    log.info(f"Conectando a {HOST}:{PORT}")
    try:
        conn = remote(HOST, PORT)
    except:
        log.error("No se pudo conectar. Verifica tu internet o si el CTF sigue activo.")
        return

    # Leer el archivo valid_pass.c local
    log.info(f"Leyendo {VALID_PASS_FILE}")
    try:
        with open(VALID_PASS_FILE, 'rb') as f:
            code = f.read()
    except FileNotFoundError:
        log.error(f"El archivo {VALID_PASS_FILE} no fue encontrado.")
        log.error("Asegúrate de crear 'valid_pass.c' dentro de la carpeta 'src/'")
        conn.close()
        return

    # Esperar al prompt del servidor
    # El servidor suele enviar texto antes de pedir el código.
    # Usamos recvuntil para sincronizar.
    try:
        conn.recvuntil(b"code (end with EOF or Ctrl+D):")
    except EOFError:
        log.warning("El servidor no envió el prompt esperado, enviando código de todas formas...")

    # Enviar el código al servidor
    log.info(f"Enviando {len(code)} bytes de código...")
    conn.send(code)

    # Enviar EOF para señalar el fin de la entrada (simula Ctrl+D)
    conn.shutdown('send')

    # Recibir e imprimir toda la salida (hasta que el servidor cierre)
    log.info("Recibiendo respuesta del servidor...")
    response = conn.recvall().decode("utf-8", errors="ignore")
    
    print("\n" + "="*40)
    print(response)
    print("="*40 + "\n")

    conn.close()

if __name__ == "__main__":
    main()
