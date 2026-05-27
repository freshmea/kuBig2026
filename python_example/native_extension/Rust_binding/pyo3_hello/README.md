# Rust Binding: PyO3 Hello

Rust로 Python extension module을 만드는 예제입니다. 빌드 결과는 Python에서 `import rust_hello`로 가져올 수 있는 `.pyd/.so` 바이너리입니다.

## 구조

```text
pyo3_hello/
  Cargo.toml
  pyproject.toml
  src/lib.rs
  rust_hello.pyi
  py.typed
```

## 빌드 준비

```bash
python3 -m pip install maturin
```

Rust toolchain은 `rustup`으로 설치되어 있어야 합니다.

## 설치 방법 1: 현재 가상환경에 설치

`maturin develop`은 현재 활성화된 virtual environment에만 설치합니다.

```bash
source /home/aa/.venv/bin/activate
maturin develop
```

이 방식은 VS Code 인터프리터도 같은 가상환경으로 맞춰야 `import rust_hello`가 정상 동작합니다.

## 설치 방법 2: 특정 Python에 설치

현재 사용 중인 `maturin 1.13.3`에서는 `maturin develop -i ...` 옵션을 지원하지 않습니다.
특정 인터프리터를 지정하려면 wheel을 만든 뒤 그 Python으로 설치해야 합니다.

```bash
maturin build -i /usr/bin/python3
/usr/bin/python3 -m pip install target/wheels/rust_hello-0.1.0-cp310-cp310-manylinux_2_34_x86_64.whl --force-reinstall
```

wheel 파일명은 Python 버전과 플랫폼에 따라 달라질 수 있습니다.

## 실행

```bash
/usr/bin/python3 /home/aa/kuBig2026/python_example/basic/a118_rust_binding.py
```

## 수업 포인트

- `#[pyfunction]`은 Rust 함수를 Python 함수로 노출합니다.
- `#[pymodule]`은 Python에서 import할 module을 만듭니다.
- `.pyi`는 Rust 바이너리 module을 Python 타입 관점에서 설명합니다.
