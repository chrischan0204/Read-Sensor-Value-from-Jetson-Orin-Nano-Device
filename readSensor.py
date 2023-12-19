##############Composed: 2023.12.10###############
#############Composer: Prodan Marco##############
import smbus
import time
#Detect I2CBus7
bus = smbus.SMBus(7)
#Sensor Address 0x36
address = 0x36

def readValue(n):
    value = bus.read_byte_data(address, n)
    return value

while True:
    byte1 = readValue(0)
    byte2 = readValue(1)
    byte3 = readValue(2)
    byte4 = readValue(3)
    current = (byte1 & 0x0F) << 8 + byte2
    print("Current Value",current)
    position = (byte3 & 0x0F) << 8 + byte4
    print("Position Value", position)
    time.sleep(1)