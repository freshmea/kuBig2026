# import a35_variable_length_keyward_argument
# 유명한 라이브러리 이름을 파일로 만들면 X
# import test_package
# import test_package.module_a
# import test_package.module_b
from a35_variable_length_keyward_argument import print_n_times as pnt
from test_package.module_a import module_var_a
from test_package.module_b import module_var_b


def main():
    print("hello, world")
    print(__name__)
    # a35_variable_length_keyward_argument.print_n_times(1, 2, 3)
    # print_n_times(4, 5, 6, a="aaa")
    pnt(1, 2, 3, b="bbb")
    # print(test_package.module_a.module_var_a)
    # print(test_package.module_b.module_var_b)
    print(module_var_a)
    print(module_var_b)


# import 를 당했을 때. __main__ 이 아니게 된다.
if __name__ == "__main__":
    main()
