#include <stdio.h>

void push(int data);
int pop(void);
int stack[50];
int tos = 0; // top of stack

int main(void)
{
    push(100);
    push(200);
    push(300);

    printf("첫 pop() 리턴 값: %d\n", pop());    // 300
    printf("두번째 pop() 리턴 값: %d\n", pop());// 200
    printf("세번째 pop() 리턴 값: %d\n", pop());// 100
    return 0;
}

void push(int data)
{
    stack[tos] = data;
    // tos = tos + 1;
    ++tos;
}

int pop(void)
{
    --tos;
    return stack[tos];
}
