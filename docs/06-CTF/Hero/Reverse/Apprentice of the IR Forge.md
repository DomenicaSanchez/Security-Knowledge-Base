# ⚙️ Category: Reverse Engineering / Compilation / Automation

#technique/brute-force #technique/scripting #tool/pwntools #tool/gcc #category/reverse

---

## 📘 Description

**Author:** Teddysbears

The **Apprentice of the IR Forge** challenge takes place in a "molten realm" of computation where code transformations are key. The objective is to provide a C source file to a remote server via TCP. The server expects a specific function named `SWORD_OF_THE_HERO` with a precise (but unknown) return type and argument list to unlock the flag.

---

## 🛠 Tools Used

- **Python:** For automation and brute-forcing logic.
- **Pwntools:** To manage the TCP connection and interact with the remote service.
- **Docker:** To replicate the server environment locally for testing.
- **GCC (implicitly):** The remote server uses a compiler to process the submitted C code.
    

---

## ⚙️ Methodology

### 1. Initial Recon

The challenge provided an archive containing a Python submission script and a Dockerfile. Analysis of the environment suggested that the server compiles the submitted C code and checks for a specific function signature. If the signature does not match what the server expects, it returns a "Nope" message.

### 2. Strategy: Automated Brute Force

Since the function name `SWORD_OF_THE_HERO` was known, but the signature was not, I developed a Python script (`brute_force.py`) to systematically test combinations of:

- **Return Types:** `void`, `int`, `long`, `char*`, etc.
- **Argument Lists:** Varying numbers of integers, pointers, and themed names.

### 3. Exploitation Script

The script automatically generates a C file, sends it to the server, and checks the response for the flag.

```python
#!/usr/bin/env python3
from pwn import *

# Configuration
HOST = "reverse.heroctf.fr"
PORT = 7002
VALID_PASS_FILE = "src/valid_pass.c"

# Possible return types and argument lists to test
return_types = ["void", "int", "char*", "long", "long long", "void*"]
argument_lists = [
    "", "int a", "int a, int b", "char* s", "long a", "int strength, int magic"
]

def create_c_file(ret_type, args):
    """Generates the C file content with the given signature."""
    return_stmt = "return;" if ret_type == "void" else "return 0;"
    code = f"""
#include <stdlib.h>
int main() {{ return 0; }}
{ret_type} SWORD_OF_THE_HERO({args}) {{ {return_stmt} }}
"""
    with open(VALID_PASS_FILE, "w") as f:
        f.write(code)

def test_signature(ret_type, args):
    """Tests a specific signature against the server."""
    create_c_file(ret_type, args)
    try:
        conn = remote(HOST, PORT, level='error')
        with open(VALID_PASS_FILE, 'rb') as f:
            conn.send(f.read())
        conn.shutdown('send')
        response = conn.recvall(timeout=3).decode("utf-8", errors="ignore")
        conn.close()
        
        if "Hero{" in response:
            print(f"[+] SUCCESS! Signature: {ret_type} SWORD_OF_THE_HERO({args})")
            print(f"[+] Flag: {response}")
            return True
        return False
    except Exception:
        return False

# Main loop iterates through combinations until success
for ret in return_types:
    for args in argument_lists:
        if test_signature(ret, args):
            break
```

### 4. Results

The script successfully identified the correct signature and captured the flag from the server response.

---

## 🏁 Flag

`Hero{Yu0_f0rG3d_y0uR_oWn_p47H_4pPr3nT1cE}`