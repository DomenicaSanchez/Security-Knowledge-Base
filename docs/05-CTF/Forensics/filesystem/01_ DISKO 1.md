# 🕵️ Category: Forensics / filesystem

---

## 📘 Description
Can you find the flag in this disk image?Download the disk image ../src/disko-1.dd.gz

---

## 🛠 Tools Used
- #tool/string
---
## ⚙️ Methodology
First, I decompressed the file using `gzip` [[Commands & Tools]]
`gzip -d disko-1.dd.gz`
![[05-CTF/Forensics/filesystem/img/01_decompressed.png]]

Then, using `strings` combined with `grep`, I was able to find the flag:
`strings disko-1.dd | grep "CTF"`
![[01_findTheFlag.png]]

____
## 🏁 Flag
picoCTF{1t5_ju5t_4_5tr1n9_be6031da}
