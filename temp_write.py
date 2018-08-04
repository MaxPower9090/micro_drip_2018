#!/usr/bin/python
#script liest den TempSensor aus und schreibt die werte in eine File mit yyyymmdd.txt format

import sys
import time
import Adafruit_DHT

wert = 0
humidity = 0
temp_correction = -2
temperature = 0
sensor = 11	# type of DHT Sensor (11 = DHT11 / 12 = DHT12 )
pin = 27	# pin on the raspberry

filename = time.strftime("%Y%m%d.txt")		#filename by date
filename = "/home/pi/Temp/"+filename		# I'm a python nooob and don't know how to solve this problem more elegantly ;)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) 	#get the temp from DHT Sensor
wert = temperature + temp_correction				#correction for the value if needed

try:

	d = open(filename,"a")    	# opens file for wirting on the end of it
	d.write(str(wert)+" \n")	#writes the value to the file
#	d.write('\n')
#	print wert

except:
	print ("failed to open")
	sys.exit(0)

d.close()

sys.exit(0)
