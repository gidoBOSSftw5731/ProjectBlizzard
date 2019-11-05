#!/usr/bin/python

import os
import time
#import picamera

#from datetime import datetime
## Import GPIO library
import RPi.GPIO as GPIO

## Set basic variables: GPIO pin and file archive location.
switch1 = 40
#file_location = '/var/tmp/pipicts'

## Use board pin numbering.
GPIO.setmode(GPIO.BOARD)
## Setup GPIO Pin 40 to IN
GPIO.setup(switch1, GPIO.IN)
## Turn on GPIO pin 40
GPIO.input(switch1)
print('ACTIVATED')
## Loop watching for switch activity.
while True:
  if GPIO.input(switch1) == False:
    print('foo')

## Reset to start
GPIO.cleanup()