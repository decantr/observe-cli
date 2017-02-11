#!/usr/bin/python

# For this to work it requires your IR Sensor to be plugged into
# vcc > 2  (5V)
# out > 33
# gnd > 34

#Imports

import time
import os

# Variables
irPin = 40

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
def MOTION(irPin):
	print('IR Event: Detected')
	talePhoto()

def takePhoto():
	with picamera.PiCamera() as camera:
		camera.capture(time.strftime('%m%d_%H:%M:%S')+'.jpg')
		print('IR Event: Picture taken')

# Program

GPIO.setmode(GPIO.BOARD)
GPIO.setup(irPin,GPIO.IN)

try:
	while True:
		if GPIO.input(irPin):
			print ("Motion Detected!")
		time.sleep(1)
	# print ('IR Event: Binding IR Sensor on GPIO pin' + str(irPin))
	# GPIO.add_event_detect(irPin,GPIO.RISING,callback=MOTION)
	# print('IR Event: Sleeping')
	# while 1:
	# 	time.sleep(1)
except KeyboardInterrupt:
	pass
	print('Exiting...')
	GPIO.cleanup()