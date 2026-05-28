# webview_example

Linux에서 pywebview를 GTK 백엔드로 실행하는 예제다.

## 시스템 패키지 설치

Ubuntu 22.04 기준으로 아래 패키지가 필요하다.

```bash
sudo apt-get update
sudo apt-get install -y \
  gobject-introspection \
  libgirepository1.0-dev \
  gir1.2-gtk-3.0 \
  gir1.2-webkit2-4.1 \
  libcairo2-dev
```

필수 이유는 다음과 같다.

- `PyGObject`가 GTK Python 바인딩을 제공한다.
- `gir1.2-webkit2-4.1`가 pywebview의 GTK WebView 백엔드에 필요하다.
- `libgirepository1.0-dev`, `gobject-introspection`, `libcairo2-dev`는 `PyGObject`, `pycairo` 빌드에 필요하다.

## Python 의존성 설치

이 프로젝트는 `uv`를 사용한다.

가상환경과 잠금 파일 기준으로 의존성을 맞출 때:

```bash
cd /home/aa/kuBig2026/python_example/webview_example
uv sync
```

현재 프로젝트에 들어 있는 핵심 Python 패키지는 다음과 같다.

- `pywebview>=6.2.1`
- `pygobject==3.50.0`

참고로 Ubuntu 22.04 + Python 3.13 환경에서는 최신 `PyGObject`가 바로 빌드되지 않아 `3.50.0`으로 고정했다.

## 새 패키지 추가

새 Python 패키지를 프로젝트 의존성에 추가할 때:

```bash
cd /home/aa/kuBig2026/python_example/webview_example
uv add 패키지명
```

예시:

```bash
uv add requests
```

이 명령은 다음을 자동으로 처리한다.

- `pyproject.toml`에 의존성 추가
- `uv.lock` 갱신
- `.venv`에 즉시 설치

GTK 관련 패키지를 다시 추가해야 한다면 다음처럼 실행하면 된다.

```bash
uv add "PyGObject==3.50.0"
uv add pywebview
```

이미 `pyproject.toml`이 수정된 상태에서 잠금 파일과 가상환경만 다시 맞추고 싶다면:

```bash
uv sync
```

## 실행

```bash
cd /home/aa/kuBig2026/python_example/webview_example
uv run python main.py
```

GTK 백엔드 import만 빠르게 확인하려면:

```bash
uv run python -c "import gi; gi.require_version('Gtk', '3.0'); import webview.platforms.gtk"
```
