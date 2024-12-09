# Makefile for Miracl Privacy CA Remote Attestation Project

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++11 -O2 -Wall

# Directories
INCLUDE_DIR = /root/codes/miracl-core/include
LIBRARY_DIR = /root/codes/miracl-core/lib

# Source files
SRC_DIR = /root/codes/miracl-exp/tutorial-04/src
OBJ_DIR = /root/codes/miracl-exp/tutorial-04/bin
SRC_FILES = main.cpp ca.cpp prover.cpp verifier.cpp

# Object files
OBJ_FILES = $(SRC_FILES:%.cpp=%.o)

# Output binary
BIN = main

all: $(BIN)

$(BIN): $(OBJ_FILES)
	$(CXX) $(CXXFLAGS) -o $(OBJ_DIR)/$(BIN) $(OBJ_FILES) -L$(LIBRARY_DIR) -lmiracl

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

clean:
	rm -f $(OBJ_DIR)/*.o
	rm -f $(OBJ_DIR)/$(BIN)
