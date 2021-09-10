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

import network


def resetDigitalPins():
    for i in range(8):
        digital.pin(i,0)

def flash():
    for i in range(3):
        flashLED = Pin(4, Pin.OUT)
        flashLED.on()
        time.sleep(0.1)
        flashLED.off()
        time.sleep(0.1)

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
	version = data['version']
	return code, version

def getCode():
    while True:
        try:
            code, version = getSource() 
        except Exception as e:
            print(e)
            requests.Response.close
            gc.collect()
            sta_if.disconnect()
            time.sleep(0.5)
            sta_if.connect('Khang Hoang', 'khangthinh')
            print('network status: '+ str(sta_if.isconnected()))
            pass
        else:
            oled.fill(0)
            oled.show()
            oled.text('firmware: '+ version, 0 ,0)
            oled.show()
            f = open("script.py", "w")
            f.write(code)
            f.close()
            break

def runScript():
    f = open("script.py", "r")
    script = f.read()
    f.close()
    exec(script)

flash()
resetDigitalPins()

ssid = 'Khang Hoang'
wp2_pass = 'khangthinh'

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(ssid, wp2_pass)
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())    

getCode()
runScript()


  
		





