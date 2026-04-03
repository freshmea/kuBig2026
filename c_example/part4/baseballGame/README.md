# baseballGame

조건문, 반복문, 배열, 함수 분리, 난수 생성, 게임 루프를 함께 연습하기 위한 미니 프로젝트 예제다.

## 게임 규칙

- 1부터 9 사이의 서로 다른 숫자 3개를 맞힌다.
- 자리와 숫자가 모두 맞으면 `Strike`
- 숫자만 맞고 자리가 다르면 `Ball`
- 3 `Strike`가 되면 게임 종료

## 실행 방법

프로젝트 루트에서 CMake로 빌드한 뒤 실행한다.

```bash
cmake -S . -B build
cmake --build build --target baseballGame
./build/c_example/part4/baseballGame/baseballGame
```

## 학습 포인트

- 난수 생성과 중복 없는 숫자 만들기
- 사용자 입력 반복 처리
- 함수로 게임 로직 분리하기
- `strike`, `ball` 판정 알고리즘 이해

## 실습지

- [숫자 야구 실습지](실습지.md)
