#include "iotLogReport.h"

#include <stdlib.h>

int main(void)
{
    const char *inputPath = "sensor_log.dat";
    const char *outputPath = "report.out";
    FILE *fin = fopen(inputPath, "r");
    FILE *fout = fopen(outputPath, "w");
    int logCount;
    int loadedCount;
    SensorLog *logs;
    SensorLog **table;

    if (fin == NULL || fout == NULL)
    {
        fprintf(stderr, "입력 또는 출력 파일을 열 수 없습니다. 실행 위치를 확인하세요.\n");
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
    printf("리포트 생성 완료: %s\n", outputPath);

    free(logs);
    free(table);
    fclose(fin);
    fclose(fout);

    return 0;
}
