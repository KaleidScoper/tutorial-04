CC = g++
CFLAGS = -I../../miracl-core/include -L../../miracl-core/lib -lmiracl
SRC = src/
BUILD = build/

all: ca prover verifier

ca: $(SRC)ca.cpp $(SRC)utils.cpp
	$(CC) $(CFLAGS) -o $(BUILD)ca $(SRC)ca.cpp $(SRC)utils.cpp

prover: $(SRC)prover.cpp $(SRC)utils.cpp
	$(CC) $(CFLAGS) -o $(BUILD)prover $(SRC)prover.cpp $(SRC)utils.cpp

verifier: $(SRC)verifier.cpp $(SRC)utils.cpp
	$(CC) $(CFLAGS) -o $(BUILD)verifier $(SRC)verifier.cpp $(SRC)utils.cpp

clean:
	rm -rf $(BUILD)*
