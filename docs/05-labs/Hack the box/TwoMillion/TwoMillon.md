TwoMillion is an Easy difficulty Linux box that was released to celebrate reaching 2 million users on HackTheBox. The box features an old version of the HackTheBox platform that includes the old hackable invite code. After hacking the invite code an account can be created on the platform. The account can be used to enumerate various API endpoints, one of which can be used to elevate the user to an Administrator. With administrative access the user can perform a command injection in the admin VPN generation endpoint thus gaining a system shell. An .env file is found to contain database credentials and owed to password re-use the attackers can login as user admin on the box. The system kernel is found to be outdated and CVE-2023-0386 can be used to gain a root shell.

## How many TCP ports are open?
I verified connection 
`ping -c 5 10.10.11.221`
![[01TM-ping.png]]
I review open ports
`nmap -sV 10.10.11.221`
![[01TM-nmap.png]]

**Solution**: 2

## What is the name of the JavaScript file loaded by the `/invite` page that has to do with invite codes?
Another time. I review open ports 
`nmap -sC -sV 10.10.11.221`
![[02TM-nmap.png]]

I observed that no had solution DNS for `http://2millon.htb` so i added `10.10.11.221 2million.htb` resolution for DNS 
`sudo nano /etc/hosts` 
![[02TM-hosts.png]]

I opened the web `http://2millon.htb` and opened section `invited` . Then opened the browser dev tools and reviewed networks and obtained the name of source
![[02TM-sourceName.png]]

**Solution**: inviteapi.min.js

## What JavaScript function on the invite page returns the first hint about how to get an invite code? Don't include () in the answer.

I used tool [[de4js]] for convert js ofusqued to js redeable for identified fuction
![[03TM-de4js.png]]
![[03MT-redeable js.png]]
**Solution**: makeInviteCode

## The endpoint in `makeInviteCode` returns encrypted data. That message provides another endpoint to query. That endpoint returns a `code` value that is encoded with what very common binary to text encoding format. What is the name of that encoding?

We can understand the difference between **encryption** and **encoding**.

|           | What do                                               | propose                      |
| --------- | ----------------------------------------------------- | ---------------------------- |
| Encrypted | Transforms data into something unreadable using a key | security/confidentiality     |
| Encoded   | Converts binary data into text without a key\|        | Compatibility / Transmission |
Base64 is an _encoding_ method, not encryption.  
It converts binary data into readable text using a standard character set, but it doesn’t hide or protect the information.  
Anyone can decode Base64 without a key — it’s used for data transmission, not for security.
 
**How to encode and decode**
```
# decode
echo "SGVsbG8sIEhUQhE=" | base64 -d
# output: Hello, HTB!
```

```
# encode
echo -n "Hello, HTB!" | base64
# output: SGVsbG8sIEhUQhE=
```

**Solution**: base64

## What is the path to the endpoint the page uses when a user clicks on "Connection Pack"?
Verify the URL:
`curl -s -X POST http://2million.htb/api/v1/invite/generate`

Identify and decode the encoded data:
```
echo "SkNIQU0tS1NHTlotRlFJS0ItUDJVTEk=" | base64 -d 
# Result: JCHAM-KSGNZ-FQIKB-P2ULI (an invite code)
```

Create a user and log in.
![[05TM-login.png]]

After logging in, go to **Labs > Access**. Using the browser dev tools, select **Connection Pack** and observe the request URL.
![[05TM-ConnectionPack.png]]

**Solution**: /api/v1/user/vpn/generate

## How many API endpoints are there under `/api/v1/admin`?

Query the route `/api/v1` and and review all endpoints listed under `/admin`
![[06TM-endpoints.png]]
**Solution**: 3

## What API endpoint can change a user account to an admin account?

From the previous exercise, we identified that the endpoint capable of changing a user account uses the **PUT** method.
The endpoint `/api/v1/admin/settings/update` is accessed via the **PUT** method. 

**Solution:** `/api/v1/admin/settings/update`

## What API endpoint has a command injection vulnerability in it?
I listed the API endpoints under `/api/v1/admin` and saw `/api/v1/admin/vpn/generate` uses **POST**.
Endpoints that accept POST and generate configs or files often call system utilities, so I identified it as likely vulnerable.

**Solution**: /api/v1/admin/vpn/generate

## What file is commonly used in PHP applications to store environment variable values?
I knew from experience that PHP frameworks (e.g., Laravel) commonly store environment variables in a hidden file named **`.env`**.
I didn’t have to find it in the project.

**Solution**:  .env

## Submit the flag located in the admin user's home directory.
