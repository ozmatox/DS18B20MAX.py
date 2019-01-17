#!/usr/bin/python
#>>>>ozmatox<<<<<


import os
import time
import w1thermsensor

from w1thermsensor import W1ThermSensor
from random import randrange
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "041752f7bbff")
temp = sensor.get_temperature()
msg = "Temperatura Pomieszczenia  :  " + str(temp) + " C"

print(temp)
show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))

