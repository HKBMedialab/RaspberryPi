# PIR - random audio player
# by hkbMediaLab and luk, 2019

import RPi.GPIO as GPIO
import time, os, random, glob
                                                                                                                                                                                      
list = glob.glob("/media/usb/*.mp3")              # list all *.mp3 files in a folder on USB-drive. Plugin before start.
GPIO.setwarnings(False)                                                                                                                                                               
GPIO.setmode(GPIO.BOARD)                                                                                                                                                              
GPIO.setup(16, GPIO.IN)                           # Read output from PIR motion sensor
while True:
        i=GPIO.input(16)                                                                                                                                                              
        if i==0:                                  # When output from motion sensor is LOW
                print "No intruders",i            # GPIO.output(3, 0)  #Turn OFF LED
                time.sleep(0.3)                   # rather small timeout between sensor reading, even 1.0 is fine.                                                                                                                                  
        elif i==1:                                # When output from motion sensor is HIGH
                print "Intruder detected",i       # GPIO.output(3, 1)  #Turn ON LED
                file = random.choice(list)        # choose random file from list                                                                                                                                   
                print file
                os.system("omxplayer '" + file + "'") # play file with omxplayer
                time.sleep(0.3)                                                                                                                                                       
                                                                                                                                                                                      
