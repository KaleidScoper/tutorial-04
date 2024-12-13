function startCA() {
  // 生成CA的公私钥对
  const privateKeyCA = generatePrivateKey();
  const publicKeyCA = generatePublicKey(privateKeyCA);

  // 保存CA的公钥
  console.log("CA 公钥:", publicKeyCA);
}

function generatePrivateKey() {
  // 生成一个随机私钥
  return Math.floor(Math.random() * 1000);
}

function generatePublicKey(privateKey) {
  // 使用简单的公钥生成算法
  return privateKey * 2;
}
