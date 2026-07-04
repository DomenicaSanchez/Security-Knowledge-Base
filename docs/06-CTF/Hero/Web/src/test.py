import bcrypt

# Hash del reto Revoked Revenge
target_hash = b"$2b$12$iCsYF7eMyJQaeM4M2pzR1u0PX3ZHhsZW8Yz75BXJvuRVKsMAVlagi"
rockyou_path = "/usr/share/wordlists/rockyou.txt"

print(f"[*] Iniciando ataque masivo (Top 5000) contra el hash...")

try:
    with open(rockyou_path, "r", encoding="latin-1") as f:
        count = 0
        for line in f:
            # Limpiamos saltos de linea
            password = line.strip()
            
            # Probamos la contraseña
            # Imprimimos cada 10 intentos para no saturar la pantalla
            if count % 10 == 0:
                print(f"[-] Intento {count}: Probando '{password}'...", end="\r")
            
            if bcrypt.checkpw(password.encode('utf-8'), target_hash):
                print(f"\n\n{'='*40}")
                print(f"[+] ¡CONTRASEÑA ENCONTRADA!: {password}")
                print(f"{'='*40}")
                exit()
            
            count += 1
            
            # Límite de seguridad para que tu PC no explote (5000 intentos)
            if count >= 5000:
                print("\n\n[!] Se alcanzaron los 5000 intentos sin éxito.")
                print("[*] Si ves esto, necesitamos ampliar el límite a 10000.")
                exit()
                
except FileNotFoundError:
    print("[!] Error: No encuentro el archivo rockyou.txt en /usr/share/wordlists/")
