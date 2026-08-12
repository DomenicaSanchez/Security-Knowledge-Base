# 🕵️ Category: Web / Information Leakage / IDOR

---

## 📘 Description

**Challenge Description**

> "A new recipe-sharing platform launched for the Latin American cooking crowd: profiles, recipes, the usual. Word is the admin's profile has something the rest of us don't."

The challenge presents a recipe-sharing platform named **Mise en Place**, where users can register and publish cooking recipes. The registration flow is intentionally simplified and only requires a username, display name, and short description, without any password authentication.

The objective is to obtain the flag stored within the administrator's private profile by identifying weaknesses in the application's access control mechanisms.

During the assessment, an exposed backend API leaked sensitive user information, including the administrator's UUID. Since the application relied solely on the supplied object identifier without verifying ownership, it was vulnerable to an **Insecure Direct Object Reference (IDOR)** attack.

---

## 🛠 Tools Used

- Browser Developer Tools (F12)
- Browser View Source (`Ctrl + U`)
- curl

---

## ⚙️ Methodology

### 1. Initial Recon & Session Analysis

After accessing the application, a standard testing account was created using the **Join** functionality.

Once registration completed, the application redirected the browser to a profile endpoint similar to:

```text
https://6760c63441372b37.chal.ctf.ae/profile/d7ab46b6-a29f-4e53-a63c-8bdc0cb86217
```

Several aspects of the application's session management were analyzed.

The browser storage revealed a Flask session cookie containing the authenticated session information.

The URL structure also indicated that every user profile was uniquely identified through a UUID v4 value:

```text
/profile/<uuid>
```

This suggested that profile authorization depended on object identifiers rather than opaque session references.

---

### 2. Static Source Code Inspection

The public homepage displayed several recipes published by different users.

Selecting any recipe redirected directly to its author's profile instead of an individual recipe endpoint, indicating that user objects represented the primary application resources.

To identify hidden functionality, the HTML source code of the landing page was inspected using:

```text
Ctrl + U
```

Near the bottom of the document, inside the footer section, a developer comment referenced an internal API endpoint:

```text
/api/users
```

Although the endpoint was not linked anywhere within the user interface, the comment exposed its existence and suggested that it supplied user information to the application.

---

### 3. API Enumeration (Information Leakage)

To verify whether the hidden endpoint enforced proper authorization controls, a direct request was issued using the Browser:

```bash
https://6760c63441372b37.chal.ctf.ae/api/users
```

The server responded with a JSON document containing every registered account.

Example response:

```json
{
  "pagination": {
    "page": 1,
    "pages": 1,
    "per_page": 10,
    "total": 8
  },
  "users": [
    {
      "display_name": "Chef Admin",
      "joined": "2025-11-01",
      "role": "admin",
      "username": "chef_admin",
      "uuid": "eb611d17-e3e2-4bcb-905c-07c3797a036b"
    }
  ]
}
```

The response exposed sensitive information that should never have been publicly accessible, including:

- Usernames
- Roles
- Registration dates
- UUIDs
- Administrator account details

Most importantly, it revealed the administrator's UUID:

```text
eb611d17-e3e2-4bcb-905c-07c3797a036b
```

This information disclosure eliminated the need to guess or brute-force the identifier.

---

### 4. Exploitation (IDOR)

UUID version 4 identifiers contain approximately 122 bits of randomness, making brute-force attacks computationally infeasible.

However, because the application disclosed the administrator's UUID through the exposed API endpoint, the only remaining requirement was to request the corresponding profile directly.

The following URL was accessed:

```text
https://6760c63441372b37.chal.ctf.ae/profile/eb611d17-e3e2-4bcb-905c-07c3797a036b
```

The server successfully returned the administrator's profile without verifying whether the authenticated user was authorized to access that object.

The backend trusted the supplied UUID and failed to enforce object-level authorization, resulting in an **Insecure Direct Object Reference (IDOR)** vulnerability.

The administrator's private profile was rendered successfully, exposing the challenge flag.

---

## 🏁 Flag

**flag**: flag{fa07cb865a5ce90a}