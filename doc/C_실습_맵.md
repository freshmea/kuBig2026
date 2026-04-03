# C 실습 맵

---

이 문서는 `c_example/` 아래 예제들이 어떤 학습 목표와 연결되는지 빠르게 보여 주는 안내서다. 수업 후 복습이나 보강 과제 선정에 사용한다.

## 학습 흐름

---

| 단계 | 위치 | 핵심 주제 | 수강생이 할 수 있어야 하는 것 | 추천 산출물 |
| --- | --- | --- | --- | --- |
| 1 | `c_example/part1` | 출력, 자료형, 연산자 | 기본 입출력과 자료형 차이를 설명한다 | 값 출력 변형 문제 1개 |
| 2 | `c_example/part2` | 조건문, 반복문, 배열 | 조건 분기와 반복 구조를 직접 작성한다 | 점수 판정 또는 배열 합계 프로그램 |
| 3 | `c_example/part3` | 함수, 포인터, 정렬 | 함수 분리와 포인터 전달 방식을 구분한다 | 정렬 함수 수정 과제 |
| 4 | `c_example/part4` | CMake, 분할 컴파일, 미니 프로젝트 | 여러 파일로 구성된 프로그램을 빌드한다 | `carSerial` 또는 `baseballGame` 수정 |
| 5 | `c_example/part5` | 구조체, 문자열, 파일 입출력 기초 | 구조체로 데이터를 묶고 표준 입출력을 사용한다 | 구조체 기반 데이터 출력 과제 |
| 6 | `c_example/part6` | 동적 할당, 파일 처리, 보고서 생성 | 파일 기반 데이터를 읽고 동적으로 처리한다 | `scoreProcess`, `iotLogReport` 확장 |

## 수업 연결 예시

---

### part1

- 추천 예제: `hello.c`, `literal.c`, `limit.c`
- 수업 포인트: C 프로그램의 기본 구조, 출력 형식, 자료형 크기

### part2

- 추천 예제: `passFail.c`, `scoreGrade.c`, `sumArray.c`, `findMax.c`
- 수업 포인트: 조건문, 반복문, 배열, 누적 계산

### part3

- 추천 예제: `swap.c`, `selectionSorting.c`, `qsort.c`, `arraycompare.c`
- 수업 포인트: 함수 설계, 포인터, 배열 전달, 정렬 비교

### part4

- 추천 예제: `carSerial`, `myRandom`, `baseballGame`
- 수업 포인트: 분할 컴파일, 헤더 파일, CMake, 미니 프로젝트 구조

### part5

- 추천 예제: `struct.c`, `structArray.c`, `stringExample.c`, `charGetPut4.c`
- 수업 포인트: 구조체, 문자열 함수, 표준 입출력, 파일 입출력

### part6

- 추천 예제: `dynamicAllocation.c`, `scoreProcess`, `iotLogReport`
- 수업 포인트: 동적 메모리 할당, 파일 데이터 처리, 중간 규모 과제

## 복습 우선순위

---

1. 시험 또는 미니 프로젝트 전에는 `part2`와 `part3`를 먼저 복습한다.
2. 파일 처리 과제를 하기 전에는 `part5`와 `part6`를 같이 본다.
3. 팀 프로젝트 준비 전에는 `part4/baseballGame`, `part6/iotLogReport`를 우선 확인한다.

## 다음 문서

---

- [C 예제 인덱스](../c_example/README.md)
- [실습 제출 템플릿](실습_제출_템플릿.md)
