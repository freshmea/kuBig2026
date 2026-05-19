# PyWebView 탁상 시계 (Frontend/Backend 분리)

학생들이 WebView 앱 구조를 확장하기 쉽도록 프론트엔드와 백엔드를 분리한 데모입니다.

## 구조

```
PyWebView/
	app/
		backend/
			server.py        # localhost JSON API (/api/clock)
		frontend/
			index.html       # UI 마크업
			style.css        # 스타일
			app.js           # DOM 텍스트 갱신 로직
		main.py            # PyWebView + 서버 부팅
	hello.py             # 실행 진입점
```

## 통신 흐름

1. Python 백엔드가 `127.0.0.1`의 랜덤 포트에서 API 서버를 실행합니다.
2. PyWebView는 해당 localhost URL을 로드합니다.
3. 프론트엔드 JavaScript가 `/api/clock`을 1초마다 호출합니다.
4. 받은 JSON으로 시간/날짜 텍스트만 DOM에 갱신합니다.

문서 전체를 매초 리로드하지 않아서 검은 화면 문제를 피하고, 구조도 확장하기 쉽습니다.

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
uv run hello.py
```
