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
  use_rust_hello.py
```

## 빌드 준비

```powershell
pip install maturin
```

Rust toolchain은 `rustup`으로 설치되어 있어야 합니다.

## 빌드

```powershell
maturin develop -i /usr/bin/python3
```

## 실행

```powershell
python use_rust_hello.py
```

## 수업 포인트

- `#[pyfunction]`은 Rust 함수를 Python 함수로 노출합니다.
- `#[pymodule]`은 Python에서 import할 module을 만듭니다.
- `.pyi`는 Rust 바이너리 module을 Python 타입 관점에서 설명합니다.
