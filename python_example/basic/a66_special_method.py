class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        self.__aa = "secret key"

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}"

    def __repr__(self):
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\
            {self.get_sum()}\t {self.get_average()}"

    def __str__(self) -> str:
        return f"{self.name}\t {self.korean}\t {self.math}\t {self.english}\t {self.science}\
            {self.get_sum()}\t {self.get_average()} str"

    # 사칙연산 + - * /
    def __add__(self, other):
        return self.get_sum() + other.get_sum()

    def __sub__(self, other):
        return self.get_sum() - other.get_sum()

    def __mul__(self, other):
        return self.get_sum() * other.get_sum()

    def __truediv__(self, other):
        return self.get_sum() / other.get_sum()

    # 관계 연산자 greater than -> gt , less than -> lt, equal -> eq, nagative ->ne
    # grather than equal -> ge, less than equal ->le
    def __gt__(self, value):
        if isinstance(value, Student):
            return self.get_sum() > value.get_sum()
        else:
            # raise
            return "error"


def main():
    students = [
        Student("abc", 34, 65, 35, 94),
        Student("gdf", 34, 45, 45, 50),
        Student("wtr", 36, 75, 63, 94),
        Student("nbd", 47, 65, 85, 70),
        Student("ujd", 88, 95, 75, 33),
        Student("efg", 64, 65, 55, 40),
        Student("dgd", 33, 25, 75, 93),
    ]
    print("student[0] > student[1]", students[0] > students[1])
    print("student[0] > student[1]", students[0] > 90)
    print("student[0] + student[1]", students[0] + students[1])
    print("student[0] - student[1]", students[0] - students[1])
    print("student[0] * student[1]", students[0] * students[1])
    print("student[0] / student[1]", students[0] / students[1])


if __name__ == "__main__":
    main()
