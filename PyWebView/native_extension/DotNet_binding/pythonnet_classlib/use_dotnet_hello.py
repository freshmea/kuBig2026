from dotnet_hello import Hello, add


def main() -> None:
    hello = Hello("Python")
    print(hello.greet())
    print(add(8, 9))


if __name__ == "__main__":
    main()
