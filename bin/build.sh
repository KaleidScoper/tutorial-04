#!/bin/bash

# Set paths
PROJECT_DIR="/root/codes/miracl-exp/tutorial-04"
SRC_DIR="${PROJECT_DIR}/src"
OBJ_DIR="${PROJECT_DIR}/bin"
INCLUDE_DIR="/root/codes/miracl-core/include"
LIBRARY_DIR="/root/codes/miracl-core/lib"

# Compile the project using Makefile
cd ${PROJECT_DIR}
make

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Build completed successfully."
else
    echo "Build failed."
fi
