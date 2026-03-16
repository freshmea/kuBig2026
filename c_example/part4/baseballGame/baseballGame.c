#include "baseballGame.h"

void generate_number(int *question)
{
    srand(time(NULL));
    for (int i = 0; i < SIZE; ++i)
    {
        question[i] = rand() % 9 + 1;
        for (int j = 0; j < SIZE; ++j)
        {
            if (i == j)
            {
                continue;
            }
            if (question[j] == question[i])
            {
                --i;
                break;
            }
        }
    }
//     // 임시로 체크
//     for (int i = 0; i < SIZE; ++i)
//     {
//         printf("%d ", question[i]);
//     }
}

void input_numbers(int *answer)
{
    printf("숫자를 %d개 넣으세요: \n", SIZE);
    for (int i = 0; i < SIZE; ++i)
    {
        scanf("%d", &answer[i]);
    }
}

bool check_result(const int *question, const int *answer, int *strike, int *ball)
{
    *strike = 0;
    *ball = 0;

    for (int i = 0; i < SIZE; ++i)
    {
        for (int j = 0; j < SIZE; ++j)
        {
            if (question[i] == answer[j])
            {
                if (i == j)
                    (*strike)++;
                else
                    (*ball)++;
            }
        }
    }

    printf("Strike: %d \t Ball: %d\n", *strike, *ball);
    return (*strike == SIZE);
}
