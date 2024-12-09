#验证者

import utils

def verify_report(report, report_signature, public_key_attester, public_key_ca):
    # 验证AIK公钥的签名
    if not utils.verify_signature(report['aik_public_key'], report['aik_signature'], public_key_ca):
        print("验证失败：CA的AIK签名无效")
        return False
    
    # 验证报告的签名
    if not utils.verify_signature(report['report'], report['report_signature'], public_key_attester):
        print("验证失败：示证者的报告签名无效")
        return False
    
    print("验证成功：报告有效")
    return True
