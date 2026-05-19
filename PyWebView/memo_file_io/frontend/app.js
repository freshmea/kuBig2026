const noteEl = document.getElementById('note');
const statusEl = document.getElementById('status');
const loadButton = document.getElementById('load');
const saveButton = document.getElementById('save');

async function loadNote() {
    const result = await window.pywebview.api.load_note();
    noteEl.value = result.text;
    statusEl.textContent = '파일에서 불러왔습니다.';
}

async function saveNote() {
    const result = await window.pywebview.api.save_note(noteEl.value);
    statusEl.textContent = `저장 완료: ${result.path}`;
}

window.addEventListener('pywebviewready', loadNote);
loadButton.addEventListener('click', loadNote);
saveButton.addEventListener('click', saveNote);
