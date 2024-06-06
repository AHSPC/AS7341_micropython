from time import sleep
from machine import SoftI2C, Pin
from as7341 import AS7341

i2c = SoftI2C(sda=Pin(0), scl=Pin(1))
sensor = AS7341(i2c)

sensor.led = True

for _ in range(100):
    readings = sensor.get_readings()
    # print(readings)

    # Prints the color name and value for whatever the strongest wavelength is.
    # NOTE: this is not really a very accurate way to tell which color the sensor is seeing.
    maxK = ""
    maxV = 0
    for k, v in readings.items():
        if v > maxV:
            maxV = v
            maxK = k
    print(maxK, maxV)

    # sleep(0.05) # not necessary, as sensor.get_readings() takes a bit of time anyways


sensor.led = False
