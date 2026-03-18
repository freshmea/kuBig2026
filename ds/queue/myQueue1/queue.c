#include "queue.h"

int queue[100];
int front;
int rear;

void push(int data)
{
    queue[rear++] = data;
}
int pop(void)
{
    return queue[front++];
}