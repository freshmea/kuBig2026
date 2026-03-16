#include "baseballGame.h"

int main()
{
    int question[SIZE] = {0};
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
