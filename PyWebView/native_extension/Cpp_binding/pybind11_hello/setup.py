from setuptools import Extension, setup
import pybind11


setup(
    name="cpp_hello",
    version="0.1.0",
    ext_modules=[
        Extension(
            "cpp_hello",
            ["src/cpp_hello.cpp"],
            include_dirs=[pybind11.get_include()],
            language="c++",
        )
    ],
    py_modules=["cpp_hello"],
)
