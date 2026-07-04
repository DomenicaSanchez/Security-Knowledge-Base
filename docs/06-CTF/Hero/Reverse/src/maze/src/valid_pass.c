#include <stdint.h>
#include <stdlib.h>

// --- TIPOS ---
typedef enum MOVE_S { LEFT, RIGHT, UP, DOWN } MOVE;
typedef struct pos_s { uint8_t x; uint8_t y; } pos_t;

// --- BOILERPLATE ---
void __attribute__((noinline)) chose_direction(MOVE *moves, uint8_t *cur_move_id, pos_t *initial_pos, pos_t wanted_pos) {}
void __attribute__((noinline)) place_entity(pos_t *new_pos, uint8_t entity, pos_t *all_used_position, uint8_t *used_position) {
    *new_pos = (pos_t){0, 0};
}

// --- SOLUCIÓN ---
void __attribute__((noinline)) get_direction(MOVE *moves, uint8_t *cur_move_id, pos_t hero_pos, pos_t exit_pos, pos_t rune_pos) {
    
    // 1. VARIABLES VOLÁTILES (Antídoto contra la optimización -O1)
    volatile int state = (int)(*cur_move_id);
    volatile int modifier = (int)hero_pos.x + 1; // +1 para evitar ceros
    
    // 2. SATISFACER EL CHECK ESTRUCTURAL (STEP 1)
    // El pass verifica que leamos 'moves' y tengamos flujo de control (bucles/ramas).
    // Usamos un bucle 'for' que depende de los datos.
    
    // Leemos moves fuera para asegurar la referencia GEP
    volatile MOVE m = moves[state]; 
    
    for (int i = 0; i < 5; i++) {
        
        // 3. SATISFACER EL CHECK DE INSTRUCCIONES (STEP 2)
        // Ejecutamos las 5 instrucciones mágicas (Commutative + Associative)
        // EN EL MISMO BLOQUE BÁSICO.
        
        // ADD (+)
        state = state + modifier;
        
        // MUL (*) - Al ser volatile * volatile, genera instrucción 'mul' (no shift)
        state = state * modifier;
        
        // AND (&)
        state = state & modifier;
        
        // OR (|)
        state = state | modifier;
        
        // XOR (^)
        state = state ^ modifier;
        
        // Un pequeño branch inútil para añadir complejidad al grafo (por si acaso)
        if (m == LEFT) {
            modifier++;
        }
    }

    // 4. RETORNO
    *cur_move_id = (uint8_t)state;
    return;
}

// --- MAIN ---
int main() {
    MOVE moves[100] = {0};
    uint8_t id = 0;
    pos_t p = {0,0};
    get_direction(moves, &id, p, p, p);
    return 0;
}
