from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


class TodoApi:
    def __init__(self) -> None:
        self._next_id = 3
        self._todos = [
            {"id": 1, "title": "Create", "done": True},
            {"id": 2, "title": "Read, Update, Delete", "done": False},
        ]

    def list_todos(self) -> list[dict[str, object]]:
        return self._todos

    def create_todo(self, title: str) -> list[dict[str, object]]:
        clean_title = title.strip()
        if clean_title:
            self._todos.append({"id": self._next_id, "title": clean_title, "done": False})
            self._next_id += 1
        return self._todos

    def update_todo(self, todo_id: int, title: str, done: bool) -> list[dict[str, object]]:
        for todo in self._todos:
            if todo["id"] == todo_id:
                todo["title"] = title.strip()
                todo["done"] = done
                break
        return self._todos

    def delete_todo(self, todo_id: int) -> list[dict[str, object]]:
        self._todos = [todo for todo in self._todos if todo["id"] != todo_id]
        return self._todos


def main() -> None:
    webview.create_window(
        "07 Todo CRUD",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=TodoApi(),
        width=620,
        height=540,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
