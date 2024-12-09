# CA代码

import utils

class CA:
    def __init__(self):
        self.private_key, self.public_key = utils.generate_keypair()
    
    def register_attester(self):
        private_key_attester, public_key_attester = utils.generate_keypair()
        signature = utils.sign(public_key_attester, self.private_key)
        return public_key_attester, signature

    def issue_aik(self, public_key_attester):
        private_key_aik, public_key_aik = utils.generate_keypair()
        # 修正签名操作的参数，使用 CA 的私钥签名
        signature_aik = utils.sign(public_key_aik, self.private_key)
        signature_ca_aik = utils.sign(public_key_aik, self.private_key)
        return (private_key_aik, public_key_aik), signature_ca_aik
