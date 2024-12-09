// 工具函数头文件

#ifndef UTILS_H
#define UTILS_H

#include "miracl.h"
#include <string>

// 初始化Miracl
void init_miracl();

// 生成密钥对
void generate_keypair(csprng &rng, big &priv_key, epoint *&pub_key, ecurve *curve);

// 保存密钥
void save_keypair(const char *pub_file, const char *priv_file, big &priv_key, epoint *pub_key);

// 签名
void sign_data(big &priv_key, big &data, char *signature);

// 验证签名
bool verify_signature(epoint *pub_key, big &data, char *signature);

#endif
