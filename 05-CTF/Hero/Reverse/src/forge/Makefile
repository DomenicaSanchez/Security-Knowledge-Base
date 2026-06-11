CC = clang

SRC = src/
BIN = bin/

VALID_PASS = valid_pass
LLVM_PASS = apprentice_of_the_IR_forge
LLVM_EMIT = emit

VPASS = $(SRC)$(VALID_PASS).c
OUT = $(BIN)$(VALID_PASS)
LIB = $(BIN)$(LLVM_PASS).so

EMIT = $(BIN)$(LLVM_EMIT).ll

$(EMIT): $(VPASS)
	$(CC) -O1 -emit-llvm -S $< -o $@
	
$(OUT): $(LIB)
	$(CC) -O1 -fpass-plugin=$< $(VPASS) -o $@

init:
	@echo "Running apprentice_of_the_IR_forge"
	@echo ---------------------------------
	mkdir -p bin

all: init $(EMIT) $(OUT) 

clean:
	rm $(OUT) $(EMIT)
