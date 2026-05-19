# 03 API Bridge 파일 목록 단계별 실습

## 1. 수업 목표

- `fetch + localhost 서버` 방식과 `pywebview.api` bridge 방식을 비교한다.
- JavaScript에서 Python 객체의 메서드를 직접 호출하는 흐름을 이해한다.
- 파일 시스템 접근은 Python이 담당하고, JS는 버튼 이벤트와 화면 렌더링만 담당하게 만든다.

## 2. 최종 결과물

- 데모 폴더: `bridge_file_list`
- 실행: `uv run bridge_file_list/main.py`
- 핵심 파일:
  - `bridge_file_list/main.py`
  - `bridge_file_list/frontend/index.html`
  - `bridge_file_list/frontend/app.js`

최종 동작:

1. 앱이 실행되면 Python이 `demo_files` 폴더와 예제 파일을 준비한다.
2. 사용자가 버튼을 누른다.
3. JS가 `window.pywebview.api.list_files()`를 호출한다.
4. Python이 파일 이름, 확장자, 크기를 계산해서 반환한다.
5. JS가 반환된 데이터만 화면에 출력한다.

---

## 3. 단계별 실습

### 단계 A. 먼저 JS만으로 생각해 보기

#### A-1. 질문

"버튼을 누르면 특정 폴더의 파일 목록을 보여주려면 JS만으로 가능할까?"

#### A-2. 문제점

- 일반 브라우저 JS는 로컬 폴더를 마음대로 읽을 수 없다.
- 보안상 웹 페이지가 사용자의 디스크 전체를 탐색하면 안 된다.
- PyWebView 앱에서도 파일 시스템 권한은 Python 쪽에서 다루는 편이 명확하다.

#### A-3. 결론

파일 목록 조회는 Python이 처리한다.
JS는 "목록을 요청한다"와 "받은 목록을 그린다"만 담당한다.

강의 포인트:
- 데스크톱 앱의 강점은 Python이 OS 자원에 접근할 수 있다는 점이다.

---

### 단계 B. Python API 객체 만들기

#### B-1. 구현

`main.py`에 JS에서 호출할 클래스를 만든다.

```python
class FileListApi:
    def list_files(self) -> list[dict[str, str | int]]:
        files = []
        for path in sorted(DEMO_DIR.iterdir()):
            if path.is_file():
                files.append({
                    "name": path.name,
                    "suffix": path.suffix or "(none)",
                    "size": path.stat().st_size,
                })
        return files
```

#### B-2. 설명

- `Path.iterdir()`는 폴더 안의 항목을 순회한다.
- `path.is_file()`로 파일만 골라낸다.
- `path.stat().st_size`로 파일 크기를 구한다.
- 반환값은 JSON으로 바뀔 수 있는 단순 자료형이어야 한다.

#### B-3. 자주 생기는 실수

- `Path` 객체 자체를 반환하면 JS에서 다루기 어렵다.
- 파일 크기 계산을 JS에서 하려고 하면 구조가 어색해진다.
- 파일 목록 정렬을 하지 않으면 실행마다 순서가 다르게 보일 수 있다.

강의 포인트:
- bridge로 넘기는 데이터는 `str`, `int`, `bool`, `list`, `dict`처럼 단순하게 유지한다.

---

### 단계 C. PyWebView 창에 API 연결하기

#### C-1. 구현

```python
webview.create_window(
    "03 API Bridge File List",
    url=(FRONTEND_DIR / "index.html").as_uri(),
    js_api=FileListApi(),
)
```

#### C-2. 문제 해결 개념

- `js_api=FileListApi()`가 Python 객체를 JS에 노출한다.
- JS에서는 `window.pywebview.api.list_files()`로 호출한다.
- localhost 서버를 따로 만들지 않아도 된다.

#### C-3. fetch 방식과 비교

- `fetch`: HTTP API 설계, 라우팅, 상태 코드 학습에 좋다.
- `pywebview.api`: 데스크톱 앱 내부에서 Python 기능을 직접 호출하기 좋다.

강의 포인트:
- 둘 중 하나만 정답이 아니다. 수업 목적에 따라 도구가 다르다.

---

### 단계 D. JS는 얇게 유지하기

#### D-1. 구현

```js
async function loadFiles() {
    const files = await window.pywebview.api.list_files();
    renderFiles(files);
}
```

#### D-2. JS 역할

- 버튼 클릭 이벤트 연결
- Python 함수 호출
- 반환된 데이터를 `<li>`로 표시

#### D-3. JS가 하지 않는 일

- 폴더 생성
- 파일 탐색
- 파일 크기 계산
- 경로 처리

강의 포인트:
- 이 수업은 Python 심화 수업이다. JS는 UI 연결층으로 제한한다.

---

## 4. 체크리스트

- [ ] `uv run bridge_file_list/main.py`로 실행된다.
- [ ] 앱 실행 시 예제 파일이 자동 생성된다.
- [ ] 버튼 클릭 시 파일 목록이 표시된다.
- [ ] 파일 목록 계산은 Python 코드에 있다.
- [ ] JS에는 파일 시스템 로직이 없다.

## 5. 확장 과제

- 특정 확장자만 필터링한다.
- 파일 수정 시간을 표시한다.
- 폴더 경로를 Python 상수에서 설정 파일로 분리한다.
