# kuBig2026

---

고려대 개발자 양성과정에서 쓰이는 저장소 입니다.

[교육생 슬라이드](https://docs.google.com/presentation/d/1igQGshYUiAKx2f91brdvskaBBEhlvog_YM9Dt9nse1I/edit?usp=sharing)

---

## 빠른 시작

---

- 저장소 clone 후 `git submodule update --init --recursive` 를 먼저 실행한다.
- 호스트 예제 빌드에는 `cmake`, `gcc` 가 필요하다.
- Pico 실습에는 `gcc-arm-none-eabi`, `libnewlib-arm-none-eabi`, `libstdc++-arm-none-eabi-newlib` 가 추가로 필요하다.
- 호스트 예제만 확인할 때는 `cmake -S . -B build -DKUBIG_BUILD_ATMEGA128=OFF -DKUBIG_BUILD_PICO=OFF` 로 임베디드 외부 프로젝트를 제외할 수 있다.
- [온보딩 체크리스트](doc/온보딩_체크리스트.md)
- [1주차 수업 운영안](doc/1주차_수업운영안.md)
- [2주차 수업 운영안](doc/2주차_수업운영안.md)
- [C 실습 맵](doc/C_실습_맵.md)
- [문제 해결 가이드](doc/문제해결_가이드.md)
- [프로젝트 평가 루브릭](doc/프로젝트_평가_루브릭.md)
- [실습지 모음](doc/실습지_모음.md)
- [강사용 수업 준비 체크리스트](doc/강사용_수업준비_체크리스트.md)

## C 언어

---

- 수업 목표
  - C언어를 배워 프로그래밍 능력을 향상 시킨다.
  - 기본적인 프로젝트 관리와 CMake를 이용한 빌드 방법을 익힌다.
  - VsCode 를 활용하는 기술을 익히고 디버깅 방법을 익힌다.
  - 최종 프로젝트 - 볼링 게임
- 추천 학습 순서
  - [온보딩 체크리스트](doc/온보딩_체크리스트.md)
  - [1주차 수업 운영안](doc/1주차_수업운영안.md)
  - [2주차 수업 운영안](doc/2주차_수업운영안.md)
  - [C 실습 맵](doc/C_실습_맵.md)
  - [C 예제 인덱스](c_example/README.md)
  - [표준 입출력 함수 정리](doc/표준 입출력 함수 정리.md)
- [과정 진행 사항](doc/c_programming.md)
- [C 언어 시험 링크](https://forms.gle/fgCp9ZdNhPGGpKwJ6)

---

## Atmega128 - embedded programming

---

- 수업 목표
  - Atmega128을 이용한 임베디드 프로그래밍을 통해 하드웨어와 소프트웨어를 연결하는 방법을 익힌다.
  - Atmega128의 기본적인 사용법을 익히고 이를 이용한 프로젝트를 수행한다.
  - Atmega128의 입출력을 이용한 프로젝트를 수행한다.
- 추천 학습 순서
  - [문제 해결 가이드](doc/문제해결_가이드.md)
  - [과정 진행 사항](doc/atmega128.md)
  - [Atmega128 예제 인덱스](atmega128/README.md)
- [Atmega128 시험 링크](https://forms.gle/oJrCYyPsPQ7hWCce6)

---

## Project 1 - C Programming, Atmega128

---

- 프로젝트 목표
  - C언어를 이용한 프로그램을 작성하고 MQTT를 이용하여 데이터를 송수신하는 방법을 익힌다.
  - Atmega128을 이용한 프로젝트를 수행하거나 raspberry pico2w를 이용한 프로젝트를 수행한다.
  - [키트 링크](https://icfactory.co.kr/product/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4-%ED%94%BC%EC%BD%942w-%EC%96%BC%ED%8B%B0%EB%B0%8B-%EC%8A%A4%ED%83%80%ED%84%B0-%ED%82%A4%ED%8A%B8/1629/)
  - [샘플 코드](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/index.html)
- 프로젝트 준비 문서
  - [첫 프로젝트 제한 사항](doc/첫 프로젝트.md)
  - [프로젝트 제안서 템플릿](doc/프로젝트_제안서_템플릿.md)
  - [프로젝트 마일스톤 체크리스트](doc/프로젝트_마일스톤_체크리스트.md)
  - [실습 제출 템플릿](doc/실습_제출_템플릿.md)
  - [프로젝트 평가 루브릭](doc/프로젝트_평가_루브릭.md)
  - [MQTT 예제 안내](network/README.md)
- 프로젝트 깃링크
  - [1조](https://github.com/tkdtn412/fitness-pico)
  - [2조](https://github.com/Gwiin/hrd_first_project)
  - [3조](https://github.com/Segangs/PicoTeam2)
