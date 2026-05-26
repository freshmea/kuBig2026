from pathlib import Path


def main():
    path = Path(r"D:\repository\kuBig2026\python_example\data")
    # f = open(path + "\\text.txt", "w")
    # f.write("Hello Python Programming...!")
    # f.close()
    with open(path / "text.txt", "a", encoding="utf-8") as f:
        f.write("hello!!!")


if __name__ == "__main__":
    main()
