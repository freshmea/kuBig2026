def main():
    # 선언 할 필요 없음
    # int_a = int()
    int_a = 10
    print(int_a)
    print(type(int_a))
    int_a = "ten"
    print(int_a)
    print(type(int_a))

    # 변수명, 함수명 a_b_c ... thePythonClass -> 식별자
    # convention
    # 변수명 함수명 -> 소문자 시작
    # 클래스 명 -> 대문자 시작, built-in 은 소문자 시작


# import 를 당했을 때. __main__ 이 아니게 된다.
if __name__ == "__main__":
    main()
