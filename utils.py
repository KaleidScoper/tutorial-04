# 工具函数（签名、验证等）

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os

def generate_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def sign(data, private_key):
    key = RSA.import_key(private_key)
    h = SHA256.new(data.encode())  # 确保数据是字符串并进行编码
    signature = pkcs1_15.new(key).sign(h)
    return signature

def verify_signature(data, signature, public_key):
    key = RSA.import_key(public_key)
    h = SHA256.new(data.encode())  # 确保数据是字符串并进行编码
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

def generate_report_data():
    # 这个函数应该生成实际的报告数据，以供证明过程使用
    return "Sample report data"
