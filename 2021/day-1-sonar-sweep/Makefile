# Compiler options
COMPILER=g++
OPTIONS=-g -std=c++17 -Wall
COMPILE=$(COMPILER) $(OPTIONS)

# Directories
BUILD=build
COMMON=../common

all: build common main

main: main.cpp common
	$(COMPILE) main.cpp $(COMMON)/common.o -o main.out

common:
	$(COMPILE) -c $(COMMON)/common.cpp -o $(COMMON)/common.o

build:
	mkdir -p $(BUILD)

clean:
	rm -rf *.o main.out main.dSYM $(BUILD)

.PHONY: build clean