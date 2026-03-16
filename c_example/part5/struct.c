#include <stdio.h>

struct data
{
    int year;
    int month;
    int day;
};

int main(void)
{
    struct data d;
    d.year = 2026;
    d.month = 7;
    d.day = 19;

    printf("%d-%d-%d\n", d.year, d.month, d.day);
    return 0;
}
