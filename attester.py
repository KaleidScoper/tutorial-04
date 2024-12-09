#示证者的功能

import utils

def attest(aik_keypair):
    # 修正解包语句，确保取出正确的私钥和公钥
    private_key_aik = aik_keypair[0]
    public_key_aik = aik_keypair[1]
    report_data = utils.generate_report_data()
    report_signature = utils.sign(report_data, private_key_aik)
    return report_data, report_signature
