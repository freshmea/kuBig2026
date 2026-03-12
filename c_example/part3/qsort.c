#include <stdlib.h>
#include <stdio.h>

int compare(const void *a, const void *b);

int main(void)
{
    int nums[10] = {40, 20, 52, 12, 34, 64, 93, 42, 42, 5};
    int indexN = sizeof(nums) / sizeof(int);

    qsort(nums, indexN, sizeof(int), compare);

    for (int i = 0; i < indexN; ++i)
    {
        printf("%d, ", nums[i]);
    }
    printf("\n");
    return 0;
}

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}