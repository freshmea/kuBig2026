# kuBig2026

---

고려대 개발자 양성과정에서 쓰이는 저장소이다.

[교육생 슬라이드](https://docs.google.com/presentation/d/1igQGshYUiAKx2f91brdvskaBBEhlvog_YM9Dt9nse1I/edit?usp=sharing)

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

## 2026-3-10

---

- 1교시: 복습
- 2교시: make 사용법, stringCopy,
- 3교시: 산술 연산자, 관계 연산자, 논리연산자, C 언어에서의 true 와 false, stdbool 사용법
- 4교시: oddEven triangle triangle2 compare compare2 작성
- 5교시: 증감연산자, 타입 캐스팅, sizeof 연산자, 복합 대입 연산자
- 6교시: 비트 연산자.