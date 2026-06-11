# 🕵️ Category: Forensics / file analysis

---

## 📘 Description
You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.Download the jpg image ../src/01-src.jpg

---

## 🛠 Tools Used
#tool/exiftool 
#tool/steghide

---

## ⚙️ Methodology

I analyzed the image using `exiftool` and identified a suspicious Base64-encoded string.

![[01_analyse img.png]]

After decoding the Base64 string, I found the entry `steghide:cEF6endvcmQ=`.  
The value `cEF6endvcmQ=` was also Base64, so I decoded it to obtain the password:
![[02_decoder and identified.png]]

Using the recovered password, I extracted the hidden data with:
`steghide extract -sf 01-src.jpg` 
When prompted, I entered the password `pAzzword`, which successfully revealed the embedded text.
![[03_decoder and obtained txt.png]]

Review: [[Commands & Tools]] [[steghide]]
____
## 🏁 Flag
**flag**: picoCTF{h1dd3n_1n_1m4g3_871ba555}
