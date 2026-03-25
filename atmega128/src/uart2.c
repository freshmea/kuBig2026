#include <avr/interrupt.h>
#include <avr/io.h>
#include <stdio.h>



FILE OUTPUT = FDEV_SETUP_STREAM(uart0Transmit, NULL, _FDEV_SETUP_WRITE);
FILE INPUT = FDEV_SETUP_STREAM(NULL, uart0Receive, _FDEV_SETUP_READ);

int main(void)
{
    uart0Init();
    stdin = &INPUT;
    stdout = &OUTPUT;


}