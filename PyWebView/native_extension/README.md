# Python Native/Binary Binding Examples

Python에서 다른 언어로 만든 바이너리를 가져오는 방식을 비교하는 교육 예제 모음입니다.

## 폴더 구조

- `C_binding/`: CPython C API, C extension, Python wrapper, 동적 로딩/임베딩 예제
- `Rust_binding/`: Rust로 Python extension module을 만드는 PyO3 예제
- `Cpp_binding/`: C++ 코드를 Python module로 노출하는 pybind11 예제
- `Java_binding/`: Java `.jar`를 Python wrapper에서 사용하는 JPype 예제
- `DotNet_binding/`: .NET assembly를 Python wrapper에서 사용하는 pythonnet 예제

## 수업 순서 추천

1. `C_binding/simple_wrapper`: C 함수는 작게 두고 Python class와 `.pyi`로 감싸는 구조
2. `Rust_binding/pyo3_hello`: Rust가 Python module이 되는 구조
3. `Cpp_binding/pybind11_hello`: C++ class/function이 Python module이 되는 구조
4. `Java_binding/jpype_jar`: JVM을 시작하고 Java class를 Python wrapper로 감싸는 구조
5. `DotNet_binding/pythonnet_classlib`: CLR assembly를 Python wrapper로 감싸는 구조
6. `C_binding/cpython_type_extension`: C에서 Python object/type 자체를 직접 구현하는 고급 구조

## 핵심 비교

| 방식 | Python에서 보이는 것 | 바이너리 | 타입 정보 |
| --- | --- | --- | --- |
| CPython C API | `.pyd/.so` module | C extension | `.pyi`, `py.typed` |
| PyO3 | `.pyd/.so` module | Rust extension | `.pyi`, `py.typed` |
| pybind11 | `.pyd/.so` module | C++ extension | `.pyi`, `py.typed` |
| JPype | Python wrapper package | `.jar` | wrapper의 `.pyi` |
| pythonnet | Python wrapper package | `.dll` | wrapper의 `.pyi` |

초보자에게는 “바이너리 구현”과 “Python 사용 API”를 분리해서 보여주는 wrapper 방식이 가장 이해하기 쉽습니다.
