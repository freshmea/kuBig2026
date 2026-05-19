const screenEl = document.getElementById('screen');
let screens = {};

function showScreen(name) {
    const screen = screens[name];
    screenEl.innerHTML = `<h1>${screen.title}</h1><p>${screen.body}</p>`;
}

document.querySelectorAll('button[data-screen]').forEach((button) => {
    button.addEventListener('click', () => showScreen(button.dataset.screen));
});

window.addEventListener('pywebviewready', async () => {
    screens = await window.pywebview.api.get_screen_data();
    showScreen('home');
});
