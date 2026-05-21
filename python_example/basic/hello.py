def main():
    print("hello, world")
    print(__name__)


# import 를 당했을 때. __main__ 이 아니게 된다.
if __name__ == "__main__":
    main()
