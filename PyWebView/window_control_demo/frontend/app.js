const statusEl = document.getElementById('status');

document.querySelectorAll('button[data-action]').forEach((button) => {
    button.addEventListener('click', async () => {
        const action = button.dataset.action;
        statusEl.textContent = await window.pywebview.api[action]();
    });
});
