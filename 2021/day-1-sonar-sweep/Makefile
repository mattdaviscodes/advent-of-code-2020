COMPILER=g++
OPTIONS=-g -std=c++17 -Wall
COMPILE=$(COMPILER) $(OPTIONS)
BUILD=build

all: build main

main.out: main.cpp $(BUILD)/readFile.o
	$(COMPILE) main.cpp $(BUILD)/readFile.o -o main.out

$(BUILD)/readFile.o: readFile.cpp readFile.h
	$(COMPILE) -c readFile.cpp -o $(BUILD)/readFile.o

build:
	mkdir -p $(BUILD)

clean:
	rm -rf *.o main.out main.dSYM $(BUILD)

.PHONY: build clean