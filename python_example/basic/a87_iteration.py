from collections.abc import Iterable


class SimpleIter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


def main():
    print(isinstance(SimpleIter(1, 5), Iterable))

    for i in SimpleIter(1, 5):
        print(i)


if __name__ == "__main__":
    main()
