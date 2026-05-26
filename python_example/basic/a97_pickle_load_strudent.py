import pickle
from pathlib import Path

from student_model import Student


def main():
    students = []
    path = Path(r"D:\repository\kuBig2026\python_example\data\test.pickle")
    with path.open("rb") as f:
        try:
            while data := pickle.load(f):
                students.append(data)
        except EOFError:
            pass

    print("이름\t 국어\t 수학\t 영어\t 과학\t 총점\t 평균")
    for student in students[0]:
        print(student)


if __name__ == "__main__":
    main()
