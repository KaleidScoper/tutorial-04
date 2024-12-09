// 示证者的代码

#include "utils.h"

int main() {
    init_miracl();

    // 加载CA公钥
    epoint *PK_CA = load_public_key("../keys/CA_pub.txt");

    // 模拟示证者生成AIK密钥
    csprng rng;
    big SK_AIK = mirvar(0);
    epoint *PK_AIK = epoint_init();
    ecurve curve(/* curve parameters */);
    generate_keypair(rng, SK_AIK, PK_AIK, &curve);

    // 签名
    char signature[64];
    sign_data(SK_AIK, PK_AIK->X, signature);

    // 保存AIK公钥
    save_keypair("../keys/AIK_pub.txt", "../keys/AIK_priv.txt", SK_AIK, PK_AIK);

    cout << "Prover: AIK generated and signed. Data saved in 'keys/' directory." << endl;
    return 0;
}
