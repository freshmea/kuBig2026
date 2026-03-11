// 최대값 찾기 - 순회
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAXINDEX 100

int main(void)
{
    int nums[MAXINDEX];
    srand(time(NULL)); //seed!
    for (int i = 0; i < MAXINDEX; ++i){
        nums[i] = rand() % 1000;
        printf("%d ", nums[i]);
    }

    int max;
    max = nums[0];
    for (int i = 0; i < MAXINDEX;++i){
        if (max < nums[i]){
            max = nums[i];
        }else{
            max = max;
        }
    }
    printf("최대값 : %d\n", max);
    return 0;
}