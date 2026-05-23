# C Binding Examples

C로 만든 코드를 Python에서 사용하는 예제입니다.

## 예제

- `simple_wrapper/`: C extension은 함수만 제공하고, Python class와 `.pyi`가 사용자 API를 설명합니다.
- `cpython_type_extension/`: C에서 Python class/type을 직접 구현하는 고급 예제입니다. 기존 `mymodule` 예제를 이 위치로 옮겼습니다.
- `dynamic_loading/`: C 프로그램이 shared library를 동적으로 로딩하는 예제입니다.
- `python_vm_embedding/`: Python VM/interpreter 개념 설명용 C 예제입니다.

## 수업 포인트

`simple_wrapper`와 `cpython_type_extension`은 둘 다 `.pyd/.so` 형태로 Python에서 import할 수 있습니다. 차이는 다음과 같습니다.

- `simple_wrapper`: C 함수 + Python wrapper class + `.pyi`
- `cpython_type_extension`: C에서 Python object/type을 직접 생성

초보자 실습은 `simple_wrapper`부터 시작하고, 내부 구조 설명 단계에서 `cpython_type_extension`으로 넘어가면 됩니다.
