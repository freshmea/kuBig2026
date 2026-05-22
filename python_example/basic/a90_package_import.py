import test_package
from test_package import *
from test_package import package_func


def main():
    print(module_var_a)
    print(module_var_b)
    module_a_func()
    print(test_package.module_var_a)
    test_package.module_b_func()
    print(test_package.Module_a())

    package_func()


if __name__ == "__main__":
    main()
