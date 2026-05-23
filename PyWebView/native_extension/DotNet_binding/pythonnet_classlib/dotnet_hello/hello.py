from pathlib import Path

import clr


_loaded = False


def load_assembly() -> None:
    global _loaded
    if _loaded:
        return

    dll_path = (
        Path(__file__).resolve().parents[1]
        / "HelloLibrary"
        / "bin"
        / "Release"
        / "net8.0"
        / "HelloLibrary.dll"
    )
    clr.AddReference(str(dll_path))
    _loaded = True


class Hello:
    def __init__(self, name: str) -> None:
        load_assembly()
        from HelloLibrary import HelloService

        self._service = HelloService(name)

    def greet(self) -> str:
        return str(self._service.Greet())


def add(left: int, right: int) -> int:
    load_assembly()
    from HelloLibrary import HelloService

    return int(HelloService.Add(left, right))
