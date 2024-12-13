// CA逻辑

const crypto = require('crypto');
const fs = require('fs');

class CA {
  init() {
    const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', { modulusLength: 2048 });
    this.privateKey = privateKey.export({ type: 'pkcs1', format: 'pem' });
    this.publicKey = publicKey.export({ type: 'spki', format: 'pem' });

    fs.writeFileSync('./server/keys/ca-keys.json', JSON.stringify({
      privateKey: this.privateKey,
      publicKey: this.publicKey
    }));
  }

  sign(data) {
    const sign = crypto.createSign('SHA256');
    sign.update(data);
    sign.end();
    return sign.sign(this.privateKey, 'hex');
  }

  verify(data, signature, publicKey) {
    const verify = crypto.createVerify('SHA256');
    verify.update(data);
    verify.end();
    return verify.verify(publicKey, signature, 'hex');
  }

  issueCert(publicKey) {
    const signature = this.sign(publicKey);
    return { publicKey, signature };
  }
}

module.exports = CA;
