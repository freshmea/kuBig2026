// usbipd attach --wsl --busid 7-3
// cd build/atmega128-build/
// ls
// lsusb
// history
// lsusb
// sudo chmod 666 /dev/bus/usb/001/002
// ninja upload

#include <avr/io.h>

int main(void)
{
    DDRC = 0x0F; // led 설정
    DDRE = 0x00; // switch 설정
    while(1){
        PORTC = PINE >> 4;
    }
}