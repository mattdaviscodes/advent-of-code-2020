# Compiler options
COMPILER=g++
OPTIONS=-g -std=c++17 -Wall
COMPILE=$(COMPILER) $(OPTIONS)

# Directories
BUILD=build
COMMON=../common

all: build util main

main: main.cpp util
	$(COMPILE) main.cpp $(COMMON)/util.o -o main.out

util:
	$(COMPILE) -c $(COMMON)/util.cpp -o $(COMMON)/util.o

build:
	mkdir -p $(BUILD)

clean:
	rm -rf *.o main.out main.dSYM $(BUILD)

.PHONY: build clean