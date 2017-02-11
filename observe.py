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
def MOTION(irPin):
	print('IR Event: Detected')
	talePhoto()

def takePhoto():
	with picamera.PiCamera() as camera:
		camera.capture(time.strftime('%m%d_%H:%M:%S')+'.jpg')
		print('IR Event: Picture taken')

# Program

sense.setmode(sense.BCM)
sense.setup(irPin,sense.IN)

try:
	print ('IR Event: Binding IR Sensor on GPIO pin' + str(irPin))
	sense.add_event_detect(irPin,sense.RISING,callback=MOTION)
	print('IR Event: Sleeping')
	while 1:
		time.sleep(1)
except KeyboardInterrupt:
	pass
	print('Exiting...')
	sense.cleanup()