# AS7341_mycropython

Tested with an RPI Pico. 

Depends on Adafruit's `register` and `i2c_device` libraries. See our micropython port of
`i2c_device` [here](https://github.com/AHSPC/adafruit_i2c_device_micropython). `register` seems to work unchanged.

See Adafruit's AS7341 circuitpython library repository for other usage examples (they will need to be ported).
A simple example is shown in ./test.py.

An additional `get_readings()` method is provided to abstract away from the individual channels and wavelengths.
It additionally ignores all OSErrors via try-catch and calls itself recursively if one is encountered (specific to AHS's Electronics Workshop class).
