#!/usr/bin/python

# For this to work it requires your IR Sensor to be plugged into
# vcc > 2  (5V)
# out > 33
# gnd > 34

#Imports

import time
import os

# Variables
irPin = 33

# Checks

if os.getuid() != 0:
	print('ERROR: Please run as root')
	quit()

try:
	import RPi.GPIO as sense
except ImportError:
	print('ERROR: Please intall \'RPi.GPIO\' module')
	quit()

try:
	import picamera
except ImportError:
	print('ERROR: Please install \'picamera\' module')
	quit()

# Methods

def takePhoto():
	print('IR Event: Detected')
	with picamera.PiCamera() as camera:
		camera.capture(time.strftime('%m%d_%H:%M:%S')+'.jpg')
		print('IR Event: Picture taken')

# Program

print('Binding IR Sensor on GPIO pin ',irPin)
sense.setmode(sense.BOARD)
sense.setup(irPin,sense.IN)
sense.add_event_detect(irPin,sense.RISING,callback=takePhoto)

try:
	print('IR Event: Sleeping')
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	pass
finally:
	print('Exiting...')
	sense.cleanup()