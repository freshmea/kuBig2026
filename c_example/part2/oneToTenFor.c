#include <stdio.h>

int main(void)
{
    int i = 0;
    for (; i < 10; ++i)
    {
        printf("%d \n", i + 1);
    }
    printf("%d", i);
    return 0;
}