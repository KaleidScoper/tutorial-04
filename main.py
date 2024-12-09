import ca
import verifier
import attester

def main():
    # 初始化 CA
    ca_obj = ca.CA()

    # 示证者注册
    public_key_attester, signature_attester = ca_obj.register_attester()

    # 平台身份证书颁发
    aik_keypair, signature_ca_aik = ca_obj.issue_aik(public_key_attester)

    # 示证者生成报告并签名
    report, report_signature = attester.attest(aik_keypair[0])  # 传递 (private_key_aik, public_key_aik)

    # 验证者验证报告
    verifier.verify_report(report, report_signature, aik_keypair[0][1], signature_ca_aik, ca_obj.public_key)

if __name__ == "__main__":
    main()
