# 🕵️ Category: Metadata - PDF

## 📘 Description
Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.Find the PDF file here [Hidden Confidential Document](01-confidential.pdf) and uncover the flag within the metadata.
#tool/exiftool
____
## 🛠 Tools Used
- [[exiftool]]
---

## ⚙️ Methodology
To extract metadata, I used the following command:
```
exiftool 01-confidential.pdf
``` 
To decode the Base64 string, I used:
```
echo "cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0=" | base64 -d
``` 

____
## 🏁 Flag
picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}

