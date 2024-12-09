// 工具函数（签名/验签，密钥生成等)

#include "utils.h"
#include <fstream>
#include <ctime>

// 初始化Miracl
void init_miracl() {
    miracl *mip = mirsys(5000, 16);
    mip->IOBASE = 16;
}

// 生成密钥对
void generate_keypair(csprng &rng, big &priv_key, epoint *&pub_key, ecurve *curve) {
    priv_key = mirvar(0);
    bigrand(curve->order, priv_key);
    pub_key = epoint_init();
    ecurve_mult(priv_key, curve->G, pub_key);
}

// 保存密钥
void save_keypair(const char *pub_file, const char *priv_file, big &priv_key, epoint *pub_key) {
    ofstream pub(pub_file);
    ofstream priv(priv_file);

    priv << priv_key << endl;

    big x = mirvar(0), y = mirvar(0);
    epoint_get(pub_key, x, y);
    pub << x << endl << y << endl;

    pub.close();
    priv.close();
    mirkill(x);
    mirkill(y);
}

// 签名
void sign_data(big &priv_key, big &data, char *signature) {
    ecdsa_sign(priv_key, data, signature);
}

// 验证签名
bool verify_signature(epoint *pub_key, big &data, char *signature) {
    return ecdsa_verify(pub_key, data, signature);
}
