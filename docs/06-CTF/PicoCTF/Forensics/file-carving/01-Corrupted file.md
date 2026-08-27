# 🕵️ Category: File carving

---

## 📘 Description
This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?Download the file src/01-file
 #tool/magic_number
____
## 🛠 Tools Used
- [[Magics numbers]]

---

## ⚙️ Methodology
I reviewed the bytes of the corrupted file and noticed that the first line didn’t start with the correct magic number.  
The hint was the word **JFIF**, meaning the magic number should be `FF D8 FF`.
![[01-Corrupted file.png]]
To fix this, I used the following commands:
![[01-Fix corrupted file.png]]
```bash
## Edit corrupted file
hexeditor 01-file

## Open file
eog 01-file
```

![[01- solution corrupted file.png]]
Check this link to learn more ways to solve similar cases: [[Magics numbers]]
____
## 🏁 Flag
picoCTF{r3st0r1ng_th3_by73s_939a65f5}
