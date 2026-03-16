#pragma once
#include <stdio.h>

typedef struct
{
    int year;
    int month;
    int day;
} Date;

void printDate(const Date *pDate);
void setDate(Date *pDate, const int year, const int month, const int day);