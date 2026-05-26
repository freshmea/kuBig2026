class Person:
    def __init__(self, b):
        self.b = b

    def greeting(self):
        print("안녕하세요!")


class University:
    def __init__(self, a):
        self.a = a

    def massage_credit(self):
        print("학점관리")


class Undergraduate(Person, University):
    def __init__(self):
        Person.__init__(self, 1)
        University.__init__(self, 2)

    def study(self):
        print("공부하기")


def main():
    james = Undergraduate()
    james.greeting()
    james.massage_credit()
    james.study()
    print(james.a, james.b)
    print(Undergraduate.__mro__)


if __name__ == "__main__":
    main()
