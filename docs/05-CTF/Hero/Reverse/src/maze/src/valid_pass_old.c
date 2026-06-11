#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_X 10
#define MAX_Y 10

#define ORCS 'O'

char g_map[MAX_X][MAX_Y];

typedef enum MOVE_S {
  LEFT = 0,
  RIGHT,
  UP,
  DOWN
} MOVE;

typedef struct pos_s{
  uint8_t x;
  uint8_t y;
} pos_t;

void __attribute__((noinline)) chose_direction(MOVE *moves, uint8_t *cur_move_id, pos_t *initial_pos, pos_t wanted_pos) {
  // TODO
}

void __attribute__((noinline)) place_entity(pos_t *new_pos, uint8_t entity, pos_t *all_used_position, uint8_t *used_position) {
  int in_place = 0;
  while(!in_place) {
    
    *new_pos = (pos_t){rand() % MAX_X, rand() % MAX_Y};
    if(!(*used_position)) {
      goto set_pos;
    }
    for(uint8_t i = 0; i < *used_position; i++) {
      if((new_pos->x != all_used_position[i].x) || (new_pos->y != all_used_position[i].y)) {
        in_place = 1;
        break;
      }
    }
  }

set_pos:
  g_map[new_pos->x][new_pos->y] = entity;
  all_used_position[(*used_position)++] = *new_pos;
}

// We absolutely want to avoid ORCS('O') because they would kill us.
void __attribute__((noinline)) get_direction(MOVE *moves, uint8_t *cur_move_id, pos_t hero_pos, pos_t exit_pos, pos_t rune_pos) {
  pos_t new_pos = hero_pos;
  pos_t wanted_pos = rune_pos; 
  // TODO

  
  return;
}

void show_map() {
  for(uint8_t i = 0; i < MAX_X; i++) {
    for(uint8_t j = 0; j < MAX_Y; j++) {
      printf("%c", g_map[j][i]);
    }
    printf("\n");
  }

  return;
}

int main() {
  pos_t all_used_position[10] = {0};
  uint8_t nb_used_position = 0;
  pos_t hero_pos = {0};
  pos_t exit_pos = {0};
  pos_t rune_pos = {0};
  pos_t orcs_pos = {0};
  MOVE moves[100] = {0};
  uint8_t cur_move_id = 0;
  srand(time(0));

  memset(g_map, 'M', MAX_X * MAX_Y);

  place_entity(&hero_pos, 'H', all_used_position, &nb_used_position);
  // TODO
  show_map();
  get_direction(moves, &cur_move_id, hero_pos, exit_pos, rune_pos);

  for(uint8_t i = 0; i < cur_move_id; i++) {
    char *mov_to_print = NULL;
    switch(moves[i]) {
      case LEFT:
        mov_to_print = "LEFT";
        break;
      case RIGHT:
        mov_to_print = "RIGHT";
        break;
      case UP:
        mov_to_print = "UP";
        break;
      case DOWN:
        mov_to_print = "DOWN";
        break;
    }
    printf("%s ", mov_to_print);
  }
  printf("\n");
  return 0;
}
