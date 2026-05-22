class A:
    pass


def main():
    dict_a = {}
    dict_b = dict()
    print(type(dict_a))
    print(type(dict_b))

    # set 이랑 해깔리수 있음.
    set_a = {1, 2}
    print(type(set_a))
    a = A()
    dict_c = {"a": 1234, "b": 897, "c": 876, 1234: 5678, 3.14: 1.111, a: 4.444, "1234": 5679}
    print(type(dict_c))
    print(dict_c)
    print(dict_c[a])
    print(dict_c[3.14])
    print(dict_c["c"])
    print(dict_c["1234"])


if __name__ == "__main__":
    main()
