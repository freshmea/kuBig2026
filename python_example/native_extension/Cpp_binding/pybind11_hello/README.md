# C++ Binding: pybind11 Hello

C++ 함수와 클래스를 Python module로 노출하는 예제입니다.

## 빌드 준비

```powershell
pip install pybind11 setuptools
```

## 빌드

```powershell
python setup.py build_ext --inplace
```

Windows에서는 Visual Studio Build Tools의 `cl.exe`가 활성화되어 있어야 합니다.

## 실행

```powershell
python use_cpp_hello.py
```

## 수업 포인트

- C++ `class Hello`가 Python의 `Hello` class처럼 보입니다.
- `.pyd/.so` 바이너리 module을 import합니다.
- `.pyi` 파일로 Python에서 보이는 API를 설명합니다.
