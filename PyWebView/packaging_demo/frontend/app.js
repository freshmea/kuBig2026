const envEl = document.getElementById('env');
const commandEl = document.getElementById('command');

window.addEventListener('pywebviewready', async () => {
    const env = await window.pywebview.api.get_environment();
    envEl.innerHTML = Object.entries(env)
        .map(([key, value]) => `<dt>${key}</dt><dd>${value}</dd>`)
        .join('');
    commandEl.textContent = await window.pywebview.api.get_pyinstaller_command();
});
