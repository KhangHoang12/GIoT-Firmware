import time
from machine import Pin, SoftI2C

class AHT20:
	def __init__(self):
		self.temperature
		self.humidity

	def read():
		i2c = SoftI2C(scl=Pin(0), sda=Pin(16))
		i2c.writeto(56, bytearray([0xac, 0x33, 0x00]))

		time.sleep(0.016)

		data = i2c.readfrom(56, 6)

		humidity = data[1]
		humidity <<= 8
		humidity += data[2]
		humidity <<= 4
		humidity += (data[3] >> 4)
		humidity /= 1048576.0
		humidity *= 100

		temperature = data[3] & 0x0f
		temperature <<= 8
		temperature += data[4]
		temperature <<= 8
		temperature += data[5]
		temperature = temperature / 1048576.0*200.0-50.0  # Convert to Celsius	
		print(temperature)
		print(humidity)

		return temperature, humidity
		
		


