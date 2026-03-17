#include <stdio.h>
#include <unistd.h>

int main(void)
{
    char ch = 'a';

    printf("프로그램 시작\n");
    putchar(ch);
    fflush(stdout);
    sleep(1);
    printf("putchar 실행후\n");
    putc(ch, stdout);
    fflush(stdout);
    sleep(1);
    return 0;
}