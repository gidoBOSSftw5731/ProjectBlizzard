#!/usr/bin/python3

import os
import time
#import picamera

#from datetime import datetime
## Import GPIO library
import RPi.GPIO as GPIO

## Set basic variables: GPIO pin and file path
switch1 = 40
file_location = '/usr/share/nginx/doorsense/status'

## Use board pin numbering.
GPIO.setmode(GPIO.BOARD)
## Setup GPIO Pin 40 to IN
GPIO.setup(switch1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
## Turn on GPIO pin 40
GPIO.input(switch1)

#open file once
f = open(file_location, "w")

print('ACTIVATED')
## Loop watching for switch activity.
while True:
    f.seek(0, 0)
    if GPIO.input(switch1):
        f.writ("0") # closed
    else:
        f.write("1") # open

