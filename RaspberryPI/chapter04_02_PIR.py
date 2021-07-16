import RPi.GPIO as GPIO
import time

sensor = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor, GPIO.IN)

print ("PIR Ready ....")
time.sleep(5)

try:
    while True:
        if GPIO.input(sensor) == 1:
            print("Motion Detected !")
            time.sleep(1)
        
        if GPIO.input(sensor) == 0:
            print('clear')
            time.sleep(0.2)
            
except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup()
