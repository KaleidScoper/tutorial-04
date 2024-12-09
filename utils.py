# 工具函数（签名、验证等）
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP

# 生成公私钥对
def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# 签名
def sign(private_key, message):
    key = RSA.import_key(private_key)
    h = SHA256.new(message.encode())
    signer = pkcs1_15.new(key)
    return signer.sign(h)

# 验证签名
def verify_signature(public_key, signature, message):
    key = RSA.import_key(public_key)
    h = SHA256.new(message.encode())
    verifier = pkcs1_15.new(key)
    try:
        verifier.verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
