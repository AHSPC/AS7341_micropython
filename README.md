# AS7341_mycropython

Tested with an RPI Pico. 

Depends on Adafruit's register and i2c_device libraries. See our micropython port of
i2c_device [here](https://github.com/AHSPC/adafruit_i2c_device_micropython). Adafruit register seems to work unchanged.

See Adafruit's circuitpython repository for other usage examples (will need to be ported).
A simple example is shown in ./test.py.

An additional `get_readings()` method is provided to abstract away from the individual channels and wavelengths.
It additionally ignores all OSErrors via try-catch (specific to AHS Electronics Workshop class)
