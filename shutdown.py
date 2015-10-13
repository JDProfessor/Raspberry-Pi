#!/usr/bin/python

import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

shutdown_btn = 18  #GPIO.1
pulldown = 23      #GPIO.4
led = 24       	   #GPIO.5

GPIO.setup(shutdown_btn,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #pull down shutdown_btn
GPIO.setup(pulldown,GPIO.OUT) #set pulldown out 0
GPIO.output(pulldown, 0)
GPIO.setup(led,GPIO.OUT)      #set led out 1
GPIO.output(led, 1)

def onPress(channel):
	os.system("poweroff")
	for i in range (3):
		GPIO.output(led, 0)
		time.sleep(0.1)
		GPIO.output(led, 1)
		time.sleep(0.1)
	GPIO.cleanup()

GPIO.add_event_detect(shutdown_btn,GPIO.RISING,callback= onPress,bouncetime=500)

try:
	while 1:
		time.sleep(2)
except:
	GPIO.cleanup()
