# 🕵️ Category: Steganography

---

## 📘 Description
How about some hide and seek?Download this file ../src/01_unknown.zip

---

## 🛠 Tools Used
- [[exiftool]]

---
## ⚙️ Methodology
I extracted the contents of the ZIP file using the command: `unzip -d 01_unknown.zip`
![[05-CTF/Forensics/steganography/img/01_decompressed.png]]

I inspected the metadata of the JPG file with:  `exiftool ukn_reality.jpg `
![[01_analyst-metadata.png]]

I decoded the suspicious Base64 string found in the metadata
`echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==" | base64 -d`
____
## 🏁 Flag
picoCTF{ME74D47A_HIDD3N_3b9209a2}
