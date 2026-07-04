# `scripts/length_extension_attack`

### 🕵️ Information

**What is Length Extension Attack?**

A Python command-line utility that automates **Hash Length Extension Attacks** using the `hashpumpy` library. It generates a valid forged signature and message by appending arbitrary data to an existing signed message without requiring knowledge of the secret key.

**Why is it useful?**

This script simplifies the exploitation of applications vulnerable to hash length extension attacks. Instead of manually calculating padding and forging signatures, it automatically generates the modified message, the new signature, and optionally a ready-to-use exploit URL. It is useful for CTF challenges, penetration testing labs, and cryptography research.

---

### ⚡ Requirements

- **Interpreter:** Python 3.8+
- **Libraries/Modules:**

```
pip install hashpumpy
```

---

### 🚀 Usage

How to run the script.

**Basic execution:**

```bash
python3 length_extension_attack.py \    
	-s <original_hash> \    
	-d "<original_message>" \    
	-a "<payload_to_append>" \    
	-k <secret_key_length>
```

**Generate a complete exploit URL:**

```bash
python3 length_extension_attack.py \    
	-s <original_hash> \ 
	-d "<original_message>" \    
	-a "<payload_to_append>" \    
	-k <secret_key_length> \    
	-u "https://target/download"
```

**Help menu:**

```bash
python3 length_extension_attack.py --help
```

---

### 🧪 Features & Examples

#### **Feature 1: Forge a signed message**

Generate a new valid signature after appending arbitrary data to the original signed message.

```bash
python3 length_extension_attack.py \    
	-s 41f55a0b9d9266ada1dee2e3fe2fd236cc0491fff56c22700b4d2bc858ba6a66 \
	-d "action=download&file=public/notes.txt" \
	-a "&file=private/flag.txt" \    
	-k 16
```

---

#### **Feature 2: Generate a complete exploit URL**

Automatically URL-encodes the forged message and builds a ready-to-use URL for the target application.

```bash
python3 length_extension_attack.py \
	-s 41f55a0b9d9266ada1dee2e3fe2fd236cc0491fff56c22700b4d2bc858ba6a66 \
	-d "action=download&file=public/notes.txt" \
	-a "&file=private/flag.txt" \
	-k 16 \
	-u "https://target/download"
```

---

### 📂 Output Format

The script prints formatted console output containing:

- Original signature
- Original message
- Appended payload
- Forged signature
- Forged message
- URL-encoded forged message
- Complete exploit URL (if `--url` is provided)

Example:

``` bash
====================================================
Hash Length Extension Attack
====================================================
[+] New Signature
5d7c...

[+] URL Encoded Message
action%3Ddownload...

[+] Exploit URL
https://target/download?token=...&sig=...
```

---

### 🧠 Notes & Best Practices

- **Permissions:** No elevated privileges are required.
- **Optimization:** If the secret key length is unknown, automate multiple executions over a range of likely key lengths (e.g., 8–64 bytes).
- **Warnings:**
    - This script only works against applications that compute signatures using vulnerable constructions such as `Hash(secret || message)`.
    - It **does not work** against HMAC implementations (`HMAC-SHA1`, `HMAC-SHA256`, etc.).
    - The success of the attack depends on correctly estimating the secret key length.
- **Author/License:** Doménica Sánchez & Kevin Villacis