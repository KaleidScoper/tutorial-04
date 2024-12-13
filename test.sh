#!/bin/bash

# 此脚本并非启动or测试脚本，与项目功能无关。

rm -rf tutorial-04

rm -rf tutorial-04-main

sleep 1

unzip tutorial-04-main.zip

sleep 1

mv tutorial-04-main tutorial-04

sleep 1

rm *.zip

sleep 1

ls -l

exit 0