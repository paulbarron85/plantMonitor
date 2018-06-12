import RPi.GPIO as GPIO
import time

print "Hello World!"
print ("Press CTRL+C to exit")
# Pin Definitions:
pumpPin = 23 # Broadcom pin 23 (P1 pin 16)

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pumpPin, GPIO.OUT)

try:
    while 1:
        GPIO.output(pumpPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pumpPin, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print "\nGoodbye World!"
    GPIO.cleanup()
