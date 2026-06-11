
The Linux philosophy centers on simplicity, modularity, and  openness. Linux follows five core principes:
1. Everything is a file
2. Small, single-purpose programs
3. Ability to chain programs togother to perform complex tasks
4. Avoid captive user interfaces .- you can work with the shell 
5. Configuration data stored in a text file 
____
-  [[#Components]]
- [[#Linux Architecture]]
	- [[#Kernel]]
-  [[#File System Hierarchy]]
- [[#File content]]

____
# Components

1. Bootloader.- piece od code that runs to guide the booting process
   ![[Pasted image 20250907113915.png]]

2. OS Kernel.- It manages the resources for system's I/O devices at the hardware level.
![[Pasted image 20250907114045.png]]

3.  Daemons,.- Background services that ensure that key functions such as scheduling, printing, and multimedia are working correctly.  Daemons are usually named with a trailing "d" at the end, such us `sshd`, `httpd`, or `cron`.  with the commmand  in	[[Commands & Tools]]
![[Pasted image 20250907115352.png]]
		**Internally, a daemon does the following:**
			 - **Forks** – It creates a child process that runs independently.
			 - **Closes standard file descriptors** – It closes `stdin`, `stdout`, and `stderr` so it doesn't use the terminal.
			 - **Becomes an orphan process** – It detaches from the terminal and is adopted by `init` or `systemd`.
			- **Runs in the background** – It keeps running in the background, waiting for events or performing scheduled tasks.
		**Create a daemon**
			1. Create a file my_daemon.sh
				`nano  my_daemon.sh`
	![[Pasted image 20250907122554.png]]
			2. Execute in background service and
				`chmod +x my_daemon.sh`
				`./my_daemon.sh &`
			3. Review logs
				`ps aux | grep bash`
				`tail -f /tmp/my_daemon.log`
	![[Pasted image 20250907122513.png]]
	 
4.  OS Shell.-  the command language interprete
5.  Graphics server.- Manages the connection between thw system (OS and applications) and external input/output devices like keyboard, mouse, or monitor
6. Windows Manager.- Decorate and manage how to present windows to user. There are many options, including GNOME, KDE, MATE, Unity, and Cinnamon.
7. Utilities.- Utility = Command = small program designed to perform a specific function.
---
# Linux Architecture

![[Pasted image 20250907194546.png]]
### Kernel

**What the Kernel Does Behind the Scenes**

| **Action You Perform** | **What the Kernel Does**                                                          |
| ---------------------- | --------------------------------------------------------------------------------- |
| You turn on the PC     | The kernel is loaded into RAM and takes control of the system.                    |
| You move the mouse     | The kernel reads input events from the USB device.                                |
| You type something     | The kernel handles keyboard input and delivers it to the active application.      |
| You open Brave browser | The kernel creates a new process and allocates memory to it.                      |
| You visit a website    | The kernel manages network access, DNS resolution, ports, and sockets.            |
| You save a file        | The kernel writes to the filesystem using the appropriate disk drivers.           |
| You use the camera     | The kernel loads the webcam driver and connects it to the application.            |
| You shut down the PC   | The kernel terminates processes, unmounts filesystems, and powers off the system. |

Example kernel

```
# kernel_module.c
#include <linux/init.h>    // Para macros de inicialización y limpieza
#include <linux/module.h>  // Necesario para todos los módulos kernel
#include <linux/kernel.h>  // Para printk()

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Sanduchito");
MODULE_DESCRIPTION("Simple module - kernel");

static int __init hello_init(void) {
    printk(KERN_INFO "Hello kernel! Load module.\n");
    return 0;  // 0 indica que se cargó correctamente
}

static void __exit hello_exit(void) {
    printk(KERN_INFO "Bye  kernel! Download module.\n");
}

module_init(hello_init);
module_exit(hello_exit);

```

```
# Makefile
obj-m += kernel_module.o

all:
        make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
        make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

```

```
# Step 1: Write kernel_module.c
# Step 2: Create a Makefile
# Step 3: Run 'make'
# Result: You get 'kernel_module.ko'
# Step 4: Load the module
sudo insmod kernel_module.ko
dmesg | tail  # See the kernel message

# Step 5: Clean up the files if you don't need them anymore
make clean
```

**Kernel Module Components – What They Are and Why We Use Them**

| **Component**      | **Simple Description**                                                                               | **Why We Use It**                                                        |
| ------------------ |:---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `kernel_module.c`  | C source code that defines a simple kernel module (e.g., prints a message on load and unload).       | To learn the structure of a basic Linux kernel module.                   |
| `Makefile`         | Contains instructions to compile the module using the kernel's build system.                         | To correctly generate the `.ko` file that is compatible with the kernel. |
| `make`             | Command that executes the rules in the Makefile; compiles `kernel_module.c` into `kernel_module.ko`. | To build the module automatically without typing all commands manually.  |
| `kernel_module.ko` | The compiled module in binary format, ready to be loaded into the kernel.                            | It's the final output to be loaded as a kernel extension.                |
| `sudo insmod *.ko` | Command that loads the compiled module into the kernel.                                              | To activate and run the module's code from within the kernel space.      |
| `dmesg`            | Displays kernel messages (including output from `printk()` calls in the module).                     | To confirm that the module was loaded and is functioning properly.       |
| `sudo rmmod`       | Command that removes the module from the kernel.                                                     | To cleanly stop and unload the module.                                   |
| `make clean`       | Deletes temporary build files created during compilation.                                            | To keep the working directory clean with only source files remaining.    |
 review : [[Malware_rootkit.canvas|Malware_rootkit]]

**User Space vs Kernel Space**

- Scripts and compilation → user space
- Kernel modules (.ko) → kernel space
- 
So in your workflow: .sh → make → .ko, only the .ko file is actually running inside the kernel. The rest just prepare or call it.

| Action                               | Space        | Interacts with kernel?                                        |
| ------------------------------------ | ------------ | ------------------------------------------------------------- |
| `.sh` script execution               | User space   | No, only calls programs                                       |
| `make` compilation                   | User space   | No, just generates files                                      |
| `.ko` module loading                 | Kernel space | Yes, directly runs in kernel, can modify kernel behavior      |
| Running `/bin` commands inside `.sh` | User space   | They **use the kernel** via system calls, but don’t modify it |
____

# File System Hierarchy

The linux operating systme is documented in the Filesystem HIerarchy Standard FHS. Linux is structured with the following standard top-level directories:
![[Pasted image 20250909165102.png]]

| Path     | Description                                                                          | Example(s)                                              |
| -------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| `/`      | Root filesystem; contains files needed to boot before other filesystems are mounted. | `/init`, `/lost+found`                                  |
| `/bin`   | Essential command binaries.                                                          | `/bin/ls`, `/bin/cp`, `/bin/mkdir`                      |
| `/boot`  | Bootloader, kernel, and boot files.                                                  | `/boot/vmlinuz`, `/boot/grub/`                          |
| `/dev`   | Device files for hardware access.                                                    | `/dev/sda`, `/dev/null`, `/dev/tty`                     |
| `/etc`   | System configuration files; may also hold app configs.                               | `/etc/passwd`, `/etc/hosts`, `/etc/ssh/sshd_config`     |
| `/home`  | User home directories.                                                               | `/home/dsmcamila/`, `/home/dsmcamila/Downloads/`        |
| `/lib`   | Shared libraries required for system boot.                                           | `/lib/x86_64-linux-gnu/libc.so.6`                       |
| `/media` | Mount point for removable media.                                                     | `/media/usb/`, `/media/cdrom/`                          |
| `/mnt`   | Temporary mount point for filesystems.                                               | `/mnt/data/` (manual mounts)                            |
| `/opt`   | Optional/third-party software.                                                       | `/opt/google/chrome/`, `/opt/lampp/`                    |
| `/root`  | Home directory for the root user.                                                    | `/root/.bashrc`, `/root/Downloads/`                     |
| `/sbin`  | System administration binaries.                                                      | `/sbin/ifconfig`, `/sbin/reboot`                        |
| `/tmp`   | Temporary files (cleared on reboot).                                                 | `/tmp/tmp1234.log`, `/tmp/.X11-unix/`                   |
| `/usr`   | User utilities, libraries, documentation, etc.                                       | `/usr/bin/python3`, `/usr/share/man/`                   |
| `/var`   | Variable data: logs, mail, web files, cron jobs.                                     | `/var/log/syslog`, `/var/www/html/`, `/var/spool/mail/` |

Hostorically, the `/etc/passwd` file stored password hashes, but now those stored in `/etc/shadow`

____
# File content

![[Pasted image 20250910181638.png]]

| **Column Content** | **Description**                                                                  |
| ------------------ | -------------------------------------------------------------------------------- |
| `drwxr-xr-x`       | Type and permissions                                                             |
| `2`                | Number of hard links to the file/directory                                       |
| `dsmcamila` first  | Owner of the file/directory                                                      |
| `dsmcamila`        | Group owner of the file/directory                                                |
| `4096`             | Size of the file or the number of blocks used to store the directory information |
| `sep 7 20:28`      | Date and time                                                                    |
| `Kernel`           | Directory name                                                                   |

___
**Previous**: [[Essential Linux Commands]]
**Next:** [[Introduction to Shell]]
___
