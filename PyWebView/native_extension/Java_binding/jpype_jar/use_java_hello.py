from java_hello import Hello, add


def main() -> None:
    hello = Hello("Python")
    print(hello.greet())
    print(add(5, 7))


if __name__ == "__main__":
    main()
