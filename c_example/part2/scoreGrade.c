// int 로 점수를 입력을 받아서 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D,60점 미만이면 F 를 출력하세요!
#include <stdio.h>

int main(void)
{
    int num;
    char grade = 'F';
    printf("점수를 넣으세요 : \n");
    scanf("%d", &num);

    if (num >= 90)
    {
        grade = 'A';
    }
    else if (num >= 80)
    {
        grade = 'B';
    }
    else if (num >= 70)
    {
        grade = 'C';
    }
    else if (num >= 60)
    {
        grade = 'D';
    }
    printf("%d 는 %c 등급입니다.\n", num, grade);
    return 0;
}