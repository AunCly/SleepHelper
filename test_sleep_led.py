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
nb_repetition_current = 6
time_per_repetion_cycle = global_duration_s/(nb_repetition_start-nb_repetition_end)

#time_start = time.time()

# Cyclic ratio is varied 0 to 100 and then 100 to 0

#try:
while nb_repetition_current > 5:
    sleep_time_dc_cycle = ((((60/nb_repetition_current)/2))/100)
    #sleep_time_dc_cycle = sleep_time_dc_cycle-(sleep_time_dc_cycle/200)
    #sleep_time_dc_cycle = 0.0495
    #print("sleep_time = "+str(sleep_time_dc_cycle))
    time_start = time.time()
    for dc in range(1, 101, 1):
        #LED.ChangeDutyCycle(dc)
        #print(dc);
        time.sleep(sleep_time_dc_cycle)
    for dc in range(99, -1, -1):
        #LED.ChangeDutyCycle(dc)
        #print(dc);
        time.sleep(sleep_time_dc_cycle)
    print(str(time.time()-time_start))
    break;
        #if time.time() > time_start+time_per_repetion_cycle :
            #nb_repetition_current = nb_repetition_current-1;
            
#except KeyboardInterrupt:
    #pass
    
#LED.stop()

#GPIO.cleanup()
