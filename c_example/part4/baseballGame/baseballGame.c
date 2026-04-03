#include "baseballGame.h"

static bool has_duplicate_digits(const int *numbers)
{
    for (int i = 0; i < SIZE; ++i)
    {
        for (int j = i + 1; j < SIZE; ++j)
        {
            if (numbers[i] == numbers[j])
            {
                return true;
            }
        }
    }

    return false;
}

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
    while (true)
    {
        printf("1부터 9 사이의 서로 다른 숫자 %d개를 넣으세요:\n", SIZE);

        for (int i = 0; i < SIZE; ++i)
        {
            scanf("%d", &answer[i]);
        }

        bool in_range = true;
        for (int i = 0; i < SIZE; ++i)
        {
            if (answer[i] < 1 || answer[i] > 9)
            {
                in_range = false;
                break;
            }
        }

        if (!in_range)
        {
            printf("1부터 9 사이 숫자만 입력하세요.\n");
            continue;
        }

        if (has_duplicate_digits(answer))
        {
            printf("중복되지 않은 숫자를 입력하세요.\n");
            continue;
        }

        break;
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
