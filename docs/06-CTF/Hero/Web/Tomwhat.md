This writeup for the **Tomwhat** challenge focuses on **Broken Access Control** through **Apache Tomcat Misconfigurations**. It has been translated into English with reusable tags for your database.

---

# 🌐 Category: Web / Apache Tomcat / Session Manipulation

#technique/session-manipulation #technique/broken-access-control #vulnerability/misconfiguration #tool/apache-tomcat #category/web

---

## 📘 Description

**Author:** Worty

The **Tomwhat** challenge involves an Apache Tomcat server with default example servlets left enabled. By exploiting the `SessionExample` servlet, an attacker can manually set session attributes. The objective is to impersonate an administrative user (`darth_sidious`) to gain access to a restricted area located at `/dark/admin`.

---

## 🛠 Tools Used

- **Browser:** To interact with the web application and manipulate session attributes.
- **Apache Tomcat Examples:** Specifically the `SessionExample` servlet.

---

## ⚙️ Methodology

### 1. Initial Recon

The application appears to be running on an Apache Tomcat server. A common misconfiguration in such environments is leaving the `/examples/` directory accessible. Navigating to the following URL confirms that the session manipulation servlet is available: `http://dyn11.heroctf.fr:12311/examples/servlets/servlet/SessionExample`

### 2. Vulnerability Discovery (Session Manipulation)

The `SessionExample` servlet allows users to define custom session attributes. Since the application likely checks for a specific `username` attribute in the session to verify administrative privileges, this servlet can be used to inject the required identity.

### 3. Exploitation (Session Attribute Injection)

In the "Session State" form of the servlet, the following attributes were injected:

- **Name of Session Attribute:** `username`
- **Value of Session Attribute:** `darth_sidious`

After clicking **Submit**, the session table updates to reflect the new attribute, effectively binding the administrative username to the current session cookie.

![[01_Tomwhat.png]]

### 4. Flag Retrieval

With the malicious session active, I navigated to the restricted administrative path: `http://dyn11.heroctf.fr:12311/dark/admin`

Because the session now contains the required `username=darth_sidious` attribute, the server grants access to the page, revealing the flag.

![[02_Tomwhat.png]]

---

## 🏁 Flag

`Hero{...}` _(Note: Capture the flag from the administrative panel shown in screenshot `02_Tomwhat.png`)_