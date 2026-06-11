CC = clang
OPT = opt

SRC = src/
BIN = bin/

VALID_PASS = valid_pass
LLVM_PASS = the_maze_of_the_sorcerer
LLVM_EMIT = emit

LPASS = $(SRC)$(LLVM_PASS).cpp
LIB = $(BIN)$(LLVM_PASS).so

VPASS = $(SRC)$(VALID_PASS).c
OUT = $(BIN)$(VALID_PASS)

EMIT = $(BIN)$(LLVM_EMIT).ll
VEMIT = $(BIN)$(VALID_PASS).ll

$(EMIT): $(VPASS)
	$(CC) -O1 -emit-llvm -S $< -o $@

$(VEMIT): $(EMIT) $(LIB)
	$(OPT) -load-pass-plugin $(LIB) -passes=custom_pass $< -o $@
	
$(OUT): $(VEMIT)
	$(CC) $< -o $@

init:
	@echo "Building" $(LLVM_PASS)
	@echo ---------------------------------
	mkdir -p bin
	

all: init $(OUT) $(EMIT)

clean:
	rm $(OUT) $(EMIT)
