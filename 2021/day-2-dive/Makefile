# Compiler options
COMPILER=g++
OPTIONS=-g -std=c++17 -Wall
COMPILE=$(COMPILER) $(OPTIONS)

# Directories
BUILD=build
COMMON=../common

all: build common main

main: main.cpp common
	$(COMPILE) main.cpp $(COMMON)/readFile.o -o main.out

common:
	$(COMPILE) -c $(COMMON)/readFile.cpp -o $(COMMON)/readFile.o

build:
	mkdir -p $(BUILD)

clean:
	rm -rf *.o main.out main.dSYM $(BUILD)

.PHONY: build clean