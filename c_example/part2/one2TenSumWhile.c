#include <stdio.h>

int main()
{
    int sum = 0;
    int i = 1;
    while(i<=10){
        sum += i;
        i++;
    }
    printf("1 부터 10 까지의 합은 : %d\n", sum);
    return 0;
}