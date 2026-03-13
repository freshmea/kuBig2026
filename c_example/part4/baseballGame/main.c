#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#define SIZE 3

void generate_number(int* question);
void input_numbers(int* answer);
bool check_result(const int* question,const int* answer,int* strike,int* ball);

int main()
{
    int question[SIZE];
    int answer[SIZE];
    int count = 0;
    int strike, ball;

    generate_number(question);

    while(true){
        input_numbers(answer);
        count++;

        if (check_result(question, answer, &strike, &ball)){
            break;
        }
    }

    printf("축하합니다.congraturation!! 시도 횟수는 %d 입니다.\n", count);
    return 0;
}