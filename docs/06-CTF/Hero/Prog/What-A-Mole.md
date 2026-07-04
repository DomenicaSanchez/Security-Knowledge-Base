This writeup for the **Whac-A-Mole** challenge focuses on **Image Processing** and **Network Automation**. It has been translated into English with reusable tags for your database.

---

# 💻 Category: Programming / Image Processing / Automation

#technique/automation #technique/image-processing #tool/opencv #tool/pwntools #tool/numpy #category/prog

---

## 📘 Description

The **Whac-A-Mole** game requires counting the number of moles in an image provided over a TCP connection. Because the background and moles have distinct colors, the most effective approach is to create a color mask and use the `connectedComponentsWithStats` function from OpenCV to count the elements.

---

## 🛠 Tools Used

- **Python**: For automation and logic.    
- **OpenCV (cv2)**: For image processing and masking.
- **NumPy**: For handling image arrays.
- **Pwntools**: To handle the TCP connection and server interaction.

---

## ⚙️ Methodology

### 1. Environment Setup

A virtual environment was created on Kali Linux to install the necessary libraries for image processing and network communication.

```bash
python3 -m venv ~/mi_entorno
source ~/mi_entorno/bin/activate ## activate
pip install opencv-python numpy pwntools
```

### 2. Initial Recon & Scripting

Using the provided template, an initial script (`Solve.py`) was developed to connect to the server, receive the Base64-encoded image, and save it as `last.png` for visual inspection.


```python
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

    # Save image for inspection
    cv2.imwrite("last.png", img)

    # Optional DEBUG:
    print("[*] Saved image to last.png")

    # *** TEST MODE: return 0 until image is analyzed ***
    return 0

while True:
    line = io.recvline()
    if b"IMAGE:" in line:
        b64img = io.recvline().strip()
        log.info(f"Got image (length {len(b64img)})")
        io.recvuntil(b">> ")

        # Convert base64 → bytes
        img_bytes = base64.b64decode(b64img)

        # Process and return response
        answer = count_moles(img_bytes)
        io.sendline(str(answer).encode())

    elif b"Wrong answer!" in line or b"Hero" in line:
        print(line.decode().strip())
        io.close()
        break
    else:
        log.info(line.decode().strip())
```

![[01WM_last.png]]

### 3. Image Analysis & Masking

After inspecting `last.png`, the HSV color space was used to create a threshold mask for the "dirt" area surrounding the moles. Noise was cleaned using morphological operations (`MORPH_OPEN` and `MORPH_CLOSE`) before counting the components.

```python
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

    # Threshold for the mole's dirt/ground
    lower = np.array([5, 80, 20])
    upper = np.array([25, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    # Noise cleanup
    kernel = np.ones((7, 7), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Count connected components
    n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask)

    return n_labels - 1  # subtract 1 for the background
```

### 4. Exploitation & Flag Capture

Running the modified solver allowed the script to automatically process multiple images and submit the correct counts, eventually receiving the flag from the server.

---

## 🏁 Flag

`Hero{...}`