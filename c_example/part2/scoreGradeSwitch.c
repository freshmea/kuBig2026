// int 로 점수를 입력을 받아서 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D,60점 미만이면 F 를 출력하세요!
#include <stdio.h>

int main(void)
{
    int num;
    char grade;
    printf("점수를 넣으세요 : \n");
    scanf("%d", &num);

    switch(num/10){
        case 10:
            grade = 'A';
            break;
        case 9:
            grade = 'A';
            break;
        case 8:
            grade = 'B';
            break;
        case 7:
            grade = 'C';
            break;
        case 6:
            grade = 'D';
            break;
        default:
            grade = 'F';
            break;
        }
    printf("%d 는 %c 등급입니다.\n", num, grade);
    return 0;
}