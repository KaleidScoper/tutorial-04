# CA代码
import utils

class CA:
    def __init__(self):
        self.private_key, self.public_key = utils.generate_keypair()
    
    def register_attester(self):
        # 示证者生成公私钥对
        private_key_attester, public_key_attester = utils.generate_keypair()
        
        # 示证者发送自己的公钥和签名给CA
        signature = utils.sign(private_key_attester, self.private_key)
        return public_key_attester, signature

    def issue_aik(self, public_key_attester):
        # 示证者生成AIK的公私钥对
        private_key_aik, public_key_aik = utils.generate_keypair()
        
        # 示证者签名AIK的公钥
        signature_aik = utils.sign(private_key_aik, public_key_attester)
        
        # CA生成签名的AIK公钥
        signature_ca_aik = utils.sign(public_key_aik, self.private_key)
        return (public_key_aik, signature_aik), signature_ca_aik
