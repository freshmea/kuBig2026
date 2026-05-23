from .module_a import Module_a, module_a_func, module_var_a
from .module_b import Module_b, module_b_func, module_var_b

__all__ = ["module_var_a", "module_var_b", "module_a_func"]


def package_func():
    print("이것은 패키지 함수입니다.")


# 패키지 테스트코드
def main():
    print(" test_package 패키지에서 실행되는 프린트다.")
    print(Module_a())
    print(Module_b())
    print(module_b_func())


if __name__ == "__main__":
    main()
