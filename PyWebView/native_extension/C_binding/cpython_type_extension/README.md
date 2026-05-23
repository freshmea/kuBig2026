# CPython Type Extension

기존 `mymodule` C extension 예제입니다. C 코드에서 `Hello` Python type 자체를 직접 구현합니다.

## 포함 내용

- `mymodule/mymodule.c`: `PyObject_HEAD`, `PyTypeObject`, `PyModuleDef`를 사용하는 고급 C extension
- `mymodule/mymodule.pyi`: Python 사용자에게 보이는 타입 정보
- `mymodule/py.typed`: 타입 정보를 제공하는 패키지임을 표시
- `setup.py`: extension module 빌드 스크립트

## 빌드

```powershell
python setup.py build_ext --inplace
```

Windows에서는 `cl.exe`가 활성화된 Visual Studio Build Tools 환경에서 실행해야 합니다.

## 실행

```powershell
python -c "import mymodule; h = mymodule.Hello('Python'); print(h.greet()); mymodule.print_hello()"
```

## 학습 목적

이 예제는 초보자용이 아니라 `.pyd/.so` extension 내부에서 Python object가 어떻게 만들어지는지 보여주는 심화 예제입니다.
