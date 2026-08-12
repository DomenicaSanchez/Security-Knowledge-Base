## 📘 Description

### **What is Phantom?**

Phantom is a cryptography challenge where user sessions are protected with **AES-GCM** encryption. The objective is to obtain administrator privileges in order to access the **Admin Recovery Key (flag)**.

### **Why is it useful?**

This challenge demonstrates that even when a strong cryptographic algorithm such as AES-GCM is correctly used, an implementation mistake can completely bypass its security. Instead of attacking the encryption itself, the vulnerability is found in the application's exception handling logic.

![[01PA_block-try.png]]

---

## 🛠 Tools Used
- Python 3 (to review the source code)
- `curl`
- Linux Terminal
- Web Browser (optional)
- [[Cryptographic Verification Fallback Bypass]]

No brute-force attacks or cryptographic attacks were required.

---

## ⚙️ Methodology
### Step 1 – Analyze the Source Code

The first step was reviewing the `decrypt_session()` function.

It was discovered that when AES-GCM verification fails, the application executes a fallback mechanism:
![[02PA_vulnerable-code.png]]

Instead of rejecting the session, the application directly decodes the cookie as a Base64-encoded JSON object.
### Step 2 – Create a Fake Administrator Session

A JSON object was created with administrator privileges.

```
{    "user": "guest",    "role": "admin"}
```

The JSON was then encoded into Base64.

```
echo -n '{"user":"guest","role":"admin"}' | base64
```

Output:

```
eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoiYWRtaW4ifQ==
```

### Step 3 – Send the Forged Cookie

The generated token was sent as the `session_token` cookie.

```bash
curl -k --cookie "session_token=eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoiYWRtaW4ifQ==" \https://501b979e2ad4301c.chal.ctf.ae/dashboard
```

The `-k` option was required because the challenge server was using an expired TLS certificate.
![[03PA_flag.png]]

---

## 🧠 Notes & Best Practices

### **Root Cause**

The application correctly encrypts session data using **AES-GCM**, which provides both confidentiality and integrity.

However, the error handling introduces a critical vulnerability.

Whenever AES-GCM authentication fails, the application executes the following fallback:

```python
except Exception:    
	session_data = json.loads(base64.b64decode(cookie))
```

Instead of rejecting the invalid session, it trusts the decoded JSON directly.

As a result, an attacker can create any session by simply encoding arbitrary JSON into Base64.

No knowledge of the encryption key is required.

### **Key Takeaways**

- Strong cryptography does not guarantee application security.
- Authentication failures should never fall back to unauthenticated data.
- AES-GCM integrity verification failures must immediately invalidate the session.
- Always review exception handling around cryptographic operations.

---

## 🏁 Flag
The administrator dashboard was successfully accessed by exploiting the insecure fallback logic inside the session validation process.

**Recovered flag:**

```
flag{9592a597428c3fb7}
```