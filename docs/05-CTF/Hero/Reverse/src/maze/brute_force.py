#!/usr/bin/env python3
from pwn import *

HOST = "reverse.heroctf.fr"
PORT = 7001
VALID_PASS_FILE = "src/valid_pass.c"

# Mantenemos las estructuras del juego para que no falle la firma de la función
BOILERPLATE_TOP = """
#include <stdint.h>
#include <stdlib.h>

typedef enum MOVE_S { LEFT, RIGHT, UP, DOWN } MOVE;
typedef struct pos_s { uint8_t x; uint8_t y; } pos_t;

void __attribute__((noinline)) chose_direction(MOVE *moves, uint8_t *cur_move_id, pos_t *initial_pos, pos_t wanted_pos) {}
void __attribute__((noinline)) place_entity(pos_t *new_pos, uint8_t entity, pos_t *all_used_position, uint8_t *used_position) {}
"""

BOILERPLATE_MAIN = """
int main() {
    MOVE moves[100];
    uint8_t id = 0;
    pos_t p = {0,0};
    get_direction(moves, &id, p, p, p);
    return 0;
}
"""

def generate_loop_maze(complexity):
    """
    Genera un bucle que contiene instrucciones con propiedades matemáticas especiales
    para satisfacer los requisitos del Segundo y Tercer Paso.
    """
    # Cuerpo del laberinto con "hechizos" (instrucciones específicas)
    body = """
    // Variables volatile para forzar instrucciones de MEMORIA (Load/Store)
    volatile int a = 10;
    volatile int b = 20;
    volatile int c = 0;

    // Estructura cíclica (Paso 1 completado)
    while (a < 100) {
        
        // --- Paso 2/3: Inyección de Instrucciones ---

        // 1. Commutative & Associative (Conmutativa y Asociativa)
        // Ejemplo: Suma (+) y Multiplicación (*)
        c = a + b; 
        c = a * b;

        // 2. Idempotent (Idempotente: x op x = x)
        // Ejemplo: OR bit a bit (|) o AND (&) consigo mismo
        c = a | a;
        c = a & a;

        // 3. Nilpotent (Nilpotente: x op x = 0 o anula)
        // Ejemplo: XOR (^) consigo mismo da 0
        c = a ^ a;

        // 4. Fence-like (Barrera de memoria)
        // Esto genera una instrucción 'fence' en LLVM IR
        __sync_synchronize();

        // Control del bucle para que no sea infinito (y genere el bloque básico correcto)
        a++;
    }
    """
    return body



def generate_switch_maze(complexity):
    """Genera un laberinto basado en Switch Case (Ramificaciones puras)"""
    cases = ""
    for i in range(complexity):
        cases += f"        case {i}: x += {i}; break;\n"
    
    body = f"""
    volatile int x = {complexity};
    switch(x) {{
{cases}
        default: x = 0;
    }}
    """
    return body

def create_payload(logic_body):
    code = f"""
{BOILERPLATE_TOP}

// La función objetivo es get_direction 
void __attribute__((noinline)) get_direction(MOVE *moves, uint8_t *cur_move_id, pos_t hero_pos, pos_t exit_pos, pos_t rune_pos) {{
    {logic_body}
    return;
}}

{BOILERPLATE_MAIN}
"""
    with open(VALID_PASS_FILE, "w") as f:
        f.write(code)
    return code

def test_complexity(generator_func, n, type_name):
    log.info(f"Probando {type_name} con complejidad: {n}")
    create_payload(generator_func(n))
    
    try:
        conn = remote(HOST, PORT, level='error')
        with open(VALID_PASS_FILE, 'rb') as f:
            conn.send(f.read())
        conn.shutdown('send')
        
        response = conn.recvall(timeout=3).decode("utf-8", errors="ignore")
        conn.close()
        
        # Buscamos si pasamos al menos el PRIMER paso
        if "First step succeeded" in response:
            print("\n" + "="*50)
            print(f"[+] ¡AVANCE! Estructura correcta encontrada ({type_name}={n})")
            print(f"Respuesta del servidor:\n{response}")
            print("="*50 + "\n")
            return True
        elif "Hero{" in response: # ¡Por si acaso!
            print(f"[+] FLAG: {response}")
            return True
            
        return False
    except:
        return False

def main():
    log.info("Iniciando escaneo de estructura del laberinto...")
    
    # 1. Probar Bucles (Loops) - El enunciado los menciona explícitamente
    for i in range(1, 20):
        if test_complexity(generate_loop_maze, i, "Loops"):
            return

    # 2. Probar Switch Cases (Ramificaciones masivas)
    for i in range(1, 30):
        if test_complexity(generate_switch_maze, i, "SwitchCases"):
            return

    log.failure("No se encontró la estructura base. Quizás necesitamos mezclar ambos.")

if __name__ == "__main__":
    main()
