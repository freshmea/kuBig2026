#include <stdio.h>

char *myStrcpy(char *pDes, const char *pSrc);

int main(void)
{
    // strcpy 함수
    char str2[200] = "strawberry";
    myStrcpy(str2, "apple");
    printf("str2: %s\n", str2);
    myStrcpy(str2, "banana");
    printf("str2: %s\n", str2);
    printf("str2: %s\n", myStrcpy(str2, "pineaplle"));
    return 0;
}

char *myStrcpy(char *pDes, const char *pSrc)
{
    char *pA = pDes;

    while(*pSrc != '\0')
    {
        *pDes = *pSrc;
        pDes++;
        pSrc++;
    }
    *pDes = '\0';
    return pA;
}
