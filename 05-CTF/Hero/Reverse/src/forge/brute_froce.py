#!/usr/bin/env python3
from pwn import *
import time

# Configuración
HOST = "reverse.heroctf.fr"
PORT = 7002
VALID_PASS_FILE = "src/valid_pass.c"

# Lista de posibles tipos de retorno
return_types = ["void", "int", "char*", "long", "long long", "void*"]

# Lista de posibles argumentos (cadenas de texto que van dentro de los paréntesis)
argument_lists = [
    "",                         # Sin argumentos
    "int a",                    # Un entero
    "int a, int b",             # Dos enteros
    "int a, int b, int c",      # Tres enteros
    "char* s",                  # Un string/puntero
    "char* s, int a",           # String y entero
    "int a, char** argv",       # Estilo Main
    "long a",                   # Un long
    "void* ptr",                # Puntero genérico
    "int* ptr",                 # Puntero a entero
    "int strength, int magic"   # Nombres temáticos (por si acaso, aunque importa el tipo)
]

def create_c_file(ret_type, args):
    """Genera el contenido del archivo C con la firma dada."""
    # Cuerpo básico para que compile. Si pide retorno, devolvemos 0 o null.
    return_stmt = "return;"
    if ret_type != "void":
        return_stmt = "return 0;"
    
    code = f"""
#include <stdlib.h>

int main() {{
    return 0;
}}

{ret_type} SWORD_OF_THE_HERO({args}) {{
    {return_stmt}
}}
"""
    with open(VALID_PASS_FILE, "w") as f:
        f.write(code)
    return code

def test_signature(ret_type, args):
    """Prueba una firma específica contra el servidor."""
    signature = f"{ret_type} SWORD_OF_THE_HERO({args})"
    log.info(f"Probando firma: {signature}")
    
    create_c_file(ret_type, args)
    
    try:
        # Conexión rápida
        conn = remote(HOST, PORT, level='error')
        
        with open(VALID_PASS_FILE, 'rb') as f:
            conn.send(f.read())
        conn.shutdown('send')
        
        response = conn.recvall(timeout=3).decode("utf-8", errors="ignore")
        conn.close()
        
        # Verificar éxito
        if "Hero{" in response:
            print("\n" + "="*50)
            print(f"[+] ¡ÉXITO! La firma correcta es: {signature}")
            print(f"[+] Flag encontrada:\n{response}")
            print("="*50 + "\n")
            return True
        elif "Nope" in response:
            return False # Firma incorrecta
        else:
            # Si no dice Nope ni Hero, algo raro pasó (error de compilación, etc)
            # log.warning(f"Respuesta inesperada para {signature}:\n{response}")
            return False

    except Exception as e:
        log.warning(f"Error probando {signature}: {e}")
        return False

def main():
    log.info("Iniciando fuerza bruta de firmas...")
    
    for ret in return_types:
        for args in argument_lists:
            if test_signature(ret, args):
                return
            # Pequeña pausa para no saturar demasiado (opcional)
            # time.sleep(0.1)

    log.failure("No se encontró la firma correcta en la lista predefinida.")

if __name__ == "__main__":
    main()
