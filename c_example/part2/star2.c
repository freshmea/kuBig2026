// 피라미드 형태 출력 이중 for 문 사용.
//     *
//    ***
//   *****
//  *******
// *********
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
    system("clear");
    int height;
    printf("피라미드의 높이를 넣으세요 : \n");
    scanf("%d", &height);

    for (int i = 1; i <= height; ++i)
    {
        // space 출력
        for (int j = 1; j <= height - i; ++j)
        {
            printf(" ");
        }
        // * 출력
        for (int j = 1; j <= 2 * i - 1;++j){
            printf("*");
        }
        sleep(1);
        printf("\n");
    }
    return 0;
}