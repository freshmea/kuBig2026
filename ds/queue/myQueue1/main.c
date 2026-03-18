#include "queue.h"

int main(void)
{
    push(100);
    push(200);
    printf("첫번째 pop(): %d\n", pop()); // 100

    push(300);
    printf("두번째 pop(): %d\n", pop()); // 200
    printf("세번째 pop(): %d\n", pop()); // 300
    return 0;
}