mport RPi.GPIO as GPIO
import time
import os, random, glob
                                                                                                                                                                                      
list = glob.glob("/media/usb/*.mp3")
GPIO.setwarnings(False)                                                                                                                                                               
GPIO.setmode(GPIO.BOARD)                                                                                                                                                              
GPIO.setup(16, GPIO.IN)         #Read output from PIR motion sensor
while True:
        i=GPIO.input(16)                                                                                                                                                              
        if i==0:                 #When output from motion sensor is LOW
                print "No intruders",i          #GPIO.output(3, 0)  #Turn OFF LED
                time.sleep(0.3)                                                                                                                                                       
        elif i==1:               #When output from motion sensor is HIGH
                print "Intruder detected",i             #GPIO.output(3, 1)  #Turn ON LED
                file = random.choice(list)                                                                                                                                            
                print file
                os.system("omxplayer '" + file + "'")
                time.sleep(0.3)                                                                                                                                                       
                                                                                                                                                                                      