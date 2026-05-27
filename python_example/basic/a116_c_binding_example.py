import simple_hello


def main():
    simple_hello.print_hello()
    a = simple_hello.Hello("choi")
    print(a.name)
    # a.greet()


if __name__ == "__main__":
    main()
