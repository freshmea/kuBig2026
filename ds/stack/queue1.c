#include <stdio.h>

int queue[100];
int front;
int rear;

void push(int data);
int pop(void);
// 여러개의 큐를 다룰 수 없다. -> 구조체를 사용한다.
// 데이터의 갯수가 정해져 있다. 100개 -> 동적할당으로 해결
// 여러번 사용하면 데이터가 적어도 배열맥스를 넘긴다.
// 큐에 데이터를 넣지 않고 빼면 에러 발생
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