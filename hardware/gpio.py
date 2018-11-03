import RPi.GPIO as GPIO
import time

print ("Hello World!")
print ("Press CTRL+C to exit")
# Pin Definitions:
gpioPin01 = 1 # Broadcom pin 01 (Pi pin 28)
gpioPin02 = 2 # Broadcom pin 02 (Pi pin 03)
gpioPin03 = 3 # Broadcom pin 03 (Pi pin 05)
gpioPin04 = 4 # Broadcom pin 04 (Pi pin 07)
gpioPin01 = 5 # Broadcom pin 01 (Pi pin )
gpioPin02 = 6 # Broadcom pin 02 (Pi pin )
gpioPin03 = 7 # Broadcom pin 03 (Pi pin )
gpioPin04 = 8 # Broadcom pin 04 (Pi pin )
gpioPin01 = 9 # Broadcom pin 01 (Pi pin )

gpioPin10 = 10 # Broadcom pin 02 (Pi pin )
gpioPin11 = 11 # Broadcom pin 03 (Pi pin )
gpioPin12 = 12 # Broadcom pin 04 (Pi pin )
gpioPin13 = 13 # Broadcom pin 01 (Pi pin )
gpioPin14 = 14 # Broadcom pin 02 (Pi pin )
gpioPin15 = 15 # Broadcom pin 03 (Pi pin )
gpioPin16 = 16 # Broadcom pin 01 (Pi pin )
gpioPin17 = 17 # Broadcom pin 02 (Pi pin )
gpioPin18 = 18 # Broadcom pin 03 (Pi pin )
gpioPin19 = 19 # Broadcom pin 04 (Pi pin )

gpioPin20 = 20 # Broadcom pin 20 (Pi pin 38)
gpioPin21 = 21 # Broadcom pin 21 (Pi pin 40)
gpioPin22 = 22 # Broadcom pin 22 (Pi pin 15)
gpioPin23 = 23 # Broadcom pin 23 (Pi pin 16)
gpioPin24 = 24 # Broadcom pin 24 (Pi pin 18)
gpioPin25 = 25 # Broadcom pin 25 (Pi pin 22)
gpioPin26 = 26 # Broadcom pin 26 (Pi pin 37)

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpioPin21, GPIO.OUT)
GPIO.setup(gpioPin26, GPIO.OUT)

try:
    while 1:
        GPIO.output(gpioPin21,GPIO.HIGH)
        GPIO.output(gpioPin26,GPIO.HIGH)
        print ("LED ON")
        time.sleep(3)
        GPIO.output(gpioPin21, GPIO.LOW)
        GPIO.output(gpioPin26, GPIO.LOW)
        print ("LED OFF")
        time.sleep(3)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print ("\nGoodbye World!")
    GPIO.cleanup()
