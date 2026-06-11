#tool/tool-name

______

## 🕵️ Information

**What is ToolName?**  
It is a command-line utility used to calculate and verify SHA-256 (Secure Hash Algorithm 256-bit) cryptographic hashes.

**Why is it useful in cybersecurity?**  
- **Forensics:** To ensure the integrity of evidence and prove that files haven't been tampered with.
- **Malware Analysis:** To identify known malicious files by comparing their hashes against databases like VirusTotal.
- **CTFs:** To find a specific file among hundreds or to verify downloaded challenge files.

---

## ⚡ Installation

### Install using package manager

```bash
sudo apt install coreutils
```
### Verify installation

```bash
sha256sum --version
```
---

## ⚡ Quick Cheat Sheet

### 📜 Basic usage
```bash
sha256sum <file_name>
```
### 🔍 Verify multiple files
```bash
sha256sum files/*
```
### 📂 Check against a list
```bash
sha256sum -c checksum.txt
```
***(Checks if the files listed in the text match their hashes)***

---

## 🧪 Example Use Case

**Identify a specific file in a haystack:** In a CTF, if you are given a specific hash and a folder full of files, you can pipe the output to find the exact match: `sha256sum files/* | grep <target_hash>`
    
---

## 🧠 Notes

- **Integrity over Secrecy:** Remember that hashing is not encryption; you cannot "reverse" a hash to get the original data, but you can use it to verify it.
- **Wildcards:** Use `*` to process an entire directory at once.
- **Output format:** The output always shows the hash followed by the file path.