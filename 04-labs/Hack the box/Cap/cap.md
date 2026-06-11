## Task 1
- **How many TCP ports are open?**
I ran an nmap ping:
` nmap -PS 10.10.10.245` 
![[Pasted image 20251021132156.png]]
That discovered three open TCP ports
## Task 2
- **After running a "Security Snapshot", the browser is redirected to a path of the format `/[something]/[id]`, where `[id]` represents the id number of the scan. What is the `[something]`?**
I opened the web server at `http://10.10.10.245/` (port 80 was open). 
![[Pasted image 20251012003703.png]]
After running a snapshot the browser redirects to a path like `http://10.10.10.245/data/9` .
![[Pasted image 20251012003920.png]]
So the `[something]`is `[data]`

## Task 3
- **Are you able to get to other users' scans?**
Yes, by changing the `id` in the URL I could access scan results for other users.
![[Pasted image 20251012004926.png]]
![[Pasted image 20251012004942.png]]
THe scan pages references other scan IDs, and by interating those IDs I was able to view scans that didn´t belong to my user account.

## Task 3
- **What is the ID of the PCAP file that contains sensative data?**
I downloaded several files(pcap captures)
![[Pasted image 20251012005600.png]]

## Task 4
- **What is the ID of the PCAP file that contains sensative data?**
The PCAP with sensitive information was `ID 0`
![[Pasted image 20251012005800.png]]

## Task 5
- **Which application layer protocol in the pcap file can the sensetive data be found in?**
The captured sensitive credentials appeared in the aplication-layer protocol (FTP). 
![[Pasted image 20251012005800.png]]

The capture included a username and password
```
user: nathan
password: Buck3tH4TF0RM3!
```

## Task 6
**We've managed to collect nathan's FTP password. On what other service does this password work?**
Using the captured credentials, I was able to connect to the targer over SSH
![[Pasted image 20251012011358.png]]

## Submit user flag
- **Submit the flag located in the nathan user's home directory.**
![[Pasted image 20251021135305.png]]

## Task 8
- **What is the full path to the binary on this machine has special capabilities that can be abused to obtain root privileges?**
I checked the target for shells/groups and available capabilities
```
id
cat /etc/passwd | grep sh$
```
![[Pasted image 20251021121858.png]]

Then I listed file capabilities
`getcap -r 2>/dev/null`
![[Pasted image 20251021122752.png]]
That showed an interesting capability on a Python binary `/usr/bin/python3.8`. The machine name `CAP` hinted at capabilities being relevant.

Using [[GTFOBins]] as a reference, I confirmed that Python binary with `CAP_SETUID` can used to obtain a root shell.
![[Pasted image 20251021123139.png]]

![[Pasted image 20251021123340.png]]

In my session I exploited that capability
`/usr/bin/python3.8 -c 'import os; os.setuid(0); os.system("/bin/sh")'`
![[Pasted image 20251021125006.png]]

## Submit root flag
Get a root shell and then read the flag from `/root`
![[Pasted image 20251021125811.png]]

___
## Extra
### **POSIX :**
POSIX is a set of standardized APIs and conventions for Unix-like operating systems that defines how programs and the system should behave, enabling portability and consistent behavior across different Unix/Linux systems.
### POSIX Capabilities
POSIX capabilities are a mechanism defined within POSIX that divides **root privileges** into small, fine-grained “pieces.”

- Each piece (capability) allows a specific action, such as:    
    - `CAP_SETUID` → change UID
    - `CAP_NET_BIND_SERVICE` → bind to low-numbered ports
    - `CAP_NET_RAW` → send/receive raw network packets
        
- When a **normal user runs a binary with a capability**, the **process inherits that privilege**, but the user itself does **not** become root.
### Getcap
`getcap` is a utility that lists **POSIX capabilities** assigned to executables. It shows which fine-grained privileges (e.g., `cap_setuid`, `cap_net_raw`) a binary has.

**Example:**
```
getcap /usr/bin/python3.8 # Output: /usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
```
This output indicates that `/usr/bin/python3.8` has the `CAP_SETUID` and `CAP_NET_BIND_SERVICE` capabilities active, meaning the binary can change UID and bind to low-numbered ports when executed.