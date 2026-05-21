class A:
    def __repr__(self):
        return "this is class A!!!-by CSK"


def main():
    print(12345)
    print(1_234_567)
    print("choi su gil")
    print('python "class"')
    print(3.142592)

    print("this is", "python", "class!!")
    print(10, 20, 30, "hi", "fifty\n")
    print()

    print("this is", "python", "class!!", sep="_", end="")
    print("this is", "python", "class!!", sep="-")
    print(A())
    print(type(A()))


if __name__ == "__main__":
    main()
