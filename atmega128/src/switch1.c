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
    uint8_t switch0;
    while (1)
    {
        switch0 = PINE; // 0b 0101 0000
        PORTC = switch0 >> 4; // 0b 0000 0101
        // ... 시간이 걸리는 코드
        //... 인터럽트로 스위치 제어
    }
}