# 🕵️ Category: Network / PCAP

---

## 📘 Description
A digital ghost has breached my defenses, and my sensitive data has been stolen! 
😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!Find the PCAP file here **../src/01-myNetworkTraffic.pcap** and try to get the flag.

---
## 🛠 Tools Used
- #tool/string 

---

## ⚙️ Methodology

I used the strings command to extract printable text
`strings -t d 01-myNetworkTraffic.pcap | grep "=="`
![[01-Ph4nt0m 1ntrud3r.png]]

We noticed that some strings end only with `=`, which is not useful.  
Valid Base64 strings usually end with `==`.  
So we focused on those and decoded them from Base64.

| base64<br>   | decoded |
| ------------ | ------- |
| ezF0X3c0cw== | {1t_w4s |
| cGljb0NURg== | picoCTF |
| bnRfdGg0dA== | nt_th4t |
| Yt8ksMM=     | -       |
| 3psv5C4=     | -       |
| YQEFzIU=     | -       |
| YmhfNHJfOQ== | bh_4r_9 |
| a23/UbI=     | -       |
| TOGSGg4=     | -       |
| bpzQ0R8=     | -       |
| fQ==         | }       |
| nfu4Vww=     | -       |
| J4auZMY=     | -       |
| ePRXDio=     | -       |
| fjIzQwk=     | -       |
| XThGxuE=     | -       |
| ckBkZLk=     | -       |
| CJr4oDk=     | -       |
| BgJLB0c=     | -       |
| XzM0c3lfdA== | _34sy_t |
| NTlmNTBkMw== | 59f50d3 |
| dgV9v0s=     | -       |
Finally, we ordered the valid decoded strings to reconstruct the flag.

____
## 🏁 Flag
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_959f50d3}
