#!/usr/bin/env python
 
#import RPi.GPIO as GPIO 
import time
 
#GPIO.setmode(GPIO.BCM) 
#GPIO.setup(4, GPIO.OUT)
 
# create PWM object. gpio=4 freq=50Hz
#LED = GPIO.PWM(4, 50)
 
# start PWM cycle with 0 (LED off)
#LED.start(0)
 
global_duration_m = 20
global_duration_s = 20*60
nb_repetition_start = 11
nb_repetition_end = 6
nb_repetition_current = 11
time_per_repetion_cycle = global_duration_s/6
time_start = time.time()

# Cyclic ratio is varied 0 to 100 and then 100 to 0
print('------- Debut du test ---------')
rep = 0
nb_cycle=1
#try:
while nb_repetition_current > 5:
    sleep_time_dc_cycle = ((((60/nb_repetition_current)/2))/100)
    sleep_time_dc_cycle = sleep_time_dc_cycle-(sleep_time_dc_cycle/200)
    #sleep_time_dc_cycle = 0.0495
    for dc in range(1, 101, 1):
        #LED.ChangeDutyCycle(dc)
        #print(dc);
        time.sleep(sleep_time_dc_cycle)

    for dc in range(99, -1, -1):
        #LED.ChangeDutyCycle(dc)
        #print(dc);
        time.sleep(sleep_time_dc_cycle)
    rep = rep+1
    if time.time() > time_start+(nb_cycle*time_per_repetion_cycle) :
        print("-- Fin du cycle de "+str(nb_repetition_current)+" Rep / minutes --")
        print("-- Nb de rep pour le cycle "+str(rep)+"  --")
        nb_repetition_current = nb_repetition_current-1
        rep = 0
        nb_cycle = nb_cycle+1
            
#except KeyboardInterrupt:
    #pass
    
#LED.stop()

#GPIO.cleanup()
