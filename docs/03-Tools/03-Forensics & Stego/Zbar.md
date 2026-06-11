#tool/tool-zbar

______

## 🕵️ Information

**What is ToolName?**  
zbar is an open source software for reading bar code from videos in real time and images files.

Zbarimg is a command-line to scans and decodes QR codes and barcodes from image files like:
- PNG
- JPEG
- TIFF
- GIF
- PDF
- PostScript (PS)
Zbrcam is a command- line to scans and decodes QR codes and barcodes from videos in real time froma web cam and support video formats like:
- YUYV
- MJPG (MJPEG)
- GREY
- Y800
-
**Why is it useful in CTFS?**  
zbar can you help to stract hifdden data quickly and efficiently and common uses are:
- Extract hidden flags in QR codes from images or GIFs
- Process multiple QR codes at once
- Combine with other tools like `tr`, `sort`, or `uniq` to reconstruct flags.

---

## ⚡ Installation

### Install using package manager

```bash
sudo apt install zbar-tools
```
### Verify installation

```bash
zbarimg --help
```

---

## ⚡ Quick Cheat Sheet

### 🕵️ Scan QR code from image
Read and decode a QR code from a file:
```bash
zbarimg nombre_archivo.png
```
### 🧼 Clean output (no QR-Code: prefix)
Get only the raw data:
```bash
zbarimg --raw nombre_archivo.png   
```
### 🔍 Scan from inverted/dark QR
If colors are reversed, invert the image on the fly:
```bash
zbarimg --set test-inverted <(convert nombre_archivo-dark.png -negate -)   
```
### 📦 Process multiple images
Scan all PNGs in a folder:
```bash
zbarimg *.png 
```

