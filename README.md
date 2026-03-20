# kuBig2026

---

고려대 개발자 양성과정에서 쓰이는 저장소이다.

[교육생 슬라이드](https://docs.google.com/presentation/d/1igQGshYUiAKx2f91brdvskaBBEhlvog_YM9Dt9nse1I/edit?usp=sharing)

```text
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

wsl --install -d Ubuntu-22.04
wsl --set-default-version 2
wsl --set-version Ubuntu-22.04 2
wsl -l -v

- 터미널에서 유저 정보 입력
git config --global user.email freshmea@gmail.com
git config --global user.name freshmea
```

---

## 2026-03-09

---

- 구글 슬라이드 자기소개
- wsl 설치
- vscode, git 설치
- OS 설명 ( 리눅스, wsl2 사용하기로 함)
- vscode remote wsl2 연결하고 git clone 하기
- hello world c 프로그램 작성하기
- literal 프로그램 작성 - int d, char c, char* s, octal o, hex h, float f, double lf, long double ldf, long long ll, unsigned int u, unsigned long long llu, pointer p, string s
- limit 프로그램 작성 - int, char, float, double, long double, long long, unsigned int, unsigned long long
- 과제 : [마크다운 정리UTUBE](https://www.youtube.com/watch?v=kMEb_BzyUqk) [마크다운 블로그](https://www.heropy.dev/p/B74sNE)
- 과제 : mermaid 로 그래프 그리기 해보기

---

## 2026-3-10

---

- 1교시: 복습
- 2교시: make 사용법, stringCopy,
- 3교시: 산술 연산자, 관계 연산자, 논리연산자, C 언어에서의 true 와 false, stdbool 사용법
- 4교시: oddEven triangle triangle2 compare compare2 작성
- 5교시: 타입 캐스팅 fahr2Celcius, sizeof 연산자
- 6교시: 증감연산자 increment, 음수의 표현, 폰 노이만의 바이트머신
- 7교시: 비트연산, fourbit, fourbit2, genderRatio
- 8교시: 대소문자 구분, 알파벳 구분
- 과제 : [make 문법](https://code-lab1.tistory.com/370), [vscode 단축키](https://inpa.tistory.com/entry/VS-Code-%E2%8F%B1%EF%B8%8F-%EC%9C%A0%EC%9A%A9%ED%95%9C-%EB%8B%A8%EC%B6%95%ED%82%A4-%EC%A0%95%EB%A6%AC)

---

## 2026-3-11

---

- 1교시: 흐름제어 - 조건문
- 2교시: if ~ else 문, switch 문(passFail, passFail2, posZeroNeg, scoreGrade, scoreGradeSwitch), random(dice)
- 3교시: for 문(one2Ten, one2TenSum, a2bSum)
- 4교시: while 문 do~ while 문
- 5교시: 구구단, star 예제
- 6교시: 배열 - 배열의 선언과 초기화, 배열의 인덱스, 배열과 포인터, 2차원 배열
- 7교시: 배열 연습 , lotto, dice2
- 8교시: 배열 연습 , sumArray, findmax, sumMatrix
- 과제 : 없음

---

## 2026-3-12

---

- 1교시: swap, 함수 설명, add 함수 작성
- 2교시: swap 을 함수로 작성, 정렬 - 선택정렬
- 3교시: 정렬 - 버블 정렬, qsort
- 4교시: 이중 포인터, 포인터 연산
- 5교시: 리틀 엔디안 빅 엔디안
- 6교시: 함수 포인터
- 7교시: void 포인터
- 8교시: 포인터와 배열, 함수로 배열 넘기기 arraycompare
- 과제 : 없음

---

## 2026-3-13

---

- 1교시: cmake 설명, cmake 로 빌드 하는 방법
- 2교시: carSerial 예제, 분할 컴파일 연습
- 3교시: cmake VsCode 설정, 디버깅 설정(gdb)
- 4교시: cc -c , cc -o 활용해서 링킹 빌드, makefile 작성
- 5교시: myRandom 예제 - static 변수, extern 키워드 사용법
- 6교시: baseball 게임 만들기 - 게임 설명, main 함수 작성
- 7교시: baseball 게임 만들기 - 실습
- 8교시: baseball 게임 만들기 - 실습
- 과제 : [cmake 사용법](https://nx006.tistory.com/36), [cmake 할때 쪼오오금 도움이 되는 문서](https://gist.github.com/luncliff/6e2d4eb7ca29a0afd5b592f72b80cb5c?permalink_comment_id=3300758)

---

## 2026-3-16

---

- 1교시: 복습, 구조체
- 2교시: 구조체 선언, 초기화, typedef
- 3교시: date 구조체 예제
- 4교시: twoDouble 구조체 예제
- 5교시: 구조체 배열 예제 structArray, selfReference(linked List)
- 6교시: union 설명, union 예제, enum 설명, enum 예제
- 7교시: string.h 라이브러리 함수 설명(strlen, strcpy, strncpy, strcat, strcmp)
- 8교시: 표준입출력함수(getchar, putchar, gets, puts, scanf, printf)과 파일 입출력 함수(getc, putc, fgets, fputs, fscanf, fprintf) 정리
- 과제 : 없음

---

## 2026-3-17

---

- 1교시: 복습, 구조체
- 2교시: 표준입출력함수(getchar, putchar, gets, puts, scanf, printf)과 파일 입출력 함수(getc, putc, fgets, fputs, fscanf, fprintf) 정리
- 3교시: 표준 입출력 함수 정리
- 4교시: 파일 입출력, file descriptor, file pointer 예제
- 5교시: 동적할당 malloc, free 예제
- 6교시: 기타 동적할당 함수 - calloc, realloc
- 7교시: scoreProcess 예제 설명
- 8교시: scoreProcess 예제 실습
- 과제 : scoreProcess 의 데이터 수를 파일 읽을 때 얻어와서 자동으로 실행하게 만들기

---

## 2026-3-18

---

- 1교시: 복습, 과제 풀이
- 2교시: 데이터구조 DataStructure 설명
- 3교시: 스택 설명, 스택 예제mystack1 - 전역 변수 제거, 구조체 사용mystack2
- 4교시: 큐 설명, 큐 예제myqeue1 - 전역 변수 제거, 구조체 사용
- 5교시: 리스트 작성 - linked list 예제
- 6교시: list1 예제 설명, list1 예제 실습
- 7교시: 스택 - 동적할당 예제 stack3
- 8교시: 스택 - 동적할당 예제 stack3 2
- 과제 : 없음

---

## 2026-3-19

---

- 1교시: 복습, 네트워크 설명
- 2교시: MQTT 설명, MQTT 설치
- 3교시: 네트워크 테스트, wsl2 netsh 명령어로 포트포워딩 설정, 방화벽 설정
- 4교시: MQTT 예제 작성 - publisher, CMake 라이브러리 추가 설정
- 5교시: stack4 - generic stack 예제 설명
- 6교시: Queue3 - 동적 할당 및 generic queue 예제 설명
- 7교시: Queue3 실습
- 8교시: Queue3 실습
- 과제 : 없음

---

## 2026-3-20

---

- 1교시: 복습, 볼링 예제 설명
- 2교시: 볼링 실습
- 3교시: 볼링 실습
- 4교시: 볼링 문제 풀이
- 5교시: 교재 리뷰
- 6교시: 교재 리뷰
- 7교시: 시험
- 8교시: 시험 문제 풀이
- 과제 : 없음
