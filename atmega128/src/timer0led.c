#include <avr/io.h>
#include <avr/interrupt.h>

uint8_t led_data = 0x00;
volatile uint8_t timer0_cnt = 0;

ISR(TIMER0_OVF_vect);

int main(void){
    DDRC = 0x0F;

    TCCR0 = _BV(CS02) | _BV(CS01) | _BV(CS00); // 분주비 1024
    TIMSK = _BV(TOIE0);
    sei();

    while(1)
    {
        if (timer0_cnt == 100) // 1초 마다 if 문이 작동
        {
            led_data++; // 얼마 만큼의 시간이 흐르면 실행되는가? -> 1초 마다 작동
            if (led_data > 0x0F)
                led_data = 0;
            timer0_cnt = 0;
        }
        PORTC = led_data;
    }
}

ISR(TIMER0_OVF_vect)
{
    cli();
    TCNT0 = 112; // 112 ~ 255 144 번//  1번 카운트 할때 16M /1024 = 15625  1초 -> 117번
    timer0_cnt++;
    sei();
}