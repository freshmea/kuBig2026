// 입력받은 char 가 알파벳인지 아닌지 출력하세요!
#include <stdbool.h>
#include <stdio.h>

int main(void)
{
    char ch;
    printf("char 를 입력하세요: ");
    scanf("%c", &ch);

    bool isAlphabet;
    isAlphabet = ('A' <= ch && ch <= 'Z') || ('a' <= ch && ch <= 'z');
    printf("%c 는 %s\n", ch, isAlphabet ? "알파벳 입니다." : "알파벳이 아닙니다.");
    return 0;
}
