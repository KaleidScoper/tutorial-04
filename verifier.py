#验证者
import utils

def verify_report(report, report_signature, public_key_attester, public_key_ca):
    # 验证AIK公钥的签名
    if not utils.verify_signature(report['aik_public_key'], report['aik_signature'], public_key_ca):
        print("Verification failed: CA's AIK signature is not valid")
        return False
    
    # 验证报告的签名
    if not utils.verify_signature(report['report'], report['report_signature'], public_key_attester):
        print("Verification failed: Attester's report signature is not valid")
        return False
    
    print("Verification successful: Report is valid")
    return True
