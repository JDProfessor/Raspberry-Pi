#!/usr/bin/python

import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

shutdown_btn = 18  #GPIO.1
pulldown_btn = 23  #GPIO.4

GPIO.setup(shutdown_btn,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #pull down shutdown_btn
GPIO.setup(pulldown_btn,GPIO.OUT)
GPIO.output(pulldown_btn, 0)

def onPress(channel):
	os.system("poweroff")
	time.sleep(0.5)
	GPIO.cleanup()

GPIO.add_event_detect(shutdown_btn,GPIO.RISING,callback= onPress,bouncetime=500)

try:
	while 1:
		time.sleep(2)
except:
	GPIO.cleanup()
