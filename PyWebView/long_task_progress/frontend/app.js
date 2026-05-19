const barEl = document.getElementById('bar');
const messageEl = document.getElementById('message');
const startButton = document.getElementById('start');

function render(state) {
    barEl.value = state.progress;
    messageEl.textContent = `${state.progress}% · ${state.message}`;
    startButton.disabled = state.running;
}

async function refreshUntilDone() {
    const state = await window.pywebview.api.get_progress();
    render(state);
    if (state.running) {
        setTimeout(refreshUntilDone, 200);
    }
}

startButton.addEventListener('click', async () => {
    render(await window.pywebview.api.start_task());
    refreshUntilDone();
});

window.addEventListener('pywebviewready', refreshUntilDone);
