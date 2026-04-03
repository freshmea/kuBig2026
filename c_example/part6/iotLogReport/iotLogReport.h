#pragma once

#include <stdio.h>

#define DEVICE_NAME_SIZE 16

typedef struct
{
    char deviceId[DEVICE_NAME_SIZE];
    double temperature;
    double humidity;
    int signal;
    int warningCount;
} SensorLog;

int count_logs(FILE *fp);
int load_logs(FILE *fp, SensorLog *logs, int count);
void analyze_logs(SensorLog *logs, int count);
void build_sorted_table(SensorLog *logs, SensorLog **table, int count);
void print_report(FILE *fp, SensorLog **table, int count);
