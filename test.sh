#!/bin/bash

# 此脚本用于重命名解压文件夹。
# 并非启动or测试脚本，与项目功能无关。
# 国内VPS无法git pull，我懒得配置代理了。

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
