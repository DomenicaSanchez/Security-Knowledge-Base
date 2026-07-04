Return:  [[Practice Labs]]

This is a game to learn Linux through [[Commands & Tools]].
1. Level 0
	*Resolution:*
		Used `ssh bandit0@bandit.labs.overthewire.org -p 2220`
	*Password:*
		bandit0
		
2. Level 0-1
	*Resolution:*
		Used `cat` command to read the  `readme` file
	*Password:* 
		ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

3. Level 1-2
	*Resolution:*
		Used `cat` command to read the  `/home/bandit1/-` file
	*Password:* 
		263JGJPfgU6LtdEvgfWU1XP5yac29mFx
		
4. Level 2-3
	*Resolution:*
		Used `cat` command to read the  `"spaces in this filename"
` file
	*Password:* 
		MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
		
5. Level 3-4
	*Resolution:*
		Used `cat` command to read the  `..Hiding-From-You`  file into `inhere` directory
		The file `..Hiding-From-You` was obtained using the `ls -la` command 		
	*Password:* 
		2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
		
6. Level 4-5
	*Resolution:*
		Go to the `inhere` directory
		Use `file ./*` to check the type of each file.
		Then, use `cat` command to read  `./-file07`  , which is the file with ASCII text data.
	*Password:* 
		4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
		
7. Level 5-6
	*Resolution:*
	Use  `find ./* -type f -not -executable -size 1033c -readable` command. 
	Then, use `cat` command to read  `./maybehere07/.file2` 
	
	*Password:* 
		HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
	
8. Level 6-7
	*Resolution:*
	Use  `find ./* -type f -not -executable -size 1033c -readable` command. 
	Then, use `cat` command to read  `/var/lib/dpkg/info/bandit7.password` 

	*Password:* 
	morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

9. Level 7-8
	*Resolution:*
	Use  `grep -i 'millionth' data.txt` command. 
	*Password:* 
		dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
	
10. Level 8-9
	*Resolution:*
	Use  `sort data.txt | uniq -u` command. 
	*Password:* 
		4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
		
11. Level 9-10
	*Resolution:*
	Use  `strings data.txt | grep -i =` command. 	
	The `String` command is used to obtain non-binary characters.
	*Password:* 
		FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
		
12. Level 10-11
	*Resolution:*
	Use  `base64 --decode data.txt` command. 		
	The base65 command is used to encode or decode data in base64 format. It is a standard for representing binaries data as ASCII text.
	*Password:* 
		dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr	

13. Level 11-12
	*Resolution:*
	Use  `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'` command. 		
	The [tr] command stands for translate, and it is a Linux utility used to replace, delete or compress characters. Its basic syntax is:
		`tr [options] set1 [set2]`
	
	ROT13 is a simple type of cipher from the Cesar family  It shifts each letter 13 positions forward in the alphabet. If you apply ROT13 twice, you can recover the original text.
	
	*Password:* 
		7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

datos binarios 
14. Level 12-13
	*Resolution:*
	The file `data` contains a **hexdump** of a file that was **compressed multiple times** using different formats (gzip, bzip2, tar, etc.).  
	You need to **revert the hexdump**, then **decompress repeatedly** to get the password
	1. Convert the hexdump back to binary: xxd -r data.txt >  `hexToBinary `
		- `xxd -r`: reverses hexdump to binary    
		- `> hexToBinary`: saves it to a file
	2. Check what type of file it is: `file hexToBinary`
		- The `file` command tells you what kind of file it is (gzip, bzip2, tar, etc.)
	3. Rename the file: `mv hexToBinary hexToBinary.gz`
		- Rename the file to match its format (e.g., `.gz`, `.bz2`, `.tar`)
	4. Decompress based on the file type:
		`gzip -d hexToBinary.gz     # if it's gzip`
		`bzip2 -d hexToBinary.bz2   # if it's bzip2`
		`tar -xf hexToBinary.tar    # if it's a tar file`
		- After each step, use `file` again to check the new file 
		- Repeat until it's just text				
	*Password:*
		FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

