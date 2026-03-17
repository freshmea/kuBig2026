#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *pInt;
    double *pDouble;

    pInt = (int *)malloc(sizeof(int));
    if (pInt == NULL)
    {
        printf("메모리가 부족합니다.\n");
        exit(1);
    }
    pDouble = (double *)malloc(sizeof(double));

    *pInt = 10;
    *pDouble = 3.4;

    printf("정수형으로 사용: %d\n", *pInt);
    printf("실수형으로 사용: %lf\n", *pDouble);

    free(pInt);
    free(pDouble);
    return 0;
}