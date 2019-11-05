#!/usr/bin/python3

import os
import time
#import picamera

#from datetime import datetime
## Import GPIO library
import RPi.GPIO as GPIO

## Set basic variables: GPIO pin
switch1 = 40
#file_location = '/var/tmp/pipicts'

## Use board pin numbering.
GPIO.setmode(GPIO.BOARD)
## Setup GPIO Pin 40 to IN
GPIO.setup(switch1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
## Turn on GPIO pin 40
GPIO.input(switch1)
print('ACTIVATED')
## Loop watching for switch activity.
while True:
    if GPIO.input(switch1):
        print('closed')
    else:
        print('open')

    time.sleep(.1)

