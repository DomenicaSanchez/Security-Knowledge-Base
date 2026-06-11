# 🌐 Category: Web / ACE (Arbitrary Code Execution)

#technique/python-execution #vulnerability/ace #vulnerability/rce #tool/netcat #category/web

---

## 📘 Description

**SurgoCompany™** launched a new Customer Service platform where users can submit issues and upload attachments. The system's security is flawed because it attempts to "validate" uploaded Python scripts by executing them directly using the dangerous `exec()` function.

The goal is to exploit this execution to read a file named `flag.txt` located in the same directory as the server's source code.

---

## 🛠 Tools Used

- **netcat (nc):** To interact with the challenge server.
- **Python:** For developing the exploit payload.
- **Surgo Email Platform:** To send the malicious attachment to the support system.
    

---

## ⚙️ Methodology

### 1. Source Code Review

- **File Audit:** Reviewing `src.py` revealed that the `check_attachment` function runs the content of the uploaded file to verify its "security".
- **Output Redirection:** It was identified that the standard output (`stdout`) of the executed script is sent back through the active `nc` connection.
    

### 2. Payload Construction

- **Script Logic:** I developed a Python script using the `os` library to locate and read `flag.txt` on the server.
- **Data Exfiltration:** The script simply prints the file's content so it is captured by the network tunnel.
    

**Payload Example:**

```python
import os
# Read and print the flag
if os.path.exists('flag.txt'):
    print(open('flag.txt').read())
```

### 3. Exploitation

- **Connection:** Established a session via `nc` to the target server.
- **Trigger:** Sent the malicious Python file as an attachment in a support email.
- **Result:** The server executed the code, and the flag was displayed in the terminal before the connection closed.

---

## 🏁 Flag

`pascalCTF{ch3_5urG4t4_d1_ch4ll3ng3}`