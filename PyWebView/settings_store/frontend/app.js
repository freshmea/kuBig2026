const themeEl = document.getElementById('theme');
const fontSizeEl = document.getElementById('fontSize');
const lastCountEl = document.getElementById('lastCount');
const saveButton = document.getElementById('save');
const previewEl = document.getElementById('preview');
const statusEl = document.getElementById('status');

function collectSettings() {
    return {
        theme: themeEl.value,
        fontSize: Number(fontSizeEl.value),
        lastCount: Number(lastCountEl.value),
    };
}

function applySettings(settings) {
    themeEl.value = settings.theme;
    fontSizeEl.value = settings.fontSize;
    lastCountEl.value = settings.lastCount;
    document.body.dataset.theme = settings.theme;
    previewEl.style.fontSize = `${settings.fontSize}px`;
    previewEl.textContent = `마지막 카운터 값: ${settings.lastCount}`;
}

async function loadSettings() {
    applySettings(await window.pywebview.api.load_settings());
}

async function saveSettings() {
    const settings = collectSettings();
    applySettings(settings);
    const result = await window.pywebview.api.save_settings(settings);
    statusEl.textContent = `저장 완료: ${result.path}`;
}

window.addEventListener('pywebviewready', loadSettings);
themeEl.addEventListener('change', () => applySettings(collectSettings()));
fontSizeEl.addEventListener('input', () => applySettings(collectSettings()));
lastCountEl.addEventListener('input', () => applySettings(collectSettings()));
saveButton.addEventListener('click', saveSettings);
