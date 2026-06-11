#tool/tshark 🦈 (Advanced Study Guide)

---

## 🕵️ Information

**What is TShark?** It is the CLI equivalent of Wireshark. It processes network traffic in a "pipeline" fashion, making it incredibly powerful for filtering massive datasets that would crash a GUI.

**Why use it for CTFs/Forensics?** 1. **Speed:** Filter 1GB of traffic in seconds. 2. **Parsing:** Extract passwords, filenames, or hashes directly to your terminal. 3. **Evidence:** Prove exactly _when_ and _how_ an attack occurred.

---

## ⚡ Quick Cheat Sheet

### 📜 1. Basic Operations

- **Read a file:** `tshark -r file.pcapng`
- **Live Capture (Interface):** `tshark -i eth0`
- **Save filtered results to a new file:** `tshark -r input.pcap -Y "filter" -w output.pcap`

### 🔍 2. Advanced Filtering (-Y)

- **Specific IP:** `tshark -r file.pcapng -Y "ip.addr == 192.168.1.1"`
- **Exclude a protocol:** `tshark -r file.pcapng -Y "!arp && !dns"`    
- **Multiple conditions:** `tshark -r file.pcapng -Y "tcp.port == 80 && ip.src == 10.0.0.5"`

### 🧩 3. Data Extraction (-T fields -e)

- **Extract HTTP Hosts:** `tshark -r file.pcapng -T fields -e http.host`
- **Extract User-Agents:** `tshark -r file.pcapng -T fields -e http.user_agent`
- **Extract DNS Queries:** `tshark -r file.pcapng -T fields -e dns.qry.name`
    

---

## ⏱️ Time & Vulnerability Analysis

This is critical for identifying **when** an attack happened and **what** was targeted.

### 🕒 Time Analysis

- **Show absolute time (Date and Time):** `tshark -r file.pcapng -t ad` (Output: 2026-01-27 10:39:28)
- **Find Delta Time (Time since previous packet):** `tshark -r file.pcapng -T fields -e frame.number -e frame.time_delta`
    

> _Useful for spotting automated scripts or brute-force attacks (very small, consistent time deltas)._

### 🛡️ Vulnerability & Attack Identification

- **Identify Port Scanning:** `tshark -r file.pcapng -Y "tcp.flags.syn == 1 && tcp.flags.ack == 0"`
    

> _High volume of these from one IP = Port Scan._

- **Detect Cleartext Passwords (HTTP/FTP/Telnet):** `tshark -r file.pcapng -Y "http.authbasic || ftp || telnet"`    
- **Find Large Data Transfers (Exfiltration):** `tshark -r file.pcapng -T fields -e ip.src -e frame.len | sort -rn | head -n 10`
    

> _Shows the largest packets; helps find where data was stolen._

---

## 💡 Pro Tips for CTFs

### 💬 Reconstructing the "True" Content

When you see `telnet.data`, it often looks like `L\r\ni\r\nn\r\nu\r\nx`. Use the **Follow Stream** command to clean it: `tshark -r file.pcapng -q -z follow,tcp,ascii,0`

### 🕵️ Hunting for the "Backdoor"

If an attacker creates a user, they often use `useradd`. You can search for this string across the entire capture: `tshark -r file.pcapng -Y "frame contains \"useradd\""`

---

## 🏗️ Command Structure Master Formula

tshark−r[file]−t[timef​ormat]−Y"[filter]"−Tfields−e[field]

| Parameter | Function | Common Values                                   |
| --------- | -------- | ----------------------------------------------- |
| **-r**    | Read     | `file.pcapng`                                   |
| **-t**    | Time     | `ad` (absolute), `d` (delta), `r` (relative)    |
| **-Y**    | Filter   | `http`, `tcp.port == 4444`, `ip.src == x.x.x.x` |
| **-T**    | Type     | `fields` (to extract specific columns)          |
| **-e**    | Element  | `frame.time`, `ip.addr`, `tcp.payload`, `text`  |
