from machine import PWM, Pin
import utime

color1 = PWM(Pin(13))
color1.freq(500)

color2 = PWM(Pin(14))
color2.freq(500)

color3 = PWM(Pin(15))
color3.freq(500)


color1.duty_u16(50*655) #red
color2.duty_u16(50*655) #blue
color3.duty_u16(50*655) #green
utime.sleep_ms(1000)