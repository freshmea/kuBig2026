import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    # Descriptor -> attr , getattr, setattr, delattr
    @property
    def radius(self):
        return self.__radius

    @radius.getter
    def radius(self):
        print("getter")
        return self.__radius

    @radius.setter
    def radius(self, value):
        print("setter")
        if isinstance(value, int) and value > 0:
            self.__radius = value
        else:
            print("양의 정수만 넣으시오.")

    def get_area(self):
        return math.pi * (self.__radius**2)


def main():
    circle = Circle(10)
    print(circle.radius)
    circle.radius = 20
    circle.radius = 3.14
    circle.radius = -5
    print(circle.get_area())

    # descriptor
    print(circle.__dict__)
    print(vars(circle))
    print(getattr(circle, "get_area"))
    print(getattr(circle, "get_area")())
    print(getattr(circle, "get_area2", None))

    # _ 의 쓰임
    for _ in range(100):
        print("loop", end="")
    a_tu = 1, 2, 3, "valuable text"
    _, _, _, text = a_tu
    print(text)


if __name__ == "__main__":
    main()
