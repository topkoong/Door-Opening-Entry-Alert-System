import Adafruit_BBIO.GPIO as GPIO
import time
PIR_PIN = "P8_14"
GPIO.setup(PIR_PIN, GPIO.IN)
try:
    print "Waiting for PIR to settle ..."
  # Loop until PIR output is 0
    while GPIO.input(PIR_PIN) == 1:
    print "Ready"
    i = 0
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING) #thread callbacks
    #enables interrupts on the pin, and tells the code to wait until an event occurs
    while 1: #skip a variable check
        time.sleep(1)
        if GPIO.event_detected(PIR_PIN):
            print PIR_PIN
            print "event detected!"
            i += 1
            print i
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
