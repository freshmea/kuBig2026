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

cd ~
 ls
 mkdir kuBig2026
 ls
 cd kuBig2026
 ls
 nano test.c
 cat test.c
 cc -o test.out test.c
 ls
 ./test.out
 sudo apt install gcc
