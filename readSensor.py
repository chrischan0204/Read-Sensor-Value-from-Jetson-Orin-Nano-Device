##############Composed: 2023.12.10###############
#############Composer: Prodan Marco##############
import smbus
import time
#Detect I2CBus7
bus = smbus.SMBus(7)
#Sensor Address 0x36
address = 0x36

def readValue():
    value = bus.read_byte_data(address, 1)
    return value

while True:
    value = readValue()
    print("Sensor",value)
    time.sleep(1)