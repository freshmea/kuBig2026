#include "SHT2x.h"
#include "TWI_driver.h"
#include "lcd.h"
#include <avr/interrupt.h>
#include <avr/io.h>
#include <util/delay.h>

void printf_2dot1(uint8_t sense, uint16_t sense_temp);

uint16_t temperaturC, humidityRH;

int main(void)
{
    Init_TWI();
    lcdInit();
    SHT2x_Init();
    nt16 sRH;
    nt16 sT;
    uint8_t error = 0;

    while(1)
    {
        error |= SHT2x_MeasureHM(HUMIDITY, &sRH);
        error |= SHT2x_MeasureHM(TEMP, &sT);
        temperaturC = SHT2x_CalcTemperatureC(sT.u16) * 10;
        humidityRH = SHT2x_CalcRH(sRH.u16) * 10;
        if (error == SUCCESS)
        {
            lcdGotoXY(0, 0);
            printf_2dot1(TEMP, temperaturC);
            lcdGotoXY(0, 1);
            printf_2dot1(HUMIDITY, humidityRH);
        }
        else{
            lcdGotoXY(0, 0);
            lcdPrintData(" Temp: --.-C", 12);
            lcdGotoXY(0, 1);
            lcdPrintData(" Humi: --.-%", 12);
        }
        _delay_ms(30);
    }
    return 0;
}

void printf_2dot1(uint8_t sense, uint16_t sense_temp)
{
    if (sense == TEMP)
        lcdPrintData(" Temp: ", 7);
    else
        lcdPrintData(" Humi: ", 7);

    // 각 자릿수 분리
    uint8_t d100 = (sense_temp / 100) % 10; // 백의 자리
    uint8_t d10 = (sense_temp / 10) % 10;   // 십의 자리
    uint8_t d1 = sense_temp % 10;           // 소수점 자리

    // 백의 자리가 있으면 출력
    if (d100 > 0)
        lcdDataWrite(d100 + '0');

    // 십의 자리는 백의 자리가 출력됐으면 '0'이라도 출력, 아니면 0보다 클 때만 출력
    if (d100 > 0 || d10 > 0)
    {
        lcdDataWrite(d10 + '0');
    }
    else
    {
        // 0.5도 같은 경우를 위해 일의 자리가 0이면 0이라도 찍어줌
        lcdDataWrite('0');
    }

    lcdDataWrite('.');
    lcdDataWrite(d1 + '0');
    lcdDataWrite(sense == TEMP ? 'C' : '%');
}