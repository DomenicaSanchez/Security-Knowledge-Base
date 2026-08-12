# 🕵️ Category: Crypto / Length Extension Attack / Flask

---

## 📘 Description

**Challenge Description**

> "SecureVault signs every download link so you can't grab the files you're not meant to. The dev team is very confident about this."

The challenge provides a compressed asset named `public.zip`, which contains the source code of the application. The objective is to bypass the cryptographic signature verification protecting download tokens in order to access a restricted resource (`private/flag.txt`) hosted on a remote Flask server.

The application implements its own message authentication mechanism using the following construction:

```text
SHA256(SECRET_KEY || message)
```

Since SHA-256 follows the Merkle-Damgård construction, this implementation is vulnerable to a **Length Extension Attack**, allowing an attacker to generate a valid signature for an extended message without knowing the secret key.

Additionally, Flask keeps the **last occurrence** of duplicated query parameters. By appending a second `file` parameter (`file=private/flag.txt`), the original value is overridden, allowing unauthorized access to the protected file while preserving a valid signature.

---

## 🛠 Tools Used

- #script/length_extension_attack 
---

## ⚙️ Methodology

### 1. Initial Recon & Extraction

The provided challenge archive (`public.zip`) could not be extracted correctly using the default `unzip` utility. Instead, `7z` was used to recover the application source code.

```bash
7z x public.zip
```

Once extracted, the contents were inspected to identify how download requests were authenticated.

---

### 2. Source Code Analysis

Reviewing the `app.py` file revealed the custom signing function:

```python
hashlib.sha256(
    SECRET_KEY.encode() + message.encode()
).hexdigest()
```

This corresponds to the following construction:

```text
SHA256(secret || message)
```

Because SHA-256 is based on the Merkle-Damgård construction, prepending the secret key before the message makes the implementation vulnerable to a **Hash Length Extension Attack**.

The source code also disclosed that the secret key length was:

```text
16 bytes
```

This information is required by the attack tool to reconstruct the internal SHA-256 state correctly.

---

### 3. Obtain a Valid Download Token

Accessing the `/files` endpoint produced a legitimate download link containing a signed message and its corresponding signature.

**Original Message**

```text
action=download&file=public/notes.txt
```

**Original Signature**

```text
41f55a0b9d9266ada1dee2e3fe2fd236cc0491fff56c22700b4d2bc858ba6a66
```

These values became the starting point for the attack.

---

### 4. Prepare the Exploitation Environment

A Python virtual environment was created and activated.

```bash
python3 -m venv venv

source venv/bin/activate
```

The required dependency was then installed.

```bash
pip install hashpumpy
```

---

### 5. Perform the Length Extension Attack

A modular and reusable exploitation tool [[length_extension_attack]] was developed to automate Hash Length Extension Attacks against applications that authenticate requests using constructions such as:

```text
SHA256(secret || message)
```

The script leverages the **hashpumpy** library and exposes a command-line interface through `argparse`, allowing it to be reused across different CTF challenges by simply providing the required parameters:

- Original signature
- Original signed message
- Payload to append
- Estimated secret key length
- Target URL (optional)
- Custom parameter names for the token and signature
- Custom encoding (default: `latin-1`)

The tool was executed using the values obtained during reconnaissance:

```bash
python3 script_hashpumpy.py \
    -s "41f55a0b9d9266ada1dee2e3fe2fd236cc0491fff56c22700b4d2bc858ba6a66" \
    -d "action=download&file=public/notes.txt" \
    -a "&file=private/flag.txt" \
    -k 16 \
    -u "https://2146d178b1707faa.chal.ctf.ae/download"
```

During execution, the script automatically:

- Reconstructed the internal SHA-256 state from the original digest.
- Generated the required Merkle-Damgård padding.
- Appended the attacker-controlled payload.
- Produced a valid forged signature.
- URL-encoded the forged message while preserving the binary padding using the selected encoding.
- Generated a complete exploit URL ready to be sent to the vulnerable application.

Example execution output:

```text
============================================================
        Hash Length Extension Attack
============================================================

[*] Performing Length Extension Attack...

[+] Original Signature
41f55a0b9d9266ada1dee2e3fe2fd236cc0491fff56c22700b4d2bc858ba6a66

[+] Original Message
action=download&file=public/notes.txt

[+] Appended Payload
&file=private/flag.txt

------------------------------------------------------------

[+] Forged Signature
d0879064cb03ba2b82c21160ca5812fee87263a380c95c9c7cd7495aa8f75398

[+] Forged Message
action=download&file=public/notes.txt...&file=private/flag.txt

[+] URL Encoded Message
action%3Ddownload%26file%3Dpublic/notes.txt%C2%80...

[+] Exploit URL
https://2146d178b1707faa.chal.ctf.ae/download?token=action%3Ddownload%26file%3Dpublic/notes.txt%C2%80...&sig=d0879064cb03ba2b82c21160ca5812fee87263a380c95c9c7cd7495aa8f75398
```

---

### 6. Exploit the Vulnerable Endpoint

The generated exploit URL was sent to the vulnerable `/download` endpoint.

The forged token contained two `file` parameters:

```text
file=public/notes.txt
file=private/flag.txt
```

Flask's query parameter parser retains the **last occurrence** of duplicated parameters, causing the application to process:

```text
file=private/flag.txt
```

Although the requested file had changed, the newly forged signature remained valid because it had been generated through the Length Extension Attack. As a result, the server accepted the request and returned the contents of the protected resource.

---

## 🏁 Flag

**flag**: flag{95245460c6131ec3}
