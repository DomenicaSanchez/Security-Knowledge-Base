#!/usr/bin/env python3
from pwn import *

# Configuración del servidor remoto del CTF
HOST = "reverse.heroctf.fr"
PORT = 7002

# Ruta a tu archivo local
VALID_PASS_FILE = "src/valid_pass.c"

def main():
    # Conectando al servicio remoto
    log.info(f"Conectando a {HOST}:{PORT}")
    conn = remote(HOST, PORT)

    # Leyendo el archivo local valid_pass.c
    log.info(f"Leyendo {VALID_PASS_FILE}")
    try:
        with open(VALID_PASS_FILE, 'rb') as f:
            code = f.read()
    except FileNotFoundError:
        log.error(f"¡Archivo {VALID_PASS_FILE} no encontrado!")
        return

    # Enviando el código al servidor
    log.info(f"Enviando {len(code)} bytes de código")
    conn.send(code)

    # Enviamos EOF para indicar que terminamos de enviar el archivo
    conn.shutdown('send')

    # Recibir y mostrar toda la salida (aquí debería salir la flag)
    log.info("Recibiendo respuesta del servidor...")
    response = conn.recvall().decode("utf-8", errors="ignore")
    print("\n" + "="*40)
    print(response)
    print("="*40 + "\n")

    conn.close()

if __name__ == "__main__":
    main()
