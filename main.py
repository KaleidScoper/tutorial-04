#主函数
import ca
import verifier
import attester

def main():
    # 初始化
    ca_obj = ca.CA()

    # 示证者注册
    public_key_attester, signature_attester = ca_obj.register_attester()

    # 平台身份证书颁发
    aik_keypair, signature_aik = ca_obj.issue_aik(public_key_attester)

    # 示例远程证明
    report, report_signature = attester.attest(aik_keypair)
    verifier.verify_report(report, report_signature, public_key_attester, ca_obj.public_key)

if __name__ == "__main__":
    main()
