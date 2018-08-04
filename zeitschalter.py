#!/usr/bin/env python
# controls a relails module over the raspberry pi 

import sys
import RPi.GPIO as GPIO
import time
import drip_time

zeit = 180  #backup if  drip_time() fails 
zeit = drip_time.drip_time() # drip_time() returns a delay time calculated by the average temperature
print ("zeit")

GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # on
time.sleep(zeit) # time for the pump
print(time.strftime("%d.%m.%Y %H:%M:%S"))
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # off

sys.exit(0)
