#include <stdio.h>

typedef struct
{
    double left;
    double right;
}Vision;

void exchange(Vision *robot);

int main(void)
{
    Vision robot;

    printf("시력 입력: ");
    scanf("%lf %lf", &robot.left, &robot.right);
    exchange(&robot);
    printf("바뀐 시력 : %.1lf %.1lf\n", robot.left, robot.right);
    return 0;
}

void exchange(Vision *robot)
{
    double temp;
    temp = robot->left;
    robot->left = robot->right;
    robot->right = temp;
}
