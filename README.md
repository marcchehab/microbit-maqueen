# microbit-maqueen
Python functions for DFRobot Maqueen Robot. Main difference in this fork are docstrings and that it's not implemented as a class. Also, [maqueen_boilerplate.hex](maqueen_boilerplate.hex) is a project file you can directly use in [the microbit online editor](https://python.microbit.org/v/3/reference).

## Usage
Sample program for testing front LEDs, reading distance, patrol and controlling motors:

```
import microbit
import maqueen

# Testing LEDs
maqueen.set_led(0, 1)
microbit.sleep(1000)
maqueen.set_led(1, 1)
microbit.sleep(1000)
maqueen.set_led(0, 0)
microbit.sleep(1000)
maqueen.set_led(1, 0)

# Reading distance
distance = maqueen.read_distance()
microbit.display.scroll(distance)

# Reading patrol sensors
for i in range(0, 10):
    l = maqueen.read_patrol(0)
    maqueen.set_led(0, l == 1)
    r = maqueen.read_patrol(1)
    maqueen.set_led(1, r == 1)
    microbit.sleep(1000)

# Testing motors
maqueen.set_motor(0,-255)
maqueen.set_motor(1, 100)
microbit.sleep(2000)

maqueen.motor_stop_all()
```