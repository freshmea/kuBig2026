#include "stack3.h"

int main(void)
{
    Stack s1, s2;

    initStack(&s1, 10);
    initStack(&s2, 100);

    push(&s1, 100);
    push(&s1, 200);
    push(&s1, 300);

    printf("s1 첫 pop() 리턴 값: %d\n", pop(&s1));     // 300
    printf("s1 두번째 pop() 리턴 값: %d\n", pop(&s1)); // 200
    printf("s1 세번째 pop() 리턴 값: %d\n", pop(&s1)); // 100

    push(&s2, 700);
    push(&s2, 800);
    push(&s2, 900);

    printf("s2 첫 pop() 리턴 값: %d\n", pop(&s2));     // 900
    printf("s2 두번째 pop() 리턴 값: %d\n", pop(&s2)); // 800
    printf("s2 세번째 pop() 리턴 값: %d\n", pop(&s2)); // 700

    printf("s1 스택 메모리 사이즈는 : %d\n", s1.size);
    printf("s2 스택 메모리 사이즈는 : %d\n", s2.size);


    // size 를 넘겼을 때 assert작동 확인
    // max index 를 넘어 갔을 때 100 개채울 때 에러
    for (int i = 0; i < 101; ++i)
    {
        push(&s2, i);
        printf("%d , \n", i);
    }
    // 데이터가 없을 때 assert작동 확인
    // 데이터가 부족할때
    for (int i = 0; i < 102; ++i)
    {
        printf("%d번째 pop(): %d\n", i, pop(&s2));
    }

    cleanupStack(&s1);
    cleanupStack(&s2);
    return 0;
}