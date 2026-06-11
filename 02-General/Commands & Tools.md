Every [[Practice Labs]] & [[CTF Central Hub]] command that is executed from the CLI (Command Line Interface) consists of one or more “parts”.  These parts are called “arguments” and, typically, they are separated by spaces.  An argument can be one of three things: the command itself, an option, or a parameter.
- [Commands](#Commands)
- [Tools](#Tools)
- [[#Filter content]]
- [[#Enumeration]]

![[Arguments-Command.png]]

![[Permisos-en-sistema-de-archivos.jpg]]


---
# Commands 

| Command                             | Description                                                                                                                                                |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| systemctl list-units --type=service | List active services (Daemons)                                                                                                                             |
| `\D{%Y-%m-%d}`                      | Date (YYYY-MM-DD)                                                                                                                                          |
| `\H`                                | Full hostname                                                                                                                                              |
| `\j`                                | Number of jobs managed by the shell                                                                                                                        |
| `\n`                                | Newline                                                                                                                                                    |
| `\r`                                | Carriage return                                                                                                                                            |
| `\s`                                | Name of the shell                                                                                                                                          |
| `\t`                                | Current time 24-hour (HH:MM:SS)                                                                                                                            |
| `\T`                                | Current time 12-hour (HH:MM:SS)                                                                                                                            |
| `\@`                                | Current time                                                                                                                                               |
| `\u`                                | Current username                                                                                                                                           |
| `\w`                                | Full path of the current working directory                                                                                                                 |
| `whoami`                            | Displays current username.                                                                                                                                 |
| `id`                                | Returns users identity                                                                                                                                     |
| `hostname`                          | Sets or prints the name of current host system.                                                                                                            |
| `uname`                             | Prints basic information about the operating system name and system hardware.                                                                              |
| `pwd`                               | Returns working directory name.                                                                                                                            |
| `ifconfig`                          | The ifconfig utility is used to assign or to view an address to a network interface and/or configure network interface parameters.                         |
| `ip`                                | Ip is a utility to show or manipulate routing, network devices, interfaces and tunnels.                                                                    |
| `netstat`                           | Shows network status.                                                                                                                                      |
| `ss`                                | Another utility to investigate sockets.                                                                                                                    |
| `ps`                                | Shows process status.                                                                                                                                      |
| `who`                               | Displays who is logged in.                                                                                                                                 |
| `env`                               | Prints environment or sets and executes command.                                                                                                           |
| `lsblk`                             | Lists block devices.                                                                                                                                       |
| `lsusb`                             | Lists USB devices                                                                                                                                          |
| `lsof`                              | Lists opened files.                                                                                                                                        |
| `lspci`                             | Lists PCI devices.                                                                                                                                         |
| `man <tool>`                        | Opens man pages for the specified tool.                                                                                                                    |
| `<tool> -h`                         | Prints the help page of the tool.                                                                                                                          |
| `apropos <keyword>`                 | Searches through man pages' descriptions for instances of a given keyword.                                                                                 |
| `cat`                               | Concatenate and print files.                                                                                                                               |
| `whoami`                            | Displays current username.                                                                                                                                 |
| `id`                                | Returns users identity.                                                                                                                                    |
| `hostname`                          | Sets or prints the name of the current host system.                                                                                                        |
| `uname`                             | Prints operating system name.                                                                                                                              |
| `pwd`                               | Returns working directory name.                                                                                                                            |
| `ifconfig`                          | The `ifconfig` utility is used to assign or view an address to a network interface and/or configure network interface parameters.                          |
| `ip`                                | Ip is a utility to show or manipulate routing, network devices, interfaces, and tunnels.                                                                   |
| `netstat`                           | Shows network status.                                                                                                                                      |
| `ss`                                | Another utility to investigate sockets.                                                                                                                    |
| `ps`                                | Shows process status.                                                                                                                                      |
| `who`                               | Displays who is logged in.                                                                                                                                 |
| `env`                               | Prints environment or sets and executes a command.                                                                                                         |
| `lsblk`                             | Lists block devices.                                                                                                                                       |
| `lsusb`                             | Lists USB devices.                                                                                                                                         |
| `lsof`                              | Lists opened files.                                                                                                                                        |
| `lspci`                             | Lists PCI devices.                                                                                                                                         |
| `sudo`                              | Execute command as a different user.                                                                                                                       |
| `su`                                | The `su` utility requests appropriate user credentials via PAM and switches to that user ID (the default user is the superuser). A shell is then executed. |
| `useradd`                           | Creates a new user or update default new user information.                                                                                                 |
| `userdel`                           | Deletes a user account and related files.                                                                                                                  |
| `usermod`                           | Modifies a user account.                                                                                                                                   |
| `addgroup`                          | Adds a group to the system.                                                                                                                                |
| `delgroup`                          | Removes a group from the system.                                                                                                                           |
| `passwd`                            | Changes user password.                                                                                                                                     |
| `dpkg`                              | Install, remove and configure Debian-based packages.                                                                                                       |
| `apt`                               | High-level package management command-line utility.                                                                                                        |
| `aptitude`                          | Alternative to `apt`.                                                                                                                                      |
| `snap`                              | Install, remove and configure snap packages.                                                                                                               |
| `gem`                               | Standard package manager for Ruby.                                                                                                                         |
| `pip`                               | Standard package manager for Python.                                                                                                                       |
| `git`                               | Revision control system command-line utility.                                                                                                              |
| `systemctl`                         | Command-line based service and systemd control manager.                                                                                                    |
| `ps`                                | Prints a snapshot of the current processes.                                                                                                                |
| `journalctl`                        | Query the systemd journal.                                                                                                                                 |
| `kill`                              | Sends a signal to a process.                                                                                                                               |
| `bg`                                | Puts a process into background.                                                                                                                            |
| `jobs`                              | Lists all processes that are running in the background.                                                                                                    |
| `fg`                                | Puts a process into the foreground.                                                                                                                        |
| `curl`                              | Command-line utility to transfer data from or to a server.                                                                                                 |
| `wget`                              | An alternative to `curl` that downloads files from FTP or HTTP(s) server.                                                                                  |
| `python3 -m http.server`            | Starts a Python3 web server on TCP port 8000.                                                                                                              |
| `ls`                                | Lists directory contents.                                                                                                                                  |
| `cd`                                | Changes the directory.                                                                                                                                     |
| `clear`                             | Clears the terminal.                                                                                                                                       |
| `touch`                             | Creates an empty file.                                                                                                                                     |
| `mkdir`                             | Creates a directory.                                                                                                                                       |
| `tree`                              | Lists the contents of a directory recursively.                                                                                                             |
| `mv`                                | Move or rename files or directories.                                                                                                                       |
| `cp`                                | Copy files or directories.                                                                                                                                 |
| `nano`                              | Terminal based text editor.                                                                                                                                |
| `which`                             | Returns the path to a file or link.                                                                                                                        |
| `find`                              | Searches for files in a directory hierarchy.                                                                                                               |
| `updatedb`                          | Updates the locale database for existing contents on the system.                                                                                           |
| `locate`                            | Uses the locale database to find contents on the system.                                                                                                   |
| `more`                              | Pager that is used to read STDOUT or files.                                                                                                                |
| `less`                              | An alternative to `more` with more features.                                                                                                               |
| `head`                              | Prints the first ten lines of STDOUT or a file.                                                                                                            |
| `tail`                              | Prints the last ten lines of STDOUT or a file.                                                                                                             |
| `sort`                              | Sorts the contents of STDOUT or a file.                                                                                                                    |
| `grep`                              | Searches for specific results that contain given patterns.                                                                                                 |
| `cut`                               | Removes sections from each line of files.                                                                                                                  |
| `tr`                                | Replaces certain characters.                                                                                                                               |
| `column`                            | Command-line based utility that formats its input into multiple columns.                                                                                   |
| `awk`                               | Pattern scanning and processing language.                                                                                                                  |
| `sed`                               | A stream editor for filtering and transforming text.                                                                                                       |
| `wc`                                | Prints newline, word, and byte counts for a given input.                                                                                                   |
| `chmod`                             | Changes permission of a file or directory.                                                                                                                 |
| `chown`                             | Changes the owner and group of a file or directory.                                                                                                        |
## Filter content

| Command                                  | Description                                                                                             |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `cut -d "delimiter" -f {field_number} `  | Extract specific fields from each line using a delimiter                                                |
| `grep "pattern" file`                    | Search line with a pattern                                                                              |
| `awk 'condition { action }' file`        | write and read lines from a file or input, split them into fields, and perform actions on those fields. |
| `sed 's/old_pattern/new_pattern/g' file` | Replace a pattern with another pattern                                                                  |
| `wc -l`                                  | Useful to know how many successful matches we have.                                                     |


--- 
# Tools
Now, to exploit different machines in Hack The Box or TryHackMe we need a variaty of tools. I present a table with name of each tool and its respective basic command.

| Tool         | Command                                                                      |
| ------------ | ---------------------------------------------------------------------------- |
| [[gobuster]] | gobuster dir -u  [URL] -w [WORDLIST] -x [EXTENSIONES] -t [HILOS] -o [OUTPUT] |
| [[steghide]] | steghide extract -sf [image]<br>                                             |

# Enumeration
Commands for privilege enumeration

| Command                   | Description                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `getcap -r / 2>/dev/null` | Recursively list POSIX "privilege bits" assigned to binaries so you can spot candidates for escalation (hides errors). |
____

___
 Resource: https://www.fossnotes.com/the-3-piece-anatomy-of-linux-commands/
 Command with Practical Examples: https://labex.io/es/tutorials/linux-linux-find-command-with-practical-examples-422682
SetUID, SetGID, and Sticky Bits in Linux File Permissions: https://www.geeksforgeeks.org/linux-unix/setuid-setgid-and-sticky-bits-in-linux-file-permissions/
Permisos en LInux: https://naps.com.mx/blog/ejemplos-explicados-de-permisos-en-linux/
