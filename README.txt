# micro_drip_2018
Water pump controlling for micro drip system with temperature measuring @ raspberry pi


Files:
make_txt.py
  quick@dirty way to create a yyyymmdd.txt file in the right directory
  
temp_write.py
  makes a temperature measure with the DTH11 sensor (DTH Files have to be imported to the same folder) 
  then the value is writen to the file yyyymmdd.txt to the end of the file
  
drip_time.py
  is a module that makes an average temperature of the measured temperature values stored in the yyyymmdd.txt and 
  returns a time in second back 
  --> logic should be modified to your needs
    
zeitschalter.py
  controls the raspberry pi and puts a signal on the selected pin for activate and deactivate the connected relais / pump 
  for the micro drip system.
  the delay time ( time the pump should be on ) is set by calling the module drip_time()
  
  
