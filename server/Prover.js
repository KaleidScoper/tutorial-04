// 示证者逻辑

const crypto = require('crypto');
const fs = require('fs');

class Prover {
  constructor(ca) {
    this.ca = ca;
    this.proverKeys = {};
    this.aikKeys = {};
  }

  register() {
    const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', { modulusLength: 2048 });
    this.proverKeys = { publicKey, privateKey };
    const signature = this.ca.sign(publicKey.export({ type: 'spki', format: 'pem' }));

    fs.writeFileSync('./server/keys/provers.json', JSON.stringify({
      publicKey: publicKey.export({ type: 'spki', format: 'pem' }),
      privateKey: privateKey.export({ type: 'pkcs1', format: 'pem' }),
      signature,
    }));
  }

  getAIKPublicKey() {
    const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', { modulusLength: 2048 });
    this.aikKeys = { publicKey, privateKey };
    const signature = crypto.createSign('SHA256');
    signature.update(publicKey.export({ type: 'spki', format: 'pem' }));
    signature.end();
    return {
      aikPublicKey: publicKey.export({ type: 'spki', format: 'pem' }),
      signature: signature.sign(this.proverKeys.privateKey, 'hex'),
    };
  }

  generateReport() {
    const report = JSON.stringify({ PCR: [1, 2, 3] });
    const signature = crypto.createSign('SHA256');
    signature.update(report);
    signature.end();
    return {
      report,
      signature: signature.sign(this.aikKeys.privateKey, 'hex'),
      aikPublicKey: this.aikKeys.publicKey.export({ type: 'spki', format: 'pem' }),
    };
  }
}

module.exports = Prover;
