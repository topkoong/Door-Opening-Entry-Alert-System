import Adafruit_BBIO.GPIO as GPIO
import time
PIR_PIN = "P8_14"
GPIO.setup(PIR_PIN, GPIO.IN)
print "PIR Module Test (CTRL-C to exit)"
try:
    print "Waiting for PIR to settle ..."
    i = 1
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING) #thread callbacks
    #enables interrupts on the pin, and tells the code to wait until an event occurs
    print "Ready"
    while 1: #skip a variable check
        if GPIO.event_detected(PIR_PIN):
            if GPIO.input(PIR_PIN) == 1:
                print "event detected!"
                print " %s time(s)" % i
                i += 1
            elif  GPIO.input(PIR_PIN) == 0:
                print "Ready"
        time.sleep(1)
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
