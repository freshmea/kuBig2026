# PyWebView 수업용 데모

학생들이 WebView 앱 구조를 확장하기 쉽도록 구성한 Python 심화 수업용 데모입니다.

기준 Python 버전은 3.13입니다.
JS는 버튼 이벤트와 화면 표시 정도로 최소화하고, 파일 처리/검증/CRUD/DB/작업 상태 관리는 Python 코드에 둡니다.

## 구조

```
PyWebView/
	timer/
		backend/
			server.py        # localhost JSON API (/api/clock)
		frontend/
			index.html       # UI 마크업
			style.css        # 스타일
			app.js           # DOM 텍스트 갱신 로직
		main.py            # PyWebView + 서버 부팅
	click/
		backend/
			server.py        # 카운터 API + SSE 동기화
		frontend/
			index.html
			style.css
			app.js
		main.py
	bridge_file_list/      # pywebview.api로 Python 함수 직접 호출
	memo_file_io/          # 파일 읽기/쓰기
	settings_store/        # JSON 설정 저장
	validation_scores/     # 입력 검증
	todo_crud/             # 메모리 기반 CRUD
	todo_sqlite/           # SQLite 연동
	long_task_progress/    # thread 기반 긴 작업 진행률
	window_control_demo/   # 창 제어
	screen_router/         # 화면 전환
	packaging_demo/        # 패키징 경로 확인
	doc/
		01_수업자료_웹뷰_단계별_실습.md
		02_click_단계별_실습.md
		03_API브리지_파일목록_단계별_실습.md
		...
		12_앱패키징_단계별_실습.md
		99_배경지식_공식문서_링크.md
```

## timer 통신 흐름

1. Python 백엔드가 `127.0.0.1`의 랜덤 포트에서 API 서버를 실행합니다.
2. PyWebView는 해당 localhost URL을 로드합니다.
3. 프론트엔드 JavaScript가 `/api/clock`을 1초마다 호출합니다.
4. 받은 JSON으로 시간/날짜 텍스트만 DOM에 갱신합니다.

문서 전체를 매초 리로드하지 않아서 검은 화면 문제를 피하고, 구조도 확장하기 쉽습니다.

## click 통신 흐름

1. Python 백엔드가 고정 포트 `49321`에서 카운터 서버를 실행합니다.
2. 이미 서버가 실행 중이면 새 서버를 띄우지 않고 기존 서버를 사용합니다.
3. 버튼 클릭 시 프론트엔드가 `POST /api/counter/increase` 또는 `POST /api/counter/decrease`를 호출합니다.
4. Python 서버가 값을 계산하고, SSE(`/api/counter/events`)로 모든 창에 변경값을 전달합니다.

## 추가 데모 실행

```powershell
uv run bridge_file_list/main.py
uv run memo_file_io/main.py
uv run settings_store/main.py
uv run validation_scores/main.py
uv run todo_crud/main.py
uv run todo_sqlite/main.py
uv run long_task_progress/main.py
uv run window_control_demo/main.py
uv run screen_router/main.py
uv run packaging_demo/main.py
```

## 실행 방법

1. 가상환경 생성 (최초 1회)

```powershell
uv venv
```

2. 의존성 설치

```powershell
uv sync
```

3. 앱 실행

```powershell
uv run timer/main.py
uv run click/main.py
```
