#include "iotLogReport.h"

int count_logs(FILE *fp)
{
    int count = 0;
    char line[128];

    while (fgets(line, sizeof(line), fp) != NULL)
    {
        if (line[0] != '\n' && line[0] != '\r')
        {
            count++;
        }
    }

    rewind(fp);
    return count;
}

int load_logs(FILE *fp, SensorLog *logs, int count)
{
    int loaded = 0;

    while (loaded < count)
    {
        int matched = fscanf(
            fp,
            "%15s %lf %lf %d",
            logs[loaded].deviceId,
            &logs[loaded].temperature,
            &logs[loaded].humidity,
            &logs[loaded].signal
        );

        if (matched == EOF)
        {
            break;
        }

        if (matched != 4)
        {
            return loaded;
        }

        logs[loaded].warningCount = 0;
        loaded++;
    }

    return loaded;
}

void analyze_logs(SensorLog *logs, int count)
{
    for (int i = 0; i < count; ++i)
    {
        logs[i].warningCount = 0;

        if (logs[i].temperature >= 30.0)
        {
            logs[i].warningCount++;
        }

        if (logs[i].humidity >= 70.0)
        {
            logs[i].warningCount++;
        }

        if (logs[i].signal <= 40)
        {
            logs[i].warningCount++;
        }
    }
}

void build_sorted_table(SensorLog *logs, SensorLog **table, int count)
{
    for (int i = 0; i < count; ++i)
    {
        table[i] = &logs[i];
    }

    for (int i = 0; i < count - 1; ++i)
    {
        for (int j = i + 1; j < count; ++j)
        {
            if (table[i]->warningCount < table[j]->warningCount)
            {
                SensorLog *tmp = table[i];
                table[i] = table[j];
                table[j] = tmp;
            }
        }
    }
}

void print_report(FILE *fp, SensorLog **table, int count)
{
    int warningDevices = 0;

    fprintf(fp, "---------------------------------------------\n");
    fprintf(fp, "            IoT Sensor Summary\n");
    fprintf(fp, "---------------------------------------------\n");
    fprintf(fp, "%-12s %7s %8s %8s %8s\n", "Device", "Temp", "Hum", "Signal", "Warn");

    for (int i = 0; i < count; ++i)
    {
        if (table[i]->warningCount > 0)
        {
            warningDevices++;
        }

        fprintf(
            fp,
            "%-12s %7.1f %8.1f %8d %8d\n",
            table[i]->deviceId,
            table[i]->temperature,
            table[i]->humidity,
            table[i]->signal,
            table[i]->warningCount
        );
    }

    fprintf(fp, "---------------------------------------------\n");
    fprintf(fp, "Devices with warnings: %d / %d\n", warningDevices, count);

    if (count > 0)
    {
        fprintf(fp, "Highest risk device: %s\n", table[0]->deviceId);
    }
}
