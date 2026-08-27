# 🕵️ Category: Forensics / file-analysis/ Verify

---

## 📘 Description
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.`ssh -p 61352 ctf-player@rhea.picoctf.net`Using the password `1db87a14`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

- Checksum: 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a
- To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file>`.

---

## 🛠 Tools Used
- #tool/sha256sum: To calculate file hashes.
- #tool/grep: To filter the output and find the matching hash.
- #tool/bash: For script execution.
---
## ⚙️ Methodology

After connecting to the instance via SSH, I listed the contents of the home directory and found:
![[01V_list.png]]

- `checksum.txt`: Contains the target SHA-256 hash.
- `decrypt.sh`: A script used to decrypt the correct file.
- `files/`: A directory containing numerous potential flag files (true and false).

To find the correct file without checking each one manually, I calculated the hashes with [[sha256sum]] for all files in the directory and filtered the results using the provided checksum:
```bash
sha256sum files/* | grep 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a
```

**Output:** `55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a files/2cdcb2de`

The output confirmed that the file `files/2cdcb2de` matches the legitimate hash. Finally, I executed the decryption script on the verified file:
```bash
./decrypt.sh files/2cdcb2de
```

____
## 🏁 Flag
**flag**: picoCTF{trust_but_verify_2cdcb2de}