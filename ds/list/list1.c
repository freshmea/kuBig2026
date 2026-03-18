#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
} Node;

void insertNode(int data, Node *p);
void deleteList(Node *p);
void deleteNode(Node *p, int data);

int main(void)
{
    Node *p;
    p = malloc(sizeof(Node));

    p->data = 100;
    // 두번째 데이터 생성
    p->next = malloc(sizeof(Node));
    p->next->data = 200;

    // 세번째 데이터 생성
    p->next->next = malloc(sizeof(Node));
    p->next->next->data = 300;

    p->next->next->next = malloc(sizeof(Node));
    p->next->next->next->data = 400;

    // ...

    // 삽입 코드
    // insertNode(3, p);
    // insertNode(3, p->next);
    // insertNode(3, p->next->next);

    // 삭제 코드
    // deleteNode(p, 300);

    // 출력 코드
    Node *tmp;
    tmp = p;
    while(tmp ){
        printf("%d\n", tmp->data);
        tmp = tmp->next;
    }

    // list 를 제거 하는 코드
    deleteList(p);
    free(p);
    return 0;
}

void insertNode(int data, Node *p)
{
    Node *tmp = malloc(sizeof(Node));
    tmp->data = data;
    tmp->next = p->next;
    p->next = tmp;
}

void deleteList(Node *p)
{
    Node *tmp = malloc(sizeof(Node));
    Node *tmp2 = malloc(sizeof(Node));
    tmp = p->next;
    for (int i = 0; i < 1;++i){
        tmp = tmp->next;
    }
    tmp2 = p->next;
    for (int i = 0; i < 2; ++i)
    {
        tmp2 = tmp2->next;
    }
    tmp2 = tmp->next;
    free(tmp);
    free(tmp2);
}

void deleteNode(Node *p, int data)
{
    Node *tmp = p->next;
    Node *tmp2 = p->next->next;
    while(tmp){
        if(tmp->data == data )
            break;
        tmp = tmp->next;
        tmp2 = tmp2->next;
    }
    if(tmp ){
        Node *tmp3 = tmp;
        tmp2->next = tmp->next;
        free(tmp3);
    }
}