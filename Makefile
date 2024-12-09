# Makefile for Miracl Privacy CA Remote Attestation Project

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++11 -O2 -Wall

# Directories
INCLUDE_DIR = /root/codes/miracl-core/include
LIBRARY_DIR = /root/codes/miracl-core/lib
HEADERS_DIR = /root/codes/miracl-exp/tutorial-04/src

# Source files
SRC_DIR = /root/codes/miracl-exp/tutorial-04/src
OBJ_DIR = /root/codes/miracl-exp/tutorial-04/bin
SRC_FILES = main.cpp ca.cpp prover.cpp verifier.cpp

# Object files
OBJ_FILES = $(patsubst %.cpp, $(OBJ_DIR)/%.o, $(SRC_FILES))

# Output binary
BIN = $(OBJ_DIR)/main

all: $(BIN)

$(BIN): $(OBJ_FILES)
	$(CXX) $(CXXFLAGS) -o $(BIN) $(OBJ_FILES) -I$(INCLUDE_DIR) -I$(HEADERS_DIR) -L$(LIBRARY_DIR) -lmiracl

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -I$(HEADERS_DIR) -c $< -o $@

clean:
	rm -f $(OBJ_DIR)/*.o
	rm -f $(BIN)
