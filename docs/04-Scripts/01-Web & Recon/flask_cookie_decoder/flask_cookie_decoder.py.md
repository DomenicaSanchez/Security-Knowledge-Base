# flask_cookie_decoder.py

🕵️ **Information / Información**

- **What is it?** A local Python script designed to decode, decompress, and format Flask web session cookies.
- **¿Qué es?** Un script local en Python diseñado para decodificar, descomprimir y dar formato a las cookies de sesión web de Flask.
    
- **Why is it useful?** Flask session cookies are Base64URL-encoded and frequently compressed with `zlib`. This script automates the extraction, padding correction, and pretty-printing of the underlying session data directly in your terminal without relying on external web tools.
- **¿Por qué es útil?** Las cookies de sesión de Flask están codificadas en Base64URL y frecuentemente comprimidas con `zlib`. Este script automatiza la extracción, corrección de _padding_ y visualización estructurada de los datos de la sesión directamente en tu terminal, sin depender de herramientas web externas.

⚡ **Requirements**
- **Interpreter:** Python 3.x
- **Libraries:** Standard library only (`base64`, `zlib`, `json`). No third-party packages required.

🚀 **Usage**

- **Basic execution:**
```bash 
    python3 flask_cookie_decoder.py
```
_(The script will interactively prompt you to paste the cookie string)._

🧪 **Features & Examples**
- **Automatic Format Detection:** Identifies whether the cookie uses `zlib` compression (indicated by a leading `.`) or standard Base64 encoding.
- **Padding Repair:** Automatically calculates and appends missing Base64 `=` padding characters to prevent decoding errors.
- **JSON Formatting:** Automatically formats and color-indents JSON payloads for immediate readability.

📂 **Output Format**
Direct console output formatted as structured JSON or plain text.

🧠 **Notes & Best Practices**
- **Scope:** This script performs **read-only decoding**. It does not forge or sign cookies (generating a valid signature requires knowledge of the application's server-side `SECRET_KEY`).
- **Privacy & Security:** All processing occurs entirely offline on your local machine, ensuring sensitive session identifiers are never sent to third-party web services.