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



def getFirmware():
    url = 'https://my-json-server.typicode.com/KhangHoang12/GIoT-Firmware/firmware'
    response = requests.get(url)
    firmware = json.loads(response.text)
    firmware = str(firmware['source'])
    scriptFile = open("script.py","w")
    scriptFile.write(firmware)
    scriptFile.close()

    f = open("script.py","r")
    sourcecode = f.read()
    print('Firmware downloaded succesfully')
    print(sourcecode)
    return sourcecode

def getSource():
    url = 'https://my-json-server.typicode.com/KhangHoang12/GIoT-Firmware/firmware'
    response = requests.get(url)
    data = json.loads(response.text)
    code = data['source']
    exec(data['source']) 




