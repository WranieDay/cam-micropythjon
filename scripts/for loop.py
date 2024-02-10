#written by Cameron on 1/20/24
#this file makes the LED blink

from include.rcc_library import Raft
import utime

myraft = Raft()

for x in range(3):
    myraft.led_on()
    utime.sleep_ms(500)
    myraft.led_off()
    utime.sleep_ms(500)

for x in range(3):
    myraft.led_on()
    utime.sleep_ms(250)
    myraft.led_off()
    utime.sleep_ms(250)

for x in range(3):
    myraft.led_on()
    utime.sleep_ms(500)
    myraft.led_off()
    utime.sleep_ms(500)