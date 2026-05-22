import datetime


def main():
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    # return 결과를 수정
    print(list_a + list_b)
    # elephant sign
    print(list_a := list_a.__add__(list_b))

    # list 자체를 수정
    list_a.extend(list_b)
    print(list_a)

    # * 연산
    print(list_a * 4)
    print(list_a.__mul__(4))

    # append
    list_b.append("추가 원소")  # type: ignore
    print(list_b)

    # insert
    list_b.insert(3, 7)
    print(list_b)

    # 삭제
    print(list_b.pop())
    print(list_b)
    print(list_b.pop(0))
    print(list_b)
    list_b.remove(6)

    print(list_b)
    print(list_b.index(7))
    list_b = ["a", "b", "c", "d", "e", "f"]
    list_e = [*str("abcdefchoi su gil")]
    print(list_b.index("e"))
    print(list_e)
    print(list_e.__len__())
    print(len(list_e))

    print("k" in list_e)
    print("g" in list_e)

    # 메모리 삭제
    # del
    del list_e[4]

    # del 사용자 정의 객체를 삭제 하는 경우
    print(list_e)
    ptime = datetime.datetime.now()
    list_e.append(ptime)  # type : ignore
    print(list_e[16])
    del list_e[16]
    del ptime
    print(list_e)
    # print(ptime)


if __name__ == "__main__":
    main()
