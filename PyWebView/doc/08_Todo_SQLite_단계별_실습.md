# 08 Todo SQLite 단계별 실습

## 1. 수업 목표

- 메모리 CRUD의 한계를 이해하고 SQLite 저장으로 확장한다.
- Python 표준 라이브러리 `sqlite3`로 테이블 생성과 CRUD를 구현한다.
- 앱 재실행 후에도 데이터가 유지되는 구조를 만든다.

## 2. 최종 결과물

- 데모 폴더: `todo_sqlite`
- 실행: `uv run todo_sqlite/main.py`
- DB 파일: `todo_sqlite/data/todos.sqlite3`

최종 동작:

1. 앱 시작 시 Python이 DB 파일과 테이블을 준비한다.
2. Todo 추가 시 DB에 INSERT한다.
3. 목록 조회 시 DB에서 SELECT한다.
4. 완료 체크 시 UPDATE한다.
5. 삭제 버튼 클릭 시 DELETE한다.

---

## 3. 단계별 실습

### 단계 A. 메모리 CRUD의 문제 확인

#### A-1. 이전 수업 복습

`todo_crud`는 Python 리스트로 CRUD를 구현했다.

#### A-2. 문제점

- 앱을 종료하면 리스트가 사라진다.
- 실제 앱은 데이터를 유지해야 한다.
- 파일 저장도 가능하지만 검색/수정/삭제가 늘어나면 DB가 더 적합하다.

#### A-3. 해결

SQLite를 사용한다.

강의 포인트:
- SQLite는 별도 서버 없이 파일 하나로 동작하므로 데스크톱 앱 수업에 적합하다.

---

### 단계 B. DB 경로와 연결 함수 만들기

#### B-1. 구현

```python
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "todos.sqlite3"

def _connect(self) -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
```

#### B-2. 설명

- DB 파일도 앱 데이터이므로 `data` 폴더에 둔다.
- `row_factory = sqlite3.Row`를 쓰면 컬럼 이름으로 값을 읽을 수 있다.

#### B-3. 트릭

연결 코드를 함수로 분리하면 모든 CRUD 메서드가 같은 방식으로 DB에 접근한다.

---

### 단계 C. 테이블 생성

#### C-1. 구현

```python
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0
    )
    """
)
```

#### C-2. 설명

- `id`: 자동 증가 기본키
- `title`: Todo 제목
- `done`: SQLite에는 bool 타입 대신 0/1 정수로 저장
- `IF NOT EXISTS`: 이미 테이블이 있어도 오류를 내지 않는다.

강의 포인트:
- 앱 시작 시 필요한 테이블을 준비하면 최초 실행이 편해진다.

---

### 단계 D. SELECT 구현

#### D-1. 구현

```python
rows = conn.execute("SELECT id, title, done FROM todos ORDER BY id DESC").fetchall()
return [{"id": row["id"], "title": row["title"], "done": bool(row["done"])} for row in rows]
```

#### D-2. 문제 해결 개념

DB row는 그대로 JS에 넘기기 어렵다.
dict 리스트로 변환해서 bridge 반환값을 단순하게 만든다.

---

### 단계 E. INSERT, UPDATE, DELETE 구현

#### E-1. INSERT

```python
conn.execute("INSERT INTO todos (title, done) VALUES (?, 0)", (clean_title,))
```

#### E-2. UPDATE

```python
conn.execute("UPDATE todos SET done = ? WHERE id = ?", (int(done), todo_id))
```

#### E-3. DELETE

```python
conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
```

#### E-4. 트릭

SQL 문자열에 값을 직접 붙이지 않는다.
항상 `?` 파라미터 바인딩을 사용한다.

강의 포인트:
- SQL injection은 웹 서버만의 문제가 아니다. SQL 값 전달 습관은 처음부터 바르게 잡는다.

---

## 4. 체크리스트

- [ ] 앱 실행 시 DB 파일이 생성된다.
- [ ] Todo를 추가하면 DB에 저장된다.
- [ ] 앱 재실행 후에도 Todo가 남아 있다.
- [ ] 완료 체크가 DB에 반영된다.
- [ ] 삭제가 DB에서 제거된다.

## 5. 확장 과제

- 마감일 컬럼 추가
- 생성 시각 저장
- 완료 항목 전체 삭제
