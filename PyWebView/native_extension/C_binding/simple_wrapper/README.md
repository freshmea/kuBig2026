# Simple Wrapper Extension

이 예제는 `.pyd/.so`로 빌드되는 C extension과 `.pyi`, `py.typed`, Python class wrapper의 관계를 초보자가 이해하기 쉽게 보여줍니다.

핵심 아이디어:

- C 코드는 Python 객체 클래스를 직접 만들지 않습니다.
- C 코드는 단순 함수만 제공합니다.
- Python 코드가 그 C 함수를 감싸서 `Hello` 클래스를 만듭니다.
- `.pyi` 파일은 사용자와 IDE/type checker에게 보이는 타입 정보를 설명합니다.
- `py.typed`는 이 패키지가 타입 정보를 제공한다는 표시입니다.

## 구조

```text
simple_wrapper/
  setup.py
  simple_hello/
    _hello_core.c      # C extension: 함수만 제공
    hello.py           # Python wrapper: Hello 클래스 제공
    hello.pyi          # hello.py 타입 정보
    __init__.py        # 공개 API re-export
    __init__.pyi       # 패키지 공개 API 타입 정보
    py.typed
```

## 빌드

Windows에서는 일반 PowerShell이 아니라 **x64 Native Tools Command Prompt for VS** 또는 Visual Studio Build Tools 환경에서 실행하세요.

```powershell
python setup.py build_ext --inplace
```

현재 PowerShell에서 `cl.exe`를 찾지 못하면 빌드가 실패합니다. 이 경우 코드를 고칠 문제가 아니라 C 컴파일러 환경을 먼저 활성화해야 합니다.

## 실행

```powershell
python -c "from simple_hello import Hello, print_hello; h = Hello('Python'); print(h.greet()); print_hello()"
```

## 수업 포인트

1. `_hello_core.c`는 compiled object가 되는 낮은 수준 구현입니다.
2. `hello.py`는 학생에게 익숙한 Python class를 제공합니다.
3. `hello.pyi`와 `__init__.pyi`는 실제 실행 코드가 아니라 타입 설명서입니다.
4. `py.typed`가 있으면 type checker가 패키지의 타입 정보를 신뢰합니다.
5. 고급 단계에서 `../cpython_type_extension/mymodule/mymodule.c`처럼 C에서 직접 Python type을 만드는 방식으로 확장할 수 있습니다.

## 기존 고급 예제와 차이

`../cpython_type_extension/mymodule/mymodule.c`는 C에서 `Hello` Python type 자체를 직접 만듭니다. 그래서 `PyObject_HEAD`, `PyTypeObject`, `tp_new`, `tp_init`, `tp_methods` 같은 내부 구조를 모두 다뤄야 합니다.

이 예제는 그 복잡도를 줄이기 위해 C에서는 다음 두 함수만 제공합니다.

- `make_greeting(name) -> str`
- `print_hello() -> None`

그리고 Python의 `hello.py`가 익숙한 방식으로 `Hello` 클래스를 만듭니다. 따라서 학생은 먼저 `.pyd/.so` 모듈, Python wrapper, `.pyi`, `py.typed`의 역할을 분리해서 이해할 수 있습니다.
