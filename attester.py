#示证者的功能

import utils

def attest(aik_keypair):
    private_key_aik, public_key_aik = aik_keypair  # 解包元组
    report_data = utils.generate_report_data()
    report_signature = utils.sign(report_data, private_key_aik)
    return report_data, report_signature
