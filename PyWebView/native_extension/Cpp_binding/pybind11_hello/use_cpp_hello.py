import cpp_hello


def main() -> None:
    hello = cpp_hello.Hello("Python")
    print(hello.greet())
    print(cpp_hello.add(3, 4))


if __name__ == "__main__":
    main()
