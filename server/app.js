// 主服务器文件

const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const CA = require('./CA');
const Prover = require('./Prover');
const Verifier = require('./Verifier');

const app = express();
app.use(bodyParser.json());
app.use(express.static('public'));

const ca = new CA();
const prover = new Prover(ca);
const verifier = new Verifier(ca);

app.post('/initCA', (req, res) => {
  ca.init();
  res.send({ message: 'CA initialized.' });
});

app.post('/registerProver', (req, res) => {
  prover.register();
  res.send({ message: 'Prover registered.' });
});

app.post('/issueCert', (req, res) => {
  const result = ca.issueCert(prover.getAIKPublicKey());
  res.send(result);
});

app.post('/remoteAttest', (req, res) => {
  const report = prover.generateReport();
  const result = verifier.verify(report);
  res.send(result);
});

app.listen(3000, () => console.log('Server running on port 3000'));
