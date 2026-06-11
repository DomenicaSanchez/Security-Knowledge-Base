-  [[#User Management]]
- [[#Package Management]]
- [[#Service and Process Management]]


___
# User Management

User management is a fundamental because create new user accounts or assign existing users to specific groups to enforce appropriate access controls.
The `/etc/shadow` file is a critical system file that stores encrypted password information for all user accounts. Only root can modify this file.
## Execution as a root
Use `sudo` command to perform task that require elevated privileges.
![[01SM-Execution as root.png]]

Here is a list that will help us to better understand and deal with user management.

| **Command** | **Description**                                                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sudo`      | Execute command as a different user.                                                                                                                       |
| `su`        | The `su` utility requests appropriate user credentials via PAM and switches to that user ID (the default user is the superuser). A shell is then executed. |
| `useradd`   | Creates a new user or update default new user information.                                                                                                 |
| `userdel`   | Deletes a user account and related files.                                                                                                                  |
| `usermod`   | Modifies a user account.                                                                                                                                   |
| `addgroup`  | Adds a group to the system.                                                                                                                                |
| `delgroup`  | Removes a group from the system.                                                                                                                           |
| `passwd`    | Changes user password.                                                                                                                                     |
Understanding how user accounts, permissions, and authentication mechanisms operate enables us to identify vulnerabilities, exploit misconfigurations, and assess the security posture of a system effectively.

# Package Management
**Package management** is a tool responsible for installing, updating, modifying, and removing software packages in a system. These packages can include programs, libraries, or dependencies required for applications and systems to function properly.

The features that most package management systems provide are:
- Package downloading
- Dependency resolution
- A standard binary package format
- Common installation and configuration locations
- Additional system-related configuration and functionality
- Quality control

There are different **package managers** depending on the context or programming language used. For example:
- Systems based on Debian or Ubuntu use **dpkg** or **apt**.
- **Python** uses **pip**.
- **JavaScript** uses **npm** or **yarn**.
- Systems such as **Arch Linux** use **pacman**, among others.

Here is a list of examples of such programs:

| **Command** | **Description**                                                                                                                                                                                                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dpkg`      | The `dpkg` is a tool to install, build, remove, and manage Debian packages. The primary and more user-friendly front-end for `dpkg` is aptitude.                                                                                                                                                                                                        |
| `apt`       | Apt provides a high-level command-line interface for the package management system.                                                                                                                                                                                                                                                                     |
| `aptitude`  | Aptitude is an alternative to apt and is a high-level interface to the package manager.                                                                                                                                                                                                                                                                 |
| `snap`      | Install, configure, refresh, and remove snap packages. Snaps enable the secure distribution of the latest apps and utilities for the cloud, servers, desktops, and the internet of things.                                                                                                                                                              |
| `gem`       | Gem is the front-end to RubyGems, the standard package manager for Ruby.                                                                                                                                                                                                                                                                                |
| `pip`       | Pip is a Python package installer recommended for installing Python packages that are not available in the Debian archive. It can work with version control repositories (currently only Git, Mercurial, and Bazaar repositories), logs output extensively, and prevents partial installs by downloading all requirements before starting installation. |
| `git`       | Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals.                                                                                                                                                                                  |

The use of package management is important because it helps to **maintain the system easily**, **automate the installation of dependencies**, and **keep the software up to date and secure**.

## **Package Management (Short Version)**
**APT (Advanced Package Tool)** is used in Debian-based Linux systems to install, update, and remove software. It automatically handles dependencies and makes package management easier.

APT uses repositories that store all available packages. These repositories can be _stable_, _testing_, or _unstable_, and are listed in files like `/etc/apt/sources.list` or `/etc/apt/sources.list.d/parrot.list`.

You can search, view, and install packages using these commands:
```
# View repository list
cat /etc/apt/sources.list.d/parrot.list

# Search for packages
apt-cache search impacket

# Show package information
apt-cache show impacket-scripts

# List installed packages
apt list --installed

# Install a package
sudo apt install impacket-scripts -y

```

APT stores package information in a local database called the **APT cache**, allowing offline searches.
## **DPKG**
`dpkg` installs packages directly from `.deb` files. It doesn’t handle dependencies automatically like APT.
```
# Download .deb file
wget http://archive.ubuntu.com/ubuntu/pool/main/s/strace/strace_4.21-1ubuntu1_amd64.deb

# Install .deb file
sudo dpkg -i strace_4.21-1ubuntu1_amd64.deb

# Verify installation
strace -h

```

## **Git**

**Git** is used to download and manage code repositories from GitHub or other sources.

```
# Create a folder and clone a repository
mkdir ~/nishang/ && git clone https://github.com/samratashok/nishang.git ~/nishang

```

**Summary:**  
APT and DPKG are tools used to manage software packages in Linux. APT handles dependencies and repositories, while DPKG installs `.deb` files directly. Git is used to download and manage code projects.

# Service and Process Management



___
**Return**: [[Essential Linux Commands]]