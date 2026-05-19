const form = document.getElementById('form');
const titleEl = document.getElementById('title');
const listEl = document.getElementById('list');

function render(todos) {
    listEl.innerHTML = '';
    for (const todo of todos) {
        const item = document.createElement('li');
        item.innerHTML = `
            <input class="done" type="checkbox" ${todo.done ? 'checked' : ''} />
            <input class="edit" type="text" value="${todo.title}" />
            <button class="delete" type="button">삭제</button>
        `;
        item.querySelector('.done').addEventListener('change', async (event) => {
            render(await window.pywebview.api.update_todo(todo.id, item.querySelector('.edit').value, event.target.checked));
        });
        item.querySelector('.edit').addEventListener('change', async (event) => {
            render(await window.pywebview.api.update_todo(todo.id, event.target.value, item.querySelector('.done').checked));
        });
        item.querySelector('.delete').addEventListener('click', async () => {
            render(await window.pywebview.api.delete_todo(todo.id));
        });
        listEl.appendChild(item);
    }
}

async function loadTodos() {
    render(await window.pywebview.api.list_todos());
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    render(await window.pywebview.api.create_todo(titleEl.value));
    titleEl.value = '';
});

window.addEventListener('pywebviewready', loadTodos);
