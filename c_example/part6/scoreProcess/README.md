# scoreProcess

파일 입력, 구조체 배열, 총점 계산, 등수 계산, 포인터 정렬을 함께 연습하기 위한 예제다.

## 입력 형식

`score.dat`는 다음 형식을 사용한다.

```text
이름 국어 영어 수학
```

예시:

```text
ParkJungSeok 100 100 100
LeeYoungHo 99 85 91
```

## 실행 방법

프로젝트 루트에서 CMake로 빌드한 뒤 실행하면 입력과 출력 파일은 이 폴더(`c_example/part6/scoreProcess`) 기준으로 처리된다. 따라서 VS Code에서 `build/.../scoreProcess`를 직접 실행해도 같은 데이터를 사용한다.

```bash
cmake -S . -B build
cmake --build build --target scoreProcess
./build/c_example/part6/scoreProcess/scoreProcess
cat c_example/part6/scoreProcess/score.out
```

## 학습 포인트

- 파일에서 학생 수 자동 계산
- 구조체 배열에 성적 데이터 저장
- 총점과 평균 계산
- 등수 계산 로직 이해
- 포인터 배열로 정렬 결과 출력

## 실습지

- [성적 처리 실습지](실습지.md)
