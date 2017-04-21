#!/usr/bin/env python
 
import RPi.GPIO as GPIO 
import time
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(4, GPIO.OUT)
 
# creation d'un objet PWM. canal=4 frequence=50Hz
LED = GPIO.PWM(4, 50)
 
# demarrage du PWM avec un cycle a 0 (LED off)
LED.start(0)
 
# On fait varier le rapport cyclique de 0 a 100 puis de 100 a 0
try:
    while 1:
        for dc in range(0, 101, 1):
            LED.ChangeDutyCycle(dc)
            time.sleep(0.0272)
        for dc in range(100, -1, -1):
            LED.ChangeDutyCycle(dc)
            time.sleep(0.0272)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
