#include "queue2.h"

int main(void)
{
    Qu qu1, qu2;
    initQueue(&qu1);
    initQueue(&qu2);
    push(&qu1, 100);
    push(&qu1, 200);
    printf("첫번째 pop(): %d\n", pop(&qu1)); // 100

    push(&qu1, 300);
    printf("두번째 pop(): %d\n", pop(&qu1)); // 200
    printf("세번째 pop(): %d\n", pop(&qu1)); // 300

    push(&qu2, 700);
    push(&qu2, 800);
    printf("첫번째 pop(): %d\n", pop(&qu2)); // 700

    push(&qu2, 900);
    printf("두번째 pop(): %d\n", pop(&qu2)); // 800
    printf("세번째 pop(): %d\n", pop(&qu2)); // 900

    return 0;
}