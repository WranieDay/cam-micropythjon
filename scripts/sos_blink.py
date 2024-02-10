#written by Cameron on 1/20/24
#this file makes the LED blink

from include.rcc_library import Raft
import utime
from machine import Pin, PWM

myraft = Raft()
pin = 2
percent = 50

pwm_pin = PWM(Pin(pin))

pwm_pin.freq(30)

pwm_pin.duty_u16(percent*655)