// 主服务器文件

const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const CA = require('./CA');
const Prover = require('./Prover');
const Verifier = require('./Verifier');

const app = express();
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '../public'))); // 设置静态文件目录

// 实例化各模块
const ca = new CA();
const prover = new Prover(ca);
const verifier = new Verifier(ca);

// 处理根路径请求，返回前端主页面
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../index.html'));
});

// CA 初始化
app.post('/initCA', (req, res) => {
  ca.init();
  res.send({ message: 'CA initialized.' });
});

// 示证者注册
app.post('/registerProver', (req, res) => {
  prover.register();
  res.send({ message: 'Prover registered.' });
});

// 平台身份证书颁发
app.post('/issueCert', (req, res) => {
  const result = ca.issueCert(prover.getAIKPublicKey());
  res.send(result);
});

// 远程证明
app.post('/remoteAttest', (req, res) => {
  const report = prover.generateReport();
  const result = verifier.verify(report);
  res.send(result);
});

// 启动服务器
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
  console.log(`Access it via http://localhost:${PORT}`);
});
