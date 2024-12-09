#示证者的功能
import utils

def attest(aik_keypair):
    # 示证者生成报告
    report_data = utils.generate_report_data()
    
    # 使用AIK私钥签名报告
    report_signature = utils.sign(report_data, aik_keypair['private_key'])
    
    # 返回报告数据和签名
    return {'report': report_data, 'report_signature': report_signature, 'aik_public_key': aik_keypair['public_key']}, report_signature
