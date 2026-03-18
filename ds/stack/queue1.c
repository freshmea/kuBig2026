#include <stdio.h>

int queue[100];
int front;
int rear;

void push(int data);
int pop(void);

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

void push(int data)
{
    queue[rear++] = data;
}
int pop(void)
{
    return queue[front++];
}