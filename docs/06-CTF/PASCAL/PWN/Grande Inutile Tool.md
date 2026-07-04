# 💣 Category: Pwn / Git Analysis / SUID

#technique/suid #technique/symlink #vulnerability/logic-flaw #tool/ln #category/pwn

---

## 📘 Description

### Grande Inutile Tool

**Author:** Alan Davide Bovo (`@AlBovo`)

This challenge involves a custom tool called **`mygit`**, designed to simulate basic Git functionality. However, it handles repository metadata in an insecure way.

The binary has the **SUID bit set**, meaning it runs with root privileges. The objective is to identify how the tool manages control files and exploit its logic to read the protected flag located at `/flag`.

---

## 🛠 Tools Used

- **ls / find:** To identify the SUID bit on the binary.
- **ln (link):** To create symbolic links and redirect metadata reads.
- **mygit:** The target custom binary.
- **cat / grep:** To read and search for the flag pattern.

---

## ⚙️ Methodology

### 1. Initial Recon

First, I searched for binaries with the **SUID** bit enabled. I confirmed that `/usr/bin/mygit` had the permission set as `-rwsr-xr-x`, meaning any user executing it does so with root's authority.

When initializing a repo with `mygit init`, the tool creates a hidden `.mygit` folder. While the folder is protected, the tool relies on reading files inside it (like `HEAD`) to determine the repository's status.

### 2. Vulnerability Discovery (Symlink Attack)

The tool is designed to read the content of `.mygit/HEAD`. Because the binary runs as root, it can read **any** file the user points to, even if the user themselves doesn't have permission to see it.

By creating a **symbolic link** named `HEAD` that points to `/flag`, we can trick `mygit` into reading the flag and displaying its contents in the output of the `status` command.

### 3. Exploitation

**Step-by-step execution:**

1. Create a workspace directory where you have write permissions.
2. Manually create the `.mygit` directory structure that the tool expects.
3. Link the internal metadata file `HEAD` directly to the system flag.
    

**Execution Commands:**

Bash

```
# Create the environment
mkdir .mygit

# Link the protected flag to the git metadata file
ln -s /flag .mygit/HEAD

# Execute the SUID binary to trigger the read
mygit status
```

---

## 🏁 Flag

`pascalCTF{m4ny_fr13nds_0f_m1n3_h4t3_git_btw}`