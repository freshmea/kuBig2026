const form = document.getElementById('form');
const titleEl = document.getElementById('title');
const listEl = document.getElementById('list');

function render(todos) {
    listEl.innerHTML = '';
    for (const todo of todos) {
        const item = document.createElement('li');
        item.innerHTML = `
            <input class="done" type="checkbox" ${todo.done ? 'checked' : ''} />
            <span class="${todo.done ? 'completed' : ''}">${todo.title}</span>
            <button type="button">삭제</button>
        `;
        item.querySelector('.done').addEventListener('change', async (event) => {
            render(await window.pywebview.api.toggle_todo(todo.id, event.target.checked));
        });
        item.querySelector('button').addEventListener('click', async () => {
            render(await window.pywebview.api.delete_todo(todo.id));
        });
        listEl.appendChild(item);
    }
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    render(await window.pywebview.api.create_todo(titleEl.value));
    titleEl.value = '';
});

window.addEventListener('pywebviewready', async () => {
    render(await window.pywebview.api.list_todos());
});
