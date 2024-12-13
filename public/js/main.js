document.getElementById('initCA').addEventListener('click', async () => {
    const res = await fetch('/initCA', { method: 'POST' });
    const data = await res.json();
    displayOutput(data.message);
  });
  
  document.getElementById('registerProver').addEventListener('click', async () => {
    const res = await fetch('/registerProver', { method: 'POST' });
    const data = await res.json();
    displayOutput(data.message);
  });
  
  document.getElementById('issueCert').addEventListener('click', async () => {
    const res = await fetch('/issueCert', { method: 'POST' });
    const data = await res.json();
    displayOutput(JSON.stringify(data));
  });
  
  document.getElementById('remoteAttest').addEventListener('click', async () => {
    const res = await fetch('/remoteAttest', { method: 'POST' });
    const data = await res.json();
    displayOutput(data.message);
  });
  
  function displayOutput(message) {
    const output = document.getElementById('output');
    output.innerText = message;
  }
  