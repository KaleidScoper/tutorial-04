# tutorial-04

 安徽大学《可信计算实验课》第三次实验源码。

# 功能

 1. CA启动：生成私钥和公钥。
 2. 示证者注册：生成示证者的公私钥对，并用CA的私钥签署AIK公钥。
 3. 验证者验证：通过CA的公钥验证示证者的AIK公钥的签名。

# 使用方法

 1. 使用下面的命令将其克隆至现有的 Web 服务器的根目录。
 ```bash
 git clone https://github.com/KaleidScoper/tutorial-04.git
 ```
 2. 浏览器访问http://您的服务器地址:您的服务器端口/tutorial-04/index.php
