from datetime import datetime
import time
import os
import RPi.GPIO as GPIO
from apscheduler.schedulers.background import BackgroundScheduler
import threading

LEDPin = 21 # Broadcom pin 21 (Pi pin 40)
pumpPin = 26 # Broadcom pin 26 (Pi pin 37)
lampBlueLowPin = 20

def setupPins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPin, GPIO.OUT)
    GPIO.setup(pumpPin, GPIO.OUT)
    GPIO.setup(lampBlueLowPin, GPIO.OUT)

class pumpWater(threading.Thread):
    def __init__(self,pumpTime):
        threading.Thread.__init__(self)
        self.pumpTime=pumpTime
    
    def run(self):
        GPIO.output(LEDPin,GPIO.HIGH)
        GPIO.output(pumpPin,GPIO.HIGH)
        print('Turning pump ON @ %s' % datetime.now())
        time.sleep(self.pumpTime)
        GPIO.output(LEDPin, GPIO.LOW)
        GPIO.output(pumpPin, GPIO.LOW)
        print('Turning pump OFF @ %s' % datetime.now())

def lampBlueON():
    GPIO.output(lampBlueLowPin,GPIO.HIGH)
    print('Turning blue lamp ON LOW @ %s' % datetime.now())

def lampBlueOFF():
    GPIO.output(lampBlueLowPin,GPIO.LOW)
    print('Turning blue lamp OFF @ %s' % datetime.now())    
    
if __name__ == '__main__':
    setupPins()

    morningPump=pumpWater(pumpTime=600)
    morningBlueON=threading.Thread(target=lampBlueON)
    morningBlueOFF=threading.Thread(target=lampBlueOFF)
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: morningPump.start(),'cron',hour=20,minute=47)
    scheduler.add_job(lambda: morningBlueON.start(),'cron',hour=20,minute=48)
    scheduler.add_job(lambda: morningBlueOFF.start(),'cron',hour=20,minute=49)  
    scheduler.start()
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)            
    except (KeyboardInterrupt, SystemExit):
        pass
    
    finally:
        GPIO.cleanup()
        scheduler.shutdown()
        print('Shutting down sheduler')
