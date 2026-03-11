// scanf로 입력받은 변수 a, b 에 대해서 a ~ b 까지의 합을 출력 하세요. for 문을 사용해서

#include <stdio.h>

int main()
{
    int a, b;
    printf("정수 a 와 b 를 넣으세요: ");
    scanf("%d %d", &a, &b);

    int sum = 0;
    for (int i = a; i <= b; ++i)
    {
        sum = sum + i;
    }
    printf("%d 부터 %d 까지의 합은 : %d\n", a, b, sum);
    return 0;
}