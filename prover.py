# 证明者代码
import socket
import json
from utils import generate_key_pair, sign, verify_signature

CA_ADDRESS = ('localhost', 5000)

# 连接到CA
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(CA_ADDRESS)

    # 示证者生成公私钥对
    SK_P, PK_P = generate_key_pair()
    signature_PK_P = sign(CA_ADDRESS, PK_P)

    # 发送注册信息到CA
    data = {
        'SK_P': SK_P,
        'PK_P': PK_P,
        'signature_PK_P': signature_PK_P
    }
    s.sendall(json.dumps(data).encode())
    response = s.recv(1024).decode()
    AIK_PK, AIK_signature, PK_P_response, response_signature = json.loads(response)

    # 请求平台身份证书
    SK_AIK, PK_AIK = generate_key_pair()
    AIK_signature = sign(PK_P_response, PK_AIK)

    # 发送AIK证书申请到CA
    data = {
        'PK_AIK': PK_AIK,
        'AIK_signature': AIK_signature,
        'PK_P_response': PK_P_response,
        'response_signature': response_signature
    }
    s.sendall(json.dumps(data).encode())
    response = s.recv(1024).decode()
    AIK_CA_signature = json.loads(response)

    # 远程证明
    REPORT = ...  # PCR数据
    REPORT_signature = sign(SK_AIK, REPORT)
    data = {
        'REPORT': REPORT,
        'REPORT_signature': REPORT_signature,
        'PK_AIK': PK_AIK,
        'AIK_CA_signature': AIK_CA_signature
    }
    s.sendall(json.dumps(data).encode())
    response = s.recv(1024).decode()
    verification_result = json.loads(response)
    if verification_result['status'] == 'verified':
        print("Remote attestation successful.")
