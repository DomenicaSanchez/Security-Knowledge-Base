#tool/steghide 
___
## 🕵️ Information
**What is Steghide?**
**Steghide** is a command-line tool used to **hide and extract information** from files like **JPG, BMP, WAV, and AU**.  
It embeds data without altering the visual or audible appearance of the file.

**Why it's useful in CTFs**
Steghide helps you quickly:
- Extract hidden flags
- Reveal embedded text files
- Uncover data protected with passphrases
- Practice creating your own stego payloads
CTFs often hide passwords in **metadata, base64 strings, or comments** — Steghide is the tool that unlocks them.
---

## ⚡ Quick Cheat Sheet

###  🕵️Check file info
See if a file _might_ contain embedded data:
`steghide info -sf file.jpg`

### 📤 Extract hidden content
Extract and let the tool prompt for the passphrase:
`steghide extract -sf file.jpg`

Extract using a known password:
`steghide extract -sf file.jpg -p "pAzzword"`

### 📥 Embed data into an image/audio
Hide a text file inside an image:
`steghide embed -cf cover.jpg -ef secret.txt`

Embed using a password:
`steghide embed -cf cover.jpg -ef secret.txt -p "pAzzword"`

