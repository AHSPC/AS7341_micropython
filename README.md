# AS7341_mycropython

Tested very briefly with an RPI Pico. Micropython doesn't have `monotonic()`, so
`_wait_for_data()` is ported poorly (can be improved later).

Depends on Adafruit's register and i2c_device libraries. See our micropython port of
i2c_device [here](https://github.com/AHSPC/adafruit_i2c_device_micropython). Adafruit register seems to work unchanged.

See Adafruit's circuitpython repository for other usage examples (will need to be ported).
Here's a super simple example in pure micropython:
```python
from time import sleep
from machine import I2C, Pin
from as7341 import AS7341

i2c = I2C(id=0, sda=Pin(0), scl=Pin(1))
sensor = AS7341(i2c)


def bar_graph(read_value):
    scaled = int(read_value / 1000)
    return "[%5d] " % read_value + (scaled * "*")


sensor.led = True

while True:
    print("F1 - 415nm/Violet  %s" % bar_graph(sensor.channel_415nm))
    print("F2 - 445nm//Indigo %s" % bar_graph(sensor.channel_445nm))
    print("F3 - 480nm//Blue   %s" % bar_graph(sensor.channel_480nm))
    print("F4 - 515nm//Cyan   %s" % bar_graph(sensor.channel_515nm))
    print("F5 - 555nm/Green   %s" % bar_graph(sensor.channel_555nm))
    print("F6 - 590nm/Yellow  %s" % bar_graph(sensor.channel_590nm))
    print("F7 - 630nm/Orange  %s" % bar_graph(sensor.channel_630nm))
    print("F8 - 680nm/Red     %s" % bar_graph(sensor.channel_680nm))
    # print("Clear              %s" % bar_graph(sensor.channel_clear))
    # print("Near-IR (NIR)      %s" % bar_graph(sensor.channel_nir))
    print("\n------------------------------------------------")
    sleep(1)
```
