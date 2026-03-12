#include <stdio.h>

int main(void)
{
    // p가 주소를 가리켜야 된다.
    //  int *p;
    //  *p = 200;

    // 주소를 가리키면 오류가 나지 않음.
    int a;
    int *p;
    p = &a;

    return 0;
}