# CA代码
import socket
import json
from utils import generate_key_pair, sign, verify_signature

CA_ADDRESS = ('localhost', 5000)

# 初始化
SK_CA, PK_CA = generate_key_pair()

# 监听连接
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(CA_ADDRESS)
    s.listen(1)
    print(f"CA listening on {CA_ADDRESS}")
    
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024).decode()
            client_data = json.loads(data)
            
            if 'SK_P' in client_data:  # 示证者注册请求
                SK_P = client_data['SK_P']
                PK_P = client_data['PK_P']
                signature_PK_P = client_data['signature_PK_P']

                # 验证示证者的公钥是否合法
                if verify_signature(PK_CA, signature_PK_P, PK_P):
                    AIK_SK, AIK_PK = generate_key_pair()
                    AIK_signature = sign(PK_P, AIK_PK)

                    response_data = {
                        'PK_AIK': AIK_PK,
                        'AIK_signature': AIK_signature,
                        'PK_P_response': PK_P,
                        'response_signature': signature_PK_P
                    }
                    conn.sendall(json.dumps(response_data).encode())

            elif 'PK_AIK' in client_data:  # 平台身份证书颁发请求
                AIK_PK = client_data['PK_AIK']
                AIK_signature = client_data['AIK_signature']
                PK_P_response = client_data['PK_P_response']
                response_signature = client_data['response_signature']

                # 验证AIK签名和PK_P_response的签名
                if verify_signature(PK_CA, response_signature, PK_P_response) and verify_signature(PK_P_response, AIK_signature, AIK_PK):
                    AIK_CA_signature = sign(PK_CA, AIK_PK)
                    conn.sendall(json.dumps({'AIK_CA_signature': AIK_CA_signature}).encode())

            elif 'REPORT' in client_data:  # 远程证明请求
                REPORT = client_data['REPORT']
                REPORT_signature = client_data['REPORT_signature']
                PK_AIK = client_data['PK_AIK']
                AIK_CA_signature = client_data['AIK_CA_signature']

                # 验证AIK_CA_signature
                if verify_signature(PK_CA, AIK_CA_signature, PK_AIK):
                    # 验证REPORT
                    if verify_signature(PK_AIK, REPORT_signature, REPORT):
                        conn.sendall(json.dumps({'status': 'verified'}).encode())
                    else:
                        conn.sendall(json.dumps({'status': 'unverified'}).encode())
