#!/bin/bash

# 启动CA
python3 /path/to/tutorial-04/ca.py &

# 等待CA启动
sleep 1

# 启动示证者
python3 /path/to/tutorial-04/client.py &

# 等待示证者启动
sleep 1

# 启动证明者
python3 /path/to/tutorial-04/prover.py
