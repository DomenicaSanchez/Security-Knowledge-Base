This writeup for **Very Simple Framer** focuses on **Image Steganography** through pixel-level analysis of a border. It has been translated into English with reusable tags for your database.

---

# 🖼️ Category: Steganography / Image Forensics

#technique/image-forensics #technique/scripting #tool/pillow #category/steganography

---

## 📘 Description

**Author:** Marco Balducci (`@Mark-74`)

This challenge provides a JPG image (`output.jpg`) that appears normal but features an artificially added 1-pixel frame. Along with the image, a Python script (`chal.py`) is provided, which demonstrates how a binary message was encoded into the colors (black/white) of that specific border.

---

## 🛠 Tools Used

- **Python (PIL/Pillow):** For image processing and pixel manipulation.
- **chal.py:** Used for reverse-engineering the encoding algorithm.


---

## ⚙️ Methodology

### 1. Script Analysis

- **Encoding Pattern:** Analyzing `chal.py` revealed that the message is converted to binary and placed along the border in a specific sequence: $Top \rightarrow Right \rightarrow Bottom \rightarrow Left$.
- **Bit Representation:** The bits are represented by specific pixel colors: `0` corresponds to black `(0,0,0)` and `1` corresponds to white `(255,255,255)`.

### 2. Extraction Logic

- **Reverse Scripting:** I developed a retrieval script to traverse the border coordinates in the exact same order defined in the original code.
- **Binary Reconstruction:** For each pixel along the path, the script evaluates whether the color is white or black to reconstruct the original bit string.
- **ASCII Conversion:** The resulting bits were grouped into 8-bit blocks (bytes) and converted from binary to plain text ASCII.
    

---

## 🏁 Flag

`pascalCTF{Wh41t_wh0_4r3_7h0s3_9uy5???}`