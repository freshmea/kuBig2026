#include "iotLogReport.h"

#include <stdlib.h>

int main(void)
{
    const char *inputPath = "/home/aa/kuBig2026/c_example/part6/iotLogReport/sensor_log.dat";
    const char *outputPath = "/home/aa/kuBig2026/c_example/part6/iotLogReport/report.out";
    FILE *fin = fopen(inputPath, "r");
    FILE *fout = fopen(outputPath, "w");
    int logCount;
    int loadedCount;
    SensorLog *logs;
    SensorLog **table;

    if (fin == NULL || fout == NULL)
    {
        fprintf(stderr, "파일을 열 수 없습니다.\n");
        if (fin != NULL)
        {
            fclose(fin);
        }
        if (fout != NULL)
        {
            fclose(fout);
        }
        return 1;
    }

    logCount = count_logs(fin);
    if (logCount <= 0)
    {
        fprintf(stderr, "읽을 로그가 없습니다.\n");
        fclose(fin);
        fclose(fout);
        return 1;
    }

    logs = (SensorLog *)malloc(sizeof(SensorLog) * logCount);
    table = (SensorLog **)malloc(sizeof(SensorLog *) * logCount);

    if (logs == NULL || table == NULL)
    {
        fprintf(stderr, "메모리 할당 실패\n");
        free(logs);
        free(table);
        fclose(fin);
        fclose(fout);
        return 1;
    }

    loadedCount = load_logs(fin, logs, logCount);
    if (loadedCount != logCount)
    {
        fprintf(stderr, "로그 형식이 올바르지 않습니다.\n");
        free(logs);
        free(table);
        fclose(fin);
        fclose(fout);
        return 1;
    }

    analyze_logs(logs, logCount);
    build_sorted_table(logs, table, logCount);
    print_report(fout, table, logCount);

    free(logs);
    free(table);
    fclose(fin);
    fclose(fout);

    return 0;
}
