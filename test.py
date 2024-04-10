from time import sleep
from machine import SoftI2C, Pin
from as7341 import AS7341, Gain

i2c = SoftI2C(sda=Pin(0), scl=Pin(1))
print(i2c.scan())
sensor = AS7341(i2c)
sensor.gain = Gain.GAIN_32X
sensor.astep = 599 # 999
sensor.atime = 29# 100

# def bar_graph(read_value):
#     scaled = int(read_value / 1000)
#     return "[%5d] " % read_value + (scaled * "*")

sensor.led = True

for _ in range(50):
    # print("F1 - 415nm/Violet  %s" % bar_graph(sensor.channel_415nm))
    # print("F2 - 445nm//Indigo %s" % bar_graph(sensor.channel_445nm))
    # print("F3 - 480nm//Blue   %s" % bar_graph(sensor.channel_480nm))
    # print("F4 - 515nm//Cyan   %s" % bar_graph(sensor.channel_515nm))
    # print("F5 - 555nm/Green   %s" % bar_graph(sensor.channel_555nm))
    # print("F6 - 590nm/Yellow  %s" % bar_graph(sensor.channel_590nm))
    # print("F7 - 630nm/Orange  %s" % bar_graph(sensor.channel_630nm))
    # print("F8 - 680nm/Red     %s" % bar_graph(sensor.channel_680nm))
    # # print("Clear              %s" % bar_graph(sensor.channel_clear))
    # # print("Near-IR (NIR)      %s" % bar_graph(sensor.channel_nir))
    # print("\n------------------------------------------------")
    # sleep(.1)
    readings = sensor.get_readings()
    print(readings)

    max = 0
    for reading in readings:
        if reading > max:
            max = reading
    print(max)


sensor.led = False
