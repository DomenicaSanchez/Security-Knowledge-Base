#tool/magic_number
___
**Magic numbers** are specific bytes at the **very beginning of a file**.  
They tell the operating system and applications **what type of file it is** (PNG, JPG, PDF, ZIP, etc.).
They act like the file’s **ID card**. Programs do **not** trust the file extension (.jpg, .png).  They trust **these bytes**.
- [[#Why do files look “corrupted”?]]
- [[#Why do you need to repair corrupt files?]]
- [[#Common Magic Numbers (Table)]]
- [[#Forms to fix]]
---
## Why do files look “corrupted”?

A file looks corrupted when:
- the **magic number doesn’t match** the real file type, or
- the first bytes are missing or damaged.
    
Example:  
A file is named `image.jpg`, but the magic number belongs to PNG → the viewer says it's “corrupted.”

---
## Why do you need to repair corrupt files?

In CTFs and forensics, files are often:
- renamed,
- intentionally modified,
- partially broken,
- or damaged during transfer.
Fixing a file usually means **restoring the correct magic number** at the start.

---
## Common Magic Numbers (Table)

| File Type      | Magic Number (Hex)        | Notes                            |
| -------------- | ------------------------- | -------------------------------- |
| **PNG**        | `89 50 4E 47 0D 0A 1A 0A` | Always starts with these 8 bytes |
| **JPG / JPEG** | `FF D8 FF`                | Begins with SOI marker           |
| **PDF**        | `25 50 44 46`             | Represents `%PDF`                |
| **ZIP**        | `50 4B 03 04`             | Standard ZIP header              |
| **GIF**        | `47 49 46 38`             | Starts with `GIF8`               |
| **MP3**        | `49 44 33`                | Begins with ID3 tag (if present) |
| **RAR**        | `52 61 72 21`             | “Rar!”                           |
____
## Forms to fix
### **Option 1: Direct Editing (hexeditor)**
```bash
# Open the corrupted file 
hexeditor archivo_corrupto  

# Edit the magic number:
	# The cursor will be on the first byte. 
	# Type: f f d 8 
	# The line should look like: FF D8 FF E0...  
	# Save and exit Ctrl + X y Enter  

# Open the image 
eog archivo_corrupto
```
### **Option 2: Convert to Text (xxd)**
```bash
# Dump binary to text 
xxd archivo_corrupto > dump.txt 

# Edit the text dump 
nano dump.txt 

# Go to the first line: 00000000: 5c78 ffe0... 
# Replace 5c78 with ffd8 
# Final result: 00000000: ffd8 ffe0...  
# Save and exit: 
	# Ctrl + O
	# Enter 
	# Ctrl + X  

# Rebuild the fixed file 
xxd -r dump.txt > archivo_arreglado.jpg  

# Open the repaired image 
eog archivo_arreglado.jpg
```

