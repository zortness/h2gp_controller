import time
import board
import neopixel
import digitalio
import math
from analogio import AnalogIn

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

# pin used for reading in potentiometer voltage relative to 3.3V
analog_in = AnalogIn(board.A0)

# pin used to turn on valve
valve = digitalio.DigitalInOut(board.D1)
valve.direction = digitalio.Direction.OUTPUT

# voltage goes from 1.66V to 3.28V by experimentation
lo_v = 1.5 # go slightly lower so we're sure to never drop below 1 second
hi_v = 3.28
max_valve_time = 30 #seconds
purge_time = 0.5 # seconds

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

# normalize between 0 and 1 (0% and 100%)
# then multiply by 30 seconds
def conv_voltage_to_time(pin):
    v = get_voltage(pin)
    v = v - lo_v
    v = v / (hi_v - lo_v)
    return v * max_valve_time

while True:
    valve.value = False
    pixels.fill((0, 0, 0))
    s_to_wait = math.ceil(conv_voltage_to_time(analog_in))
    print(f"sleeping {s_to_wait} seconds")
    time.sleep(s_to_wait)
    pixels.fill((0, 255, 0))
    valve.value = True
    time.sleep(purge_time)
    valve.value = False
