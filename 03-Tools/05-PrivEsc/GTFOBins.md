GTFOBins is a public list of Unix binaries that shows ways they can be abused if they have unsafe permissions or special capabilities. I use it when I have a low-privilege shell: I search the binary name on GTFOBins, read the examples (shell, file transfer, privilege escalation), and try the commands on the target. For example, if `python` has `cap_setuid`, GTFOBins shows how to call `os.setuid(0)` and spawn a root shell. [gtfobins.github.io+1](https://gtfobins.github.io/?utm_source=chatgpt.com)
![[GTFOBins.png]]

For each binary it documents how legitimate features (like scripting hooks, interpreters, or file manipulation flags) can be used to: 

| Capability bit | Exploit effect                                          |
| -------------- | ------------------------------------------------------- |
| 0              | root                                                    |
| 1              | spaw shells                                             |
| 2              | upload/download files                                   |
| 3              | escalate privileges via SUID/SGID or POSIX capabilities |
| 4              | abuse `sudo` configurations                             |

When performing a local post-exploit assessment you should: 
- Enumerate SUID bits and file capabilities
- Find matching GTFOBins pages 
- Attempt the documented techniques. 
If a binary is marked with `cap_setuid+ep`, code that calls `setuid(0)` (for example via Python’s `os.setuid(0)`) can change the process UID to root and then execute a shell.
_____
**Reference:** [gtfobins.github.io+1](https://gtfobins.github.io/?utm_source=chatgpt.com)

