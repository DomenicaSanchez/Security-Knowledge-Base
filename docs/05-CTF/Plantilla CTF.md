# 🕵️ Category: Forensics / Metadata / PDF

---

## 📘 Description
A PDF file that appears to contain meaningless or corrupted content.  
The challenge indicates that the real information is hidden in the metadata of the document.

---

## 🛠 Tools Used
- exiftool
- pdfinfo
- strings (optional)
- hexdump (optional)

---

## ⚙️ Methodology

### 1. Initial Recon
- `file <filename>.pdf`
- `strings <filename>.pdf | head`

### 2. Metadata Extraction
**Using exiftool:**

____
## 🏁 Flag
(pon la flag)
