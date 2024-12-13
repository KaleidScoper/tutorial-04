// 验证者逻辑

const crypto = require('crypto');

class Verifier {
  constructor(ca) {
    this.ca = ca;
  }

  verify(report) {
    const { report: reportData, signature, aikPublicKey } = report;

    // Verify AIK Certificate with CA
    const { signature: certSignature } = this.ca.issueCert(aikPublicKey);
    const validCert = this.ca.verify(aikPublicKey, certSignature, this.ca.publicKey);
    if (!validCert) return { valid: false, message: 'Invalid AIK Certificate' };

    // Verify Report with AIK Public Key
    const verify = crypto.createVerify('SHA256');
    verify.update(reportData);
    verify.end();
    const validReport = verify.verify(aikPublicKey, signature, 'hex');
    if (!validReport) return { valid: false, message: 'Invalid Report' };

    return { valid: true, message: 'Report Verified Successfully' };
  }
}

module.exports = Verifier;