15. Level 13-14
	*Resolution:*
	Use the commnand `ssh -i sshkey.private -p 2220 bandit14@bandit`
	The [ssh] command is used for stablish a remote connection. 
	We used the `-i` option because this level provides an  identity file named `sshkey.private `
	*Password:* 
		MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

16. Level 14-15
	*Resolution:*
	Use the command `nc localhost 30000`
	The [nc] command, which stands for Netcat, is used to read and write data over network connections TCP or UDP.
	*Password:* 
		8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

17. Level 15-16
	*Resolution:*
	Use the command `openssl s_client -connect localhost:30001`
	The [openssl] command provides tools to work with SSL/TLS encryption.
	In this case, we use it in `s_client` mode to stablish a secure connection 
	*Password:* 
		kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
		
	
18. Level 16-17
	*Resolution:*
	Use the command `nmap -sV localhost -p 31000-32000` 
	Look for the port that shows the service `ssl/unknown`. In this case, it's `31790/tcp` 
	You can connect to it using either of the following commands: `ncat --ssl localhost 31790` or `openssl s_client -connect localhost:31790`
	Then,  create a directory called `/tmp/random_key` using the command `mkdir /tmp/random_key` 
	Inside `/tmp/random_key`, created a file named `private.key` and paste the obtained key into it. 
	Change the permissions of `private.key` using  `chmod 400 private.key`
	Finally,connect to the next level using the following command: `ssh -i private.key -p 2220 bandit17@bandit`
	 *Password:* 
		SSH
> 
19. Level 17-18
	*Resolution:*
	Use the command `diff --suppress-common-lines password.old password.new`
	The comman [diff] is used to compare teo files line for line. This is a particularity useful when you're trying to identify what has changed between two versions of a file, such as passworfs or configuration files.
		*Password:* 
		x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO

20. Level 18-19
	*Resolution:* 
	At this level, it is important to undestand the  `ssh` command. This command not only used to connect to a machine remotely, but also to execute commands remotely.
	First, we use `ls` to make sure the `readme` file is in the folder.
	`ssh bandit18@bandit.labs.overthewire.org -p 2220 ls`
	Then, we use `cat` to read the contents of the `readme` file.
	`ssh bandit18@bandit.labs.overthewire.org -p 2220 ls`
	*Password:* 
		cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

21. Level 19-20
	*Resolution:*
	First, we check permissions of all files in the home directory using `ls -la`, and we can see that `bandit20-do` has the setuid permissions
	Then, we execute  `./bandit20-do id` we can only view the user ID of bandit20
	Finally, we use `./bandit20-do cat  /etc/bandit_pass/bandit20` to read the password as the  `bandit20`	 user
	*Password:* 
		0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO

22. Level 20-21
	*Resolution:*
	First, we check permissions of all files in the home directory using `ls -la`, and we can see setuid binary `./suconnect `
	Then, use the command cat `cat /etc/bandit_pass/bandit20 | nc -lvp 1234 &`, where the first part reads contents of the file, and the second part sends this content through port 1234
	Finally, we can receive and read the transferred content using `./suconnect 1234` 
	*Password:* 
		EeoULMCra2q0dSkYj561DX7s1CpBuOBt
	
23. Level 21-22
	*Resolution:*
	For this level, we needed to identified a program that runs automatically at regular intervals using cron.
	First, we had to undestand cron is, it's a scheduler in UNix-like systems thats runs commands at specified times.
	Then, we navigated to `/etc/cron.d/`  using the command `cd /etc/cron.d/`. 
	We found and ran the script `cronjob_bandit22.sh`. The result was a path `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv` 
	When we tried to exucute it, we got a "operation not permmited" error. However, we were able to read its contents using `cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv` . This revealed the flag
	*Password:* 
		tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
	

24. Level 22-23
	*Resolution:*
	
	*Password:* 
	
25. Level 23-24
	*Resolution:*
	
	*Password:* 
	
26. Level 24-25
	*Resolution:*
	
	*Password:* 
27. Level 25-26
	*Resolution:*
	
	*Password:* 
	
28. Level 26-27
	*Resolution:*
	
	*Password:* 
	
29. Level 27-28
	*Resolution:*
	
	*Password:* 
	
30. Level 28-29
	*Resolution:*
	
	*Password:* 
	