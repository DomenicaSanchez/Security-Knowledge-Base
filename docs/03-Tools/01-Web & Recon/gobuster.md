**Gobuster** is a brute-force tool that sends many web requests to discover hidden directories, files, and subdomains on a server.

`gobuster dir -u [URL] -w [WORDLIST] -x [EXTENSIONS] -t [THREADS] -o [OUTPUT]`

- `dir` = Modes also include:
    - `dns` → DNS subdomain fuzzing
    - `vhost` → virtual host fuzzing
    - `s3`
    - `fuzz` (depends on the version)
        
**Key options:**
- **`-u <URL>`** = The **target URL** (must include `http://` or `https://`).
- **`-w <WORLIST>`** = The path to the wordlist used to find hidden files.
- **`-x <EXTENSIONS>`** _(optional)_ = File extensions to try (comma-separated).
- **`-t <THREADS>`** = Number of **threads** → how many requests are sent in parallel. Typical values: `10–50`.
- **`-o <OUTPUT>`** = Saves the results to a file (useful for reviewing later).

**Other flags:**
- `-e` → shows the full URL in the output.
- `-k` → ignores SSL certificate issues on HTTPS.
- `--exclude-length <NUM>` → excludes responses of a given size (handy against false 404s).
- `-s <CODES>` → only shows specific HTTP status codes (e.g. `-s 200,403`).
- `-q` → quiet mode (less noisy output).

| **Mode / Usage**             | **Command**                                                  | **Real Example**                                                                                         | **What it does**                                                            |
| ---------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Basic directory scan**     | `gobuster dir -u <URL> -w <WORDLIST>`                        | `gobuster dir -u http://10.10.10.10 -w /usr/share/wordlists/dirb/common.txt`                             | Scans for common directories/files on a website (`/admin`, `/login`, etc.). |
| **With extensions**          | `gobuster dir -u <URL> -w <WORDLIST> -x <EXTS>`              | `gobuster dir -u http://10.10.10.10 -w /usr/share/wordlists/dirb/common.txt -x php,txt,zip`              | Also tries file extensions (`index.php`, `backup.zip`).                     |
| **Adjusting threads**        | `gobuster dir -u <URL> -w <WORDLIST> -t <N>`                 | `gobuster dir -u http://10.10.10.10 -w common.txt -t 50`                                                 | Controls speed (more threads = faster, but noisier).                        |
| **Save results to file**     | `gobuster dir -u <URL> -w <WORDLIST> -o <FILE>`              | `gobuster dir -u http://10.10.10.10 -w common.txt -o results.txt`                                        | Stores the output for later review.                                         |
| **Filter HTTP status codes** | `gobuster dir -u <URL> -w <WORDLIST> -s <CODES>`             | `gobuster dir -u http://10.10.10.10 -w common.txt -s 200,403`                                            | Shows only specific status codes (e.g. `200 OK`, `403 Forbidden`).          |
| **Exclude by response size** | `gobuster dir -u <URL> -w <WORDLIST> --exclude-length <NUM>` | `gobuster dir -u http://10.10.10.10 -w common.txt --exclude-length 3456`                                 | Ignores responses with a specific size (useful for custom 404 pages).       |
| **VHOST discovery**          | `gobuster vhost -u <URL> -w <WORDLIST>`                      | `gobuster vhost -u http://site.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt` | Finds **virtual hosts** (e.g. `admin.site.htb`).                            |
| **DNS subdomain scan**       | `gobuster dns -d <DOMAIN> -w <WORDLIST>`                     | `gobuster dns -d site.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt`          | Discovers **DNS subdomains** (e.g. `dev.site.htb`).                         |
| **Ignore invalid SSL**       | `gobuster dir -u https://<URL> -k -w <WORDLIST>`             | `gobuster dir -u https://10.10.10.10 -k -w common.txt`                                                   | Skips SSL certificate errors (common in CTF/HTB environments).              |