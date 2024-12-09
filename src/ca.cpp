// CA的代码

#include "utils.h"

int main() {
    init_miracl();
    csprng rng;

    // 生成CA的密钥对
    big SK_CA = mirvar(0);
    epoint *PK_CA = epoint_init();
    ecurve curve(/* curve parameters */);
    generate_keypair(rng, SK_CA, PK_CA, &curve);

    // 保存密钥
    save_keypair("../keys/CA_pub.txt", "../keys/CA_priv.txt", SK_CA, PK_CA);

    cout << "CA initialized. Keys saved in 'keys/' directory." << endl;
    return 0;
}
