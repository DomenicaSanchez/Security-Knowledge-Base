[de4js](https://lelinhtinh.github.io/de4js/) is an interactive **JavaScript unpacker / deobfuscator** (web UI + multiple plugins) that automatically detects many common obfuscation/packing schemes (P.A.C.K.E.R., AAEncode, JJEncode, Obfuscator.io, JSFuck, string encoders, eval-wrappers, etc.) and applies staged transformations to recover readable source. It combines **pattern detection**, **unwrapping (eval execution in a safe sandbox)**, **string decoding**, and **pretty-printing** to return deobfuscated JS quickly.
![[de4js.png]]

## Primary use-case
Reverse-engineering or analyzing obfuscated JS (malicious scripts, malware loaders, packed web clients, CTF/HTB boxes) to restore control flow and literals so a human (or static analyzer) can understand behavior.

**Key technical properties:**
- Multi-unpacker pipeline (detect → unwrap → decode → format).
- Runs transformations in controlled environment to evaluate harmless wrappers.   
- Produces readable code (not guaranteed original variable names/logic).
- Fast, interactive and aimed at manual analysis workflows.

**Alternatives**
- [**js-beautify** — formateador](https://github.com/beautify-web/js-beautify)
- [**Prettier** — formateador moderno](`https://prettier.io`)
- [**JSNice**](http://www.jsnice.org)
