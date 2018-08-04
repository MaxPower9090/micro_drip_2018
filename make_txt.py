#!/usr/bin/python
#creats a yyyymmdd.txt file

import sys
import time

filename = time.strftime("%Y%m%d.txt")		
filename = "/home/pi/Temp/"+filename

try:

	d = open(filename,"w")    

except:
	print ("oeffnen nicht moeglich")
	sys.exit(0)

d.close()

sys.exit(0)
