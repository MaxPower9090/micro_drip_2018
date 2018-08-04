#!/usr/bin/python
#  calculates from the yyyymmdd.txt the average temperature and returns a time in seconds calculated by some logic 

import sys
import time

def drip_time():

	# values are in a file yyyymmdd.txt

	filename = time.strftime("%Y%m%d.txt")		#generates the filename by the date
	filename = "/home/pi/Temp/"+filename		# .... yes....				

	messungen = 0           #values measured a day
	summe =0                # sum of the values
	av_temp = 0             # average temperature

	std_drip = 3*60         # Stadard time for dayli watering- minimal
	extra_drip = 0          # additional time
	extra_einheit = 60      # ammount of time for increasing
	drip_time = 0


	try:
		d = open(filename,"r")    
	except:
		print ("oeffnen nicht moeglich")
		sys.exit(0)

	allezeilen = d.readlines()      # saving the values in "allezeilen"

	d.close()

	for zeile in allezeilen:        # read "allezeilen" 
		#print (zeile)
		summe += float(zeile)
		messungen +=1           # count the ammount of measurements
		
	#print('\n')
	#print ("Summe:", summe)

	#print("Anzahl der Messungen: ", messungen)
	#print"Anzahl der Messungen: ", messungen

	av_temp = summe / messungen     # calculating the average temperture

	#print ("Durchschnittstemperatur:", av_temp)
	#print('\n')

	#print ("Durchschnittstemperatur: {0:1f}".format(av_temp))
	#print "Durchschnittstemperatur: {0:1f}" .format(av_temp)


	#auswertung der Durchschnittstemperatur und Errechnung der "drip_time"


	if av_temp <= 20:
			extra_drip = 0

	elif av_temp<= 25:
			extra_drip = 2*extra_einheit

	elif av_temp<= 27:
			extra_drip = 3*extra_einheit

	elif av_temp<= 30:
			extra_drip = 4*extra_einheit

	else:
			extra_drip = 6*extra_einheit


	drip_time = std_drip + extra_drip       # calculate the drip time "drip_time"

	#print("Bewaesserungszeit in Minuten: ", drip_time/60)

	#print "Bewaesserungszeit in Minuten: " , drip_time/60

	return (drip_time)


	sys.exit(0)
