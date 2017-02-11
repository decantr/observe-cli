#!/usr/bin/python

# For this to work it requires your IR Sensor to be plugged into
# vcc > 2  (5V)
# out > 33
# gnd > 34
import time
import os

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

# Begin program

sense.setmode(sense.BOARD)
sense.setup(33,sense.IN)
sense.add_event_detect(33,sense.RISING,callback=takePhoto)

def takePhoto():
	print('IR Event: Detected')
	with picamera.PiCamera() as camera:
		camera.capture(time.strftime('%m%d_%H:%M:%S')+'.jpg')
		print('IR Event: Picture taken')

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	pass
finally:
	print('Shutting down program:', __name__)
	sense.cleanup()