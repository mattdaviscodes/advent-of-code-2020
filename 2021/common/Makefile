HEADERS = $(sort $(wildcard *.h))
SRCS = $(sort $(wildcard *.cpp))
OBJECTS := $(patsubst %.cpp,%.o,$(SRCS))
CXX = g++
CXX_FLAGS = -Wall -std=c++17
BUILD_DIR=build

.PHONY: default all clean

all: setup depend $(OBJECTS)

setup:
	mkdir -p $(BUILD_DIR)

#Rules to recompile template headers when they change
depend: .depend
.depend: $(HEADERS)
	rm -f ./.depend
	$(CXX) $(CXX_FLAGS) -MM $^ > ./.depend;
include .depend

%.o: %.cpp $(HEADERS)
	$(CXX) $(CXX_FLAGS) -c $< -o $(BUILD_DIR)/$@

clean:
	-rm -f $(BUILD_DIR)
	-rm -f ./.depend