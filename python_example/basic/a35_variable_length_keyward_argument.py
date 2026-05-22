def print_n_times(*args, **kargs):
    # args -> tuple
    # kargs -> dict {key:value , ...}
    for value in args:
        # print("args")
        print(value)
    # for value in kargs:
    #     print("keyward_argument")
    #     print(value, kargs[value])

    for key, value in kargs.items():
        print(key, value)


def main():
    print_n_times(1, 2, 3, 4, 5, 6, a=1, b=2, c=3)


if __name__ == "__main__":
    main()
