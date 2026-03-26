#include "at25160.h"
#include "lcd.h"
#include <avr/delay.h>
#include <avr/io.h>

#define ARRAY_SIZE(array) (sizeof(array)/ sizeof(array[0]))

uint8_t msg1[] = "welcone!!";
uint8_t msg2[] = "Atmega128-World!!";
uint8_t msg3[] = "SPI-Flash Example";

int main(void)
{
    uint8_t i = 0;
    uint8_t buf1[20] = {0};
    uint8_t buf2[20] = {0};
    uint8_t buf3[20] = {0};

    SPI_Init(); // PB0123
}
