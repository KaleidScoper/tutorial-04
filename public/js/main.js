document.addEventListener('DOMContentLoaded', () => {
  const output = document.getElementById('output');

  function log(message) {
    const p = document.createElement('p');
    p.textContent = message;
    output.appendChild(p);
  }

  document.getElementById('initCA').addEventListener('click', () => {
    fetch('/initCA', { method: 'POST' })
      .then((response) => response.json())
      .then((data) => log(data.message))
      .catch((err) => log(`初始化 CA 失败: ${err}`));
  });

  document.getElementById('registerProver').addEventListener('click', () => {
    fetch('/registerProver', { method: 'POST' })
      .then((response) => response.json())
      .then((data) => log(data.message))
      .catch((err) => log(`注册示证者失败: ${err}`));
  });

  document.getElementById('issueCert').addEventListener('click', () => {
    fetch('/issueCert', { method: 'POST' })
      .then((response) => response.json())
      .then((data) => log(data.message))
      .catch((err) => log(`颁发 AIK 证书失败: ${err}`));
  });

  document.getElementById('remoteAttest').addEventListener('click', () => {
    fetch('/remoteAttest', { method: 'POST' })
      .then((response) => response.json())
      .then((data) => log(`远程证明结果: ${JSON.stringify(data)}`))
      .catch((err) => log(`远程证明失败: ${err}`));
  });
});
