# 07 Todo CRUD 단계별 실습

## 1. 수업 목표

- Create, Read, Update, Delete의 기본 흐름을 Python 객체로 구현한다.
- Todo 목록 상태를 Python이 소유하고, JS는 이벤트 전달과 렌더링만 담당한다.
- ID 기반 데이터 수정/삭제가 왜 필요한지 이해한다.

## 2. 최종 결과물

- 데모 폴더: `todo_crud`
- 실행: `uv run todo_crud/main.py`

최종 동작:

1. Python API 객체가 Todo 리스트를 메모리에 가진다.
2. JS는 추가/수정/삭제 이벤트를 Python에 전달한다.
3. Python이 리스트를 변경한다.
4. 변경 후 전체 Todo 목록을 JS에 반환한다.
5. JS는 받은 목록을 다시 그린다.

---

## 3. 단계별 실습

### 단계 A. Todo를 화면 배열로만 관리해 보기

#### A-1. 쉬운 접근

JS 배열에 Todo를 넣고 화면에 출력할 수 있다.

#### A-2. 문제점

- Python 수업인데 핵심 상태가 JS에 생긴다.
- 나중에 파일 저장, SQLite 저장으로 연결하기 어렵다.
- 앱 로직이 프론트 코드에 섞인다.

#### A-3. 해결

Todo 상태와 CRUD 규칙을 Python 객체에 둔다.

강의 포인트:
- Python 심화 수업에서는 "상태를 Python이 소유한다"는 원칙을 반복한다.

---

### 단계 B. Python에 초기 상태 만들기

#### B-1. 구현

```python
class TodoApi:
    def __init__(self) -> None:
        self._next_id = 3
        self._todos = [
            {"id": 1, "title": "Create", "done": True},
            {"id": 2, "title": "Read, Update, Delete", "done": False},
        ]
```

#### B-2. 설명

- `_todos`는 현재 목록이다.
- `_next_id`는 새 Todo의 고유 ID를 만들기 위한 값이다.
- 제목이 같아도 ID가 다르면 다른 항목으로 구분할 수 있다.

#### B-3. 트릭

수업에서는 DB 없이 먼저 메모리 리스트로 CRUD 개념을 익힌다.
그다음 SQLite 수업으로 자연스럽게 이어간다.

---

### 단계 C. Read 구현

#### C-1. 구현

```python
def list_todos(self) -> list[dict[str, object]]:
    return self._todos
```

#### C-2. 문제점

실무에서는 내부 리스트를 그대로 반환하면 외부 변경 위험이 있다.
하지만 이 수업에서는 구조 이해가 우선이므로 단순하게 둔다.

#### C-3. 개선 아이디어

나중에는 `return [todo.copy() for todo in self._todos]`처럼 복사본을 반환할 수 있다.

---

### 단계 D. Create 구현

#### D-1. 구현

```python
def create_todo(self, title: str) -> list[dict[str, object]]:
    clean_title = title.strip()
    if clean_title:
        self._todos.append({"id": self._next_id, "title": clean_title, "done": False})
        self._next_id += 1
    return self._todos
```

#### D-2. 설명

- `strip()`으로 앞뒤 공백을 제거한다.
- 빈 문자열은 추가하지 않는다.
- 추가 후 전체 목록을 반환한다.

강의 포인트:
- 입력 정리는 JS보다 Python에서 하는 것이 안전하다.

---

### 단계 E. Update 구현

#### E-1. 구현

```python
def update_todo(self, todo_id: int, title: str, done: bool) -> list[dict[str, object]]:
    for todo in self._todos:
        if todo["id"] == todo_id:
            todo["title"] = title.strip()
            todo["done"] = done
            break
    return self._todos
```

#### E-2. 문제 해결 개념

수정할 항목을 제목으로 찾지 않고 ID로 찾는다.
제목은 사용자가 바꿀 수 있지만 ID는 시스템이 관리한다.

---

### 단계 F. Delete 구현

#### F-1. 구현

```python
def delete_todo(self, todo_id: int) -> list[dict[str, object]]:
    self._todos = [todo for todo in self._todos if todo["id"] != todo_id]
    return self._todos
```

#### F-2. 설명

리스트 컴프리헨션으로 삭제할 ID가 아닌 항목만 남긴다.

#### F-3. 트릭

초급자는 `remove()`를 먼저 떠올리지만, 조건으로 새 리스트를 만드는 방식이 더 읽기 쉽다.

---

## 4. 체크리스트

- [ ] Todo 목록이 Python에서 시작된다.
- [ ] 추가 후 새 ID가 부여된다.
- [ ] 수정은 ID 기준으로 동작한다.
- [ ] 삭제 후 전체 목록이 다시 렌더링된다.
- [ ] JS에는 CRUD 규칙이 없다.

## 5. 확장 과제

- 빈 제목일 때 오류 메시지 반환
- 완료 항목 숨기기
- Todo 목록을 파일로 저장
