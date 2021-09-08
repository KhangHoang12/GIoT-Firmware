import ujson as json
import urequests as requests
import gc

import time
import timeUTC
import digital
import ssd1306
import aht20 

from machine import SoftI2C, Pin
i2c = SoftI2C(scl=Pin(0), sda=Pin(16))
digital = digital.DIGITAL(i2c, 32)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
aht20 = aht20.AHT20
UTC = timeUTC


ssid_ = 'Khang Hoang'
wp2_pass = 'khangthinh'

import network
sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)
sta_if.connect(ssid_, wp2_pass)
print(sta_if.isconnected())


