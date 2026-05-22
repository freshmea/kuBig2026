import datetime


def main():
    # list 선언
    list_a = []
    list_b = list()
    list_c = [1, 2, 3, 4, 5, 6]

    print(list_a, list_b, list_c)
    print(type(list_a), type(list_b), type(list_c))
    ptime = datetime.datetime.now()
    list_d = [1, 2, 3.141592, "choi", ptime]
    print(list_d[3])
    list_d[3] = "kim"
    print(list_d[3])

    list_e = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(list_e)
    print(list_e[1][1])


if __name__ == "__main__":
    main()
