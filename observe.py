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
	import RPi.GPIO as GPIO
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
		camera.capture('pics/'+time.strftime('%m%d_%H:%M:%S')+'.jpg')
		print('IR Event: Picture taken')

# Program

GPIO.setmode(GPIO.BOARD)
GPIO.setup(irPin,GPIO.IN)

try:
	print ('IR Event: Binding IR Sensor on GPIO pin' + str(irPin))
	GPIO.add_event_detect(irPin,GPIO.RISING,callback=MOTION)
	print('IR Event: Sleeping')
	while 1:
		time.sleep(4)
except KeyboardInterrupt:
	print('Exiting...')
	GPIO.cleanup()