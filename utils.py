# 工具函数（签名、验证等）

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def sign(data, private_key):
    key = RSA.import_key(private_key)
    if isinstance(data, str):
        data = data.encode()  # 如果是字符串，进行编码
    h = SHA256.new(data)
    signature = pkcs1_15.new(key).sign(h)
    return signature

def verify_signature(data, signature, public_key):
    key = RSA.import_key(public_key)
    if isinstance(data, str):
        data = data.encode()  # 如果是字符串，进行编码
    h = SHA256.new(data)
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

def generate_report_data():
    # 生成实验报告数据
    return "Sample report data"
