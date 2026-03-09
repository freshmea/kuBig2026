// cc -o limit limit.c

#include <limits.h>
#include <stdio.h>

#define END_HELLO "end of file\n"
int main(void)
{
    printf("char_bit : %d\n", CHAR_BIT);
    printf("char_min : %d\n", CHAR_MIN);
    printf("char_max : %d\n", CHAR_MAX);
    printf("INT_MIN : %d \t INT_MAX : %d\n", INT_MIN, INT_MAX);
    printf("LONG_MIN : %ld \t LONG_MAX : %ld\n", LONG_MIN, LONG_MAX);
    printf(END_HELLO);
    printf("%d", 2147483648);
    return 0;
}