from pwn import *
import base64
import cv2
import numpy as np

HOST = "prog.heroctf.fr"
PORT = 8000

io = remote(HOST, PORT)

def count_moles(img_bytes):
    np_arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Threshold para la tierra del topo
    lower = np.array([5, 80, 20])
    upper = np.array([25, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    # Limpieza de ruido
    kernel = np.ones((7, 7), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Contar componentes conectadas
    n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)

    return n_labels - 1  # restar background



while True:
    line = io.recvline()
    if b"IMAGE:" in line:
        b64img = io.recvline().strip()
        log.info(f"Got image (length {len(b64img)})")
        io.recvuntil(b">> ")

        # Convertir base64 → bytes
        img_bytes = base64.b64decode(b64img)

        # Guardar y devolver respuesta dummy
        answer = count_moles(img_bytes)

        io.sendline(str(answer).encode())

    elif b"Wrong answer!" in line or b"Hero" in line:
        print(line.decode().strip())
        io.close()
        break
    else:
        log.info(line.decode().strip())
