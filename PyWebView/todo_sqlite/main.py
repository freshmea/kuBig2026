import sqlite3
from pathlib import Path

import webview

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "todos.sqlite3"


class SqliteTodoApi:
    def __init__(self) -> None:
        DATA_DIR.mkdir(exist_ok=True)
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    done INTEGER NOT NULL DEFAULT 0
                )
                """
            )

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    def list_todos(self) -> list[dict[str, object]]:
        with self._connect() as conn:
            rows = conn.execute("SELECT id, title, done FROM todos ORDER BY id DESC").fetchall()
        return [{"id": row["id"], "title": row["title"], "done": bool(row["done"])} for row in rows]

    def create_todo(self, title: str) -> list[dict[str, object]]:
        clean_title = title.strip()
        if clean_title:
            with self._connect() as conn:
                conn.execute("INSERT INTO todos (title, done) VALUES (?, 0)", (clean_title,))
        return self.list_todos()

    def toggle_todo(self, todo_id: int, done: bool) -> list[dict[str, object]]:
        with self._connect() as conn:
            conn.execute("UPDATE todos SET done = ? WHERE id = ?", (int(done), todo_id))
        return self.list_todos()

    def delete_todo(self, todo_id: int) -> list[dict[str, object]]:
        with self._connect() as conn:
            conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        return self.list_todos()


def main() -> None:
    webview.create_window(
        "08 Todo SQLite",
        url=(FRONTEND_DIR / "index.html").as_uri(),
        js_api=SqliteTodoApi(),
        width=620,
        height=540,
        resizable=True,
    )
    webview.start()


if __name__ == "__main__":
    main()
