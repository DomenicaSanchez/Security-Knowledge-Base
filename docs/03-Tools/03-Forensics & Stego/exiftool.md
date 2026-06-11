#tool/exiftool 
___
## 🕵️ Information
**What is ExifTool and why is it useful?**  
ExifTool is a command-line tool used to read, write, and edit metadata. Metadata is “data about data,” like camera model, date, GPS coordinates, or hidden comments inside a file.

**Why is it useful in CTFs?**  
Flags are often hidden in metadata fields such as _Author_, _Comment_, _Copyright_, or GPS data. ExifTool lets you inspect all of that.

---

## ⚡Quick Cheat Sheet

### 📜 Show all metadata
`exiftool file.ext`

### 🔍  Search for a keyword
Useful for spotting flags, passwords, or hints:
`exiftool file.ext | grep -i "flag"`

### 🧩  Show only common metadata
A cleaner output:
`exiftool -common file.ext`

### 📍 Extract GPS information
`exiftool -gps:all image.jpg`

### 🖼️  Extract embedded thumbnail
`exiftool -b -ThumbnailImage image.jpg > thumb.jpg`

### ✏️ Edit metadata
`exiftool -Author="Admin" file.pdf`