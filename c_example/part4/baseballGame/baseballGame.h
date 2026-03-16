#pragma once
// #ifndef BASEBALL_H
// #define BASEBALL_H

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 3

void generate_number(int *question);
void input_numbers(int *answer);
bool check_result(const int *question, const int *answer, int *strike, int *ball);

// #endif // BASEBALL_H