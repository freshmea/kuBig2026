from pathlib import Path

import jpype


def start_jvm() -> None:
    if jpype.isJVMStarted():
        return

    jar_path = Path(__file__).resolve().parents[1] / "build" / "hello-service.jar"
    jpype.startJVM(classpath=[str(jar_path)])


class Hello:
    def __init__(self, name: str) -> None:
        start_jvm()
        service_class = jpype.JClass("com.example.HelloService")
        self._service = service_class(name)

    def greet(self) -> str:
        return str(self._service.greet())


def add(left: int, right: int) -> int:
    start_jvm()
    service_class = jpype.JClass("com.example.HelloService")
    return int(service_class.add(left, right))
