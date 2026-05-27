import threading
import time

total = 0
lock = threading.Lock()


# GIL - gobal interpreter lock
# race condition
def task(name, duration):
    global total
    print(f"쓰레드 {name} 시작")
    for _ in range(1_000_000):
        with lock:
            total += 1
    time.sleep(duration)
    print(f"쓰레드 {name} {duration}초 후 완료")


def main():
    # task("first", 5)
    # task("second", 5)
    threads = []
    for i in range(4):
        t = threading.Thread(target=task, args=(f"T{i+1}", 5 + i))
        threads.append(t)
        t.start()  # 실제 함수가 실행 되는 라인
    for t in threads:
        t.join()  # block
    print("main 은 언제 실행될까요?")
    print(total)


if __name__ == "__main__":
    main()
