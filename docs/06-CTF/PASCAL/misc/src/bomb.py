from pwn import *
import re

# Configuración de conexión
host = 'scripting.ctf.pascalctf.it'
port = 6004

def solve_simple_wires(wires, serial_odd):
    """Lógica de la página 5 del manual"""
    n = len(wires)
    if n == 3:
        if 'red' not in wires: return "2"
        if wires[-1] == 'white': return "3"
        if wires.count('blue') > 1: return str(len(wires) - wires[::-1].index('blue'))
        return "3"
    elif n == 4:
        if wires.count('red') > 1 and serial_odd: return str(len(wires) - wires[::-1].index('red'))
        if wires[-1] == 'yellow' and 'red' not in wires: return "1"
        if wires.count('blue') == 1: return "1"
        if wires.count('yellow') > 1: return "4"
        return "2"
    elif n == 5:
        if wires[-1] == 'black' and serial_odd: return "4"
        if wires.count('red') == 1 and wires.count('yellow') > 1: return "1"
        if 'black' not in wires: return "2"
        return "1"
    elif n == 6:
        if 'yellow' not in wires and serial_odd: return "3"
        if wires.count('yellow') == 1 and wires.count('white') > 1: return "4"
        if 'red' not in wires: return "6"
        return "4"
    return "1"

def solve_complicated(red, blue, star, led, serial_even, parallel, batteries):
    """Lógica del Diagrama de Venn de la página 13"""
    # Combinaciones posibles según la tabla de verdad del manual
    if not red and not blue and not star and not led: return True # C
    if not red and not blue and not star and led: return False # D
    if not red and not blue and star and not led: return True # C
    if red and not blue and star and not led: return True # C
    if not red and not blue and star and led: return batteries >= 2 # B
    if red and not blue and not star and not led: return serial_even # S
    if red and not blue and not star and led: return batteries >= 2 # B
    if red and not blue and star and led: return serial_even # S
    if not red and blue and not star and not led: return serial_even # S
    if not red and blue and not star and led: return parallel # P
    if not red and blue and star and not led: return False # D
    if not red and blue and star and led: return parallel # P
    if red and blue and not star and not led: return serial_even # S
    if red and blue and not star and led: return serial_even # S
    if red and blue and star and not led: return parallel # P
    if red and blue and star and led: return False # D
    return False

def main():
    r = remote(host, port)
    
    # Capturamos la información inicial de la bomba (Edgework)
    # Buscamos el inicio de los módulos para parsear los datos previos
    initial_block = r.recvuntil(b"Module 1/100").decode()
    print(initial_block)
    
    # Extraemos metadatos necesarios para las reglas
    serial_match = re.search(r"Serial Number: (\d+)", initial_block)
    serial_last_digit = int(serial_match.group(1)[-1]) if serial_match else 0
    serial_odd = serial_last_digit % 2 != 0
    serial_even = not serial_odd
    
    batt_match = re.search(r"Batteries: (\d+)", initial_block)
    batteries = int(batt_match.group(1)) if batt_match else 0
    
    parallel_port = "parallel" in initial_block.lower()
    
    print(f"[*] Datos: Serial {'Impar' if serial_odd else 'Par'}, Batt: {batteries}, Parallel: {parallel_port}")

    while True:
        try:
            # 1. Esperar el prompt de selección y enviar Enter
            r.recvuntil(b"(press Enter):")
            r.sendline(b"")
            
            # 2. Identificar el módulo actual
            challenge = r.recvline().decode().strip()
            while not challenge or "Module" in challenge or "remaining" in challenge:
                challenge = r.recvline().decode().strip()
            
            print(f"[*] Desafío detectado: {challenge}")

            # 3. Lógica para Cables (Simples y Complicados)
            if "Wires" in challenge:
                wires_data = challenge.split(":")[1].split(",")
                
                # Si hay símbolos especiales (/), es el módulo Complicado
                if "/" in challenge or "star" in challenge or "led" in challenge:
                    to_cut = []
                    for i, w in enumerate(wires_data):
                        w = w.strip().lower()
                        if solve_complicated("red" in w, "blue" in w, "star" in w, "led" in w, 
                                             serial_even, parallel_port, batteries):
                            to_cut.append(str(i+1))
                    r.sendline(",".join(to_cut) if to_cut else "none")
                else:
                    # Cables simples de la pág 5
                    wires = [w.strip().lower() for w in wires_data]
                    r.sendline(solve_simple_wires(wires, serial_odd))

            # 4. Capturar la respuesta y buscar la flag
            response = r.recvline().decode()
            if "pascalCTF" in response:
                print(f"\n🏆 ¡RETRO EXITOSO! FLAG: {response}")
                break
                
        except EOFError:
            print("\n[!] El servidor cerró la conexión.")
            break
        except Exception as e:
            print(f"\n[!] Error en el bucle: {e}")
            break

if __name__ == "__main__":
    main()
