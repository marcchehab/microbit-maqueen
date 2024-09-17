import microbit
import machine
import utime

def set_led(lednumber, value):
	"""Enable or disable the front LEDS

	Args:
			lednumber (int): 0 = left LED, 1 = right LED
			value (int): 0 = off, 1 = on
	"""
	if lednumber == 0:
		microbit.pin8.write_digital(value)
	elif lednumber == 1:
		microbit.pin12.write_digital(value)

def read_distance():
	"""
	Reads distance from HC SR04 sensor, result is in centimeters.
	"""
	divider = 42
	maxtime = 250 * divider
	microbit.pin2.read_digital()  # just for setting PULL_DOWN on pin2
	microbit.pin1.write_digital(0)
	utime.sleep_us(2)
	microbit.pin1.write_digital(1)
	utime.sleep_us(10)
	microbit.pin1.write_digital(0)

	duration = machine.time_pulse_us(microbit.pin2, 1, maxtime)
	distance = duration/divider if duration >= 0 else 250
	return distance

def read_patrol(which):
	"""
	Reads patrol sensor, returns 0 or 1.

	Args:
			which (int): 0 = left, 1 = right
	"""
	if which == 0:  # left
		return microbit.pin13.read_digital()
	elif which == 1:  # right
		return microbit.pin14.read_digital()

def set_motor(motor, value):
	"""
	Controls the two motors

	Args:
			motor (int): 0 = left, 1 = right
			value (int): -255 (back) to +255 (forward)
	"""
	data = bytearray(3)
	if motor == 0:  # left motor
		data[0] = 0
	else:
		data[0] = 2  # right motor is 2
	if value < 0:  # ccw direction
		data[1] = 1
		value = -1*value
	data[2] = value
	microbit.i2c.write(0x10, data, False)  # 0x10 is i2c address of motor driver

def motor_stop_all():
	"""Stops all motors
	"""
	set_motor(0, 0)
	set_motor(1, 0)

