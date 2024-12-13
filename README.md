# tutorial-04

 安徽大学《可信计算实验课》第三次实验源码。

# 使用方法

 1. 在您的设备下载本项目，或者使用下面的命令克隆。注意不要将其克隆至现有的Web服务器的根目录——如果你碰巧有一个的话。
 ```bash
 git clone https://github.com/KaleidScoper/tutorial-04.git
 ```
 2. 进入项目内的server目录，然后使用下面的命令安装依赖：
 ```bash
 sudo apt update
 sudo apt install -y nodejs npm
 node -v     # 检查 Node.js 版本
 npm -v      # 检查 npm 版本
 npm init -y # 生成 package.json
 npm install express body-parser crypto --save
 npm list
 ```
 3. 执行启动命令：
 ```bash
 node app.js
 ```
 4. 浏览器访问Node.js默认端口，也就是http://您的服务器地址:3000/
 
 5. 然后获得预期输出。
